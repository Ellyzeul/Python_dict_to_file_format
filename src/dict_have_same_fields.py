def dict_have_same_fields(dict_1, dict_2):
    keys_1 = list(dict_1.keys())
    keys_2 = list(dict_2.keys())
    lim = min(len(keys_1), len(keys_2))
    
    for i in range(lim):
        if(keys_1[i] != keys_2[i]):
            return False
    return True