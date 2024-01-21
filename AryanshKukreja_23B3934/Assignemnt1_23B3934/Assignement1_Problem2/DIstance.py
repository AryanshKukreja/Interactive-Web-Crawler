from complex1 import Complex
from polar1 import Polar
import math

def distance(z1: Complex, z2: Complex):
    '''Distance between points'''
    dx = z2.x - z1.x
    dy = z2.y - z1.y
    return math.sqrt(dx**2 + dy**2)

if __name__ == '__main__':
    try:
        num_operations = int(input("Enter the number of operations: "))

        for _ in range(num_operations):
            # Take input for z1 and z2 in the form of z1.x, z1.y, z2.x, z2.y
            z1_values = input("Enter values for z1 (x y): ").split()
            z2_values = input("Enter values for z2 (x y): ").split()

            if len(z1_values) != 2 or len(z2_values) != 2:
                raise ValueError("Invalid input. Please enter values for x and y.")

            z1_x, z1_y = map(float, z1_values)
            z2_x, z2_y = map(float, z2_values)

            z1 = Complex(z1_x, z1_y)
            z2 = Complex(z2_x, z2_y)

            dist = distance(z1, z2)
            print(f"Distance between z1 {z1} and z2 {z2}: {dist}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

