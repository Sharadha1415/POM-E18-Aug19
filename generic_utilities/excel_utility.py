import xlrd

path = r'C:\Users\Ramya\PycharmProjects\POM-E18-Aug19-2025\external_files\demowebshop_testdata.xlsx'

def excel_data(sheetname):
    workbook = xlrd.open_workbook(path)                     ## book object
    worksheet = workbook.sheet_by_name(sheetname)           ## sheet object
    rows = worksheet.get_rows()                             ## generator object
    header = next(rows)

    data = {}
    for ele in rows:
        data[ele[0].value] =  ele[1].value

    return data

















