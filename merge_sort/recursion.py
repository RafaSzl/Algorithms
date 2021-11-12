# Factorial function
def f(n):
    # Stop condition
    if n == 0 or n == 1:
        return 1

    # Recursive condition
    else:
        return n * f(n - 1)


n = 4
print(f"factorial of {n} is:{f(n)}")


def sumrange(n):
    if n == 1:
        return 1

    return n + sumrange(n - 1)


print(sumrange(5))


def palindrome(num):
    i = 0
    j = len(num)
    newnum = str(num)
    if len(newnum) <= 1:
        print('True')
        return True
    if newnum[i] == newnum[j-1]:
        newnum = newnum[1:-1]
        return palindrome(newnum)
    print('False')
    return False


palindrome('34543')