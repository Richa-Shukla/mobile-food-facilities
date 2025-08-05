from pydantic import BaseModel

class Location(BaseModel):
    latitude: str
    longitude: str
    human_address: str

class FoodFacility(BaseModel):
    objectid: str
    applicant: str
    facilitytype: str
    address: str
    locationdescription: str | None = None
    status: str
    fooditems: str
    latitude: float
    longitude: float
    location: Location
