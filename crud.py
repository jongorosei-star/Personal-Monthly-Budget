 1 import json
 2 import os
 3 from datetime import datetime
 4
 5 DB_FILE = "database.json"
 6
 7 def load_data():
 8     if not os.path.exists(DB_FILE):
 9         return {}
10     with open(DB_FILE, "r") as file:
11         return json.load(file)
12
13 def save_data(data):
14     with open(DB_FILE, "w") as file:
15         json.dump(data, file, indent=4)
16
17 def generate_id(data):
18     total = len(data["transactions"]) + 1
19     return f"EXP{total:03}"
20
21 def add_transaction(data):
22     amount = data["profile"]["monthly_income"]
23     trx_type = input(
24         "Type (income/expense): "
25     ).strip().lower()
26     amount = float(input("Jumlah: "))
27     category = input("Kategori: ")
28     description = input("Deskripsi: ")
29
30     transaction = {
31         "id": generate_id(data),
32         "date": datetime.now().strftime("%Y-%m-%d"),
33         "type": trx_type,
34         "amount": amount,
35         "category": category,
36         "description": description
37     }
38     data["transactions"].append(transaction)
39     save_data(data)
40     print("Transaksi berhasil ditambahkan.")
41
42 def show_transaction(data):
43     for trx in data["transactions"]:
44         print("-" * 80)
45         print(f"ID        : {trx['id']}")