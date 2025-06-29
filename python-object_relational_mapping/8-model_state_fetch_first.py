#!/usr/bin/python3
"""Script qui affiche l'id 1 de State de la base de données."""
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

    # Requête pour récupérer l'état avec id = 1
    state = session.query(State).filter(State.id == 1).first()

    # Vérification du résultat
    if state is None:
        print("Nothing")
    else:
        print(f"{state.id}: {state.name}")

    # Fermeture propre de la session
    session.close()
