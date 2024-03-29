function transpile1 (src, grammar, fmt, grammarname, message) {
    var success = false;
    var transpiled = '';
    var jssemantics = '';
    try {
        [success, transpiled, jssemantics] = expand1 (src, grammar, fmt, grammarname);
    } catch (err) {
        success = false;
    }
    return [success, transpiled, jssemantics];
}

function fixup (s) {
    return s
        .replace (/~{/g, '${');
}

function expand1 (src, givengrammar, fmt, grammarname) {
    // expand the string src given the grammar+fmt specifications
    // grammar is the pattern(s) to be matched, fmt is how the matches
    //  are glued together to make a new string
    // return [false, trace] if pattern match fails
    // throw "internal error" if re-formatting (gluing) results in an error
    // return [false, "grammar error"] if named grammar not found
    // grammar is a string containing exactly one in Ohm-JS format
    //
    var s = '';

    var generatedObject = {};
    var generatedFmtCodeString = '';
    

    // Step 1a. Create (internal) fmt transpiler. 
    var internalgrammar = ohm.grammar (glueGrammar);
    var fmtcst = internalgrammar.match (fmt);

    if (fmtcst.failed ()) {
        return [false, "FORMAT: syntax error\n(Use fmt shorthand transpiler to debug format specification)\n\n" + internalgrammar.trace (fmt)];
    }
    // Step 1b. Transpile User's FMT spec to a JS object (for use with Ohm-JS)
    try {
        var sem = internalgrammar.createSemantics ();
        sem.addOperation ('_glue', glueSemantics);
        var generatedFmtWalker = sem (fmtcst);
        var generated = generatedFmtWalker._glue ();
        generatedFmtCodeString = fixup (generated);
        var evalstring = '(' + generatedFmtCodeString + ')'	
        generatedObject = eval(evalstring);
    } catch (err) {
        return [false, `error generating code from FMT specification evaling...\n\n${evalstring}`];
    }

    // Step 2a. Use Ohm-JS to pattern-match user's src string.
    var grammar;
    try {
	if (grammarname) {
            var grammars = ohm.grammars (givengrammar);
	    grammar = grammars [grammarname];
	    if (grammar) {
	    } else {
		return [false, `bad grammar name ${grammarname}`, '---'];
	    }
	} else {    
            grammar = ohm.grammar (givengrammar);
	}
    } catch (err) {
        return [false, "grammar error - " + err.message, 'xxx'];
    }

    var srccst = {};
    try {
        srccst = grammar.match (src);
    } catch (err) {
        return [false, err.messsage + "\n" + grammar.trace (src), 'xxx'];
    }

    if (srccst.failed ()) {
        return [false, srccst.message + "\n" + grammar.trace (src), 'xxx'];
    }

    // Step 2b. Apply fmt rewrite rules to src.
    try {
        var srcsem = grammar.createSemantics ();
        srcsem.addOperation ('_glue', generatedObject);
        var srctreewalker = srcsem (srccst);
        s = srctreewalker._glue ();
    } catch (err) {
        return [false, "failed to transpile src" + '\n' + err.message, 'xxx'];
    }
    
    return [true, s, 'const semanticsObject =' + generatedFmtCodeString + ';'];
}


var tracing = false;
var traceDepth;

const glueGrammar =
      String.raw`
SemanticsSCL {
  semantics = ws* semanticsStatement+
  semanticsStatement = ruleName ws* "[" ws* parameters "]" ws* "=" ws* code? rewrites ws*

  ruleName = letter1 letterRest*
  
  parameters = parameter*
  parameter = treeparameter | flatparameter
  flatparameter = fpws | fpd
  fpws = pname ws+
  fpd = pname delimiter
  treeparameter = "@" tflatparameter
  tflatparameter = tfpws | tfpd
  tfpws = pname ws+
  tfpd = pname delimiter

  pname = letterRest letterRest*
  rewrites = rw1 | rw2
  rw1 = "[[" ws* code? rwstringWithNewlines "]]" ws*
  rw2 = rwstring

  letter1 = "_" | "a" .. "z" | "A" .. "Z"
  letterRest = "0" .. "9" | letter1

  comment = "%%" notEol* eol
  notEol = ~eol any
  
  eol = "\n"
  ws = comment | eol | " " | "\t" | "," 
  delimiter = &"]" | &"="

  rwstring = stringchar*
  stringchar = ~"\n" any

  rwstringWithNewlines = nlstringchar*
   nlstringchar = ~"]]" ~"}}" any
  code = "{{" ws* codeString "}}" ws* 
  codeString = rwstringWithNewlines

}
`;


var varNameStack = [];


var glueSemantics = {   
    semantics: function (_1s, _2s) { 
        var __1s = _1s._glue ().join (''); 
        var __2s = _2s._glue ().join (''); 
        return `
{
${__2s}
_terminal: function () { return this.sourceString; },
_iter: function (...children) { return children.map(c => c._glue ()); }
}`; 
    },
    semanticsStatement: function (_1, _2s, _3, _4s, _5, _6, _7s, _8, _9s, _10s, _11, _12s) {
        varNameStack = [];
        var __1 = _1._glue ();
        var __2s = _2s._glue ().join ('');
        var __3 = _3._glue ();
        var __4s = _4s._glue ().join ('');
        var __5 = _5._glue ();
        var __6 = _6._glue ();
        var __7s = _7s._glue ().join ('');
        var __8 = _8._glue ();
        var __9s = _9s._glue ().join ('');
        var __10s = _10s._glue ().join ('');
        var __11 = _11._glue ();
        var __12s = _12s._glue ().join ('');
        return `
${__1} : function (${__5}) { 
_ruleEnter ("${__1}");
${__10s}
${varNameStack.join ('\n')}
var _result = \`${__11}\`; 
_ruleExit ("${__1}");
return _result; 
},
            `;
    },
    ruleName: function (_1, _2s) { var __1 = _1._glue (); var __2s = _2s._glue ().join (''); return __1 + __2s; },
    parameters: function (_1s) {  var __1s = _1s._glue ().join (','); return __1s; },
    
    parameter: function (_1) { 
        var __1 = _1._glue ();
        return `${__1}`;
    },
    flatparameter: function (_1) { 
        var __1 = _1._glue (); 
        varNameStack.push (`var ${__1} = _${__1}._glue ();`);
        return `_${__1}`;
    },
    fpws: function (_1, _2s) { var __1 = _1._glue (); var __2s = _2s._glue ().join (''); return __1; },
    fpd: function (_1, _2) { var __1 = _1._glue (); var __2 = _2._glue (); return __1; },
    
    treeparameter: function (_1, _2) { 
        var __1 = _1._glue (); 
        var __2 = _2._glue (); 
        varNameStack.push (`var ${__2} = _${__2}._glue ().join ('');`);
        return `_${__2}`; 
    },
    tflatparameter: function (_1) { 
        var __1 = _1._glue (); 
        return `${__1}`;
    },
    tfpws: function (_1, _2s) { var __1 = _1._glue (); var __2s = _2s._glue ().join (''); return __1; },
    tfpd: function (_1, _2) { var __1 = _1._glue (); var __2 = _2._glue (); return __1; },

    pname: function (_1, _2s) { var __1 = _1._glue (); var __2s = _2s._glue ().join (''); return __1 + __2s;},
    rewrites: function (_1) { var __1 = _1._glue (); return __1; },
    rw1: function (_1, _2s, codeQ, _3, _4, _5s) {
        var __2 = _2s._glue ().join ('');
        var code = codeQ._glue ();
        var __3 = _3._glue ();
        if (0 === code.length) {
            return `${__2}${__3}`;
        } else {
            throw "code in rw1 NIY";
            return `${code}${__3}`;
        }
    },
    rw2: function (_1) { var __1 = _1._glue (); return __1; },
    letter1: function (_1) { var __1 = _1._glue (); return __1; },
    letterRest: function (_1) { var __1 = _1._glue (); return __1; },

    ws: function (_1) { var __1 = _1._glue (); return __1; },
    delimiter: function (_1) { return ""; },

    rwstring: function (_1s) { var __1s = _1s._glue ().join (''); return __1s; },
    stringchar: function (_1) { var __1 = _1._glue (); return __1; },
    rwstringWithNewlines: function (_1s) { var __1s = _1s._glue ().join (''); return __1s; },
    nlstringchar: function (_1) { var __1 = _1._glue (); return __1; },

    code: function (_1, _2s, _3, _4, _5s) { return _3._glue (); },
    codeString: function (_1) { return _1._glue (); },

    // Ohm v16 requires ...children, previous versions require no ...
    _iter: function (...children) { return children.map(c => c._glue ()); },
    _terminal: function () { return this.sourceString; }
};

function _ruleInit () {
}

function traceSpaces () {
    var n = traceDepth;
    var r = '';
    while (n > 0) {
	r += ' ';
        n -= 1;
    }
    r = `[${traceDepth.toString ()}]${r}`;
    return r;
}

function _ruleEnter (ruleName) {
    if (tracing) {
        traceDepth += 1;
        console.log(`${traceSpaces ()}enter: ${ruleName.toString ()}`);
    }
}

function _ruleExit (ruleName) {
    if (tracing) {
	var spcs = traceSpaces ();
        traceDepth -= 1;
        console.log (`${traceSpaces ()}exit: ${ruleName}`); 
    }
}

function getGlueGrammar () {
    return glueGrammar;
}

var ohm = require ('ohm-js');

  const grammar = String.raw`
inits {
text = macro+
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
