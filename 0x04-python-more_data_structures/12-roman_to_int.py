#!/usr/bin/python3
def roman_to_int(roman_string):
    smm = 0
    if(roman_string and isinstance(roman_string, str)):
        IVL = {'D': 500, 'C': 100, 'M': 1000, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
        aLST = [IVL.get(x) for x in roman_string]
        for idx, chr in enumerate(aLST):
            if(idx < len(aLST) - 1):
                if aLST[idx + 1] > chr:
                    smm -= chr
                else:
                    smm += chr
            else:
                smm += chr
                return(smm)
