#!/usr/bin/python3
"""Définit la classe City pour mapper la table 'cities'."""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

# Import de la base déjà déclarée dans model_state.py
from model_state import Base


class City(Base):
    """Classe City liée à la table 'cities'."""
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
