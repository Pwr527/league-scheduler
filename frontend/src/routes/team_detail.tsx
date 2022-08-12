import { useParams } from "react-router-dom";
import { Team } from "../types";
import { useGetApi } from "../util";

export default function TeamDetail() {
  const { id } = useParams();
  const { data, loading, error } = useGetApi<Team>(`/teams/${id}`);

  if (loading) return (<h4>Loading</h4>)
  if (error) return (<h4>Error: {error}</h4>)

  return (
    <main>
      <h4>Team: {data?.name}</h4>
    </main>
  )
}