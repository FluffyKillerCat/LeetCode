letter = ""
a  = 123
while a > 26:
    letter += chr((a % 26) + 64)

    a //= 26

letter += chr(a + 64)
print(letter[::-1])