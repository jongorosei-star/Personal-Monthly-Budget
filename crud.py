import json
import os
from datetime import datetime

DB_FILE = "database.json"

def load_data():
    if not os.path.exists(DB_FILE):
        return {}
    with open(DB_FILE, "r") as file:
        return json.load(file)

def save_data(data):
    with open(DB_FILE, "w") as file:
        json.dump(data, file, indent=4)

def generate_id(data):
    total = len(data["transactions"]) + 1
    return f"EXP{total:03}"

def add_transaction(data):
    amount = data["profile"]["monthly_income"]
    trx_type = input(
        "Type (income/expense): "
    ).strip().lower()
    amount = float(input("Jumlah: "))
    category = input("Kategori: ")
    description = input("Deskripsi: ")

    transaction = {
        "id": generate_id(data),
        "date": datetime.now().strftime("%Y-%m-%d"),
        "type": trx_type,
        "amount": amount,
        "category": category,
        "description": description
    }
    data["transactions"].append(transaction)
    save_data(data)
    print("Transaksi berhasil ditambahkan.")

def show_transaction(data):
    for trx in data["transactions"]:
        print("-" * 80)
        print(f"ID        : {trx['id']}")
        print(f"Tanggal   : {trx['date']}")
        print(f"Jumlah    : {trx['amount']:,.0f}")
        print(f"Kategori  : {trx['category']}")
        print(f"Deskripsi : {trx['description']}")

def delete_transaction(data):
    trx_id = input("Masukan ID: ")
    data["transactions"] = [
        trx
        for trx in data["transactions"]
        if trx["id"] != trx_id
    ]
    save_data(data)
