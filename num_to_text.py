from typing import List, Dict, Union, Tuple

digits: Dict[int, Union[str, List[Union[str, Tuple[str]]]]] = {
    0: 'ноль',
    1 - 19: [
        ('один', 'одна'), ('два', 'две'), 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять',
        'десять', 'одинадцать', 'двенадцать', 'тринадцать', 'четырнадцать', 'пятнадцать', 'шестнадцать',
        'семнадцать', 'восемнадцать', 'девятнадцать'
    ],
    20 - 90: ['двадцать', 'тридцать', 'сорок', 'пятьдесят', 'шестьдесят', 'семьдесят', 'восемьдесят', 'девяносто'],
    100 - 900: ['сто', 'двести', 'триста', 'четыреста', 'пятьсот', 'шестьсот', 'семьсот', 'восемьсот', 'девятьсот']
}

ranks: Dict[int, Union[str, List[str]]] = {
    1: ['тысяча', 'тысячи', 'тысяч'],
    2: 'миллион',
    3: 'миллиард',
    4: 'триллион',
    5: 'квадриллион',
    6: 'квинтиллион',
    7: 'секстиллион',
    8: 'септиллион',
    9: 'октиллион',
    10: 'нониллион',
    11: 'дециллион',
    12: 'ундециллион',
    13: 'дуодециллион',
    14: 'тредециллион',
    15: 'кваттуордециллион',
    16: 'квиндециллион',
    17: 'сексдециллион',
    18: 'септендециллион',
    19: 'октодециллион',
    20: 'новемдециллион',
    21: 'вигинтиллион',
    22: 'унвигинтиллион',
    23: 'дуовигинтиллион',
    24: 'тревигинтиллион',
    25: 'кваттуорвигинтиллион',
    26: 'квинвигинтиллион',
    27: 'сексвигинтиллион',
    28: 'септенвигинтиллион',
    29: 'октовигинтиллион',
    30: 'новемвигинтиллион',
    31: 'тригинтиллион',
    32: 'унтригинтиллион',
    33: 'дуотригинтиллион',
    34: 'третригинтиллион',
    35: 'кваттуортригинтиллион',
    36: 'квинтригинтиллион',
    37: 'секстригинтиллион',
    38: 'септентригинтиллион',
    39: 'октотригинтиллион',
    40: 'новемтригинтиллион',
    41: 'квадрагинтиллион'
}


def num_to_text(num: int) -> str:
    if num < 0:
        raise ValueError('Only positive integers allowed')

    if not num:
        return digits[0]

    def divide_and_conc(tok: int, rank: int = 0) -> str:

        if rank >= 40:
            raise ValueError('Number is too big! Max value is N*10^123, where 0 < N < 1000')

        if float(tok) / 1000 > 1:
            cur = tok % 1000
            next_ = tok // 1000

            return divide_and_conc(tok=next_, rank=rank + 1).rstrip(' ') + ' ' \
                   + divide_and_conc(tok=cur, rank=rank).rstrip(' ')
        else:
            if not tok:
                return ''

            res: List[str] = []

            if not tok % 1000:
                if rank == 0:
                    res.append(digits[1 - 19][0][1])
                    res.append(ranks[rank + 1][0])
                else:
                    res.append(digits[1 - 19][0][0])
                    res.append(ranks[rank + 1])
                return ' '.join(res)
            if tok > 99:

                hundreds = tok // 100
                res.append(digits[100 - 900][hundreds - 1])

            tens = tok % 100

            if tens:
                if tens < 20:
                    if tens in [1, 2]:
                        res.append(digits[1 - 19][tens - 1][1 if rank == 1 else 0])
                    else:
                        res.append(digits[1 - 19][tens - 1])
                else:
                    res.append(digits[20 - 90][(tens // 10) - 2])
                    if tok % 10:
                        if tok % 10 in [1, 2]:
                            res.append(digits[1 - 19][(tens % 10) - 1][1 if rank == 1 else 0])
                        else:
                            res.append(digits[1 - 19][(tens % 10) - 1])
            if rank:
                last_digit = tok % 10

                if rank == 1:
                    if tens in range(11, 20) or not tens % 10:
                        res.append(ranks[rank][2])
                    elif last_digit == 1:
                        res.append(ranks[rank][0])
                    elif last_digit in range(2, 5):
                        res.append(ranks[rank][1])
                    else:
                        res.append(ranks[rank][2])
                else:
                    if tens in range(11, 20) or not tens % 10:
                        res.append(ranks[rank] + 'ов')
                    elif last_digit == 1:
                        res.append(ranks[rank])
                    elif last_digit in range(2, 5):
                        res.append(ranks[rank] + 'а')
                    else:
                        res.append(ranks[rank] + 'ов')
            return ' '.join(res)
    try:
        return divide_and_conc(num).rstrip(' ')
    except KeyError as e:
        raise ValueError('Number is too big! max value is 999 * 10**123') from e
