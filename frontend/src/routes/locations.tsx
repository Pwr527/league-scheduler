import { Link, Outlet } from "react-router-dom";
import { Place } from "../types";
import { useGetApi } from "../util";

export default function Locations()  {
  const { data, loading, error } = useGetApi<Place[]>(`/locations`);

  if (loading) return (<h4>Loading</h4>)
  if (error) return (<h4>Error: {error}</h4>)

  return (
      <main>
        <div className="container">
          <div className="row">
            <div className="col-sm">
              <h2 className="float-start">Locations</h2>   
              <Link className="btn btn-secondary float-end" to={`/locations/create`}>Create Location</Link>
              <table className="table">
                <thead>
                  <tr><th>Name</th></tr>
                </thead>
                <tbody>
                {data?.map(location => (
                  <tr key={location.id}>
                    <td><Link to={`/locations/${location.id}`}>{location.name}</Link></td>
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