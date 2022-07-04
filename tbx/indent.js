var indentation = [];
function indent1 (s) {
    var opens = (s.match (/\(\./g) || []).length;
    var closes = (s.match (/\.\)/g) || []).length;
	var r0 = s.trim ();
    var r1 = r0.replace (/\(\./g, '');
	var r2 = r1.replace (/\.\)/g, '');
    var spaces = indentation.join ('');
    var r  = spaces + r2.replace (/\n/g, spaces);
    var diff = opens - closes;
    if (diff > 0) {
	while (diff > 0) {
	    indentation.push ('  ');
	    diff -=1;
	}
    } else {
	while (diff < 0) {
	    indentation.pop ();
	    diff += 1;
	}
    }
    return r;
}

var test = String.raw`
(.def handler (self, message):
if (False):
(.
	pass
	.)
elif (message.port == 'text'):
(.self.a ().)
.)
`.split ('\n');

test.forEach (line => {
    var s = indent1 (line);
    console.log (s);
});


