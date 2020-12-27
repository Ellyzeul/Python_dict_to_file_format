from load_paths import load_paths
load_paths()
from dict_to_xlsx import dict_to_xlsx


print('\n\nWorkbook allocated on:')
print(dict_to_xlsx([{
    'field_1': 'value_1_1',
    'field_2': 'value_1_2',
    'field_3': 'value_1_3',
    'field_4': 'value_1_4'
},
{
    'field_1': 'value_2_1',
    'field_2': 'value_2_2',
    'field_3': 'value_2_3',
    'field_4': 'value_2_4'
}]))

print('\n')