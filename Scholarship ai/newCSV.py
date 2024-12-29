import pandas as pd

file = "ielts_writing_dataset.csv"
df = pd.read_csv(file)

columns_to_drop = ['Task_Type', 'Task_Response', 'Coherence_Cohesion', 'Lexical_Resource', 'Range_Accuracy','Examiner_Commen']
df = df.drop(columns=[col for col in columns_to_drop if col in df.columns])

df.to_csv("modified_ielts_writing_dataset.csv", index=False)

print("New CSV file created: 'modified_ielts_writing_dataset.csv'")
