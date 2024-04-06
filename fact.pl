fact(N,1):- N=<0.

fact(N,Y):-
    N>0,
    N1 is N-1,
    fact(N1,Y1),
    Y is N * Y1.
