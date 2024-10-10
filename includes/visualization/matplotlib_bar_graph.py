import matplotlib.pyplot as plt
import numpy as np




class BarGraphDrawer:


    def __init__(self, data_dictionary, bar_color, edge_color, x_axis_label, y_axis_label, title, width, height, save_path_and_name):
        self.data_dictionary = data_dictionary
        self.bar_color = bar_color
        self.edge_color = edge_color
        self.x_axis_label = x_axis_label
        self.y_axis_label = y_axis_label
        self.title = title
        self.width = width
        self.height = height
        self.save_path_and_name = save_path_and_name


    def draw_bar_graph(self):
        fig = plt.figure(figsize = (self.width, self.height))
        plt.bar(list(self.data_dictionary.keys()), list(self.data_dictionary.values()), color=self.bar_color, edgecolor=self.edge_color)
        plt.xlabel(self.x_axis_label)
        plt.ylabel(self.y_axis_label)
        plt.title(self.title)
        #plt.legend()
        plt.tight_layout()
        plt.savefig(self.save_path_and_name, transparent=True)





class MultiDimensionalBarGraphDrawer:

    def __init__(self, data_dictionary, dimen_color_list, x_axis_label_list, bar_color, edge_color, x_axis_label, y_axis_label, title, width, height, save_path_and_name):
        self.data_dictionary = data_dictionary
        self.dimen_color_list = dimen_color_list
        self.x_axis_label_list = x_axis_label_list
        self.bar_color = bar_color
        self.edge_color = edge_color
        self.x_axis_label = x_axis_label
        self.y_axis_label = y_axis_label
        self.title = title
        self.width = width
        self.height = height
        self.save_path_and_name = save_path_and_name

    def draw_multi_dimensional_bar_graph(self):
        fig = plt.figure(figsize = (self.width, self.height))
        x_axis = np.arange(len(self.x_axis_label_list))
        width = 0.2

        i = 0
        for label_key in self.data_dictionary:
            plt.bar(x_axis + (i*width), self.data_dictionary[label_key], width, label=label_key, color=self.dimen_color_list[i]) #, color = r, use a color array for the rest
            i += 1

        plt.xticks(x_axis, self.x_axis_label_list)
        plt.xlabel(x_axis_label)
        plt.ylabel(y_axis_label)
        plt.title(self.title)
        plt.legend()
        plt.tight_layout()
        plt.savefig(self.save_path_and_name, transparent=True)




#value_dict = {'C':20, 'C++':15, 'Java':30, 'Python':35}
#bar_color = "#007700"
#edge_color = "white"
#x_axis_label = "years"
#y_axis_label = "tenders"
#title = "Fiscal year tenders"
#width = 10
#height = 5
#save_path_and_name = "red_flag_3.jpg"

#bargraph_drawer_object = BarGraphDrawer(value_dict, bar_color, edge_color, x_axis_label, y_axis_label, title, width, height, save_path_and_name)
#bargraph_drawer_object.draw_bar_graph()



#multi_dimen_data_dicitonary = {'procuring':[100, 150, 50, 30, 20], 'supplying':[10, 120, 70, 15, 60], 'All':[120, 270, 120, 45, 80]}
#dimen_color_list = ["r", "g", "b"]
#x_axis_label_list = ["2021", "2022", "2023", "2024", "2025"]
#bar_color = "#007700"
#edge_color = "white"
#x_axis_label = "Years"
#y_axis_label = "Red flags"
#title = "Year red flags comparison"
#width = 10
#height = 5
#save_path_and_name = "red_flag_4.jpg"
#multi_dimensional_bar_graph_drawer = MultiDimensionalBarGraphDrawer(multi_dimen_data_dicitonary, dimen_color_list, x_axis_label_list, bar_color, edge_color, x_axis_label, y_axis_label, title, width, height, save_path_and_name)
#multi_dimensional_bar_graph_drawer.draw_multi_dimensional_bar_graph()
