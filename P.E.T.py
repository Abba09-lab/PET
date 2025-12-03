import csv
from datetime import date
f = "expenses.csv"


def func1(a, c, d=""):
    t = date.today().strftime("%Y-%m-%d")
    with open(f, "a", newline="") as x:
        w = csv.writer(x)
        w.writerow([t, c, a, d])


def func2():
    try:
        with open(f, "r") as x:
            r = csv.reader(x)
            for y in r:
                print(y)
    except FileNotFoundError:
        pass


def func3():
    tot = 0
    cat = {}
    try:
        with open(f, "r") as x:
            r = csv.reader(x)
            for y in r:
                amt = float(y[2])
                tot += amt
                cat[y[1]] = cat.get(y[1], 0) + amt
        print(tot)
        print(cat)
    except FileNotFoundError:
        pass


def main():
    while True:
        print("1")
        print("2")
        print("3")
        print("4")
        ch = input()
        if ch == "1":
            a = input()
            if not a.replace(".", "", 1).isdigit():
                continue
            c = input()
            d = input()
            func1(a, c, d)
        elif ch == "2":
            func2()
        elif ch == "3":
            func3()
        elif ch == "4":
            break


main()
