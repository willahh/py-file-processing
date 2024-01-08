import zipfile
import os
import shutil

# Fonction pour extraire le contenu du fichier zip actuel
def extraire_contenu_zip(nom_fichier_zip, dossier_extraction):
    with zipfile.ZipFile(nom_fichier_zip, 'r') as zip_ref:
        zip_ref.extractall(dossier_extraction)

# Fonction pour créer un nouveau fichier zip
def creer_nouveau_zip(nom_nouveau_zip, dossier_contenu):
    with zipfile.ZipFile(nom_nouveau_zip, 'w') as zip_ref:
        for dossier, sous_dossiers, fichiers in os.walk(dossier_contenu):
            for fichier in fichiers:
                chemin_complet = os.path.join(dossier, fichier)
                zip_ref.write(chemin_complet, os.path.relpath(chemin_complet, dossier_contenu))

# Fonction pour copier des fichiers spécifiques
def copier_fichiers_specifiques(source, destination):
    shutil.copyfile(source, destination)

# Traitement du flux actuel
nom_fichier_zip_actuel = "export_20231208.zip"
dossier_extraction = "dossier_extraction"
extraire_contenu_zip(nom_fichier_zip_actuel, dossier_extraction)

# Traitement pour le flux film
# Renommer le fichier zip film
nouveau_nom_fichier_zip_film = "export_AAAAMMJJ.zip"
os.rename(os.path.join(dossier_extraction, nom_fichier_zip_actuel), os.path.join(dossier_extraction, nouveau_nom_fichier_zip_film))

# Supprimer les fichiers spécifiques aux jeux vidéo du nouveau zip film
fichiers_jv_a_supprimer = ["jv_fichier1.txt", "jv_fichier2.csv", ...]  # Listez les fichiers à supprimer
for fichier in fichiers_jv_a_supprimer:
    chemin_fichier = os.path.join(dossier_extraction, nouveau_nom_fichier_zip_film, fichier)
    if os.path.exists(chemin_fichier):
        os.remove(chemin_fichier)

# Traitement pour le flux jeux vidéo
# Créer un nouveau fichier zip jeux vidéo
nouveau_nom_fichier_zip_jv = "export-jv_AAAAMMJJ.zip"
creer_nouveau_zip(nouveau_nom_fichier_zip_jv, dossier_extraction)

# Copier les fichiers spécifiques aux jeux vidéo dans le nouveau zip jeux vidéo
fichiers_jv_a_copier = ["jv_fichier3.txt", "jv_fichier4.csv", ...]  # Listez les fichiers à copier
for fichier in fichiers_jv_a_copier:
    chemin_source = os.path.join(dossier_extraction, fichier)
    if os.path.exists(chemin_source):
        copier_fichiers_specifiques(chemin_source, os.path.join(dossier_extraction, nouveau_nom_fichier_zip_jv, fichier))

# ... Ajoutez d'autres opérations de traitement si nécessaire
