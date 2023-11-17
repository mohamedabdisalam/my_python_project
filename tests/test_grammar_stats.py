from lib.grammar_stats import GrammarStats

"""
Given a string
#check returns True if the text
begins with a capital letter and ends with a 
sentence ending punctuation
"""

def test_capital_letter_and_punctuation():
    grammar_stats = GrammarStats()
    result = grammar_stats.check("This is a sentence!")
    assert result == True

def test_capital_letter_incorrect_punctuation():
    grammar_stats = GrammarStats()
    result = grammar_stats.check('This is a sentence,')
    assert result == False

"""
Return int: the percentage of texts checked so 
far that passed the check
defined in the `check` method. The number 55 represents 55%.
"""

def test_percengtage_of_text_passed_check():
    grammar_stats = GrammarStats()
    grammar_stats.check('One two three four!')
    grammar_stats.check('Five six seven eight')
    result = grammar_stats.percentage_good()
    assert result == 50
