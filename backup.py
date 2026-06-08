import shutil
from datetime import datetime
def backup_database():
    backup_name = (
      f"backup/database_"
      f"{datetime.now().strftime('%Y%m%d-%H%M%S')}.json"
    )
    shutil.copy("database.json", backup_name)
    print("Backup berhasil dibuat.")
