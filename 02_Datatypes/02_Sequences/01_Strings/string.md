# String

- Python string is the collection of the characters surrounded by single quotes, double quotes, or      triple quotes.

- The computer does not understand the characters; internally, it stores manipulated character as the combination of the 0's and 1's.

- Each character is encoded in the ASCII or Unicode character. So we can say that Python strings are also called the collection of Unicode characters.

- Strings are immutable in Python.

- We use Unicode Strings

- Negative Index supports in python

# String Operators

- Pluse (+) operator is used to concatinate the strings

- Astrics (*) operator :- It is known as repetition operator. It concatenates the multiple copies of the same string.

- Brackets [] opeartor :- It is known as slice operator. It is used to access the sub-strings of a particular string.

- Bracket with semicoln [:] Operator :- It is known as range slice operator. It is used to access the characters from the specified range.

- in Operator :- It is known as membership operator. It returns if a particular sub-string is present in the specified string.

- not in Operator :- It is also a membership operator and does the exact reverse of in. It returns true if a particular substring is not present in the specified string.

- r/R (Raw) Operator :- It is used to specify the raw string. Raw strings are used in the cases where we need to print the actual meaning of escape characters such as "C://python". 

- % modulo Operator :- It is used to perform string formatting. It makes use of the format specifiers used in C programming like %d or %f to map their values in python. We will discuss how formatting is done in python.

# Various methods are perfomed on Strings
1. len()
    - str = "Core Python" <br> print(len(str))
2. Indexing[]
    - str = "Core Python" <br> print([0])
3. Slicing[]
    - [::2] - It will access entire string in steps of 2
    - [::] - It will access string from 0th to last character.
    - [2:4:1] - It will starts from 2 and goest till 3 (n-1 [4-1 = 3]) with steps of 1
    - [2::] - It will starts from 2 and goes till end
    - [:2:] - It will starts form 0 and goes till 1 with 1 steps.
    - [-4:-1] - It will access str[-4] to str[-2] form left to right in str.
    - [-6::] - It will access from [-6] till the end of the string.
    - [-1:-4:-1] - It retrieve from str[-1] to str[-3] from right to left.
    - [-1::-1] - It will retrieve element from last to first element of the string. 
4. Repeating (*)
    - str = 'core python' <br> print(str*2)
    - s = str[5:7] <br> print(s)
5. Concatenation (+)
6. Checking Membership (in or not in)
7. Comparing Strings
8. Removing Spaces from a string (using strip(),lstrip(),rstrip())
9. Finding Sub String (find(), rfind(),index(),rindex())
10. Counting Substrings in a String (count())
11. Strings are Immutable
12. Replacing a string with another string.
13. Spliting and Joining String.
14. Change Case in String.[upper(), lower(), swapcase(), title()]
15. Checking Starting or Ending of the String with substring (startswith(), endswith())
16. String Testing Method [isalnum(), isalpha(), isdigit(), islower(), isupper(), istitle(), isspace()]
17. Formated String
18. Working with Characters. [through indexing, slicing and also test the characters]
19. Sorting Strings [(sort.str), (str1 = sorted(str))]
20. Searching in the String
21. Finding Number of Characters and Words without using len(string)
22. Inserting sub String into a string [''.join]
