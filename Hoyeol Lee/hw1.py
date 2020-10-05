print("구구단")

def gugudan():
    for x in range(1, 10):
        print(''"["+ str(x) + "단""]"'')
        for y in range(1, 10):
            print(f'{x}x{y}={x*y}',end="\t")
            if(y == 9):
                print()

gugudan()