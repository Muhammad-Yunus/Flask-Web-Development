from datetime import date

def calc_age(birth_year):
    return date.today().year - birth_year


def hello(func): 
    # Function decorator "hello()" need a child function "warpper()" to be returned 
    def wrapper():
        print("\nHello, how are you today?")
        print("May I ask you some question ?")
        answer = input("Answer [y/n] :")
        if answer == "y" : 
            func()
    return wrapper

# use decorators in a simpler way with the @ symbol called the “pie” syntax
@hello
def your_age():
    print("What year you were born?")
    year = int(input("Year :"))

    print("If you were born in %d, your current age would be %d." % (year, calc_age(year) ))

@hello
def your_father_age():
    print("What year was you father born?")
    year = int(input("Year :"))

    print("If your father was born in %d, his current age is %d years." % (year, calc_age(year) ))

# decorators wrap a function, modifying its behavior.
your_age()
your_father_age()

