def check_grammar(text):
    if text[0].isupper():
        if text[-1] in '!.?':
            return True
        else:
            return False 
    else:
        return False