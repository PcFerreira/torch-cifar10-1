#Prepare the dataset (i should probably write this in a better way tbh)
import pandas as pd
import shutil
import os

csv_file_path = './ISIC_2020_Training_GroundTruth.csv'
destination_folder = './isic_class/melanoma/' 

# Read the CSV file into a DataFrame
df = pd.read_csv(csv_file_path)

# Filter the DataFrame
filtered_melanoma = df[df['diagnosis'] == 'melanoma']

# Ensure the destination folder exists
os.makedirs(destination_folder, exist_ok=True)

# Copy unknown files
for file_path in filtered_melanoma['image_name']:
    if os.path.isfile('./train/' + file_path + '.jpg'):
        shutil.copy('./train/' + file_path + '.jpg', destination_folder)