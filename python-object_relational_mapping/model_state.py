#!/usr/bin/python3
"""
Définit la classe State qui représente la table 'states' dans la base de
données, en utilisant SQLAlchemy comme ORM.
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


Base = declarative_base()


class State(Base):
    """
    Classe représentant un état américain.

    Hérite de Base pour créer une table 'states' via SQLAlchemy.
    Attributs :
        id (int) : Identifiant unique de l'état, clé primaire.
        name (str) : Nom de l'état, non nul, chaîne de max 128 caractères.
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)

    # Relation avec la table 'cities' (déclarée dans model_city.py)
    cities = relationship("City", backref="state", cascade="all, delete")
