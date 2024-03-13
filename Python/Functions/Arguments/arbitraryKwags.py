#use (**) for unknown number of keyword arguments to be passed in function

def add_ages(**ages):
    sum = 0
    for k, v in ages.items():
        sum += v
    return sum
print("Total: ", add_ages(mtemi=23, skinny=22, ahmed=21))