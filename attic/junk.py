initially {⟪self.dirname = ''⟫}
on ➢❲directory❳ {⟪self.dirname = message.data⟫}
on ➢❲iterate❳ {⟪
    files = os.listdir (self.dirname)
    for fname in files:
        name = self.dirname + '/' + fname
        if (os.path.isfile (name)):
            self.send (self, 'filename', name, message)
        else:
            pass
⟫}
        
