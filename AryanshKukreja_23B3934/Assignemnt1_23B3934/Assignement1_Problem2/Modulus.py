from complex1 import Complex
from polar1 import Polar
import math

def modulus(z1: Complex):
    dx =  z1.x
    dy =  z1.y
    return math.sqrt(dx**2 + dy**2)

if __name__ == '__main__':
        num_operations = int(input(""))

        for _ in range(num_operations):
            z1_values = input("").split()
            if len(z1_values) != 2:
                raise ValueError("Invalid input. Please enter values for x and y.")
            z1_x, z1_y = map(float, z1_values)

            z1 = Complex(z1_x, z1_y)

            mod = modulus(z1)
            print(f"Modulus of z1 {z1}: {mod}")
