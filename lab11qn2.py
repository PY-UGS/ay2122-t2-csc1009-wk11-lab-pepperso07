class clockTime:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    # Set hour value only
    def setHours(self, hours):
        self.hours = hours

    # Set minute value only
    def setMinutes(self, minutes):
        self.minutes = minutes

    # Set second value only
    def setSeconds(self, seconds):
        self.seconds = seconds

    # Set hour, minute, second values
    def setTime(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    # Show time in format of hour:minute:second
    def showTime(self):
        return self.hours + ":" + self.minutes + ":" + self.seconds


# Take in user input for hour, minute, second values
hr = input("Enter hours: ")
min = input("Enter minutes: ")
sec = input("Enter seconds: ")

# Create an object and pass in values based on user input
time = clockTime(hr, min, sec)

# Print the time
print("The time is " + time.showTime())