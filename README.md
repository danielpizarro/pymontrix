#Pymontrix

Matrix operations library using compressed matrices based in Mondrian tesselation

##Find the max value in a matrix of 1.000.000 x 1.000.000 items

```
>>> from montrix import Zone, Montrix
>>> a = Montrix(1E6,1E6,0) #create a matrix
>>> a.set_zone(Zone(3,3,5,5,1)) #set some values
>>> a.set_zone(Zone(7,7,9,9,2)) #set some values
>>> a.set_zone(Zone(1000,1000,2000,2000,3)) #set some values
>>> max_value, max_coords = a.get_max() #find max value and its coordinates
>>> max_value
3
>>> max_coords
(1000, 1000)
>>>
```

##Merge two matrices of 1.000.000 x 1.000.000 items

```
    a = Montrix(1E6,1E6,0) #create matrix of zeros
    b = Montrix(1E6,1E6,0) #create matrix of zeros

    a.set_zone(Zone(1000,1000,20000,20000,-1))      #set some values
    b.set_zone(Zone(800000,800000,900000,900000,2)) #set some values

    min_a = a.get_min()
    max_b = b.get_max()
    
    assert_equals(min_a, (-1, (1000, 1000)))
    assert_equals(max_b, (2, (800000, 800000)))
    
    def largest_abs(x,y):
        if abs(x)>abs(y): return x
        else: return y
    
    
    a.apply(b, largest_abs) #merges two matrices using "largest_abs" function
    
    min_a = a.get_min()
    max_a = a.get_max()

    assert_equals(min_a, (-1, (1000, 1000)))    #et voilá!
    assert_equals(max_a, (2, (800000, 800000))) #more voilá!

```