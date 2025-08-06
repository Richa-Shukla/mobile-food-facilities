import json
from typing import List
from models import FoodTruck


def load_food_trucks(file_path: str) -> List[FoodTruck]:
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    # Filter out entries without coordinates
    valid_entries = [
        item for item in data
        if item.get("latitude") and item.get("longitude")
    ]

    return [FoodTruck(**item) for item in valid_entries]
