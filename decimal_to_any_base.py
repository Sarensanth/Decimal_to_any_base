def decimal_conversion(number,base):
    binary=""
    while number>0:
        binary+=str(number%base)
        number=number//base
    return binary[::-1]

number=int(input())
base=int(input())
print(decimal_conversion(number,base))