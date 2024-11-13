# Set in Python

- A set is an Unorderd collection of elements much like a set in Mathematics.
- The order of elements is not maintained in the sets.
- A set does not accept duplicate elements.
- To create a set, we should enter the elements separated by commas inside curly braces {}.

# Types of Set

- There are two types of set in python
     1. Set Datatype
     2. Frozenset Datatype

1. Set Datatype
    - To create a set, we should enter the elements separated by commas inside curly braces {}.
    - set does not maintain the order of the elements
    - We can use the set() function to create a set
    - We can covert a list into a set using set() function.
    - Sets are unordered so, we cannot retrive the elements using indexing or slicing operation.
    - update() method is used to add the elements to a set.
    - remove() method is used to remove any particular element from a set.

2. Frozentset Datatype
    - It is same as set datatype but the main difference is element of set can modified, whereas the elements of frozenset cannot be modified.
    - We can create a frozenset by passing a set to frozenset() function.
    - Another way of creating a frozenset is by passing a string to the frozenset() funciton.
        - example:- fs = forzenset("Siddhant Gautam")
    - update() and remove() methods will not work on frozensets.
    