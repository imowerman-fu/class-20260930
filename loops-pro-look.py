def main():
    meow(get_n_meows())

def get_n_meows():
    while True:
        meows = int(input('How many times does Waverly say meow? '))
        if meows <= 0:
            print('Please enter a non-negative number or zero.')
        else:
            return meows


def meow(meows):    
  for _ in range(meows):
    print('meow')  
   
    
main()