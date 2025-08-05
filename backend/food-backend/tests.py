from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

# Test: Base GET /facilities returns approved facilities
def test_get_approved_facilities():
    response = client.get("/facilities?status=APPROVED")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert all(f["status"] == "APPROVED" for f in data)


# Test: Search by applicant name
def test_search_by_applicant():
    response = client.get("/facilities?search_text=El+Tonayense")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert any("El Tonayense" in f["applicant"] for f in data)

# Test: Filter by status
def test_filter_by_status():
    response = client.get("/facilities?status=EXPIRED")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert all(f["status"] == "EXPIRED" for f in data)

# Test: Filter by search_text and status together
def test_search_and_status():
    response = client.get("/facilities?search_text=El+Tonayense&status=APPROVED")
    if response.status_code == 200:
        data = response.json()
        assert all("El Tonayense" in f["applicant"] for f in data)
        assert all(f["status"] == "APPROVED" for f in data)
    else:
        assert response.status_code == 404  # acceptable if nothing matches

# Test: Nearest facilities basic functionality
def test_nearest_facilities_default_count():
    lat, lon = 37.77, -122.41  # SF downtown
    response = client.get(f"/facilities/nearest?latitude={lat}&longitude={lon}")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) == 5
    assert all(f["status"] == "APPROVED" for f in data)

# Test: Nearest facilities with custom count
def test_nearest_facilities_custom_count():
    lat, lon, count = 37.77, -122.41, 10
    response = client.get(f"/facilities/nearest?latitude={lat}&longitude={lon}&count={count}")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) <= count


# Test: Nearest facilities with invalid input
def test_nearest_facilities_invalid_coords():
    response = client.get("/facilities/nearest?latitude=abc&longitude=xyz")
    assert response.status_code == 422  # Validation error


# Test: /facilities handles mixed case search
def test_case_insensitive_search():
    response = client.get("/facilities?search_text=el+tonayense")
    assert response.status_code == 200
    data = response.json()
    assert any("El Tonayense" in f["applicant"] for f in data)



# from fastapi.testclient import TestClient
# from main import app
#
# client = TestClient(app)
#
# def test_debug_count():
#     response = client.get("/debug/count")
#     assert response.status_code == 200
#     assert "count" in response.json()
#     assert isinstance(response.json()["count"], int)
#
# def test_search_by_applicant():
#     response = client.get("/facilities?search_text=El+Tonayense")
#     assert response.status_code == 200
#     assert all("El Tonayense" in f["applicant"] for f in response.json())
#
# def test_search_by_partial_address():
#     response = client.get("/facilities?search_text=SAN")
#     assert response.status_code == 200
#     assert all("SAN" in f["address"].upper() for f in response.json())
#
# def test_search_with_status():
#     response = client.get("/facilities?status=APPROVED")
#     assert response.status_code == 200
#     assert all(f["status"] == "APPROVED" for f in response.json())
#
# def test_nearby_default_approved():
#     response = client.get("/facilities/nearby?lat=37.77&lng=-122.41")
#     assert response.status_code == 200
#     assert len(response.json()) <= 5
#     assert all(f["status"] == "APPROVED" for f in response.json())
#
# def test_nearby_all_status():
#     response = client.get("/facilities/nearby?lat=37.77&lng=-122.41&status=ALL")
#     assert response.status_code == 200
#     assert len(response.json()) <= 5
#
# def test_no_result_404():
#     response = client.get("/facilities?search_text=ZZZZZZZZZZ")
#     assert response.status_code == 404
