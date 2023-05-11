def get_math_symbol(symbol_name):
    symbols = {
        "integral": chr(8747),
        "sum": chr(8721),
        "product": chr(8719),
        "infinity": chr(8734),
        "partial": chr(8706),
        "alpha": chr(945),
        "beta": chr(946),
        "gamma": chr(947),
        "delta": chr(948),
        "epsilon": chr(949),
        "theta": chr(952),
        "lambda": chr(955),
        "mu": chr(956),
        "sigma": chr(963),
        "omega": chr(969),
        "hash": "#",
        "left_bracket": "[",
        "right_bracket": "]",
        "left_brace": "{",
        "right_brace": "}",
        "asterisk": "*",
        "underscore": "_",
        "pipe": "|",
        "less_than": "<",
        "greater_than": ">",
        "apostrophe": "'",
        "caret": "^",
        "plus": "+",
        "minus": "-",
        "slash": "/",
        "left_paren": "(",
        "right_paren": ")",
        "percent": "%",
        "tilde": "\u223C"
    }
    if symbol_name in symbols:
        return symbols[symbol_name]
    else:
        print("Symbol not found in archive")

symbol_name = input("Enter the name of the math symbol you want to find: ")
symbol = get_math_symbol(symbol_name)
if symbol:
    print(symbol)
