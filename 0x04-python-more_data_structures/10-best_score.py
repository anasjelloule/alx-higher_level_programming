#!/usr/bin/python3
def best_score(a_dictionary):
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None

    rtn = list(a_dictionary.keys())[0]
    bg_ = a_dictionary[rtn]
    for k, v in a_dictionary.items():
        if v > bg_:
            bg_ = v
            rtn = k
            return (rtn)
