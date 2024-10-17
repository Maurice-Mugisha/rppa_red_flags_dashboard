import os
from pathlib import Path



class NonImageVisualizationMarkup:



    def set_file_name(self, file_name):
        self.file_name = file_name


    def get_red_flag_4_visual_markup(self, result_dictionary):
        red_flag_markup = '''<table border="0" cellpadding="0" cellspacing="0" width="100%" height="100%">'''
        for result_key in result_dictionary:
            result_value = result_dictionary[result_key]

            if isinstance(result_value, set) or isinstance(result_value, dict):
                continue
            color = "#FF5733" if result_value > 0 else "#008800"
            red_flag_markup += '''
                <tr>
                  <td valign="middle" align="center">
                     <label style="font-size: 48px; color: ''' + color + '''; font-family: verdan, sans-serif; font-weight: bold;">''' + str(result_value) + '''</label>
                  </td>
                  <td valign="middle" align="left" style="padding-left: 20%;">
                     <label style="font-size: 18px; color: ''' + color + '''; font-family: verdan, sans-serif; font-weight: bold;">''' + result_key.replace("_", " ") + '''</label>
                  </td>
                </tr>
                '''
        red_flag_markup += '''</table>'''
        self.create_markup(red_flag_markup)
        return red_flag_markup


    def get_red_flag_8_visual_markup(self, result_dictionary):
        red_flag_markup = '''<table border="0" cellpadding="0" cellspacing="0" width="100%" height="100%">'''
        for result_key in result_dictionary:
            result_value = result_dictionary[result_key]
            color = "#FF5733" if result_value > 0 else "#008800"
            red_flag_markup += '''
                <tr>
                  <td valign="middle" align="center">
                     <label style="font-size: 48px; color: ''' + color + '''; font-family: verdan, sans-serif; font-weight: bold;">''' + str(result_value) + '''</label>
                  </td>
                  <td valign="middle" align="left" style="padding-left: 20%;">
                     <label style="font-size: 18px; color: ''' + color + '''; font-family: verdan, sans-serif; font-weight: bold;">''' + result_key.replace("_", " ") + '''</label>
                  </td>
                </tr>
                '''
        red_flag_markup += '''</table>'''
        self.create_markup(red_flag_markup)
        return red_flag_markup


    def get_red_flag_9_visual_markup(self, result_dictionary):
        red_flag_markup = '''<table border="0" cellpadding="0" cellspacing="0" width="100%" height="100%">'''
        for result_key in result_dictionary:
            result_value = result_dictionary[result_key]
            color = "#FF5733" if result_value > 0 else "#008800"
            red_flag_markup += '''
                <tr>
                  <td valign="middle" align="center">
                     <label style="font-size: 48px; color: ''' + color + '''; font-family: verdan, sans-serif; font-weight: bold;">''' + str(result_value) + '''</label>
                  </td>
                  <td valign="middle" align="left" style="padding-left: 20%;">
                     <label style="font-size: 18px; color: ''' + color + '''; font-family: verdan, sans-serif; font-weight: bold;">''' + result_key.replace("_", " ") + '''</label>
                  </td>
                </tr>
                '''
        red_flag_markup += '''</table>'''
        self.create_markup(red_flag_markup)
        return red_flag_markup


    def get_red_flag_10_visual_markup(self, result_dictionary):
        red_flag_markup = '''<table border="0" cellpadding="0" cellspacing="0" width="100%" height="100%">'''
        for result_key in result_dictionary:
            result_value = result_dictionary[result_key]
            color = "#FF5733" if result_value > 0 else "#008800"
            red_flag_markup += '''
                <tr>
                  <td valign="middle" align="center">
                     <label style="font-size: 48px; color: ''' + color + '''; font-family: verdan, sans-serif; font-weight: bold;">''' + str(result_value) + '''</label>
                  </td>
                  <td valign="middle" align="left" style="padding-left: 20%;">
                     <label style="font-size: 18px; color: ''' + color + '''; font-family: verdan, sans-serif; font-weight: bold;">''' + result_key.replace("_", " ") + '''</label>
                  </td>
                </tr>
                '''
        red_flag_markup += '''</table>'''
        self.create_markup(red_flag_markup)
        return red_flag_markup


    def tabulate_red_flag_data(self, table_title, table_list_of_lists_data):
        red_flag_markup = '''<br />'''
        red_flag_markup += '''<table border="0" cellpadding="0" cellspacing="0" width="100%" height="100%" style="font-size:10px;">'''
        red_flag_markup += '''<tr>'''
        red_flag_markup += '''<td colspan="''' + str(len(table_list_of_lists_data[0]) + 1) + '''" align="center" valign="middle" style="background:#9F9F9F;padding:10px; font-size:14px;">''' + table_title + '''</td>'''
        red_flag_markup += '''</tr>'''
        row_number = 1
        for entry_list in table_list_of_lists_data:
            red_flag_markup += '''<tr>'''
            red_flag_markup += '''<td>''' + str(row_number) + '''</td>'''
            for item in entry_list:
                red_flag_markup += '''<td>''' + str(item) + '''</td>'''
            red_flag_markup += '''</tr>'''
            row_number += 1

        red_flag_markup += '''</table>'''
        self.append_markup(red_flag_markup)
        return red_flag_markup



    def create_markup(self, html_markup):

        file_exists = os.path.isfile(self.file_name)
        if file_exists == False:
            output_file = Path(self.file_name)
            output_file.parent.mkdir(exist_ok=True, parents=True)

        file = open(self.file_name, "w")
        file.write(html_markup)
        file.close()

    def append_markup(self, html_markup):

        file_exists = os.path.isfile(self.file_name)
        if file_exists == False:
            output_file = Path(self.file_name)
            output_file.parent.mkdir(exist_ok=True, parents=True)

        file = open(self.file_name, "a")
        file.write(html_markup)
        file.close()
