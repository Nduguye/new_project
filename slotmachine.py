import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLUMNS = 3

symbols_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

values = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

#Function that checks if the user has won
#It takes in the columns, number of lines, bet amount, and symbol values and returns the total winnings
def check_winnings(columns, lines, bet, values):
    winnings = 0
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
    return winnings
    
#We need a function that tells the user which line they have won on
def print_winning_lines(columns, lines):
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            print(f"You won on line {line + 1} with symbol {symbol}!")

#Now we need to create a function to simulate the slot machine spin
#What it does is it randomly selects symbols for each column based on the symbol counts

def get_slot_machine_spin(ROWS, COLUMNS, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            #We use _ because we don't need the actual index
            all_symbols.append(symbol)

    columns = []
    for _ in range(COLUMNS):
        column = []
        current_symbols = all_symbols[:]
        #We use slicing to create a copy of all_symbols
        for _ in range(ROWS):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)   
    return columns     

#Now we need to create a function to print the slot machine
#What it does is it takes in the columns and prints them out in a way that looks like a slot machine
def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        print()

def deposit():
    while True:
        amount = input("What amount would you like to bet? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Please enter a positive amount.")
        else:
            print("Please enter a valid number.")
    return amount

def get_number_of_lines():
    while True:
        lines = input("Enter number of lines to bet on (1-3): ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Please enter a valid number of lines.")
        else:
            print("Please enter a valid number.")
    return lines

def get_bet():
    while True:
        amount = input(f"What amount would you like to bet on each line? ${MIN_BET}-${MAX_BET} ")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} and ${MAX_BET}.")
        else:
            print("Please enter a valid number.")
    return amount
def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"You do not have enough to bet that amount, your current balance is: ${balance}")
        else:
            break

    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")

    slots = get_slot_machine_spin(ROWS, COLUMNS, symbols_count)
    print_slot_machine(slots)

    winnings = check_winnings(slots, lines, bet, values)
    print(f"You won ${winnings}")
    print_winning_lines(slots, lines)

    balance += winnings - total_bet
    print(f"Your balance is now ${balance}")
    return balance

def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press enter to spin (q to quit).")
        if answer == "q":
            break
        balance = spin(balance)

        print(f"You left with ${balance}")

main()
