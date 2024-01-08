import zipfile
import os

zip_file_path = 'static/export_20211007.zip'

def extraire_contenu_zip(nom_fichier_zip, dossier_extraction):
    with zipfile.ZipFile(nom_fichier_zip, 'r') as zip_ref:
        zip_ref.extractall(dossier_extraction)
        
  
extraire_contenu_zip(zip_file_path)

# with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
#     file_list = zip_ref.namelist();
#     print("a", file_list);
    
#     for file_name in file_list:
#         print("a", file_name)
        


print("Output");
