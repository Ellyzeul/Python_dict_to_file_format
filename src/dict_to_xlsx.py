from openpyxl import Workbook


def append_to_xlsx_recursive(ws, dic, index):
    if(isinstance(dic, list)):
        # ...
    dict_items = list(dic)
    keys = dic.keys()
    values = dic.values()
    next_index = index

    ws.append(keys)
    index += 1

    for value in values:
        if(isinstance(value, dict)):
            new_index = append_to_xlsx_recursive(ws, value, index)
            if(new_index > next_index):
                next_index = max([new_index, next_index])
            continue
        # ...

def dict_to_xlsx(src):
    wb = Workbook()
    ws = wb.active

    append_to_xlsx_recursive(ws, src, 1)

    # code goes here...

    return wb
