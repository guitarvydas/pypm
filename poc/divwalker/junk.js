var xxx = {

text : function (_macro) { 
_ruleEnter ("text");

var macro = _macro._glue ().join ('');
var _result = `${macro}`; 
_ruleExit ("text");
return _result; 
},
            
macro : function (_x) { 
_ruleEnter ("macro");

var x = _x._glue ();
var _result = `${x}`; 
_ruleExit ("macro");
return _result; 
},
            
DivSection : function (_kdiv,_macro,_kenddiv) { 
_ruleEnter ("DivSection");

var kdiv = _kdiv._glue ();
var macro = _macro._glue ().join ('');
var kenddiv = _kenddiv._glue ();
var _result = `${kdiv}${macro}${kenddiv}`; 
_ruleExit ("DivSection");
return _result; 
},
            
notdiv : function (_c) { 
_ruleEnter ("notdiv");

var c = _c._glue ();
var _result = `${c}`; 
_ruleExit ("notdiv");
return _result; 
},
            
_terminal: function () { return this.sourceString; },
_iter: function (...children) { return children.map(c => c._glue ()); }
}
;
