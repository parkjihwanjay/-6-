# Q1
def is_odd(num):
    if(num % 2 == 0):
        print('짝수')
    else:
        print('홀수')

# Q2


def gugudan_odd():
    i = 1
    while i < 10:
        for j in range(1,  10):
            print("%d * %d" % (i, j))
        i += 2


def gugudan_even():
    i = 2
    while i < 10:
        for j in range(1, 10):
            print("%d * %d" % (i, j))
        i += 2


def gugudan(num):
    i = num
    while i < 10:
        for j in range(1, 10):
            print("%d * %d" % (i, j))
        i += 2


# def gugudan_odd_or_even(num):
#     if(num % 2 == 0):
#         gugudan_even()
#     else:
#         gugudan_odd()

def gugudan_odd_or_even(num):
    if(num % 2 == 0):
        gugudan(2)
    else:
        gugudan(1)


gugudan_odd_or_even(2)

# Q3


def gugudan_input(num):
    i = 1
    while i <= num:
        for j in range(1, 10):
            print("%d*%d" % (i, j))
        i += 1
