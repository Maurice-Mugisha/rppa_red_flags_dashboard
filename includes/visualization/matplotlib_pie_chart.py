import matplotlib.pyplot as plt
import numpy as pn

import os
from pathlib import Path



class PieChartDrawer:

    def __init__(self, value_array, color_array, label_array, width, height, file_name, title):
        self.value_array = value_array
        self.color_array = color_array
        self.label_array = label_array
        self.width = width
        self.height = height
        self.file_name = file_name
        self.title = title

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def set_file_name(self, file_name):
        self.file_name = file_name

    def set_value_array(self, value_array):
        self.value_array = value_array

    def set_color_array(self, color_array):
        self.color_array = color_array

    def set_label_array(self, label_array):
        self.label_array = label_array

    def draw_pie_chart(self):
        plt.figure(figsize = (self.width, self.height))
        fig, ax = plt.subplots()
        ax.pie(self.value_array, labels=self.label_array, autopct = '%1.1f%%', wedgeprops = {"edgecolor" : "white", 'linewidth': 0, 'antialiased': True})
        ax.set_title(self.title)
        plt.pie(self.value_array, colors=self.color_array)
        plt.tight_layout()
        self.ensure_directory_exists()
        plt.savefig(self.file_name, transparent=True)

    def ensure_directory_exists(self):
        file_exists = os.path.isfile(self.file_name)
        if file_exists == False:
            output_file = Path(self.file_name)
            output_file.parent.mkdir(exist_ok=True, parents=True)


#color_list = ['green', 'black', 'blue']
#label_list = ["Submitted plan", "Did not submit plans", "excluded"]
#width = 8
#height = 3
#file_name = "red_flag_2.jpg"
#pie_chart_drawer_object = PieChartDrawer(value_list, color_list, label_list, width, height, file_name)
#pie_chart_drawer_object.draw_pie_chart()
