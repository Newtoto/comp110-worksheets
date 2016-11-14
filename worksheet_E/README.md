a)
```
s2 = 0
s3 = s0

while s3 != 0:
    s2 += s1
    s3 -= 1
```
b)
```
The loop will execute s0 number of times, and each time the loop executes, s1 is added to s2 which starts at 0.
This means that the value of s2 will be the value of s1 times s0.
```
c)
```
s0 = 10
s1 = 1

while s0 != 0:
    s2 = 0
    s3 = s0
    
    while s3 != 0:
        s2 += s1
        s3 -= 1

    s1 = s2
    s0 -= 1
```
d)
```
The outer loop runs a total of the original s0 number of times as it decreases s0 by 1 each time it runs till s0 reaches 0.

The inner loop runs s3 number of times for every time the outer loop runs.
Since s3 = s0, and s0 decreases by 1 every time the outer loop runs, the inner loop runs by (s0 - n) where n is the number of times the
outer loop has run.

The inner loop timeses s1 by the value of s3 and sets it to equal s2.
s1 is then set to the value of s2 once the inner loop has finished so the result at the end of the outer loop is that s1 = s1(s0-n),
meaning that the first time the outer loop runs, s1 = 1(s0-0) = 1(s0-0)

This means that by the final run of the outer loop for this example is:

s1 = 1(s0)(s0-1)(s0-2)(s0-3)(s0-4)(s0-5)(s0-6)(s0-7)(s0-8)(s0-9) 
where s0 represents the originial value of s0 which is 10 in this case

So this gives us:

s1 = (10)(9)(8)(7)(6)(5)(4)(3)(2)(1) = 10! [10 factorial]

```
e)
