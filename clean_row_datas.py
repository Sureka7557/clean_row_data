import pandas as pd

# Read the Excel file
df = pd.read_excel('new.xlsx')

# Split the 'Category' column by '|'
df['Category'] = df['Category'].str.split('|')
df['Amount'] = df['Amount'].str.split('|')

# Explode the DataFrame to create separate rows for each category
expanded_df = df.explode(['Category','Amount'])

# Reset the index if needed
expanded_df = expanded_df.reset_index(drop=True)

# Print the expanded DataFrame
print(expanded_df)
