from complex1 import Complex
from polar1 import Polar
import math

def arg(z1: Complex):
    dx = z1.x
    dy = z1.y
    return round(math.atan2(dy, dx),2)
if __name__ == '__main__':

        num_operations = int(input(""))

        for _ in range(num_operations):
            z1_values = input("Enter values for z1 (x y): ").split()

            if len(z1_values) != 2:
                raise ValueError("Invalid input. Please enter values for x and y.")

            z1_x, z1_y = map(float, z1_values)

            z1 = Complex(z1_x, z1_y)
            arg_result = arg(z1)
            print(f"Argument of z1 {z1}: {arg_result} radians")
