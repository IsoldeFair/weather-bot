from jsgf import parse_grammar_string


class WeatherBot:
    """Bot for checking the weather"""
    def __init__(self, grammar_path):

        with open(grammar_path) as myf:
            data = myf.read()

        self.grammar = parse_grammar_string(data)

        print(self.grammar)

    def response(self, user_input):
        rule = self.grammar.find_matching_rules(user_input)
        return rule

