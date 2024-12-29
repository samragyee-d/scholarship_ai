import pandas as pd
from transformers import AutoTokenizer

file = r"Scholarship ai\ielts_writing_dataset.csv"

df = pd.read_csv(file) 
df = df.drop(['Examiner_Commen', 'Task_Response', 'Coherence_Cohesion', 'Range_Accuracy', 'Lexical_Resource'], axis=1)

#Standardizing the text 
for col in df.columns:
    if df[col].dtype == 'object': 
        df[col] = df[col].str.lower()

#df.to_csv("your_file_lowercase.csv", index=False)


tokenizer = AutoTokenizer.from_pretrained("bert-base-cased")

sequence = df.loc[:, "Question"]
tokens = tokenizer.tokenize(sequence)

print(tokens)