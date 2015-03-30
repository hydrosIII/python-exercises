import math



def fizzbuz ():


        for i in range (1,100):



            o = i/3.0
            j = i/5.0
            f = i/15.0

            if (o).is_integer() is True:
                i = "buz"
            if (j).is_integer() is True:
                i= "fiz"
            if (f).is_integer() is True:
                i= "fizbuz"

            print i


fizzbuz()
