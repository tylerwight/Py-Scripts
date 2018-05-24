import re 

#script to get a string input of a few coordinates, and output the standard form equation for that circle


def checkio(data):
    #data is a string so number only come in certain parts of the array, then I convert them all to integers to perform path
    x1 =int(data[1])
    y1 =int(data[3])
    
    x2 =int(data[7])
    y2 =int(data[9])
    
    x3 =int(data[13])
    y3 =int(data[15])
    
    #equations to determine the 4 parts of a circle equation, used later to convert to standard form
    #equations found here http://www.ambrsoft.com/trigocalc/circle3d.htm
    A = x1*(y2-y3)-y1*(x2-x3)+x2*y3-x3*y2
    B = (x1**2+y1**2)*(y3-y2)+(x2**2+y2**2)*(y1-y3)+(x3**2+y3**2)*(y2-y1)
    C = (x1**2+y1**2)*(x2-x3)+(x2**2+y2**2)*(x3-x1)+(x3**2+y3**2)*(x1-x2)
    D = (x1**2+y1**2)*(x3*y2-x2*y3)+(x2**2+y2**2)*(x1*y3-x3*y1)+(x3**2+y3**2)*(x2*y1-x1*y2)
    
    #Using ABCD I can then calculate the radius and x/y coordinate
    r = (((B**2+C**2)-(4*A*D))/(4*(A**2)))**(0.5)
    x = (0-(B/(2*A)))
    y = (0-(C/(2*A)))
    
    #This 'checker' for this script requires that all tailing zeros are removed, so 3.0 will not work. This converts 3.0 to 3, etc
    if (x.is_integer()):
        x = int(x)
    if (y.is_integer()):
        y = int(y)
    if (r.is_integer()):
        r = int(r)
        
    #round output to 2 decimal places        
    r = round(r, 2)        
    x = round(x, 2)
    y = round(y, 2)
    
    #printing our vairables for testing
    print ("A is: ",A)
    print ("B is: ",B)
    print ("C is: ",C)
    print ("D is: ",D)
    print ("r is: ",r)
    print ("x is: ",x)
    print ("y is: ",y)
    
    #craft a string using our variables to make a circle equation in standard form
    answer = ('(x-' + str(x) + ')^2+(y-' + str(y) + ')^2=' + str(r) + '^2')
    print (answer)

    return (answer)
    #plot.savefig('hanning' + str(num) + '.pdf')

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("(2,2),(6,2),(2,6)") == "(x-4)^2+(y-4)^2=2.83^2"
    assert checkio("(3,7),(6,9),(9,7)") == "(x-6)^2+(y-5.75)^2=3.25^2"
