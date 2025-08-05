from typing import List, Optional
from math import radians, cos, sin, asin, sqrt
from models import FoodFacility
import json
from pathlib import Path

def load_food_facilities() -> List[FoodFacility]:
    data_path = Path(__file__).parent / "food_facilities.json"
    with open(data_path, "r", encoding="utf-8") as f:
        raw_data = json.load(f)

    # raw_data should be a list of dicts based on your example
    print(f"Loaded JSON records count: {len(raw_data)}")

    facilities = []
    for item in raw_data:
        try:
            facility = FoodFacility(
                objectid=item.get("objectid", ""),
                applicant=item.get("applicant", ""),
                facilitytype=item.get("facilitytype", ""),
                address=item.get("address", ""),
                locationdescription=item.get("locationdescription"),
                status=item.get("status", ""),
                fooditems=item.get("fooditems", ""),
                latitude=float(item.get("latitude", 0) or 0),
                longitude=float(item.get("longitude", 0) or 0),
                location=item.get("location", {
                    "latitude": item.get("latitude", ""),
                    "longitude": item.get("longitude", ""),
                    "human_address": item.get("location", {}).get("human_address", "")
                }),
            )
            facilities.append(facility)
        except Exception as e:
            print(f"Error parsing item: {e}")
            # you might want to log or handle it
    print(f"Successfully loaded {len(facilities)} facilities.")
    return facilities



def haversine(lon1: float, lat1: float, lon2: float, lat2: float) -> float:
    """
    Calculate the great circle distance between two points on the earth (specified in decimal degrees)
    Returns distance in kilometers.
    """
    # convert decimal degrees to radians
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine formula
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    r = 6371  # Radius of earth in kilometers
    return c * r

def filter_by_applicant_and_status(
    facilities: List[FoodFacility],
    search_text: Optional[str] = None,
    status_filter: Optional[str] = None
) -> List[FoodFacility]:
    search_text = (search_text or "").lower()
    filtered = []
    for f in facilities:
        if search_text in f.applicant.lower():
            if status_filter is None or f.status == status_filter:
                filtered.append(f)
    return filtered


def filter_by_address_and_status(
    facilities: List[FoodFacility],
    search_text: Optional[str] = None,
    status_filter: Optional[str] = None
) -> List[FoodFacility]:
    """
    Filter facilities by address (partial match) and status.
    """
    filtered = []
    search_text = (search_text or "").lower()
    for f in facilities:
        if search_text in f.address.lower():
            if status_filter is None or f.status == status_filter:
                filtered.append(f)
    return filtered

def get_nearest_facilities(
    facilities: List[FoodFacility],
    latitude: float,
    longitude: float,
    status_filter: Optional[str] = "APPROVED",
    limit: int = 5
) -> List[FoodFacility]:
    """
    Returns the `limit` nearest facilities to the given latitude and longitude.
    Filters by status if provided.
    """
    filtered = (
        [f for f in facilities if (f.status == status_filter)]
        if status_filter else facilities
    )
    # sort by distance
    sorted_facilities = sorted(
        filtered,
        key=lambda f: haversine(longitude, latitude, f.longitude, f.latitude)
    )
    return sorted_facilities[:limit]
