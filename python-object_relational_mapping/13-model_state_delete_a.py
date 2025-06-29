#!/usr/bin/python3
"""Script qui supprime un objet de la BDD."""
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

    # Suppression de l'objet dans la BDD
    states_to_delete = (
        session.query(State)
        .filter(State.name.like('%a%'))
        .all()
    )
    # Mise à jour de la BDD
    for state in states_to_delete:
        session.delete(state)
        session.commit()

    # Fermeture propre de la session
    session.close()
