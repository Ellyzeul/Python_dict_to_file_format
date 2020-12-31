from xlsxwriter import Workbook
from dict_have_same_fields import dict_have_same_fields


def append_to_xlsx_recursive(ws, dic, row=0, col=0, new_header=False):
    if(isinstance(dic, list)):
        if(dict_have_same_fields(dic[row], dic[row+1])):
    
    keys = list(dic.keys())
    values = list(dic.values())

    if(row == 0 or new_header):
        for field in keys:
            ws.write(col, row, field)
            col += 1
        row += 1
        col = 0
    next_row = row + 1

    for value in values:
        if(isinstance(value, dict)):
            new_row = append_to_xlsx_recursive(ws=ws, dic=value, row=row, col=col, new_header=True)
            if(new_row > next_row):
                next_row = max([new_row, next_row])
            continue
        # ...

def dict_to_xlsx(src, workbook_name='converted_data.xlsx'):
    wb = Workbook(workbook_name)
    ws = wb.add_worksheet()

    append_to_xlsx_recursive(ws, src)

    # code goes here...

    return wb
