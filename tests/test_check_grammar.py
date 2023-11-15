from lib.check_grammar import * 

def test_capital_letter_and_punctuation_mark():
    result = check_grammar('This is a sentence.')
    assert result == True