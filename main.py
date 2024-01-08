import zipfile
import os
import shutil

zip_file_path = 'static/export_20211007.zip'

def extraire_contenu_zip(nom_fichier_zip, dossier_extraction):
    """
    Extrait le contenu d'un fichier zip
    """
    with zipfile.ZipFile(nom_fichier_zip, 'r') as zip_ref:
        zip_ref.extractall(dossier_extraction)
        
def creer_nouveau_zip(nom_nouveau_zip, dossier_contenu):
    """
    Créer un nouveau fichier zip
    """
    with zipfile.ZipFile(nom_nouveau_zip, 'w') as zip_ref:
        for dossier, sous_dossiers, fichiers in os.walk(dossier_contenu):
            for fichier in fichiers:
                chemin_complet = os.path.join(dossier, fichier)
                zip_ref.write(chemin_complet, os.path.relpath(chemin_complet, dossier_contenu))
 
def copier_fichiers(source, destination):
    """
    Copier des fichiers
    """              
    shutil.copyfile(source, destination)



# Traitement du flux actuel
nom_fichier_zip_actuel = "export_20231208.zip"
dossier_extraction = "static/extract_tmp"
extraire_contenu_zip("static/" + nom_fichier_zip_actuel, dossier_extraction)

  
  
"""
Bloc de commentaire non exécuté 
# extraire_contenu_zip(zip_file_path, 'static/tmp')

# with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
#     file_list = zip_ref.namelist();
#     print("a", file_list);
    
#     for file_name in file_list:
#         print("a", file_name)
"""
     


print("Output");
