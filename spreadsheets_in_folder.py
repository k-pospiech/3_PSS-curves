def spreadsheets_in_folder(folder):
    """
    Function that scans the given directory and returns a list with the names of .xls, .xlsx and .csv files inside
    Taken that list, it will create the dictionary with spreadsheet name as a key, and values being lists of sheets inside
    For .csv files, it will be only a list with one item "Data", since .csv files don't have multiple sheets

    Example:
    >>> a = spreadsheets_in_folder()
    >>> print(a)
    {'ANSYS120mm2Copper_Profile.xls': ['Cable selection and operating parameters', 'Derating', 'Temperature - time', 'Voltage drop - time'], 'Input.xlsx': ['0.5mm2', '10mm2', '120mm2'], 'Template.xlsx': ['Case1', 'Case2']}
    """
    import os
    import xlrd
    import openpyxl

    # Define the extensions
    extensions = (".xls", ".xlsx", ".csv")

    # Get all files from the directory
    all_files = [file for file in os.listdir(folder) if os.path.isfile(os.path.join(folder,file))]
    # Filter the spreadsheets through extensions
    spreadsheets = [check for check in all_files if check.endswith(extensions)]

    # Extract the dictionaries of sheets inside
    worksheets = {}

    for spreadsheet in spreadsheets:
        path = os.path.join(folder, spreadsheet)

        if spreadsheet.endswith(".xls"):
            wb = xlrd.open_workbook(path, on_demand=True)
            sheets = wb.sheet_names()
            wb.release_resources()
        elif spreadsheet.endswith(".xlsx"):
            wb = openpyxl.load_workbook(path, read_only=True)
            sheets = wb.sheetnames
            wb.close()
        elif spreadsheet.endswith(".csv"):
            sheets = ["Data"]

        worksheets[spreadsheet] = sheets
    
    return worksheets