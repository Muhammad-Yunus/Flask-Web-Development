from datetime import date

def calc_age(birth_year):
    return date.today().year - birth_year

def hello_your_age():
    print("\nHello, how are you today?")

    print("May I ask you some question ?")
    answer = input("Answer [y/n] :")

    if answer == "y" : 
        print("What year you were born?")
        year = int(input("Year :"))

        print("If you were born in %d, your current age would be %d." % (year, calc_age(year) ))

def hello_father_age():
    print("\nHello how are you today?")

    print("May I ask you some question ?")
    answer = input("Answer [y/n] :")

    if answer == "y" : 
        print("What year was you father born?")
        year = int(input("Year :"))

        print("If your father was born in %d, his current age is %d years." % (year, calc_age(year) ))

hello_your_age()
hello_father_age()
