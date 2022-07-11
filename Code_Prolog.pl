male(dashrath).
male(lakshman).
male(ram).
male(bharat).
male(shatrughan).
male(hanuman).
female(sumitra).
female(kaikeyi).
female(sita).
female(kausalya).
parent(dashrath,ram).
parent(dashrath,lakshman).
parent(dashrath,bharat).
parent(dashrath,shatrughan).
parent(kausalya,ram).
parent(sumitra,lakshman).
parent(sumitra,shatrughan).
parent(kaikeyi,bharat).
wife(sita,ram).
wife(dashrath,kausalya).
wife(dashrath,kaikeyi).
wife(dashrath,sumitra).
brother(X,Y):-
 father(Z,X),father(Z,Y),X\==Y.
father(X,Y):- parent(X,Y), male(X).
mother(X,Y):- parent(X,Y), female(X).
father_in_law(M,N):-
 male(M),female(N),father(M,Y),wife(N,Y),Y==ram.
mother_in_law(M,N):- female(M),female(N),male(Y),mother(M,Y),wife(N,Y).