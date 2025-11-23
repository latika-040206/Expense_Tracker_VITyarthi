expenses = []
def add_expense():
    amount = float(input("Enter amount:"))
    category = input("Enter category(food,travel,etc):")
    date = input("Enter date(DD/MM/YYYY):")
    expense = {
        "amount":amount,
        "category":category,
        "date": date
    }
    expenses.append(expense)
    print("Expense added successfully!\n")
def  view_expenses():
     if len(expenses)== 0:
            print("No expenses recorded.\n")
            return
     print("\n---All Expenses---")
     for e in expenses:
         print(f"Amount: {e['amount']} | category: {e['category']} | Date:{e['date']}")
         print()
def total_expenses():
     total = sum(e['amount'] for e in expenses)  
     print(f"\n Total Expenses: {total}\n")
def main():
      while True:
            print("1.Add Expense")
            print("2.view Expenses")
            print("3.Total Expenses")
            print("4.Exit")
            choice = input("Enter your choice:")
            if choice == "1":
             add_expense()
            elif choice == "2":
             view_expenses()
            elif choice == "3":
             total_expenses()
            elif  choice == "4":
             print("Exiting...")
             break
            else:
              print("Invalid choice,try again.\n")
main()                            
                            