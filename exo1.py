#!/usr/bin/env python3

import os
import zipfile

def backup_files(files_list, output_zip):
    # Création du fichier zip
    with zipfile.ZipFile(output_zip, 'w', zipfile.ZIP_DEFLATED) as z:
        added_files = set()  # Utilisation d'un ensemble pour éviter les doublons
        for file_path in files_list:
            if os.path.exists(file_path):
                add_file_to_zip(z, file_path, added_files)
            else:
                print(f"Le fichier {file_path} n'existe pas et ne sera pas inclus dans la sauvegarde.")

def add_file_to_zip(zipfile_obj, file_path, added_files):
    base_name = os.path.basename(file_path)
    if base_name not in added_files:
        # Utiliser os.path.relpath pour obtenir le chemin relatif basé sur le répertoire du fichier zip
        relative_path = os.path.relpath(file_path, start=os.path.dirname(zip_filename))
        zipfile_obj.write(file_path, arcname=relative_path)
        added_files.add(base_name)
        print(f"Added {base_name}")
    else:
        print(f"Skipping duplicate file: {base_name}")

# Définition des chemins des fichiers à sauvegarder
files_to_backup = [
    "/var/log/nginx/access.log",
    "/var/log/nginx/error.log",
    # Ajoutez plus de fichiers selon vos besoins
]

# Nom du fichier zip de sortie
zip_filename = "/root/exercice1_TANOH_Alain.zip"
backup_files(files_to_backup, zip_filename)

print(f"Sauvegarde terminée, fichier créé : {zip_filename}")
