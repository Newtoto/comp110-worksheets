a) This algorithm checks a list for duplicate values
b) For every list item, the algorithm runs though every list item, so if it has to go through all of them
it is n^2
c) The (i-1)th item in the list has already been checked against all of the other items in the list, so it
doesn't need to be checked again.
d) I can't see how this will run twice as fast. Since it only stops it from running through the loop once more,
surely it would only be twice as fast if the list length was 2.
e) No, because it doesn't have to run through every item in the list any more.
f) O(N Log N) https://www.ics.uci.edu/~pattis/ICS-33/lectures/complexitypython.txt
g) O(N Log N) because of what that ^ said
h) Algorithm 2, because it only has to run throught the list once, once it's been sorted.
i) Algorithm 1 is faster for checking short lists.
