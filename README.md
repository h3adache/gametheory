gametheory
==========

scripts to help with gametheory calculations

prob.py
----------
Computes Nash equilibria for 2x2 and 3x3 games

Usage:
> python
> import prob as p
> p.prob() # follow prompt

Explanation of the algorithm is:
[http://en.wikipedia.org/wiki/Nash_equilibrium#Computing_Nash_equilibria]

### Usage as is applies to this script
run function prob. When it asks you for the payoffs enter them in the order of all payoffs for playing  
action A followed by all payoffs for playing action B (and then action C if applicable)

For example given the matrix:

A (rows)/B(columns) | Head | Tail
---|---|---
Head ( *p* ) | a1,b1 | a2,b3
Tail ( *1-p* )| a3,b2 | a4,b4

You would do: a1,a2,a3,a4 to calculate P

bayesian.py
----------

bayesian equilibrium

