For people not getting this is working:
​
x:=0 is used to assign a value to x
as 0^number = number
lets assume Y= (x := 0, [x := x ^ v for v in nums])[-1][-1]
Y is a tuple, for example: nums=[2,2,1]
you will get : Y =(0, [2, 0, 1])
:= allows us to assign a value to a variable inside a Python expression, doing x=x^v would give SYNTAX error.
Thanks to @constantstranger , I got to learn about walrus operators.