#num_to_text
### Converts given integer number to its string representation (RU/russian)

Limitations: positive integers up to N * 10^123,
where 0 < N < 1000

##examples:
```python
from num_to_text import num_to_text

print(num_to_text(1234567890987654321))

# out:
# один квинтиллион двести тридцать четыре квадриллиона пятьсот шестьдесят семь триллионов
# восемьсот девяносто миллиардов девятьсот восемьдесят семь миллионов
# шестьсот пятьдесят четыре тысячи триста двадцать один
```

Tested on python 3.8, but should be fine with python >= 3.5
and (if remove usage of typing package) possible even 2.*
