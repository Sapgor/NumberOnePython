def is_even(number):
    return number % 2 == 0
while True:
    try:
        number = int(input("введите число: "))
    except:
        print("введено не число")
        continue
    if(is_even(number)):
        print("число чётное")
    else:
        print("число нечётное")