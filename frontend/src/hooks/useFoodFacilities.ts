import { useEffect, useState } from "react";
import type { FoodFacility } from "../types/FoodFacility";

export function useFoodFacilities() {
  const [data, setData] = useState<FoodFacility[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  const url = "https://data.sfgov.org/resource/rqzj-sfat.json";

  useEffect(() => {
    fetch(url)
      .then((res) => {
        if (!res.ok) {
          throw new Error("Error fetching data");
        }
        return res.json();
      })
      .then(setData)
      .catch((err) => setError(err.message))
      .finally(() => setLoading(false));
  }, []);

  return { data, loading, error };
}
