 1 from datetime import datetime
 2
 3 def total_income(data):
 4     return sum(
 5         trx["amount"]
 6         for trx in data["transactions"]
 7         if trx.get("type", "").lower() == "income"
 8     )
 9 def total_expense(data):
10     return sum(
11         trx["amount"]
12         for trx in data["transactions"]
13         if trx.get("type", "").lower() == "expense"
14     )
15
16 def remaining_balance(data):
17     return total_income(data) - total_expense(data)
18
19 def budget_analysis(data):
20     income = total_income(data)
21     spent = total_expense(data)
22     percentage = 0
23     if income > 0:
24         percentage = (spent / income) * 100
25     print("\n===== Analysis Data =====")
26     print(f"Pendapatan  : Rp {income:,.0f}")
27     print(f"Pengeluaran : Rp {spent:,.0f}")
28     print(f"Sisa Dana   : Rp {income - spent:,.0f}")
29     print(f"Terpakai    : {percentage:.1f}%")
30     if percentage >= 85:
31         print("⚠️ Budget hampir habis.")
32     elif percentage >= 70:
33         print("⚠️ Mulai hemat.")
34     else:
35         print("✅ Kondisi aman.")
36
37 def spending_speed(data):
38     today = datetime.now().day
39     spent = sum(
40         trx["amount"]
41         for trx in data["transactions"]
42         if trx.get("type", "").lower == "expense"
43     )
44     daily_avg = spent / today
45     print("\n===== Kecepatan Belaja =====")
46     print(f"Rata-rata per hari: Rp {daily_avg:,.0f}")
47     prediction = daily_avg * 30
48     print(f"Prediksi Akhir Bulan: Rp {prediction:,.0f}")
49     income = data["profile"]["monthly_income"]
50     if prediction > income:
51         print("⚠️ Kemungkinan Over-Budget!")
52     else:
53         print("✅ Masih dalam batas aman.")
54
         