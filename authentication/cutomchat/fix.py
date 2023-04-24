import sqlite3

# initialize database connection
conn = sqlite3.connect('chatbot.db')
c = conn.cursor()

# create table to store responses
c.execute('''CREATE TABLE IF NOT EXISTS responses
             (id INTEGER PRIMARY KEY, input TEXT, output TEXT)''')

# insert some sample responses
c.execute("INSERT INTO responses (input, output) VALUES (?, ?)", ("What is a budget?", "A budget is a plan for how you will spend your money."))
c.execute("INSERT INTO responses (input, output) VALUES (?, ?)", ("How do I save money?", "You can save money by cutting back on expenses, such as eating out or buying unnecessary items."))

# commit changes to database
conn.commit()

# close database connection
conn.close()
