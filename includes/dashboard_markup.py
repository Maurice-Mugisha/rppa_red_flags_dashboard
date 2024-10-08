class DashboardMarkup:

    def __init__(self, name):
        self.name = name

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
               background: #005A9C;
               border-top-right-radius: 30em;
             }

             /* Red flags css */
             .red_flag_name, .fiscal_year_label{
               cursor: pointer;
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
                 matchedElement.style.display = "table"
              }
            </script>
        '''
        self.js = js
        return js

    def get_header(self):
        header_markup = '''
           <table id="header_table" cellpading="0" cellspacing="0" border="0">
             <tr id="header_table_top_row">
               <td align="right" valign="middle" width="14%">
                 <img src="../images/rwanda_coat_of_arms.png" width="154px" height="75px" alt="">
               </td>
               <td align="center" valign="middle" class="header_table_row_column">
                 <h1>Rwanda Public Procurement Authority</h1>
               </td>
               <td align="left" valign="middle" width="10%">
                 <img src="../images/rwandan_flag_star.png" width="77px" height="77px" alt="">
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
        '''
        self.header_markup = header_markup
        return header_markup

    def get_body(self):
        body_markup = "<body>"
        body_markup += self.get_header()
        body_markup += '''
           <table id="body_table" cellpading="0" cellspacing="0" border="0" height="70vh">
             <tr>
               <td width="15%" valign="top" align="middle">
                 <h4>Fiscal years</h4>
                 <label class="fiscal_year_label" id="fy_1" onclick="showVisualization(this, 'red_flags');">Fiscal year 1</label><br />
                 <label class="fiscal_year_label" id="fy_2">Fiscal year 2</label><br />
                 <label class="fiscal_year_label" id="fy_3">Fiscal year 3</label><br />
                 <label class="fiscal_year_label" id="fy_4">Fiscal year 4</label><br />
                 <br />
                 <hr style="height:4px; border-width:0; color:#CFCFCF; background-color:#CCCCCC; margin-left: 20%; margin-right: 20%;">
               </td>
               <td rowspan="2"></td>
               <td width="25%" rowspan="2" valign="top" align="middle">
                 <h4>Red flags</h4>
                 <label class="red_flag_name" id="rdf_1" onclick="showVisualization(this, 'red_flags');">Red flag 1</label><br />
                 <label class="red_flag_name" id="rdf_2">Red flag 2</label><br />
                 <label class="red_flag_name" id="rdf_3">Red flag 3</label><br />
                 <label class="red_flag_name" id="rdf_4">Red flag 4</label><br />
                 <hr style="height:4px; border-width:0; color:#CFCFCF; background-color:#CCCCCC; margin-left: 20%; margin-right: 20%;">
                 <table border="0" cellpadding="0" cellspacing="0" width="100%" id="rdf_1_visualiztion" class="red_flags" style="display: none;">
                   <tr>
                     <td valign="middle" align="center">For red flag 1</td>
                   </tr>
                   <tr>
                     <td valign="middle" align="center">
                       <a href="#" style="text-decoration: none; font-size: 12px;">Download report</a>
                     </td>
                   </tr>
                 </table>
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
        body_markup += self.get_footer()
        body_markup += "</body>"
        self.body_markup = body_markup
        return body_markup

    def get_sections(self):
        sections_markup = '''

        '''
        return sections_markup


    def get_red_flag_labels(self, red_flag_list):
        red_flag_label_markup_list = list()
        for red_flag in red_flag_list:
            red_flag_label_markup_list.append('''<label class="fiscal_year_label" id="fy_1" onclick="showVisualization(this, 'red_flags');">''' + red_flag + '''</label><br />''')

    def get_visualization_markup(self, info_dictionary):
        visualization_table = '''
           <table border="0" cellpadding="0" cellspacing="0" width="100%" id="rdf_1_visualiztion" class="red_flags" style="display: none;">
           <tr>
             <td valign="middle" align="center">''' + info_dictionary['visualization_link'] + '''</td>
           </tr>
           <tr>
             <td valign="middle" align="center">
               <a href="#" style="text-decoration: none; font-size: 12px;">''' + info_dictionary['report_link'] + '''</a>
             </td>
           </tr>
           </table>
        '''

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
        web_page += self.css
        web_page += self.js
        web_page += "</head>"
        web_page += self.get_body()
        web_page += "</html>"
        return web_page
