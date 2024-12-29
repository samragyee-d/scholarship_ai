import pandas as pd

# Step 1: Load the dataset
file = "Scholarship ai/ielts_writing_dataset.csv"
df = pd.read_csv(file)

# Step 2: Convert all text columns to lowercase
for col in df.columns:
    if df[col].dtype == 'object':  # This checks for text columns
        df[col] = df[col].str.lower()

# Step 3: Drop the specified columns
columns_to_drop = ['Task_Type', 'Task_Response', 'Coherence_Cohesion', 'Lexical_Resource', 'Range_Accuracy','Examiner_Commen']
df = df.drop(columns=[col for col in columns_to_drop if col in df.columns])

# Step 4: Save the modified DataFrame to a new CSV file
df.to_csv("modified_ielts_writing_dataset.csv", index=False)

print("New CSV file created: 'modified_ielts_writing_dataset.csv'")
