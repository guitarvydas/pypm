on ➢❲filename❳ {⟪
if (re.search (r'\.md$', message.data)):
    f = open (message.data, 'r')
    result = f.read ()
    self.send (self, 'text', result, message)
else:
    self.send (self, 'text', '', message)
⟫}
