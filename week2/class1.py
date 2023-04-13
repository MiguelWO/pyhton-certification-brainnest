""" 1.Rewrite your pay computation with time-and-a-half for overtime and create a function called computepay which
takes two parameters (hours and rate). Enter Hours: 45 Enter Rate: 10 Pay: 475.0 """


def computepay(hours, rate):
    pay = 0
    if hours < 40:
        pay += hours * rate
    else:
        pay += (rate * 1.5) * (hours - 40) + 40 * rate

    return pay


# print(computepay(45, 10))


# 2.2.Rewrite the grade program from the previous chapter using
# a function called computegrade that takes a score as its parameter and
# returns a grade as a string.
# Score Grade
# >= 0.9 A
# >= 0.8 B
# >= 0.7 C
# >= 0.6 D
# < 0.6 F


def computegrade(score):
    try:
        if score < 0 or score > 1:
            message = f'Error: The value entered is out of bounds'
            # raise ValueError("Error: The value entered is out of bounds")
        else:
            if 0.9 <= score <= 1:
                message = "A"
            elif 0.8 <= score < 0.9:
                message = "B"
            elif 0.7 <= score < 0.8:
                message = "C"
            elif 0.6 <= score < 0.8:
                message = "D"
            else:
                message = "F"
        return message
    except:
        raise ValueError("Bad Score input")


# print(computegrade(0.5))


# problem
# print('Good morning!')
# print('How are you feeling?')
# feeling = input()
# print('I am happy to hear that you are feeling ' + feeling + '.')
# print('Good afternoon!')
# print('How are you feeling?')
# feeling = input()
# print('I am happy to hear that you are feeling ' + feeling + '.')
# print('Good evening!')
# print('How are you feeling?')
# feeling = input()
# print('I am happy to hear that you are feeling ' + feeling + '.')

def feelings():
    print("How are you feeling?")
    feeling = input()
    print('I am happy to hear that you are feeling ' + feeling + '.' + "\n")


def greetings():
    print("Good morning!")
    feelings()
    print("Good afternoon!")
    feelings()
    print("Good evening!")
    feelings()


# 1.Write a program which repeatedly reads numbers until the
# user enters `done`. Once `done` is entered, print out the total, count,
# and average of the numbers. If the user enters anything other than a
# number, detect their mistake using try and except and print an error
# message and skip to the next number.
#
# Enter a number: 4
# Enter a number: 5
# Enter a number: bad data
# Invalid input
# Enter a number: 7
# Enter a number: done
# 16 3 5.333333333333333
#
# functions to be used:
#
# from statistics import mean
# sum() - len() - sum()/len() - mean()

def statistics():
    flag = True
    arr = []
    while flag:
        number = input("Enter a number: ")
        if number.lower() == "done":
            flag = False
            pass
        else:
            try:
                num = int(number)
                arr.append(num)
            except ValueError:
                print("Invalid Input")
                pass

    suma = sum(arr)
    length = len(arr)
    mean = suma/length

    print(f'{suma} {length} {mean}')


if __name__ == "__main__":
    # print(computegrade(2))
    # print(computepay(45, 10))
    # greetings()
    statistics()
