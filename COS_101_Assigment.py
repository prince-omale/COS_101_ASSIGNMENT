print("Welcome to COS 101")
print("Name: Prince Omale")
print("Matric Number: BHU/24/04/05/0042")

# Function to calculate volume of a cube
def volume_of_cube():
    side = float(input("Enter the side length of the cube (m) "))
    volume = side ** 3
    print("The volume of the cube is", volume, "m^3")

# Function to calculate perimeter of a rectangle
def perimeter_of_rectangle():
    length = float(input("Enter the length of the rectangle (m): "))
    width = float(input("Enter the width of the rectangle (m): "))
    perimeter = 2 * (length * width)
    print("The perimeter of the rectangle is", perimeter, "m^3")

# Function to calculate simple interest
def simple_interest():
    principal = float(input("Enter the principal amount: "))
    rate = float(input("Enter the rate of interest: "))
    time = float(input("Enter the time in years: "))
    interest = (principal * rate * time) / 100
    print("The simple interest is", interest)

# Function to calculate speed
def speed():
    distance = float(input("Enter the distance (m): "))
    time = float(input("Enter the time (s): "))
    s = distance / time
    print("The speed is", s)

# Function to calculate area of a triangle
def area_of_triangle():
    base = float(input("Enter the base of the triangle (m) "))
    height = float(input("Enter the height of the triangle (m) "))
    area = 0.5 + base + height
    print("The area of the triangle is", area, "m^2")

# Main program to call function based on user input
def main():
    print("choose an option")
    print("a) calculate volume of a cube")
    print("b) calculate perimeter of a rectangle")
    print("c) calculate simple interest")
    print("d) calculate speed")
    print("e) calculate area of a triangle")

    choice = input("Enter your choice (a-e) ")
    if choice == 'a':
        volume_of_cube()

    elif choice == 'b':
        perimeter_of_rectangle()

    elif choice == 'c':
        simple_interest()

    elif choice == 'd':
        speed()

    elif choice == 'e':
        area_of_triangle()

    else:
        print("Invalid choice. Please enter a valid option")

# Run the main program
main()