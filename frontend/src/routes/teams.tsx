import { Link, Outlet } from "react-router-dom";
import { Team } from "../types";
import { useGetApi } from "../util";

export default function Teams()  {
  const { data, loading, error } = useGetApi<Team[]>(`/teams`);

  if (loading) return (<h4>Loading</h4>)
  if (error) return (<h4>Error: {error}</h4>)

  return (
      <main>
        <div className="container">
          <div className="row">
            <div className="col-sm">
              <h2 className="float-start">Teams</h2>   
              <Link className="btn btn-secondary float-end" to={`/teams/create`}>Create Team</Link>
              <table className="table">
                <thead>
                  <tr><th>Name</th></tr>
                </thead>
                <tbody>
                {data?.map(team => (
                  <tr key={team.id}>
                    <td><Link to={`/teams/${team.id}`}>{team.name}</Link></td>
                  </tr>
                ))}
                </tbody>
              </table>
            </div>
            <div className="col-sm">
              <Outlet />
            </div>
          </div>
        </div>
      </main>
  )
}