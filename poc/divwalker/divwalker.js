var ohm = require ('ohm-js');

  const grammar = String.raw`
divwalker {
text = macro+
macro =
  | applySyntactic<DivSection>
  | notdiv
DivSection = "<div>" macro* "</div>"
notdiv = ~"<div>" ~"</div>" any
}
`;

  const actualfmt = String.raw`
text [@macro] = [[~{macro}]]
macro [x] = [[~{x}]]
DivSection [kdiv @macro kenddiv] = [[~{macro}\n]]
notdiv [c] = [[~{c}]]
`;

  var pipelineSuccess;
  var errorMessages = '';
  
  function transpile (fmt) {
      let [success, transpiled, jssemantics] = transpile1 (srctext, grammar, fmt, "divwalker", "transpile1");
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

  var testsrctext = String.raw`
<div><div><div>initially {⟪self.dirname = ''⟫}</div><div>on ➢❲directory❳ {⟪self.dirname = message.data⟫}</div><div>on ➢❲iterate❳ {⟪</div><div>&nbsp; &nbsp; files = os.listdir (self.dirname)</div><div>&nbsp; &nbsp; for fname in files:</div><div>&nbsp; &nbsp; &nbsp; &nbsp; name = self.dirname + '/' + fname</div><div>&nbsp; &nbsp; &nbsp; &nbsp; if (os.path.isfile (name)):</div><div>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; self.send (self, 'filename', name, message)</div><div>&nbsp; &nbsp; &nbsp; &nbsp; else:</div><div>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; pass</div><div>⟫}</div><div>&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</div></div></div><div><br></div>

`;

var argv = require('yargs/yargs')(process.argv.slice(2)).argv;
var srctext = require ('fs').readFileSync (argv._[0]);
console.log (transpileActual ());
