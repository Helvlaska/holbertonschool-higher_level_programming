#!/usr/bin/python3
"""Script qui ajoute l'objet 'Louisiane' à la base de données
 et affiche son id."""
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

    # Création d'une nouvelle instance
    new_state = State(name='Louisiana')
    # Ajout de la nouvelle instance à la BDD
    session.add(new_state)
    # Envoie à la BDD
    session.commit()
    # Print l'id de la nouvelle entrée
    print(new_state.id)

    # Fermeture propre de la session
    session.close()
