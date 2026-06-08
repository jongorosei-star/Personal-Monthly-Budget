 1 import shutil
 2 from datetime import datetime
 3
 4 def backup_database():
 5     backup_name = (
 6         f"backup/database_"
 7         f"{datetime.now().strftime('%Y%m%d-%H%M%S')}.json"
 8     )
 9     shutil.copy(
10         "database.json",
11         backup_name
12     )
13     print("Backup berhasil dibuat")