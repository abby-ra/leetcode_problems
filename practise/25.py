#  Utility function to return the minimum of two values
def getMin(x, y):
    return x if x < y else y

# Function to calculate the minimum angle between
# hour and minute hands
def getAngle(s):
    # Extract hours and minutes from "HH:MM"
    h = int(s[:2])
    m = int(s[3:])

    # Convert 24-hour time to 12-hour format
    h = h % 12

    # Hour hand moves 0.5 degrees per minute
    # (30 degrees per hour)
    hrAngle = 0.5 * (h * 60 + m)

    # Minute hand moves 6 degrees per minute
    minAngle = 6 * m

    # Find the absolute difference between the two angles
    angle = abs(hrAngle - minAngle)

    # Return the smaller angle of the two possible angles
    return getMin(360 - angle, angle)

if __name__ == "__main__":
    s = "06:00"
    print(f"{getAngle(s):.3f}")