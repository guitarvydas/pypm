raw {⟪
def rmCodeQuotesState0 (textList):
    if (0 == len (textList)):
        return []
    else:
        first = textList [0];
        rest = textList [1:]
        if (first == '```'):
            return self.rmCodeQuotesState1 (rest)
        else:
            return [first] + self.rmCodeQuotesState0 (rest)
        
def rmCodeQuotesState1 (textList):
    if (0 == len (textList)):
        return []
    else:
        first = textList [0];
        rest = textList [1:]
        if (first == '```'):
            return self.rmCodeQuotesState0 (rest)
        else:
            return self.rmCodeQuotesState1 (rest)
⟫}
on ➢❲text❳ {⟪
    text = message.data.split ('\n')
    result = self.rmCodeQuotesState0 (text)
    self.send ('[text]', result)
⟫}
