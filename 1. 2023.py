"""
This code calculates all 4 digit numbers, which equals 12 when all digits (besides 0) are multiplied with each other.
"""
def mr(number):
    number_str = str(number)
    replaced_str = number_str.replace('0', '1')
    result = 1
    for digit_str in replaced_str:
        digit = int(digit_str)
        result *= digit

    return result

p=[]

for i in range(1000,9999):
    i_with1 = mr(i)
    if(i_with1 == 12):
        p.append(i)

print(len(p))
