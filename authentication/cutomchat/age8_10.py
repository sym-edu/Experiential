import nltk
import random
import sqlite3
import requests
from bs4 import BeautifulSoup
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

nltk.download('punkt')
nltk.download('wordnet')

# set up the tokenizer and lemmatizer
tokenizer = nltk.RegexpTokenizer(r'\w+')
lemmatizer = WordNetLemmatizer()

# define the input questions and answers
questions = ["What is a budget?", "How can I save money?", "What is a credit score?", "What is the difference between a checking and savings account?"]
answers = ["A budget is a plan for how you will spend your money.", "You can save money by cutting expenses and putting money in a savings account.", "A credit score is a number that reflects your creditworthiness and is used by lenders to determine whether to give you a loan or credit card.", "A checking account is used for everyday spending, while a savings account is used to save money and earn interest."]

# preprocess the text for vectorization
def preprocess(text):
    tokens = tokenizer.tokenize(text.lower())
    lemmas = [lemmatizer.lemmatize(token) for token in tokens]
    return " ".join(lemmas)

# create the vectorizer and calculate similarity scores
vectorizer = TfidfVectorizer()
preprocessed_questions = [preprocess(question) for question in questions]
vectorized_questions = vectorizer.fit_transform(preprocessed_questions)

# create a database to store user data
conn = sqlite3.connect('user_data.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS user_data (user_input text, best_match text, feedback text, response text)''')
conn.commit()

def gs(user_input):
    search_url = "https://www.google.com/search?q=" + user_input
    headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299"}
    response = requests.get(search_url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    try:
        snippet = soup.find_all('div', class_='BNeawe s3v9rd AP7Wnd')[0].get_text()
        return snippet
    except:
        # if no snippet is found, tell the user the chatbot doesn't know the answer
        print("I'm sorry, I don't know the answer to that. Can you try asking another question?")

# define the chatbot
def chatbot(user_input):
        # get user input
        # user_input = input("What would you like to know? ")

        # preprocess the user input
        preprocessed_input = preprocess(user_input)
        
        # calculate similarity scores
        vectorized_input = vectorizer.transform([preprocessed_input])
        
        similarity_scores = cosine_similarity(vectorized_input, vectorized_questions)

        # find the best matching question and answer
        best_match_index = similarity_scores.argmax()
        best_match_score = similarity_scores[0][best_match_index]
        if best_match_score > 0:
            # get user feedback and store it in the database

            try:
                query = 'select response from user_data where user_input == "{}" and feedback != "no"'.format(user_input)

                c.execute(query)
                response = c.fetchone()[0]
                print(response)
                return response
            except:
                print(answers[best_match_index])
                return answers[best_match_index]
                feedback = input("Did this answer your question? ")
                if feedback.lower()=='no':
                    response = gs(user_input)
                print(response)
                feedback = input("Did this answer your question? ")
                c.execute("INSERT INTO user_data VALUES (?, ?, ?,?)", (user_input, questions[best_match_index], feedback,response))
                conn.commit()
        else:
            # use Google Search API to fetch a snippet from the search results
            search_url = "https://www.google.com/search?q=" + user_input
            headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299"}
            response = requests.get(search_url, headers=headers)
            soup = BeautifulSoup(response.text, "html.parser")
            try:
                snippet = soup.find_all('div', class_='BNeawe s3v9rd AP7Wnd')[0].get_text()
                print(snippet)
                return snippet
            except:
                # if no snippet is found, tell the user the chatbot doesn't know the answer
                return "I'm sorry, I don't know the answer to that. Can you try asking another question?"
# chatbot()