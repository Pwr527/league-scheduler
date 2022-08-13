

import React from 'react';
import ReactDOM from 'react-dom/client';
import { BrowserRouter, Routes, Route } from "react-router-dom";
import App from './App';
import Locations from "./routes/locations";
import Teams from "./routes/teams";
import Schedules from "./routes/schedules";
import Home from './routes/home';
import TeamDetail from './routes/team_detail';
import LocationDetail from './routes/location_detail';
import TeamCreate from './routes/team_create';
import LocationCreate from './routes/location_create';

const root = ReactDOM.createRoot(
  document.getElementById('root') as HTMLElement
);

root.render(
  <React.StrictMode>
  <BrowserRouter>
    <Routes>
      <Route path="/" element={<App />}>
        <Route index element={<Home/>}/>
        <Route path="locations" element={<Locations/>}>
          <Route path="create" element={<LocationCreate/>}/>
          <Route path=":id" element={<LocationDetail/>}/>
        </Route>
        <Route path="teams" element={<Teams />}>
          <Route path="create" element={<TeamCreate/>}/>
          <Route path=":id" element={<TeamDetail/>}/>
        </Route>
        <Route path="schedules" element={<Schedules />} />
        <Route path="*" element={<div><h2>Not Found</h2></div>}/>
      </Route>
    </Routes>
  </BrowserRouter>
</React.StrictMode>
);
