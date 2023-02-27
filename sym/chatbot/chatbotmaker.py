import nltk
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

def preprocess(text):
    tokens = tokenizer.tokenize(text.lower())
    lemmas = [lemmatizer.lemmatize(token) for token in tokens]
    return " ".join(lemmas)

def preprocess(text):
    tokens = tokenizer.tokenize(text.lower())
    lemmas = [lemmatizer.lemmatize(token) for token in tokens]
    return " ".join(lemmas)

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



# db_name = input("enter the database this chatbot is being stored in")
db_name = 'finance'
conn = sqlite3.connect('{}.db'.format(db_name))
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS user_data (prompt text, response text)''')
conn.commit()

# db = {}

# while True:
#     q = input('Enter the question')
#     a = input('what is the preffered answer?')
#     co = int(input('enter 1 to add another question or move to testing'))
#     if co != 1:
#         break
db = {"What is a budget?": "A budget is a financial plan that outlines your income and expenses over a certain period of time, usually a month or a year.",
    "Why is it important to have a budget?": "A budget helps you manage your money and make sure you're not spending more than you're earning. It can also help you save money and achieve your financial goals.",
    'How can you create a budget?': 'To create a budget, you need to track your income and expenses, prioritize your spending, and set financial goals. There are many online tools and apps that can help you create a budget.',
    'What is an emergency fund?': 'An emergency fund is a savings account that you set up to cover unexpected expenses, such as medical bills or car repairs.',
    'How much money should you have in your emergency fund?': 'Financial experts recommend having at least three to six months of living expenses in your emergency fund.',
    'What is a credit score?': "A credit score is a three-digit number that measures your creditworthiness. It's based on your credit history, including your payment history, amount of debt, and length of credit history.",
    'Why is a good credit score important?': 'A good credit score can help you qualify for loans and credit cards with lower interest rates and better terms. It can also make it easier to rent an apartment or get a job.',
    'How can you improve your credit score?': 'To improve your credit score, you need to make sure you pay your bills on time, keep your credit card balances low, and avoid applying for too much credit at once.',
    'What is compound interest?': "Compound interest is interest that's calculated on both the initial principal and any accumulated interest. It can help your savings grow faster over time.",
    'What is a 401(k)?': 'A 401(k) is a retirement savings plan offered by many employers. It allows you to save money for retirement on a pre-tax basis, which can lower your taxable income.',
    'How much should you contribute to your 401(k)?': "Financial experts recommend contributing at least enough to get your employer's matching contribution, if they offer one. After that, you should try to contribute as much as you can afford, up to the annual contribution limit.",
    'What is a Roth IRA?': 'A Roth IRA is a retirement savings account that allows you to contribute after-tax dollars and withdraw tax-free in retirement. It can be a good option if you expect to be in a higher tax bracket in retirement.',
    'What is a traditional IRA?': 'A traditional IRA is a retirement savings account that allows you to contribute pre-tax dollars and pay taxes on withdrawals in retirement. It can be a good option if you expect to be in a lower tax bracket in retirement.',
    'What is a mutual fund?': 'A mutual fund is a type of investment that pools money from many investors to purchase a diversified portfolio of stocks, bonds, or other assets.',
    'What is a stock?': 'A stock is a share in the ownership of a company. When you buy a stock, you become a shareholder and can potentially earn a return on your investment through dividends and capital gains.',
    'What is a bond?': 'A bond is a type of investment that represents a loan made by an investor to a borrower, typically a company or government. The borrower pays interest on the bond and repays the principal when the bond matures.',
    'What is diversification?': 'Diversification is the practice of spreading your investments across different types of assets and industries to reduce your overall investment risk. By diversifying your portfolio, you can potentially earn higher returns while reducing the impact of any one investment performing poorly.',
    'What is a stock market index?': 'A stock market index is a measure of the performance of a group of stocks that represent a particular sector or market. Examples include the S&P 500 and the Dow Jones Industrial Average.',
    'What is a stock market?': 'A stock market is a platform where stocks and other securities are bought and sold by investors. Examples include the New York Stock Exchange and the Nasdaq.',
    'What is a dividend?': "A dividend is a payment made by a company to its shareholders, typically in the form of cash or additional shares of stock. Dividends are often paid out of a company's profits.",
'What is inflation?': 'Inflation is the rate at which the general level of prices for goods and services is rising. When inflation is high, the purchasing power of your money decreases over time.',
'What is a CD?': "A CD, or certificate of deposit, is a type of savings account that typically offers a higher interest rate than a regular savings account. CDs have a fixed term, such as six months or a year, and you typically can't withdraw your money early without incurring a penalty.",
'What is a money market account?': 'A money market account is a type of savings account that typically offers a higher interest rate than a regular savings account. It may also have a higher minimum balance requirement and may limit the number of withdrawals you can make per month.',
'What is a credit card?': "A credit card is a payment card that allows you to borrow money from a bank or credit card company to make purchases. You'll typically need to pay back the borrowed amount plus interest.",
'What is a debit card?': "A debit card is a payment card that allows you to access funds in your bank account to make purchases. Unlike a credit card, you're not borrowing money when you use a debit card.",
'What is a credit limit?': 'A credit limit is the maximum amount of money you can borrow on a credit card or line of credit. Your credit limit is typically based on factors such as your credit score and income.',
'What is a minimum payment?': 'A minimum payment is the smallest amount you can pay on a credit card bill to avoid late fees and other penalties. However, making only the minimum payment will typically result in high interest charges and a longer time to pay off your balance.',
'What is a credit report?': 'A credit report is a summary of your credit history, including your payment history, amount of debt, and credit inquiries. Credit reports are used by lenders and other financial institutions to evaluate your creditworthiness.',
'What is a credit bureau?': "A credit bureau is a company that collects and maintains information about consumers' credit history. Examples include Equifax, Experian, and TransUnion.",
'What is a FICO score?': "A FICO score is a credit score developed by the Fair Isaac Corporation. It's widely used by lenders and other financial institutions to evaluate your creditworthiness.",
'What is a mortgage?': 'A mortgage is a loan used to purchase a home or other property. The borrower pays back the loan plus interest over a set period of time, typically 15 or 30 years.',
'What is a down payment?': 'A down payment is the amount of money you pay upfront when purchasing a home or other property. The size of your down payment can affect the interest rate and other terms of your mortgage.'}


# questions,answers = list(db.keys()),list(db.values())

for questions, answers in db.items():
    c.execute("INSERT INTO user_data VALUES (?, ?)", (questions, answers))
    conn.commit()

c.execute("SELECT prompt FROM user_data")
questions = [row[0] for row in c.fetchall()]
conn.commit()

vectorizer = TfidfVectorizer()
preprocessed_questions = [preprocess(question) for question in questions]
vectorized_questions = vectorizer.fit_transform(preprocessed_questions)
# vectorized_questions = vectorized_questions[::-1]

def chatbot(su = False):
    user_input = input('enter user input')
    try:
        query = 'select response from user_data where user_input == "{}" and feedback != "no"'.format(user_input)
        c.execute(query)
        response = c.fetchone()[0]
        print(response)
    except:
        preprocessed_input = preprocess(user_input)
        vectorized_input = vectorizer.transform([preprocessed_input])
        similarity_scores = cosine_similarity(vectorized_input, vectorized_questions)
        best_match_index = similarity_scores.argmax()
        best_match_score = similarity_scores[0][best_match_index]

        if best_match_score > 0:
                question = questions[best_match_index]
                c.execute("select response from user_data where prompt == '{}'".format(question))
                response = c.fetchone()[0]
                if su:
                    print(question)
                    feedback = int(input('is this query the same as yours? (1/0)'))
                    if feedback != 1:
                        question = user_input
                        response = gs(question)
                    print(response)
                    f = int(input('does this answer your question? (1/0)'))
                    if f!=1:
                        response = input('enter an alternative')
                    c.execute("INSERT INTO user_data VALUES (?, ?)", (user_input, response))
                    conn.commit()
                    print('updated')
                else:
                    print(response)
                    feedback = int(input("Did this answer your question?(1/0)"))
                    if feedback!=1:
                        response = gs(user_input)
                        question = user_input
                        print('here is an alternate response: ')
                        print(response)
                    c.execute("INSERT INTO user_data VALUES (?, ?)", (user_input, response))
                    conn.commit()
        else:
            response = gs(user_input)
            question = user_input
            c.execute("INSERT INTO user_data VALUES (?, ?)", (user_input, response))
            conn.commit()
    conn.close()
if __name__ == "__main__":
    chatbot(su=True)