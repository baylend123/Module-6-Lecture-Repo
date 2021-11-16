'''
Better to ask forgiveness than permission
A pythonic principle & fundamental part of Python control flow

A way to catch errors without halting the program

ie asking for forgiveness instead of permission
'''

'''
Keywords:
    try: run this code until an exception occurs
    except: run this code when an exception occurs
    else: run this code only if no exception occurs
    finally: run this code no matter what
'''
num = 0
try:
    print("Trying now...")
    print(4/num)
except ZeroDivisionError:
    print("oops i tried to divide by zero!")
finally:
    print("this happens no matter what")

# Possible but dangerous
num = 0
try:
    print("Trying now...")
    print(4/num)
# code will still run,  but you wont know what the error is
# bare except is not good
except :
    print("oops i tried to divide by zero!")
finally:
    print("this happens no matter what")

# Another try except block
while True:
    try:
        num = int(input("say a number "))
        print(num)
        # if no error this will break out of the loop
        break
    # if error this will run and ask for a number again because of while True
    except ValueError:
        print("try again")



