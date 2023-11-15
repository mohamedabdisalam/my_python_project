from lib.check_grammar import * 

def test_capital_letter_and_punctuation_mark():
    result = check_grammar('This is a sentence.')
    assert result == True


def test_capital_letter_and_incorrect_punctuation_mark():
    result = check_grammar('This is a sentence,')
    assert result == False

def test_lower_case_letter_and_punctuation_mark():
    result = check_grammar('this is a sentence.')
    assert result == False