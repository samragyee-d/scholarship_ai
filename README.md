# scholarship_ai
12/19/2024:

The idea:
Today I attended an alumni pannel at my highschool. I talked about how when I was a senior in highschool I applied to so many scholarships that I had left over money. 

Many students were asking me about the financial aid and scholarship application process. I told them that their essays will help them standout. Upon further reflection, I realized that the main issue I had with writing scholarship essays was making sure that I was thoroughly answering the prompt.

This sparked an idea. An AI project that would score a student's essay based on how well they answered the prompt. 

This README file will serve as a diary entry, inspired by the strucutre story of Mary Shelly's Frankenstein (iykyk).

The process:
I am not going to lie, I have no idea how to get started. Should I do backend first? Frontend first? I don't know. But I will learn as I grow. Today's goal is to do some data collection. I have already compiled all of my essays and my prompts into a single file. However, to ensure accuracy, I want to collect data from various sources. 

Tasks for today:
- Webscraping 

Fin

12/20/2024

I got the prompts and the essays to show up in pairs. But some of them are correlated wrong. Will try to fix that tommorow. 

12/21/2024-/12/24/2024
A bit busy/focusing on other things 

12/25/2024
Goals:
1. Fix the last essay
2. Export to CSV
Realizations:
- I need bad essays as well as good ones to create a good dataset. Also, how will the algorithm know how good each essay is?

Update:
- Found a CSV on kaggle that I can use to train the model to "grade" essays. 
- I can use the webscrapper data to generate recommendations for the user. So basically this means making a model to identify patterns in successful scholarship essays. 


12/28/2024
- Next step: tokenizing the sentences, computers better process numerical data.

Overall game plan:
- Tokenize and encode data
- use BERT to analyze text
- output a certain score

12/28/2024: Update #2
- Finally finished tokenizing the training and testing data. Some notes:
1. It is my first time working with Hugging Face so in the begining I opted for ineffecient approaches.
2. I had to switch from jupyter notebook back to VS Code. I initially used jupyter notebook because it was
the platform that I was used to utilizing. However, I soon realized that using VS Code was easier. 
3. I standarized the text by making everything lowercase. I now reconsidering that decision. 
4. I split the csv into training and testing data using sckit-learn
5. I was finally able to tokenize the questions and essays seperatly 
