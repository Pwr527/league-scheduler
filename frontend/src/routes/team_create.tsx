import { useEffect, useState } from "react";
import { SubmitHandler, useForm } from "react-hook-form";
import { Team } from "../types";
import { createApiObject } from "../util";

export default function TeamCreate() {
  const { register, handleSubmit } = useForm<Team>();
  const [ team, setTeam ] = useState<Team>();
  const [ loading, setLoading ] = useState(true);
  const [ error, setError ] = useState("");

  const onSubmit: SubmitHandler<Team> = async(team) => {
    const { data, loading, error } = await createApiObject<Team>('/teams', team)
    setTeam(data);
    setLoading(loading);
    if (error) { setError(error); }
  }

  if (error) return (<h4>{error}</h4>)
  return ( 
    <main>
      <h4>Create Team</h4>
      <form onSubmit={handleSubmit(onSubmit)}>
        <div className="mb-3">
          <label htmlFor="name" className="form-label">Team name</label>
          <input type="text" className="form-control" 
              id="name" 
              placeholder="Team name"
              {...register("name")} />
        </div>
        <button type="submit" className="btn btn-primary">Submit</button>
      </form>
    </main>
  )

}