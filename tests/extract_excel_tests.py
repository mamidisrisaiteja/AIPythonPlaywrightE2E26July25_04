import openpyxl

EXCEL_PATH = 'c:/Users/mamid/OneDrive/Desktop/sw/realTimeProject/ECommercePortal1/TestData/TestCaseDocument.xlsx'

wb = openpyxl.load_workbook(EXCEL_PATH)
sheet = wb.active

test_cases = []
for row in sheet.iter_rows(min_row=2, values_only=True):
    # Adjust columns as per your Excel structure
    test_id, module, title, steps, expected = row[:5]
    test_cases.append({
        'id': test_id,
        'module': module,
        'title': title,
        'steps': steps,
        'expected': expected
    })

for case in test_cases:
    print(f"ID: {case['id']}, Module: {case['module']}, Title: {case['title']}")
    print(f"Steps: {case['steps']}")
    print(f"Expected: {case['expected']}")
    print('-'*40)
