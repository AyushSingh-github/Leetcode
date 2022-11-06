look like this a1 ,a2,a3,x, y, a4, if K==2 ,we can rotate it to (with repete put the first to last)
x,y,a4,a1,a2,a3 ,then with put the second to the last
-> x,a4,a1,a2,a3,y ,with repete put first to last
-> y,x,a4,a1,a2,a3 (with repete put first to last)
-> a1,a2,a3,y,x,a4 (so look, we swap the adjacent elements of x and y!
this means we can swap aribitray two adjacent elements; so we can swap everty two different elments,
for: a,b,c,d,e,f,g (if we want to swap c and f) we can swap c,d
-> a,b,d,c,e,f,g then swap c,e
->a,b,d,e,c,f,g then swap c,f
->a,b,d,e,f,c,g then swap f,e
->a,b,d,f,e,c,g then swap d,f
->a,b,f,d,e,c,g (this is the ans);
so if we can arbitrary swap any two elements, we can get any permutations we want ,that is the ans!
​
​
​
​
So here's how you can obtain any permutation of the string if k>=2 :
Consider the string .. (x1)(x2)(x3)(x4)...(xm)(xm+1)....x(n). Lets say we want to swap xm and xm+1(any 2 arbitrary adjacent elements). We can follow these steps :
​
Push (x1)(x2)..(xm-1) behind. We get (xm)(xm+1)...(xn)(x1)(x2)..(xm-1).
Now Push xm+1 behind to get (xm)(xm+1)...(xn)(x1)(x2)..(xm-1)(xm+1).
Push xm behind to get (xm+2)..(xn)(x1)(x2)...(xm-1)(xm+1)(xm)
Push xm+2...xn behind to get (x1)(x2)(x3)(x4)...(xm+1)(xm)....x(n)
Hence, we can swap any two adjacent elements. If we can swap any two adjacent elements we can obtain any permutation (using an algorithm similiar to bubbleSort)