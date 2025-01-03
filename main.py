import sys
import os
import requests
from pathlib import Path
from utils.helper import Utils
from utils.gui import GUI

# https://raw.githubusercontent.com/asyary/PBO_UAS/refs/heads/master/db.db
APP_NAME = "Kereta KJT"

appdata_path = os.path.join(os.getenv('APPDATA'), APP_NAME)
os.makedirs(appdata_path, exist_ok=True) # Just in case dir don't exist

local_db_path = Path(appdata_path) / "db.db"
db_url = "https://raw.githubusercontent.com/asyary/PBO_UAS/refs/heads/master/db.db"

if not local_db_path.exists():
    try:
        print("Downloading database...")
        response = requests.get(db_url)
        response.raise_for_status()
        with open(local_db_path, "wb") as db_file:
            db_file.write(response.content)
        print("Database downloaded successfully.")
    except Exception as e:
        print(f"Failed to download the database: {e}")
        exit(1)

def init():
	if Utils.cek_koneksi():
		print("Berhasil terhubung ke database")
	else:
		sys.exit("Error: Tidak dapat terhubung ke database")
	GUI()

if __name__ == "__main__":
    init()