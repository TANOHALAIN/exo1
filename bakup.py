#!/usr/bin/env python3
import os
import subprocess
from datetime import datetime

# Configuration
DB_USER = "wordpress"
DB_PASSWORD = "wordpress"
DB_NAME = "wordpress"
DB_BACKUP_PATH = "/home/vagrant/sauvegarde/mariadb.sql.gz"

SITE_FILES_PATH = "/var/www/html/wordpress"
SITE_BACKUP_PATH = "/home/vagrant/sauvegarde/wp-content.tar.gz"

CONFIG_FILES_PATH = "/etc/nginx/conf.d/"
CONFIG_BACKUP_PATH = "/home/vagrant/sauvegarde/nginx.tar.gz"

DATE = datetime.now().strftime("%Y%m%d%H%M")

# Fonction pour exécuter une commande shell et gérer les erreurs
def run_command(command):
    try:
        subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True)
    except subprocess.CalledProcessError as e:
        print(f"Erreur lors de l'exécution de la commande {command}:")
        print(e.output.decode())
        exit(1)

# Créer les répertoires de sauvegarde si nécessaire
os.makedirs(DB_BACKUP_PATH, exist_ok=True)
os.makedirs(SITE_BACKUP_PATH, exist_ok=True)
os.makedirs(CONFIG_BACKUP_PATH, exist_ok=True)

# Sauvegarde de la base de données
dump_cmd = f"mysqldump -u {DB_USER} -p{DB_PASSWORD} {DB_NAME} | gzip > '{DB_BACKUP_PATH}/{DB_NAME}-{DATE}.sql.gz'"
run_command(dump_cmd)

# Sauvegarde des fichiers du site
tar_site_cmd = f"tar -czf '{SITE_BACKUP_PATH}/site-{DATE}.tar.gz' -C '{SITE_FILES_PATH}' ."
run_command(tar_site_cmd)

# Sauvegarde des fichiers de configuration
tar_config_cmd = f"tar -czf '{CONFIG_BACKUP_PATH}/config-{DATE}.tar.gz' -C '{CONFIG_FILES_PATH}' ."
run_command(tar_config_cmd)

print("Sauvegarde terminée avec succès.")
