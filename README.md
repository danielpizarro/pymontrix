#pymontrix

Matrix operations library using compressed matrices based in Mondrian tesselation

##finding the max value in a matrix of 1.000.000 x 1.000.000

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
