─────┬──────────────────────────────────────────────────────────────────────────────────
     │ File: main.py
─────┼──────────────────────────────────────────────────────────────────────────────────
   1 │ from crud import *
   2 │ from budget import *
   3 │ from report import *
   4 │ from ui import *
   5 │ from backup import backup_database
   6 │
   7 │ data = load_data()
   8 │
   9 │ while True:
  10 │     logo()
  11 │     menu()
  12 │     pilih = input("Pilih Menu: ")
  13 │     if  pilih == "1":
  14 │         add_transaction(data)
  15 │     elif pilih == "2":
  16 │         show_transaction(data)
  17 │     elif pilih == "3":
  18 │         delete_transaction(data)
  19 │     elif pilih == "4":
  20 │         budget_analysis(data)
  21 │     elif pilih == "5":
  22 │         spending_speed(data)
  23 │     elif pilih == "6":
  24 │         export_report(data)
  25 │     elif pilih == "7":
  26 │         backup_database()
  27 │     else:
  28 │         print("Sampai Jumpai 👋")
  29 │         break
  30 │     input("/nTekan Enter...")