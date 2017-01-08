#!/usr/bin/env python
import matplotlib.pyplot as plt

from .plotter import Plotter
from .constants import PLOT, COLORS


class ComparisonPlotter(Plotter):
    def __init__(self, data_list):
        temp_data = data_list[0]
        Plotter.__init__(self, temp_data['t'], temp_data['zeros'])

        self.trajectory_fig, self.trajectory_plot = plt.subplots(1, 1)
        self.position_fig, self.position_plot = plt.subplots(2, 1, sharex=True)
        self.position_error_fig, self.position_error_plot = plt.subplots(2, 1, sharex=True)
        self.control_action_fig, self.control_action_plot = plt.subplots(2, 1, sharex=True)

        self.x_ref = temp_data['x_ref']
        self.y_ref = temp_data['y_ref']
        self.data_list = data_list

    def plot_comparison(self):
        self.plot_reference(self.trajectory_plot, r'${\rm reference}$', self.y_ref, self.x_ref)
        self.plot_reference(self.position_plot[0], 'x', self.x_ref)
        self.plot_reference(self.position_plot[1], 'y', self.y_ref)

        for i in range(len(self.data_list)):
            self.trajectory_plot.plot(self.data_list[i]['x'], self.data_list[i]['y'],
                                      COLORS['line_' + str(i)],
                                      label=r'${\rm' + self.data_list[i]['controller_name'] + str(i) + r'}$')

        self.plot_zeros(self.position_error_plot[0])
        self.plot_zeros(self.position_error_plot[1])
        plt.show()
