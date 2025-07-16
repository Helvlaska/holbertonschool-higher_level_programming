def generate_invitations(template, attendees):
    # Vérifie le type de template
    if not isinstance(template, str):
        print("Erreur : le template doit être une chaîne de caractères.")
        return

    # Vérifie que attendees est bien une liste
    attendees_is_list = isinstance(attendees, list)

    # Création du variable booléenne pour savoir si c'est un dictionnaire
    all_elements_are_dicts = True

    # Vérifie si la liste contient des dictionnaires
    if attendees_is_list:
        # Boucle pour parcourir tout les éléments de la liste
        for element in attendees:
            # Vérifie si l'élément est un dictionnaire
            if not isinstance(element, dict):
                all_elements_are_dicts = False
                break
    else:
        all_elements_are_dicts = False

    # Affiche un message et on quitte la fonction si un des deux est faux
    if not attendees_is_list or not all_elements_are_dicts:
        print("Erreur : attendees doit être une liste de dictionnaires.")
        return

    # Vérifie si le template est vide
    if template.strip() == "":
        print("Template is empty, no output files generated.")
        return

    # Vérifie si la liste est vide
    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return

    # Boucle sur chaque invité avec un index qui commence à 1
    for index, person in enumerate(attendees, start=1):
        # On commence avec le contenu brut du template
        personalized = template

        # Liste des clés à remplacer
        keys = ['name', 'event_title', 'event_date', 'event_location']

        # Pour chaque clé, on remplace dans le texte
        for key in keys:
            value = person.get(key)  # récupère la valeur associée à la clé
            if value is None:
                value = "N/A"
            personalized = personalized.replace("{" + key + "}", str(value))

        # Nom du fichier de sortie
        filename = f"output_{index}.txt"

        # Écriture du fichier
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(personalized)
            print(f"✅ Fichier '{filename}' généré.")
        except Exception as e:
            print(f"Erreur lors de l’écriture de '{filename}': {e}")
