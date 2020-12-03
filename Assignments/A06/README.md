## Assignment 6 - Prime Factors
### Chad Callender
### Description:

Factoring integers is computationally difficult. Given a somewhat large number, determine if it is prime or if it can be factored. If it can be factored print out the prime factors.

### Method

This program uses **trial division** to determine if a number is prime or decompose a composite integer into its prime factors. Trial division relies on the following theorem:

**Theorem:** If n is a composite number, then n has a prime factor less than or equal to the square root of n.

Trial division relies on this theorem, requiring the program to only check the integers from 2 up to the square root. If there are no integers in this range that divide n, then n is prime. Otherwise, n is composite. Using a recursive call, the composite integer is decomposed into its prime factors because the first number to divide n will be prime.

### Files

|   #   | File                       | Description                                                |
| :---: | -------------------------- | ---------------------------------------------------------- |
|   1   | [get_factors.py](./get_factors.py)       | Main code. |

### Instructions:

Enter every number on a new line in the text document.
