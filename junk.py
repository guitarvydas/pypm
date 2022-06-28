import re

def markua (s):
    return s.replace ('\n', '').strip ().lower ().replace (' ', '--')

#s = re.sub (r'\[\[([^]]*)\]\]', f'![{m.group(g)}](resources/' + markua (m.group(g)) + ')'

# s = re.sub (r'\[\[([^]]*.png)\]\]', '\1', 'abc')
# print (s)

# spng = re.sub (r'xpy', 'p', 'xpy')
# print (spng)

# spng = re.sub (r'x(q)y', r'\1', 'xqy')
# print (spng)

# spng = re.sub (r'x(q).pngy', r'\1', 'xq.pngy')
# print (spng)

# spng = re.sub (r'\[\[(q)\]\]', r'\1', 'x[[q]]y')
# print (spng)

# spng = re.sub (r'\[\[(q)\]\]', r'\1', 'x[[q]]y abc X[[q]]Y')
# print (spng)

# spng = re.sub (r'\[\[(.\.png)\]\]', r'<<\1>>', 'x[[1.png]]y abc X[[2.png]]Y')
# print (spng)

# spng = re.sub (r'\[\[([^][]+\.png)\]\]', r'![resources/\1]', 'x[[123.png]]y abc X[[456.png]]Y')
# print (spng)

# text = 'x[[123.png]]y abc X[[456.png]]Y'
# subbed = re.sub (r'\[\[([^][]+\.png)\]\]', r'![resources/\1]', text)
# print (subbed)

text = 'x[[123 789.png]]y abc X[[456 777 A888B.png]]Y'

def dosub (match):
    sub1 = match.group (1)
    sub2 = markua (sub1)
    sub = f'![resources/{sub2}]'
    return sub

subbed = re.sub (r'\[\[([^][]+\.png)\]\]', dosub, text)
print (subbed)
