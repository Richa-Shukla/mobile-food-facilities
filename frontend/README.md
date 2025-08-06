# SF Mobile Food Facilities Finder

## Description of the Problem and Solution

This project is a React frontend application that allows users to search for San Francisco mobile food facilities (food trucks, push carts, etc.) using the public San Francisco Open Data API.

**Features:**

- Search by applicant name or street address (partial matches supported)
- Optional filtering by permit status (e.g., APPROVED, REQUESTED, EXPIRED)
- Responsive UI built with React and Ant Design components
- Dynamic filtering of data on the client side

The application fetches data from the public SF Open Data API endpoint and displays the results in an organized list format with key details like applicant, address, status, and food items.

---

## Technical / Architectural Decisions

- **React + TypeScript:** For type safety and modern frontend development.
- **Ant Design UI Library:** Provides clean, accessible, and responsive UI components out-of-the-box, reducing the need for custom CSS or UI work.
- **Custom Hook (`useFoodFacilities`):** Encapsulates data fetching and state management, promoting reusable and clean code.
- **Client-side Filtering:** Since the dataset is moderate in size and API doesn’t support complex filtering by partial matches easily, filtering is done on the client to improve UX.
- **No backend:** As the API is public and supports CORS, this is a frontend-only app for simplicity.

---

## API Documentation

### Data Source

This app uses the San Francisco Mobile Food Facilities public dataset:

- **Base URL:**  
  `https://data.sfgov.org/resource/rqzj-sfat.json`

### Key Query Parameters Used

| Parameter   | Description                                                |
| ----------- | ---------------------------------------------------------- |
| `applicant` | Filters by the name of the applicant (food truck operator) |
| `status`    | Filters by permit status (e.g., `APPROVED`, `REQUESTED`)   |
| `address`   | Filters by street name or address substring                |

### Example Requests

```http
GET https://data.sfgov.org/resource/rqzj-sfat.json?applicant=Truly Food & More&status=APPROVED

GET https://data.sfgov.org/resource/rqzj-sfat.json?$where=address LIKE '%SAN%'
```

## Critique and Future Improvements

### What I would do differently with more time

- Add server-side filtering and pagination for scalability

- Implement a backend proxy to cache and pre-process data

- Integrate a map view for spatial visualization of food trucks

- Add more detailed search filters (e.g., food items, facility type)

- Improve error handling and retry mechanisms on API failures

### What I would do differently with more time

- Client-side filtering chosen for simplicity, though it may not scale well for very large data

### Scaling considerations

- With large user base or dataset, client filtering will be slow or impractical

- Backend API with indexed search (e.g., Elasticsearch) recommended

- Caching, rate limiting, and pagination would improve performance and UX

## How to Run the Project and Tests

### Prerequisites

- Node.js v14+ installed

- npm or yarn package manager

### Setup

- Clone the repo and install dependencies by running `npm install`

### Run dev server

- run `npm start`

```

```
