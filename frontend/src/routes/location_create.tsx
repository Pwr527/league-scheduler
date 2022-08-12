import { useEffect, useState } from "react";
import { SubmitHandler, useForm } from "react-hook-form";
import { Place } from "../types";
import { createApiObject } from "../util";

export default function LocationCreate() {
  const { register, handleSubmit } = useForm<Place>();
  const [ team, setPlace ] = useState<Place>();
  const [ loading, setLoading ] = useState(true);
  const [ error, setError ] = useState("");

  const onSubmit: SubmitHandler<Place> = async(location) => {
    const { data, loading, error } = await createApiObject<Place>('/locations', location)
    setPlace(data);
    setLoading(loading);
    if (error) { setError(error); }
  }

  if (error) return (<h4>{error}</h4>)
  return ( 
    <main>
      <h4>Create Location</h4>
      <form onSubmit={handleSubmit(onSubmit)}>
        <div className="mb-3">
          <label htmlFor="name" className="form-label">Location name</label>
          <input type="text" className="form-control" 
              id="name" 
              placeholder="Location name"
              {...register("name")} />
        </div>
        <div className="mb-3">
          <label htmlFor="available_times" className="form-label">Available times</label>
          <input type="text" className="form-control" 
              id="available_times" 
              placeholder="Available times"
              {...register("available_times")} />
        </div>
        <button type="submit" className="btn btn-primary">Submit</button>
      </form>
    </main>
  )

}