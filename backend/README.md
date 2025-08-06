# 🛠️ Mobile Food Facilities – Backend

## Problem Description

The task was to build a backend service that fetches, filters, and serves data about San Francisco’s mobile food facilities. The API should support:

- Searching food facilities by applicant or address
- Filtering by permit status (e.g., APPROVED, REQUESTED, EXPIRED)
- Returning structured JSON data usable by a frontend or other clients

---

## Solution Overview

The backend is implemented using **FastAPI (Python)**, chosen for its simplicity, speed, and automatic OpenAPI docs. The service:

- Fetches the public dataset from the San Francisco Open Data API
- Caches data in-memory to improve performance
- Exposes endpoints to support filtered search
- Is tested using `pytest` and fully type-annotated

---

## Technical & Architectural Decisions

- **FastAPI**: Minimal boilerplate and great dev experience with automatic docs.
- **In-memory caching**: Since the dataset is static or slow-changing, caching avoids unnecessary network calls.
- **Separation of concerns**: Data-fetching logic is abstracted into services, keeping routes clean and testable.
- **Typed data models**: Pydantic ensures response and input data is validated and consistent.
- **Test-first approach**: Backend endpoints are testable independently of any frontend.

---

## 🚀 How to Run the Backend and Tests

### Setup Environment

```bash
# Navigate to backend folder
cd backend

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

#Run the server
uvicorn main:app --reload

Then open your browser and go to: http://localhost:8000/docs

Swagger UI will appear, allowing you to test the API interactively.

#Running tests
# (Activate virtual environment if not already) by python -m venv venv
python -m pytest tests.py

```

## API Endpoints

# GET /debug/count

Returns the total number of records from the dataset ( 499 records).

# GET /facilities

Returns a list of food facilities. Supports optional query parameters:

search_text (matches applicant name or address)

status (case-sensitive string: e.g., APPROVED)

# GET /facilities/nearest

Returns 5 closest food trucks based on coordinates.
Required parameters:

latitude

longitude
Optional parameters:

count (default: 5)

status (default: APPROVED)

# What would I have done differently with more time?

Added Redis or file-based caching with TTL/expiry control.

Implemented pagination and sorting for /facilities endpoint.

# Trade-offs Made

Used in-memory caching for simplicity instead of Redis or file-based cache.

Skipped authentication and rate limiting assuming internal or demo use.

Avoided external dependency on a database, since data is fetched from a public API.

# Scalabilty considerations

In-memory cache may not scale on multi-instance deployments. Use Redis or Memcached for shared caching.

No pagination — large dataset can cause slow/big response. Add limit, offset, and sorting parameters.

Single point of failure Containerize and deploy with orchestration (e.g., Kubernetes or AWS ECS)
