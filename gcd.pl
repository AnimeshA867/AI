% Base case: GCD of any number with 0 is the number itself.
gcd(X, 0, X) :- X > 0.

% Recursive case: Calculate GCD using Euclid's algorithm.
gcd(X, Y, G) :-
    Y > 0,
    Z is X mod Y,
    gcd(Y, Z, G).
