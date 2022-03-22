class Calculator:
    def __init__(self, first, second):
        self.first = first
        self.second = second

 
    def adder(self):
        return self.first + self.second


    def subtractor(self):
        return self.first - self.second

    def multiplier(self):
        return self.first * self.second


    def divider(self):
        return self.first / self.second

    def clear(self):
        self.first = 0
        self.second = 0


# Take in user input for 2 numbers
firstNo = float(input("Please enter the first number: "))
secondNo = float(input("Please enter the second number: "))

# Create an object and pass in values based on user input
calculate = Calculator(firstNo, secondNo)


# Print all operations
print("Sum of 2 numbers: ", calculate.adder())
print("Subtraction of 2 numbers: ", calculate.subtractor())
print("Multiplication of 2 numbers: ", calculate.multiplier())
print("Division of 2 numbers: ", calculate.divider())

calculate.clear() #reset both the first and second number to 0
print("First number:",calculate.first)
print("Second number:",calculate.second)
