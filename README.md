# Mobile Food Facilities

A web application to explore, search, and filter San Francisco’s mobile food facilities. Built using **React** for the frontend and **FastAPI** for the backend. This project uses the official San Francisco dataset to serve live or testable data.

---

## Features

- Search food trucks by applicant name or food items
- Filter results by permit status (APPROVED, EXPIRED, etc.)
- View latitude and longitude for each facility
- Auto-generated API documentation using FastAPI & Swagger
- Automated tests for frontend and backend
- Docker support for containerized backend

---

## 🛠 Tech Stack

### Frontend

- React
- AntD UI library

### Backend

- Python
- FastAPI
- Uvicorn
- Pytest

---

## 🎥 Demo Video

[![Watch the demo on YouTube](https://img.youtube.com/vi/Q-eT0WY1Nwk/0.jpg)](https://www.youtube.com/watch?v=Q-eT0WY1Nwk)

## 🧑‍💻 Local Development and testing

### 🔧 Frontend

```bash
# From frontend folder
Run
- npm install
- npm run dev
- Then open: http://localhost:5173

This will bring up a UI from where you can interact to:

- Search by name of applicant. Includes optional filter on "Status" field.
- Search by street name with partial match. Example: Searching for "SAN" should return food trucks on "SANSOME ST"

#Running frontend tests
- Make sure frontend server is running. If not, repeat above step
- run npx playwright test
```

### 🔧 Backend

```
# From backend folder
Navigate to backend folder
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt

# Run FastAPI server
uvicorn main:app --reload
Then open: http://localhost:8000/docs, which should bring up the swagger page
From the Swagger docs page, you can interact with the API endpoints

- GET debug/count**
Just to return the number of records from dataset (499 records)

- GET /facilities
Returns the list of all facilities from dataset. Takes optional parameters - search by applicant name or address(string), and status (string). Status is case sensitive

- GET facilities/nearest
Takes 2 required params - latitude, longitude
Returns the list of 5 nearest food trucks. Status is APPROVED and count is 5 by default. Can override parameters.

#Running backend tests
- run python -m venv venv
- run python -m pytest tests.py

# Run Backend with Docker
# From backend folder
docker build -t food-backend .
docker run -p 8000:8000 food-backend
```
