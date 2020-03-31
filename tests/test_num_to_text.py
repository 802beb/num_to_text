from num_to_text import num_to_text


def test_num_to_text() -> None:

    cases = {
        0: 'ноль',
        1: 'один',
        9: 'девять',
        10: 'десять',
        11: 'одинадцать',
        19: 'девятнадцать',
        20: 'двадцать',
        90: 'девяносто',
        99: 'девяносто девять',
        100: 'сто',
        101: 'сто один',
        110: 'сто десять',
        119: 'сто девятнадцать',
        199: 'сто девяносто девять',
        300: 'триста',
        4000: 'четыре тысячи',
        5001: 'пять тысяч один',
        5019: 'пять тысяч девятнадцать',
        50000: 'пятьдесят тысяч',
        51234: 'пятьдесят одна тысяча двести тридцать четыре',
        600000: 'шестьсот тысяч',
        999999: 'девятьсот девяносто девять тысяч '
                'девятьсот девяносто девять',
        7000000: 'семь миллионов',
        9000100: 'девять миллионов сто',
        1234567890: 'один миллиард двести тридцать четыре миллиона '
                    'пятьсот шестьдесят семь тысяч восемьсот девяносто',
        100500: 'сто тысяч пятьсот',
        1000000000: 'один миллиард',
        9876543212: 'девять миллиардов восемьсот семьдесят шесть миллионов'
                    ' пятьсот сорок три тысячи двести двенадцать',
        1000001: 'один миллион один',
        1230456789098: 'один триллион двести тридцать миллиардов '
                       'четыреста пятьдесят шесть миллионов '
                       'семьсот восемьдесят девять тысяч '
                       'девяносто восемь'
    }

    for c in cases:
        assert cases[c] == num_to_text(c)