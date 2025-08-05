export interface Location {
  latitude: string;
  longitude: string;
  human_address: string;
}

export interface FoodFacility {
  objectid: string;
  applicant: string;
  facilitytype: string;
  address: string;
  locationdescription?: string;
  status: string;
  fooditems: string;
  latitude: string;
  longitude: string;
  location: Location;
}
