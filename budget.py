 from datetime import datetime

 def total_income(data):
     return sum(
         trx["amount"]
         for trx in data["transactions"]
         if trx.get("type", "").lower() == "income"
     )
 def total_expense(data):
     return sum(
         trx["amount"]
         for trx in data["transactions"]
         if trx.get("type", "").lower() == "expense"
     )

 def remaining_balance(data):
     return total_income(data) - total_expense(data)

 def budget_analysis(data):
     income = total_income(data)
     spent = total_expense(data)
     percentage = 0
     if income > 0:
         percentage = (spent / income) * 100
     print("\n===== Analysis Data =====")
     print(f"Pendapatan  : Rp {income:,.0f}")
     print(f"Pengeluaran : Rp {spent:,.0f}")
     print(f"Sisa Dana   : Rp {income - spent:,.0f}")
     print(f"Terpakai    : {percentage:.1f}%")
     if percentage >= 85:
         print("⚠️ Budget hampir habis.")
     elif percentage >= 70:
         print("⚠️ Mulai hemat.")
     else:
         print("✅ Kondisi aman.")

 def spending_speed(data):
     today = datetime.now().day
     spent = sum(
         trx["amount"]
         for trx in data["transactions"]
         if trx.get("type", "").lower == "expense"
     )
     daily_avg = spent / today
     print("\n===== Kecepatan Belaja =====")
     print(f"Rata-rata per hari: Rp {daily_avg:,.0f}")
     prediction = daily_avg * 30
     print(f"Prediksi Akhir Bulan: Rp {prediction:,.0f}")
     income = data["profile"]["monthly_income"]
     if prediction > income:
         print("⚠️ Kemungkinan Over-Budget!")
     else:
         print("✅ Masih dalam batas aman.")

         
