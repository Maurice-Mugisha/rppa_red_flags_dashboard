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


    def create_markup(self, html_markup):

        file_exists = os.path.isfile(self.file_name)
        if file_exists == False:
            output_file = Path(self.file_name)
            output_file.parent.mkdir(exist_ok=True, parents=True)

        file = open(self.file_name, "w")
        file.write(html_markup)
        file.close()
