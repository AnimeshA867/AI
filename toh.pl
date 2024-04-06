toh(1,A,B,_):- 
    write('Move disk 1 from '), write(A), write(' to '), write(B),nl.
toh(N,A,B,C):-
    N>1,
    N1 is N-1,
    toh(N1,A,C,B),
    write('Move disk '),write(N), write(' from  '), write(A), write(' to '), write(B), nl,
    toh(N1,C,B,A).