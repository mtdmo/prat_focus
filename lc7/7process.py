def reverse(x):
    num = str(abs(x))
    if x < 0:
        result = -1 * int(num[::-1])
    else:
        result = int(num[::-1])
    if result not in range((-1 << 31), (1 << 31) - 1):
        return 0

    return result

print(reverse(123))
print(reverse(-123))
print(reverse(120))
print(reverse(1534236469))
