
import openpyxl
import pandas as pd



class SpreadsheetCreator:
    

    def __init__(self, file_name, data):
        self.file_name = file_name
        self.data = data


    def create_spreadsheet(self):
        workbook = openpyxl.Workbook()
        sheet = workbook.active

        for row in self.data:
            sheet.append(row)

        workbook.save(self.file_name)


file_name = "my_excel_file.xlsx"
data = [
          ["Name", "Age", "City"],
          ["Maurice", "31", "Kigali"],
          ["Mugisha", "30", "Kampala"],
          ["Muhumuza", "30", "Kabale"]
       ]
spreadsheet_creator_object = SpreadsheetCreator(file_name, data)
spreadsheet_creator_object.create_spreadsheet()
