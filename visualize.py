import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Reading the test data from 'test.txt' file
test_data = pd.read_csv('test.txt', sep='\t')

# Selecting the columns for visualization
columns_to_visualize = ['F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9', 'F10',
                        'F11', 'F12', 'F13', 'F14', 'F15', 'F16', 'F17', 'F18', 'F19', 'F20', 'F21', 'F22']

# Creating a pairplot using seaborn
sns.set(style='darkgrid')
sns.pairplot(test_data[columns_to_visualize])

# Displaying the plot
plt.show()
