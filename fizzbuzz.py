import math


def fizzbuzz_modulo():
    for i in range(0, 100):
        #r = i
        if i % 15 == 0:
            i = "fizzbuzz"
        elif i % 3 == 0:
            i = "fizz"
        elif i % 5 == 0:
            i = "buzz"
        
        print i


def fizzbuz():
    for i in range(1, 100):
        o = i / 3.0
        j = i / 5.0
        f = i / 15.0
           

        if (f).is_integer() is True:
            i = "fizbuz"

        elif (o).is_integer() is True:
            i = "buz"

        elif (j).is_integer() is True:
            i = "fiz"

        

        print i


#fizzbuzz_modulo()
fizzbuz()