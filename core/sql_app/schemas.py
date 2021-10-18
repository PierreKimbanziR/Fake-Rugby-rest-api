from pydantic import BaseModel
from typing import  List

class PlayerBase(BaseModel):
    first_name : str 
    last_name : str
    age : int
    weight: int 
    height: int 
    position: str 

class PlayerCreate(PlayerBase):
    pass

class Player(PlayerBase):
    id  : int
    team_name : str

    class Config:
        orm_mode  = True

class TeamBase(BaseModel):
    name: str
    city: str

class TeamCreate(TeamBase):
    pass 

class Team(TeamBase):
    id : int
    players : List[Player] = []

    class Config:
        orm_mode = True
