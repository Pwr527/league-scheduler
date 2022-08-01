from pathlib import Path
from itertools import combinations
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ARRAY, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from varname import nameof
from scheduler import db
from dataclasses import dataclass


@dataclass
class Location(db.Model):
    __tablename__ = "location"
    
    id: int
    name: str
    available_times: str

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    available_times = Column(ARRAY(String))

    def __init__(self, name, available_times=['5pm', '7pm']):
        self.name = name
        self.available_times = available_times
    def __str__(self):
        return self.name


@dataclass
class Game(db.Model):
    __tablename__ = "game"

    id = Column(Integer, primary_key=True)
    team1_id = db.Column(Integer, ForeignKey('team.id'), nullable=False)
    team2_id = db.Column(Integer, ForeignKey('team.id'), nullable=False)
    location = relationship(nameof(Location))
    location_id = db.Column(Integer, ForeignKey('location.id'), nullable=False)
    time = Column(DateTime)

    def __init__(self, team1, team2, location, time):
        self.team1 = team1
        self.team2 = team2
        self.location = location
        self.time = time
    def __str__(self):
        return f"{self.time} - {self.location.name} - {self.team1.name} vs {self.team2.name} "
    

@dataclass
class Scheduler:
    def __init__(self, teams, location):
        self.teams = teams
        self.location = location
        self.schedule = []
        
    def schedule_games(self):
        for t1, t2 in combinations(set(self.teams), 2):
            location, game_time = self.get_next_available_time()
            self.schedule.append(Game(t1, t2, location, game_time))
        return self.schedule

    def get_next_available_time(self):
        for l in self.location:
            if len(l.available_times) > 0:
                return l, l.available_times.pop(0)
        raise Exception("Not enough available timeslots!") 


@dataclass
class Team(db.Model):
    __tablename__ = "team"

    id: int
    name: str

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return self.name

