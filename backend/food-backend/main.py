from fastapi import FastAPI, Query, HTTPException
from typing import Optional, List
from models import FoodFacility
from utils import (
    load_food_facilities,
    filter_by_applicant_and_status,
    filter_by_address_and_status,
    get_nearest_facilities,
)

app = FastAPI(
    title="SF Mobile Food Facilities API",
    description="Search and find San Francisco mobile food trucks by applicant, address, or location",
    version="1.0.0",
)

# Load once at startup
food_facilities = load_food_facilities()

@app.get("/debug/count", summary="Get total count of loaded facilities")
def debug_count():
    return {"count": len(food_facilities)}

@app.get("/facilities", response_model=List[FoodFacility], summary="Search food facilities")
def search_facilities(
    search_text: Optional[str] = Query(None, description="Search applicant or address (partial match)"),
    status: Optional[str] = Query(None, description="Filter by status, e.g. APPROVED, REQUESTED"),
):
    if not search_text:
        # No search text: return all with optional status filter
        if status:
            results = [f for f in food_facilities if f.status == status]
        else:
            results = food_facilities
    else:
        # Search both applicant and address, merge results
        by_applicant = filter_by_applicant_and_status(food_facilities, search_text=search_text, status_filter=status)
        by_address = filter_by_address_and_status(food_facilities, search_text=search_text, status_filter=status)

        # Merge results without duplicates 
        unique = {}
        for f in by_applicant + by_address:
            unique[f.objectid] = f
        results = list(unique.values())

    if not results:
        raise HTTPException(status_code=404, detail="No matching facilities found")
    return results

@app.get("/facilities/nearest", response_model=List[FoodFacility], summary="Get nearest food facilities")
def nearest_facilities(
    latitude: float = Query(..., description="Latitude coordinate, e.g. 37.78"),
    longitude: float = Query(..., description="Longitude coordinate, e.g. -122.41"),
    status: Optional[str] = Query("APPROVED", description="Filter by status, default APPROVED"),
    limit: int = Query(5, description="Number of nearest results to return"),
):
    results = get_nearest_facilities(food_facilities, latitude, longitude, status_filter=status, limit=limit)
    if not results:
        raise HTTPException(status_code=404, detail="No matching facilities found")
    return results
