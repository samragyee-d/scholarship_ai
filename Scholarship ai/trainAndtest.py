import pandas as pd
from sklearn.model_selection import train_test_split

# Load the dataset
file = r"Scholarship ai\modified_ielts_writing_dataset.csv"
df = pd.read_csv(file)

# Split the dataset into training and testing sets
train_df, test_df = train_test_split(df, test_size=0.2, random_state=42)  # 80% for training, 20% for testing

# Save the two dataframes into separate CSV files
train_df.to_csv(r"Scholarship ai\train_ielts_writing_dataset.csv", index=False)
test_df.to_csv(r"Scholarship ai\test_ielts_writing_dataset.csv", index=False)

print("Datasets split and saved:")
print("Training data saved to 'train_ielts_writing_dataset.csv'")
print("Testing data saved to 'test_ielts_writing_dataset.csv'")
