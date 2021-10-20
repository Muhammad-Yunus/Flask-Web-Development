from datetime import date

def calc_age(birth_year):
    return date.today().year - birth_year

def hello():
    print("\nHello, how are you today?")

    print("May I ask you some question ?")
    answer = input("Answer [y/n] :")

    if answer == "y" : 
        print("What year you were born?")
        year = int(input("Year :"))

        print("If you were born in %d, your current age would be %d." % (year, calc_age(year) ))

hello("John Doe")


