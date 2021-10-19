def duplicate(somelist):
    """
    biore binary search na srodku listy
    sprawdzam

    :param somelist:
    :return:
    """
    emptylist = []
    for i in somelist:
        if len(emptylist) == 0:
            emptylist.append(i)
        else:
            if i in emptylist:
                return i
            emptylist.append(i)


nums = [3,1,3,4,2]

x = duplicate(nums)

print(x)

from random import randrange


def guessNumber(n: int) -> int:
    picked_number = randrange(n)
    print("Picked number is {}".format(picked_number))

    low, high = 0, n

    while True:
        guess = (high + low) // 2
        print('My guess is {}'.format(guess))

        if picked_number > int(guess):
            print(1)
            low = guess + 1

        elif picked_number < int(guess):
            print(-1)
            high = guess - 1

        else:
            return 0


guessNumber(10)       
