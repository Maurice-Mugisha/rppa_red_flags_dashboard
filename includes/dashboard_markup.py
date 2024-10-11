import os
from pathlib import Path




class DashboardMarkup:


    def __init__(self, file_name):
        self.file_name = file_name


    def set_fiscal_year_list(self, fiscal_year_list):
        self.fiscal_year_list = fiscal_year_list


    def set_red_flag_list(self, red_flag_list):
        self.red_flag_list = red_flag_list


    def set_fiscal_year_red_flag_map(self, fiscal_year_red_flag_dictionary):
        self.fiscal_year_red_flag_dictionary = fiscal_year_red_flag_dictionary


    def set_visualization_dictionary(self, visualization_dictionary):
        self.visualization_dictionary = visualization_dictionary


    def get_css(self):
        css = '''
           <style media="screen" type="text/css">

             body{
               width: 100%;
               height: 100%;
               margin: 0%;
               padding: 0%;
             }

             /*  header table css */

             #header_table{
               width: 100%;
               height:15vh;
               margin: 0%;
               padding: 0%;
             }

             #header_table_top_row{
               background: #FFFFFF;
               height: 70px;
               color: #334433;
             }

             #header_table_middle_row{
               background: #E5BE01;
               color: #003300;
               height: 40px;
             }

             #header_table_bottom_row{
               background: #20603D;
               height: 30px;
             }

             #header_table_row_column{
               padding:40%;
               display: static;
             }

             h1{
               height: 30px;
               margin: 7px 0px 12px;
               padding:0% 0% 0% 7%;
               font-size: 32px;
               color: #555555;
             }

             h4{
               color: #999999;
               font-weight: bold;
             }

             h6{
               height: 10px;
               margin: 3px 1px 5px;
               padding:0% 0% 0% 10%;
               color: #777777;
             }

             /* body table css */
             #body_table{
               width: 100%;
               height: 70vh;
             }

             /* footer table css */

             #footer_table{
               width: 100%;
               height: 15vh;
               background: #777777; /* #005A9C */
               border-top-right-radius: 30em;
             }

             /* Red flags css */
             .red_flag_name, .fiscal_year_label{
               cursor: pointer;
             }

             .red_flag_name{
               display: none;
               font-size: 12px;
               color: #555555;
             }

           </style>
        '''
        self.css = css
        return css


    def get_js(self):
        js = '''
            <script type="text/javascript">
              function showVisualization(callingElement, calledClass){
                 var matchingElementId = callingElement.id + "_visualiztion";
                 var matchedElement = document.getElementById(matchingElementId);
                 var calledElements = document.getElementsByClassName(calledClass);
                 for(var i=0; i<calledElements.length; i++){
                    calledElements[i].style.display = "none";
                 }
                 if(matchedElement.style.display == "none")
                    matchedElement.style.display = "table";
                 else
                    matchedElement.style.display = "none";
              }

              function showFiscalYearElements(callingElement){
                 var callingElementId = callingElement.id;
                 var matchingElementArray = document.getElementsByClassName(callingElementId + "_element");
                 var universalElementArray = document.getElementsByClassName('red_flag_name');
                 for(var i=0; i<universalElementArray.length; i++){
                     universalElementArray[i].style.display = "none";
                 }
                 for(var i=0; i<matchingElementArray.length; i++){
                     matchingElementArray[i].style.display = "block";
                 }
              }
            </script>
        '''
        self.js = js
        return js


    def get_header(self):
        header_markup = """
           <table id="header_table" cellpading="0" cellspacing="0" border="0">
             <tr id="header_table_top_row">
               <td align="right" valign="middle" width="14%">
                 <img src="images/rwanda_coat_of_arms.png" width="154px" height="75px" alt="">
               </td>
               <td align="center" valign="middle" class="header_table_row_column">
                 <h1>Rwanda Public Procurement Authority</h1>
               </td>
               <td align="left" valign="middle" width="10%">
                 <img src="images/rwandan_flag_star.png" width="77px" height="77px" alt="">
               </td>
             </tr>
             <tr id="header_table_middle_row">
               <td align="right" valign="middle" width="10%">
               </td>
               <td align="center" valign="middle" class="header_table_row_column">
                 <h6>Red Flags Dashboard</h6>
               </td>
               <td align="center" valign="middle" width="10%">
                 &nbsp;
               </td>
             </tr>
             <tr id="header_table_bottom_row">
               <td align="center" valign="middle" colspan="3">
                 <h6></h6>
               </td>
             </tr>
           </table>
        """
        self.header_markup = header_markup
        return header_markup


    def get_body(self):
        body_markup = "<body>"
        body_markup += self.get_header()
        table_markup = '''
           <table id="body_table" cellpading="0" cellspacing="0" border="0" height="70vh">
             <tr>
               <td width="12%" valign="top" align="middle">
                 <h4>Fiscal years</h4>
                 ''' + self.get_fiscal_year_markup() + '''
                 <br />
                 <hr style="height:4px; border-width:0; color:#CFCFCF; background-color:#CCCCCC; margin-left: 20%; margin-right: 20%;">
               </td>
               <td rowspan="2"></td>
               <td width="30%" rowspan="2" valign="top" align="left">
                 <h4>Red flags</h4>
                ''' + self.get_red_flag_labels() + '''
                 <hr style="height:4px; border-width:0; color:#CFCFCF; background-color:#CCCCCC; margin-left: 0%; margin-right: 20%;">
                 ''' + self.get_visualization_markup() + '''
               </td>
             </tr>
             <tr>
               <td></td>
             </tr>
             <tr>
               <td></td>
               <td></td>
               <td></td>
             </tr>
           </table>
        '''
        body_markup += table_markup
        body_markup += self.get_footer()
        body_markup += "</body>"
        self.body_markup = body_markup
        return body_markup


    def get_sections(self):
        sections_markup = '''
        '''
        return sections_markup


    def get_fiscal_year_markup(self):
        fiscal_year_markup = ""
        for fiscal_year in self.fiscal_year_list:
            fiscal_year_markup_id = fiscal_year.replace("/", "")
            fiscal_year_markup += '''<label class="fiscal_year_label" id="''' + fiscal_year_markup_id + '''" onclick="showFiscalYearElements(this);">''' + fiscal_year + '''</label><br />'''
        return fiscal_year_markup


    def get_red_flag_labels(self):
        red_flag_label_markup = ""
        for fiscal_year_id in self.fiscal_year_red_flag_dictionary:
            fiscal_year_class = fiscal_year_id.replace("/", "")
            for red_flag in self.fiscal_year_red_flag_dictionary[fiscal_year_id]:
                red_flag_id = red_flag["id"]
                red_flag_name = red_flag["name"]
                red_flag_label_markup += '''<label class="red_flag_name ''' + fiscal_year_class + '''_element" id="''' + red_flag_id + '''" onclick="showVisualization(this, 'red_flags');">''' + red_flag_name + '''</label><br />'''

        return red_flag_label_markup


    def get_visualization_markup(self):
        visualization_table = ""
        for red_flag in self.red_flag_list:
            red_flag_id = red_flag["id"]

            is_image = self.visualization_dictionary[red_flag_id]['is_image']
            visualization_link = self.visualization_dictionary[red_flag_id]['visualization_link']
            report_link = self.visualization_dictionary[red_flag_id]['report_link']

            visualization_markup = ""
            visualization_markup = '''<img src="''' + visualization_link + '''" width="100%" height="100%" />''' if is_image  == True else self.read_file(visualization_link)

            visualization_table += '''
               <table border="0" cellpadding="0" cellspacing="0" width="70%" id="''' + red_flag_id + '''_visualiztion" class="red_flags" style="display: none;">
               <tr>
                 <td valign="middle" align="center">''' + visualization_markup + '''</td>
               </tr>
               <tr>
                 <td valign="top" align="center">
                   <a href="''' + report_link + '''" style="text-decoration: none; font-size: 12px;">
                     <img src="images/report_icon.png" width="30px" height="20px" title="Download report" />
                   </a>
                 </td>
               </tr>
               </table>
            '''
        return visualization_table


    def get_footer(self):
        footer_markup = '''
           <table id="footer_table" cellpading="0" cellspacing="0" border="0" height="15vh">
             <tr>
               <td colspan="3"></td>
             </tr>
             <tr>
               <td></td>
               <td></td>
               <td></td>
             </tr>
           </table>
        '''
        self.footer_markup = footer_markup
        return footer_markup


    def get_dahsboard_html_page(self, title):
        web_page = "<!DOCTYPE html>"
        web_page += "<html>"
        web_page += "<head>"
        web_page += "<title>" + title + "</title>"
        web_page += self.get_css()
        web_page += self.get_js()
        web_page += "</head>"
        web_page += self.get_body()
        web_page += "</html>"

        file_exists = os.path.isfile(self.file_name)
        if file_exists == False:
            output_file = Path(self.file_name)
            output_file.parent.mkdir(exist_ok=True, parents=True)

        file = open(self.file_name, "w")
        file.write(web_page)
        file.close()
        return web_page


    def read_file(self, file_name):
        content = ""
        file_exists = os.path.isfile(file_name)
        if file_exists == True:
            file = open(file_name, "r")
            content = file.read()
            file.close()
        else:
            content = "Not available"
        return content
