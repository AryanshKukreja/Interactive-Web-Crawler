Ordinate.py
from polar1 import Polar
import math

def ordinate(p1: Polar):
    dx = p1.r
    dy = p1.t

    angle =dy

    result= dx * math.sin(angle)
    rounded_result=round(result,1)
    return rounded_result


if __name__ == '__main__':
    num_operations = int(input(""))

    for _ in range(num_operations):
        p1_values = input("").split()

        if len(p1_values) != 2:
            raise ValueError("Invalid input. Please enter values of r and 𝝷.")

        p1_r, p1_t = map(float, p1_values)

        p1 = Polar(p1_r, p1_t)  # Fix typo here (change p1_y to p1_t)
        ordi = ordinate(p1)
        print(f"Absissa of p1 {p1}: {ordi}")
