class Solution:
    def reverse(x):
        try:
            x += 1
            a = str(x)[::1]
            int(a)
            print(a)
        except TypeError:
            print("This is not an Integer.")
