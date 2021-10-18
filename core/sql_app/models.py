from .database import Base

from sqlalchemy import Column, ForeignKey, Integer, Float, String, Date
from sqlalchemy.orm import relationship

class Team(Base):
    __tablename__ = "teams"
    id = Column(Integer, primary_key=True)
    name = Column(String(255), unique=True)
    city = Column(String(255))
    players = relationship("Player", back_populates="team")


class Player(Base):
    __tablename__ ="players"
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(255))
    last_name = Column(String(255), index=True)
    age = Column(Integer, nullable=False)
    weight = Column(Integer)
    height = Column(Integer)
    position = Column(String(255))
    team_name = Column(String(255), ForeignKey("teams.name"))

    team = relationship("Team", back_populates="players")
