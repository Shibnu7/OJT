import pandas as pd

# Step 1: Convert the file into a DataFrame
df = pd.read_csv('air-pollution.csv')

# Print the columns to verify their names
print("Columns in the DataFrame:", df.columns)

# Step 2: Check unique values in the 'Entity' column to see what values exist
unique_entities = df['Entity'].unique()
print("Unique entities in the DataFrame:", unique_entities)

# Step 3: Create a filter based on the Entity (country)
# For this example, let's filter for 'United States' if it exists in the 'Entity' column
target_entity = 'United States'

if target_entity in unique_entities:
    entity_filter = df['Entity'].str.strip() == target_entity
    filtered_df = df[entity_filter].copy()  # Use .copy() to avoid SettingWithCopyWarning
    
    # Step 4: Find the median, mean, and standard deviation for the respective column
    # Assuming the column of interest is 'Nitrogen oxide (NOx)'
    if 'Nitrogen oxide (NOx)' in filtered_df.columns:
        filtered_df['median_NOx'] = filtered_df['Nitrogen oxide (NOx)'].median()
        filtered_df['mean_NOx'] = filtered_df['Nitrogen oxide (NOx)'].mean()
        filtered_df['std_NOx'] = filtered_df['Nitrogen oxide (NOx)'].std()
    else:
        print("Column 'Nitrogen oxide (NOx)' not found in the DataFrame")
    
    # Step 5: Delete the repeated entries
    filtered_df = filtered_df.drop_duplicates()
    
    # Step 6: Change the null values into 0
    filtered_df = filtered_df.fillna(0)
    
    # Print the resulting DataFrame
    print(filtered_df)
    
    # Optionally, save the resulting DataFrame to a new CSV file
    filtered_df.to_csv('filtered_data.csv', index=False)
else:
    print(f"Entity '{target_entity}' not found in the DataFrame")
