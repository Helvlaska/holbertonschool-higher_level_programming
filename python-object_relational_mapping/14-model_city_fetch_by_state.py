#!/usr/bin/python3
"""Script qui affiche toutes les villes regroupées par État."""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    # Connexion à la BDD
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True
    )

    # Création d'une session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Récupération de tous les États, triés par id
    states = session.query(State).order_by(State.id).all()

    # Parcours des États et affichage des villes associées
    for state in states:
        for city in state.cities:
            print(f"{state.name}: ({city.id}) {city.name}")

    # Fermeture de la session
    session.close()
