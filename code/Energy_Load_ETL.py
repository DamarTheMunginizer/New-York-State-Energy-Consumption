import os
import zipfile
import pandas as pd

# Create an empty DataFrame to add the load data into
load_df = pd.DataFrame(columns = ['Name','Load','Date'])


def compile_data(name):
    # Reading the file
    df = pd.read_csv(f'data/Load Data/{name}') 
    # Extracting the date
    df['Date'] = pd.to_datetime(df['Time Stamp']).dt.date 
    # Droping the unnecessary columns
    df.drop(['Time Stamp','Time Zone','PTID'], axis = 1,inplace = True) 
    # Grouping the data to find avg load required and converting it to dataframe
    gr_df = df.groupby('Name')['Load'].mean().reset_index() 
    gr_df['Date'] = df['Date']
     # Concatenating with the global load_df
    global load_df
    load_df = pd.concat([load_df, gr_df], ignore_index=True)
    return load_df

def unzip_folder(zip_path,extract_to):
    # Open the zip file and extract contents
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)
        print(f"Contents extracted to {extract_to}")

base_path = 'data/Load Data'

# Iterate through the range of years
for i in range(2008, 2025):
    # Construct the directory path
    directory_path = os.path.join(base_path, str(i))
    
    # Check if the directory exists
    if os.path.exists(directory_path):
        # Iterate through the files in the directory
        for zip_file in os.listdir(directory_path):
            # Construct the full path to the zip file
            zip_path = os.path.join(directory_path, zip_file)
            
            # Call your unzip function
            unzip_folder(zip_path, base_path)
    else:
        print(f"Directory for year {i} does not exist.")

# Define the base path
base_path = 'data/Load Data'

# Extracting the names of all the .csv files in Load Data folder
file_names = set([i for i in os.listdir(base_path) if i.endswith('.csv')])

# Extracting and compiling the data from all .csv files with the help of  compile_data function
for name in file_names:
    compile_data(name)

# Load all data into the Load_Data.csv file
load_df.to_csv('data/Newyork_state_load_data.csv')