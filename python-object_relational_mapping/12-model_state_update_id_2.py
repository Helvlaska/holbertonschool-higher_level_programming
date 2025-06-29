#!/usr/bin/python3
"""Script qui change le nom d'un objet State de la BDD."""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Création de la connexion
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True
    )

    # Création de toutes les tables si elles n'existent pas
    # (id, name de la classe State)
    Base.metadata.create_all(engine)

    # Création d'une session (pour lire et écrire dans une BDD)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Modification du nom de l'objet
    state = session.get(State, 2)

    # Vérifie si l'objet existe, et si oui le modifie
    if state:
        state.name = 'New Mexico'
        session.commit()

    # Fermeture propre de la session
    session.close()
