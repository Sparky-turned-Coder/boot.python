# Formatted string literals (also called f-strings for short) let you include the value of python expressions inside a string by prefixing the string with f or F and writing expressions as {expressions}

# The following example rounds pi to three decimal places after the decimal:
import math

print(f"The value of pi is approximately {math.pi:.3f}.")

table = {"sjoerd": 4127, "jack": 4098, "dcab": 7678}
for name, phone in table.items():
    print(f"{name:10} ==> {phone:10d}")
