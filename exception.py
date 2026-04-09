try:
    # Code that might cause an error
    num = int(input("Enter a number: "))
    result = 10 / num
    print("Result:", result)

except ZeroDivisionError:
    print("You cannot divide by zero!")

except ValueError:
    print("Invalid input! Please enter a number.")

finally:
    print("This block always runs (cleanup code).")