import { useParams } from "react-router-dom";
import { Place } from "../types";
import { useGetApi } from "../util";

export default function LocationDetail() {
  const { id } = useParams();
  const { data, loading, error } = useGetApi<Place>(`/locations/${id}`);

  if (loading) return (<h4>Loading</h4>)
  if (error) return (<h4>Error: {error}</h4>)

  return (
    <main>
      <h4>Location: {data?.name}</h4>
      <h5>Available times</h5>
      <ul>
        {data?.available_times.map(time => (
          <li>{time}</li>
        ))}
      </ul>
    </main>
  )
}