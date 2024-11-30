import math

hex_values = {0: "0",
              1: "1",
              2: "2",
              3: "3",
              4: "4",
              5: "5",
              6: "6",
              7: "7",
              8: "8",
              9: "9",
              10: "A",
              11: "B",
              12: "C",
              13: "D",
              14: "E",
              15: "F",
              }


def get_decimal():
    while True:
        decimal_number = int(input("Enter integer in decimal to convert to hexadecimal: "))
        if decimal_number < 0:
            pass
        else:
            break
    return decimal_number


def find_highest_power(decimal_number):
    power = 0
    while True:
        if math.floor(decimal_number / 16 ** power) >= 15:
            power += 1
        else:
            break
    return power


def convert(decimal_number, power):
    hexadecimal_number = ""
    quotient = decimal_number
    for i in range(power, -1, -1):
        divisor = 16 ** i
        if power != 0:
            quotient = math.floor(quotient / divisor)
            hexadecimal_number += hex_values[quotient]
            quotient = decimal_number % divisor
        else:
            hexadecimal_number += hex_values[quotient]

    return hexadecimal_number


def main():
    decimal_number = get_decimal()
    power = find_highest_power(decimal_number)
    hex_number = convert(decimal_number, power)
    print(f"Hexadecimal of {decimal_number} (decimal) is {hex_number}")

main()
