import pandas as pd
from datasets import load_dataset
from transformers import AutoTokenizer

# Use raw string for file paths to avoid issues with backslashes
file_train = "train_ielts_writing_dataset.csv"
file_test = "test_ielts_writing_dataset.csv"

tokenizer = AutoTokenizer.from_pretrained("bert-base-cased")

# Load dataset with correct file paths
dataset = load_dataset("csv", data_files={"train": file_train, "test": file_test})

# Tokenizing function
def tokenizing(examples):
    # Tokenize both 'Question' and 'Essays' columns separately
    tokenized_questions = tokenizer(examples["Question"], padding=True, truncation=True, return_tensors="pt")
    tokenized_essays = tokenizer(examples["Essay"], padding=True, truncation=True, return_tensors="pt")

    return {
        "input_ids_question": tokenized_questions["input_ids"],
        "input_ids_essay": tokenized_essays["input_ids"]
    }

# Apply tokenization
dataset = dataset.map(tokenizing, batched=True)

# Access tokenized data for the training set
tokenized_questions = dataset["train"]["input_ids_question"]
tokenized_essays = dataset["train"]["input_ids_essay"]

# Print first 5 tokenized questions and essays
print("Tokenized Questions:", tokenized_questions)
print("Tokenized Essays:", tokenized_essays)

