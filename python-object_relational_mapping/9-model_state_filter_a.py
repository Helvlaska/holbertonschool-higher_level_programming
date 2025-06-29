#!/usr/bin/python3
"""Script qui liste tous les objets State qui continnent la lettre 'a'."""
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

    # Requête pour la récupération de tout les pays
    states = session.query(State).filter(State.name.like('%a%')).order_by(State.id).all()

    # Boucle pour print les résultats de la requête
    for state in states:
        print(f"{state.id}: {state.name}")

    # Fermeture propre de la session
    session.close()
