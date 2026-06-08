 
from crud import *
from budget import *
from report import *
from ui import *
from backup import backup_database

data = load_data()

while True:
     logo()
     menu()
     pilih = input("Pilih Menu: ")
     if  pilih == "1":
          add_transaction(data)
     elif pilih == "2":
          show_transaction(data)
     elif pilih == "3":
          delete_transaction(data)
     elif pilih == "4":
          budget_analysis(data)
     elif pilih == "5":
          spending_speed(data)
     elif pilih == "6":
          export_report(data)
     elif pilih == "7":
          backup_database()
     else:
          print("Sampai Jumpai 👋")
          break
          
input("/nTekan Enter...")
