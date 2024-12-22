# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 00:47:49 2024

@author: kenneyke
"""
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Read the Excel file
file_path = r'D:\ODOT_SPR866\My Label Data Work\New Manual Labelling\6_Analysis\Site Analysis Confidence Score.xlsx'  # Replace with your file path
df = pd.read_excel(file_path)

# Define the object names (features) as specified
features = ['Pole-like Objects',
            'Powerlines',
            'Street_lamp',
            'Traffic Light',
            'Traffic Sign',
            'Trees',
            'Wire Conductor',
            'Lane Marking', 
            'High Vegetation',
            'Highway Gantry',
            'Telephone/TV cables', 
            'Bush',
            'Unclassified',
            'Unknown']

# Ensure the features are present in the DataFrame
df = df[['Site No.'] + features]  # Adjust column selection to match your file

# Extract only the IDs for the X-axis
df['Site No.'] = df['Site No.'].apply(lambda x: str(x).split()[-1])  # Adjust this as per the structure of your Scene No.

# Melt the DataFrame to long format for easier plotting
df_melted = df.melt(id_vars='Site No.', value_vars=features,
                    var_name='Object Name', value_name='Confidence Score')

# Define custom colors (can be hex codes or named colors)
custom_colors = ['#8c564b',
                 '#9467bd',
                 '#F7DC6F',
                 '#E67E22',
                 '#E64A19',
                 '#66BB6A',
                 '#aec7e8',
                 '#660033', 
                 '#006600',
                 '#17becf',
                  '#3399CC',
                  '#CCFF99',
                 '#9E9E9E',
                 '#78909C']

# Create a palette dictionary to map object names to custom colors
palette = dict(zip(features, custom_colors))

# Plot the scatterplot for each object against Site IDs
plt.figure(figsize=(16, 12))
ax = sns.scatterplot(x='Site No.', y='Confidence Score', hue='Object Name', data=df_melted, palette=palette, s=70, style='Object Name', markers='o')

# Customize the plot
plt.title('Distribution of Confidence Scores for Objects Across Sites', fontsize=14, fontweight='bold')
plt.ylabel('Confidence Score (%)',  fontsize=12, fontweight='bold')
plt.xlabel('Site IDs', fontsize=12, fontweight='bold')  # Label the X-axis appropriately
plt.legend(loc='upper right', bbox_to_anchor=(1.25, 1), fontsize=15)
plt.tight_layout()

# Set y-axis ticks at intervals of 5
y_ticks = range(int(df_melted['Confidence Score'].min() // 5) * 5,
                int(df_melted['Confidence Score'].max() // 5) * 5 + 5, 5)
plt.yticks(y_ticks, fontsize=12)  # Increase y-axis tick label font size

# Increase x-axis tick label font size
plt.xticks(fontsize=12)

# Show the plot
plt.show()