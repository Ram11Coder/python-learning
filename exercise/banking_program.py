# python banking program

def show_balance(balance):
    print(f"Balance : {balance}")


def deposit():
    amount = float(input("Enter the amount to deposit : "))
    if amount < 0:
        print("Deposit amount can be negative")
        return 0
    else:
        return amount


def withdraw(balance):
    amount = float(input("Enter the amount to withdraw : "))
    if amount > balance:
        print("Insufficient fund")
        return 0
    elif amount < 0:
        print("Amount greater than 0")
        return 0
    else:
        return amount


def main():
    balance = 0
    is_running = True
    while is_running:
        print("     Banking Program     ")
        print("1. Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        choice = input("Enter the choice (1-4) ")
        match choice:
            case '1':
                show_balance(balance)
            case '2':
                balance += deposit()
            case '3':
                balance -= withdraw(balance)
            case '4':
                is_running = False
            case _:
                print("Invalid choice")

    print('Thank you')


if __name__ == '__main__':
    main()
