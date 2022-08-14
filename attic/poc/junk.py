initially {⟪self.result = []⟫}
on ➢❲[text]❳ {⟪
for line in message.data:
    self.result += re.findall ('(\[\[[^\]]+\]\])',line)
self.send ('[links]', self.result)
⟫}
