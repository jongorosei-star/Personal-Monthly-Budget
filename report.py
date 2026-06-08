from datetime import datetime

def export_report(data):
    filename = (
        f"export/report_"
        f"{datetime.now().strftime('%Y%m%d')}.txt"
    )
    total = sum(
        trx["amount"]
        for trx in data["transactions"]
    )
    with open(filename, "w") as file:
        file.write("MONTHLY BUDGET REPORT\n")
        file.write("=" * 40 + "\n\n")
        for trx in data["transacsion"]:
            file.write(
                f"{trx['date']} | ",
                f"{trx['category']} | ",
                f"Rp {trx['amount']:,.0f}"
            )
