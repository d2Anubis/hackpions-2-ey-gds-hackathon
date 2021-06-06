from fuzzywuzzy import fuzz


def get_fuzzy_score(str1, str2):
    return fuzz.token_set_ratio(str1, str2)/100
