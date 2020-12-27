from load_paths import load_paths
load_paths()
from dict_have_same_fields import dict_have_same_fields


print('')

dict_1_test_1 = {
    'field_1': 1,
    'field_2': 2,
    'field_3': 3,
    'field_4': 4
}
dict_2_test_1 = {
    'field_1': 5,
    'field_2': 6,
    'field_3': 7,
    'field_4': 8
}

assert dict_have_same_fields(dict_1_test_1, dict_2_test_1) == True, 'Test 1 -- Failed - Should be True'
print('Test 1 -- Passed')

dict_1_test_2 = {
    'field_1': 1,
    'field_2': 2,
    'field_3': 3,
    'field_4': 4,
    'field_5': 5
}
dict_2_test_2 = {
    'field_1': 5,
    'field_2': 6,
    'field_3': 7,
    'field_4': 8
}

assert dict_have_same_fields(dict_1_test_2, dict_2_test_2) == True, 'Test 2 -- Failed - Should be True'
print('Test 2 -- Passed')

dict_1_test_3 = {
    'field_1': 1,
    'field_5': 2,
    'field_3': 3,
    'field_4': 4,
    'field_3': 5
}
dict_2_test_3 = {
    'field_1': 5,
    'field_2': 6,
    'field_3': 7,
    'field_4': 8
}

assert dict_have_same_fields(dict_1_test_3, dict_2_test_3) == False, 'Test 2 -- Failed - Should be False'
print('Test 2 -- Passed')

print('')