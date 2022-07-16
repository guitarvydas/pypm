
temp=temp${RANDOM}
# layer 3


cat >${temp}.pl <<'~~~'
:- use_module(library(http/json)).
?- consult("fb.pl").
?- consult("/Users/tarvydas/quicklisp/local-projects/pypm/poc/das2f/shapes.pl").
?- consult("/Users/tarvydas/quicklisp/local-projects/pypm/poc/das2f/onSameDiagram.pl").
?- consult("/Users/tarvydas/quicklisp/local-projects/pypm/poc/das2f/inside.pl").
?- consult("/Users/tarvydas/quicklisp/local-projects/pypm/poc/das2f/names.pl").
?- consult("/Users/tarvydas/quicklisp/local-projects/pypm/poc/das2f/ports.pl").
?- consult("/Users/tarvydas/quicklisp/local-projects/pypm/poc/das2f/contains.pl").
query_helper(Parent,Child):-
contains(Parent,Child),
true.
query:-
(setof([Parent,Child],query_helper(Parent,Child),Set),
json_write(user_output,Set,[width(128)])
)
;
json_write(user_output,[],[width(123)]).
~~~
cat >${temp}.js <<'~~~'
const fs = require ('fs');
var rawText = fs.readFileSync ('/dev/fd/0');
var parameters = JSON.parse(rawText);
parameters.forEach (p => {
  var Parent = p [0];
var Child = p [1];
  
if (true) { console.log (`das_fact(contains,${Parent},${Child}).`);};
});
  
~~~
swipl -g "consult(${temp})." -g 'query.' -g 'halt.' | node ${temp}.js
rm -f ${temp}.pl
rm -f ${temp}.js

