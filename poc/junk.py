initially {⟪result = []⟫}
on ➢❲[text]❳ {⟪
for line in message.data:
    result += re.findall ('(\[\[[^\]]+\]\])',line)
self.send (self, '[links]', result, message)
⟫}
