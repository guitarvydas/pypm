:- use_module(library(http/json)).
?- consult("../fb.pl").
?- consult("/Users/tarvydas/quicklisp/local-projects/pypm/poc/das2f/shapes.pl").
?- consult("/Users/tarvydas/quicklisp/local-projects/pypm/poc/das2f/names.pl").
?- consult("/Users/tarvydas/quicklisp/local-projects/pypm/poc/das2f/connection.pl").
query_helper(Parent,Edge,Sender,Receiver):-
das_fact(kind,Edge,edge),
sourceof(Edge,Sender),
targetof(Edge,Receiver),
das_fact(direct_contains,Parent,Edge),
true.
query:-
(setof([Parent,Edge,Sender,Receiver],query_helper(Parent,Edge,Sender,Receiver),Bag),
json_write(user_output,Bag,[width(128)])
)
;
json_write(user_output,[],[width(123)]).
