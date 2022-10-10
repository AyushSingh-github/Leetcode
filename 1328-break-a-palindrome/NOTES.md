* First of all if the given string is of length 1 then we cannot do anything to make it not a palindrome, so for a string of length 1 we would return an empty string.
Now let's move on.
​
* We need the lexicographically smallest possible string so obviously any character that is not "a" should become "a" in order to become the smallest possibe.
* So, simpy we can iterate over the string and check if the character is "a" or not. If not, then we simply use this index to change this character to "a".
But there's a CATCH!!!
*  What if the string is like "aba", then according to our logic it would become "aaa" but it is still a palindrome so something might be wrong with our logic.
​
Actually there's nothing wrong but we need to keep in mind that replacing the middle character of the string to anything will do nothing to make it a non-palindrome.
So, we have to add just one more logic to check if the element we are currently at is in
the middle or not.
Now, let's move on to the case where we have all a's in the string,
To work it out we can simply change the last character to "b" and we'll have the smallest
non-palindrome possible.