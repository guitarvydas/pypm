var ohm = require ('ohm-js');

  const grammar = String.raw`
divwalker {
text = macro+
macro =
  | applySyntactic<Div> -- rec
  | notdiv  -- bottom  
Div = "<div>" macro* "</div>"
notdiv = ~"<div>" ~"</div>" any
}inits {
text = macro+
macro =
  | applySyntactic<OnClause>
  | other
OnClause = tOn portname "{" verbatim "}"
verbatim = "⟪" notverbatim+ "⟫"
notverbatim = ~"⟪" ~"⟫" any
other = ~tOn any
tOn = "on" ~alnum
portname = "➢" "❲" name "❳"
name = nameFirst nameRest*
nameFirst = letter
nameRest = alnum | "_"
}

`;

  const actualfmt = String.raw`
text [@macro] = [[~{macro}]]
macro [x] = [[~{x}]]
OnClause [kon portname lb verbatim rb] = [[\nelif (message.port == "~{portname}"):(.\n~{verbatim}.)]]
verbatim [lb @notverbatim rb] = [[~{notverbatim}]]
notverbatim [c] = [[~{c}]]
other [c] = [[]]
portname [kport lb name rb] = [[~{name}]]
name [nameFirst @nameRest] = [[~{nameFirst}~{nameRest}]]
nameFirst [c] = [[~{c}]]
nameRest [c] = [[~{c}]]
tOn [kon] = [[~{kon}]]
`;

  var pipelineSuccess;
  var errorMessages = '';
  
  function transpile (fmt) {
      let [success, transpiled, jssemantics] = transpile1 (srctext, grammar, fmt, "inits", "transpile1");
      if (success) {
          return (transpiled);
      } else {
          return ("FAILED " + errorMessages + "\n" + transpiled);
      }
  }

  function transpileActual () {
      // first step in building a fmt specification: output=input
      return (transpile (actualfmt));
  }

  function transpilerError (message) {
      errorMessages += '\n' + message;
      pipelineSuccess = false;
  }

var argv = require('yargs/yargs')(process.argv.slice(2)).argv;
var srctext = require ('fs').readFileSync (argv._[0]);
console.log (transpileActual ());
