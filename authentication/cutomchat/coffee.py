import random
import urllib.request
import json
import re
import nltk
from nltk.tokenize import word_tokenize
from age8_10 import gs
# Define a list of coffee types and their descriptions
coffee_types = {
    "Espresso": "A strong and concentrated coffee that is made by forcing hot water through finely ground coffee beans.",
    "Cappuccino": "A coffee drink that is made with equal parts espresso, steamed milk, and foam.",
    "Latte": "A coffee drink that is made with espresso and steamed milk, typically topped with a small amount of foam.",
    "Americano": "A coffee drink that is made by diluting espresso with hot water.",
    "Macchiato": "A coffee drink that is made with a shot of espresso and a small amount of foamed milk.",
    "Mocha": "A coffee drink that is made with espresso, steamed milk, and chocolate syrup or powder.",
    "Flat White": "A coffee drink that is made with espresso and steamed milk, but with less foam than a latte."
}

# Define a function to search Google
# def search_google(query):
#     query = urllib.parse.quote_plus(query)
#     url = "https://google.com/search?q=" + query
#     headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"}
#     req = urllib.request.Request(url, headers=headers)
#     html = urllib.request.urlopen(req).read()
#     return re.findall('href="/url\?q=(.+?)"', html.decode('utf-8'))

# Define a function to generate a response based on user input
def generate_response(user_input):
    response = ""
    tokens = word_tokenize(user_input)
    for token in tokens:
        for key in coffee_types:
            if token.lower() == key.lower():
                response = coffee_types[key]
                break
        if response != "":
            break
    if response == "":
        google_results = gs(user_input)
        if len(google_results) > 0:
            response = "I'm not sure, but I found this link that might help: " + google_results[0]
        else:
            response = "I'm sorry, I don't have any information about that. Would you like me to search Google for you?"
    return response

# Define a function to handle user input and generate a response
def chat():
    print("Hello! I'm a coffee bot. What can I help you with today?")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "bye":
            print("Coffee bot: Goodbye!")
            break
        response = generate_response(user_input)
        print("Coffee bot: " + response)

# Download the necessary NLTK data
nltk.download('punkt')

# Start the chatbot
chat()
