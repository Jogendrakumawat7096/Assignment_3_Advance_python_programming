# '''Write python program that user to enter only odd numbers, else will raise an exception'''



try:
        number  = input("Enter Your Number : ")
        if number  % 2 == 0:
            raise ValueError("This is not an odd number!")
        else:
            print(f"You entered the odd number: {number}")
except ValueError as e:
        print(e)



