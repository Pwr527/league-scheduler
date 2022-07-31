from pathlib import Path
from itertools import combinations
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from varname import nameof
from scheduler import db

class Place(db.Model):
    __tablename__ = "place"
    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __init__(self, name, available_times=None):
        self.name = name
        self.available_times = available_times
    def __str__(self):
        return self.name
    
class Game(db.Model):
    __tablename__ = "game"
    id = Column(Integer, primary_key=True)
    team1_id = db.Column(Integer, ForeignKey('team.id'), nullable=False)
    team2_id = db.Column(Integer, ForeignKey('team.id'), nullable=False)
    place = relationship(nameof(Place))
    place_id = db.Column(Integer, ForeignKey('place.id'), nullable=False)
    time = Column(DateTime)

    def __init__(self, team1, team2, place, time):
        self.team1 = team1
        self.team2 = team2
        self.place = place
        self.time = time
    def __str__(self):
        return f"{self.time} - {self.place.name} - {self.team1.name} vs {self.team2.name} "
    

class Scheduler:
    def __init__(self, teams, place):
        self.teams = teams
        self.place = place
        self.schedule = []
        
    def schedule_games(self):
        for t1, t2 in combinations(set(self.teams), 2):
            place, game_time = self.get_next_available_time()
            self.schedule.append(Game(t1, t2, place, game_time))
        return self.schedule

    def get_next_available_time(self):
        for l in self.place:
            if len(l.available_times) > 0:
                return l, l.available_times.pop(0)
        raise Exception("Not enough available timeslots!") 


class Team(db.Model):
    __tablename__ = "team"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return self.name

