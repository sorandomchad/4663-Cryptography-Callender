## Assignment 7 - Finding Primes
### Chad Callender
### Description:

This assignment requires conducting research to find primality tests in three categories:
1. Certification
2. Compositeness
3. Deterministic

### Certification

"A primality certificate or primality proof is a succinct, formal proof that a number is prime."<sup>[[1]](#1)</sup> This is a little beyond what we are wanting to do. Our goal is to find some algorithms that find primes in a "brute force" fashion that inherently guarantee the number found is prime. So to "certify" a number is prime, we are ok with using ***trial division***.  This is the simplest primality test there is. It goes something like this: 
>Given an input number, ***n***, check whether it is evenly divisible by any prime number between ***2*** and ***√n*** (i.e. that the division leaves no remainder). If so, then ***n*** is **composite**. Otherwise, it is ***prime***.

Of course this does not mean we are looking to waste time. We still want to do things efficiently. So we look for other, faster ways of determining primes as well. 

### Compositeness
A composite number is a positive integer that can be formed by multiplying two smaller positive integers. Equivalently, it is a positive integer that has at least one divisor other than 1 and itself. Every positive integer is composite, prime, or the unit 1, so the composite numbers are exactly the numbers that are not prime and not a unit <sup>[[4]](#4)</sup>. One test for compositeness is Rabin-Miller<sup>[[5]](#5)</sup>. Look at the wikipedia page for other tests for compositeness like: [Solovay–Strassen primality test](https://en.wikipedia.org/wiki/Primality_test)<sup>[[6]](#6)</sup>.


### Deterministic
A deterministic algorithm is an algorithm which, given a particular input, will always produce the same output, with the underlying machine always passing through the same sequence of states<sup>[[7]](#7)</sup>. There is one algorithm that claims to be deterministic, but I'm not sure how generalized this algorithm is. It can be found here: https://en.wikipedia.org/wiki/AKS_primality_test

#### References:

- <a id="1">[1]</a>: https://en.wikipedia.org/wiki/Primality_test
- <a id="2">[2]</a>: https://en.wikipedia.org/wiki/Primality_certificate
- <a id="3">[3]</a>: https://primes.utm.edu/prove/index.html
- <a id="4">[4]</a>: https://en.wikipedia.org/wiki/Composite_number
- <a id="5">[5]</a>: https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test
- <a id="6">[6]</a>:https://en.wikipedia.org/wiki/Primality_test
- <a id="7">[7]</a>:https://en.wikipedia.org/wiki/Deterministic_algorithm
