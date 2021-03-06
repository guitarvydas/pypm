var ohm = require ('ohm-js');

  const grammar = String.raw`
inits {
text = macro*
macro =
  | lex_RawClause
  | other
lex_RawClause = spaces "raw" spaces "{" verbatim "}"
verbatim = "⟪" notverbatim+ "⟫"
notverbatim = ~"⟪" ~"⟫" any
other = ~"raw" any
}
`;

  const actualfmt = String.raw`
text [@macro] = [[~{macro}]]
macro [x] = [[~{x}]]
lex_RawClause [ws1 kraw ws2 lb verbatim rb] = [[~{verbatim}]]
verbatim [lb @notverbatim rb] = [[~{notverbatim}]]
notverbatim [c] = [[~{c}]]
other [c] = [[]]
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
