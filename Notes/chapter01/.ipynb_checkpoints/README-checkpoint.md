# Introduction
This is a **VERY** comprehensive introduction. Thank you.
## Variables
We can understand them as "names" that we put on numbers.
## Data Types
"a data type is a set ofo predefined values [for a variable]".

It's a way for programming languages to transform 0s and 1s into human readable values.

Examples: integer, noating point, unit number, character, string, etc.

### Primitive data Types
The programming language comes built in with many data types.

We use the built in data types to make more data types (will see this through the book)

### User Defined Data Types
users can define data types of their own , for specific usage.

## Data structures:
Here is where things get (more) interesting:

A data structure is a way to store data inside a computer. Some allow fast access, others allow fast storage.

As they say: There are many tastes for the same cake. Similarly, there are many data structures to be implemented on the same data.

## Abstract data types (ADT)
Usually data structures need specific operations.

The ADT is a collection of both:
1. Declaration of data
2. Declaration of operations

Ex: stack and LIFO

## What is an algorithm
An algorithm is a collection of steps
##  Why do we analyse algorithms?
Algorithm analysis helps us determine which algorithm to implement.
- There are Many ways to do the same thing
  - Some are Better than others
- Algorithm analysis helps us determine which algorithm to implement.

## Goal of Algorithm Analysis
Restated: **compare many characteristics about an algorithm** with other algorithms.
## What is time analysis ?
one of the characteristics we care about in an algorithm is how long it takes for us to run it.

key term: **Time complexity**

The time depends on the inpput. Examples of things we care about:
- Size of an array
- Polynomial degree
- Number of elements in a matrix
- Number of bits in the binary representation of the input Vertices
- edges in a graph

## How to compare?
we need to define **objective** measures.

usually we measure the 'rate of growth' of the time needed by the algorithm wrt the size of the input.

Basically it's _f(N)_
## Definition of rate of growth
We are computing the time it needs to compute the time needed for a certain algorithm as we have large enough inputs

we take the highest rate of growth when we have a sum of multip;le rates.

so, $x^2+x$ is similar to $x^2$ because powers of x "eat up" lower powers of x for large values.
## Rates of Growth
Ascendingly, the rates of growth are:

1, lg(n),n, nlog(n), $n^k$, $2^n$
## Types of analysis
worst case, average case and best case  

## Asymptotic notation
we look at the functions as the input grows.

Let's deal with relevant Asymptotic notations

## Big-O
**[IMPORTANT]**

This is the *tight* upper bound  

**Other words**: any algorithm can't perform worse than its Big O.

```
Example:
f(n)=O(g(n))
This meeans that f(n)<g(n) for every n bigger than a certain number
```
exercises are in [Big O Notations of different functions](big_o.txt)

## Big Omega
This is the *tight* lower bound.
**Other words**: any algorithm cant perform better that its big omega notation

```
Example:
f(n)=Omega(h(n))
This means that f(n)<h(n) for every n bigger than a certain value
```

exercises are in [Big Omega Notation exercises](big_omega.txt)
## Big Theta
This metric determines whether big o and big omega are eequal
## Guidelines for Asymptotic Notations
more in [Asymptotic Relations](asym_guidelines.txt)
## Properties of Notation s
- Transiitivity
- Reflexivity
- Symmetry
- Transpose symmetry (between o and omega)
## Master's Theorem for diividve and conqnuer
[Abdul Bari](https://www.youtube.com/watch?v=OynWkEj0S-s) has a great video abouot this.
