#!/usr/bin/python3
"""contains the class definition of a City"""
from sqlalchemy import Column, Integer, String, Table, ForeignKey
from model_state import Base


class City(Base):
    """Create a table Cities"""

    __tablename__ = "cities"
    id = Column(Integer, unique=True, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(
        Integer,
        ForeignKey("states.id"),
        nullable=False,
    )
