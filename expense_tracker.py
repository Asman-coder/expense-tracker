import csv
import os
from datetime import datetime

FILE_NAME = "expenses.csv"

# File ko check karo, agar nahi hai toh header ke saath banao
def init_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=['Date', 'Category', 'Amount', 'Note'])
            writer.writeheader()

def add_expense():
    try:
        amount = float(input("Amount kitna hai? (e.g., 120.5): "))
        category = input("Category? (Food, Travel, Study, Other): ").strip()
        note = input("Note (e.g., Swiggy, Bus): ").strip()
        date = datetime.now().strftime("%Y-%m-%d")

        with open(FILE_NAME, 'a', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=['Date', 'Category', 'Amount', 'Note'])
            writer.writerow({'Date': date, 'Category': category, 'Amount': amount, 'Note': note})
        print("\n✅ Expense Save ho gaya!\n")

    except ValueError:
        print("\n❌ Error: Amount me sirf number daalo!\n") 
    except Exception as e:
        print(f"\n❌ Kuch galat hua: {e}\n")

def view_expenses():
    if not os.path.exists(FILE_NAME):
        print("Koi data nahi hai abhi.")
        return
    
    with open(FILE_NAME, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        expenses = list(reader)
        if not expenses:
            print("Koi expense nahi mila.")
            return
        print("\n--- Saare Expenses ---")
        for row in expenses:
            print(f"{row['Date']} | {row['Category']} | Rs.{row['Amount']} | {row['Note']}")
        print("----------------------\n")

def monthly_summary():
    from collections import defaultdict
    try:
        current_month = datetime.now().strftime("%Y-%m")
        total = 0
        category_total = defaultdict(float)
        with open(FILE_NAME, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row['Date'].startswith(current_month):
                    amt = float(row['Amount'])
                    total += amt
                    category_total[row['Category']] += amt
        
        print(f"\n📊 {current_month} ka Report:")
        for cat, amt in category_total.items():
            print(f"  {cat}: Rs.{amt}")
        print(f"  Total: Rs.{total}\n")
    except Exception as e:
        print(f"Error: {e}")
def main():
    init_file()
    while True:
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Monthly Summary")
        print("4. Exit")
        choice = input("Choose karo (1-4): ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            monthly_summary()
        elif choice == '4':
            print("Bye! Paisa bachao.")
            break
        else:
            print("Galat choice!")

if __name__ == "__main__":
    main()