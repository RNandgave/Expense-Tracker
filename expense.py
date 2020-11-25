from datetime import datetime


def track():
    with open("db.txt", 'r', encoding='utf-8') as f:
        N = len(f.read().split('\n'))
    while 4:
        print("""Select Options:
            1. Add Expense
            2. Delete Expense
            3. Display Expense List
            4. Exit""")
        ch = int(input())
        if ch == 1:
            print("Enter Expense Title")
            title = input()
            print("Enter 1 to select current time or 2 for custom time")
            op = int(input())
            if op == 1:
                date = datetime.now().strftime("%D - %H:%M:%S")
            else:
                date = input()
            print("Enter Amount")
            amount = float(input())
            print("Enter Tags")
            tag = input().split()
            with open("db.txt", 'a', encoding='utf-8') as f:
                N = N+1
                f.write(f'{N+1}, {title}, {date}, {amount}, {tag}'+'\n')

        elif ch == 2:
            print("Enter task id to delete the task")
            task_id = int(input())
            with open("db.txt", 'r', encoding='utf-8') as f:
                N = f.read.split('\n')
            with open("db.txt", "w", encoding="utf-8") as f:
                f.write(N[:task_id])
                f.write(N[task_id+1:])

        elif ch == 3:
            print("THE LIST OF EXPENSES")
            with open("db.txt", encoding="utf-8") as f:
                print(f"{f.read()}")

        elif ch == 4:
            exit()


if __name__ == "__main__":
    track()
