import matplotlib.pyplot as plt
import numpy as pn



class PieChartDrawer:

    def __init__(self, value_array, color_array, label_array, width, height, save_path_and_name):
        self.value_array = value_array
        self.color_array = color_array
        self.label_array = label_array
        self.width = width
        self.height = height
        self.save_path_and_name = save_path_and_name

    def draw_pie_chart(self):
        plt.figure(figsize = (self.width, self.height))
        fig, ax = plt.subplots()
        ax.pie(self.value_array, labels=self.label_array, autopct = '%1.1f%%', wedgeprops = {"edgecolor" : "white", 'linewidth': 0, 'antialiased': True})
        ax.set_title("Some real title")
        plt.pie(self.value_array, colors=self.color_array)
        plt.tight_layout()
        plt.savefig(self.save_path_and_name, transparent=True)


#color_list = ['green', 'black', 'blue']
#label_list = ["Submitted plan", "Did not submit plans", "excluded"]
#width = 8
#height = 3
#file_name = "red_flag_2.jpg"
#pie_chart_drawer_object = PieChartDrawer(value_list, color_list, label_list, width, height, file_name)
#pie_chart_drawer_object.draw_pie_chart()
