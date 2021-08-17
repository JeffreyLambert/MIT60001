
import math


def raise_by_power(x, y):
    return x**y


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    x = int(input("Enter a number x: "))
    y = int(input("Enter a number y: "))

    x_to_the_y = raise_by_power(x=x,y=y)
    log2x = math.log2(x)
    print(f"X**y = {x_to_the_y}")
    print(f"log(x) = {log2x}")
