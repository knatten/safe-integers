#!/usr/bin/env python3
import inflect

p = inflect.engine()

max_value = 640000 #640k ought to be enough for anybody
include_file = "include/safe_numbers.h"
with open(include_file, 'w') as out:
    out.write('constexpr auto ONE = +!!"";\n')
    prev = "ONE"
    for i in range(2,max_value+1):
        n = p.number_to_words(i)\
            .replace(' ', '')\
            .replace('-', '')\
            .replace(',', '')\
            .upper()
        out.write('constexpr auto ' + n + ' = ' + prev + ' + ONE;\n')
        prev = n
    out.write('// ' + prev + ' ought to be enough for anybody\n')
