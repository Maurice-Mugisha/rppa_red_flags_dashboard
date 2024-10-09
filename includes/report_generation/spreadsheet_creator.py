
import openpyxl
import pandas as pd

import os
from pathlib import Path



class SpreadsheetCreator:


    def __init__(self, file_name, data):
        self.file_name = file_name
        self.data = data


    def create_spreadsheet(self):
        workbook = openpyxl.Workbook()
        sheet = workbook.active

        for row in self.data:
            sheet.append(row)

        self.ensure_directory_exists()
        workbook.save(self.file_name)


    def ensure_directory_exists(self):
        file_exists = os.path.isfile(self.file_name)
        if file_exists == False:
            output_file = Path(self.file_name)
            output_file.parent.mkdir(exist_ok=True, parents=True)


#file_name = "my_excel_file.xlsx"
#data = [
#          ["Name", "Age", "City"],
#          ["Maurice", "31", "Kigali"],
#          ["Mugisha", "30", "Kampala"],
#          ["Muhumuza", "30", "Kabale"]
#       ]
#spreadsheet_creator_object = SpreadsheetCreator(file_name, data)
#spreadsheet_creator_object.create_spreadsheet()
