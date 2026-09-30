while True:
    meows = int(input('How many times does Waverly say meow? '))
    if meows <= 0:
        print('Please enter a non-negative number or zero.')
        continue
    else:
        break


for _ in range(meows):
    print('meow')