import cohere
from cohere.classify import Example
from dotenv import dotenv_values
import pandas as pd

def classify_text(text,examples):
  classifications = co.classify(
    model='large',
    inputs=[text],
    examples=examples
    )
  return classifications.classifications[0].prediction

config = dotenv_values(".env")  

co = cohere.Client(config.get("API_KEY"))

df = pd.read_csv('dataset.csv',names=['query','intent'])

X, y = df["query"], df["intent"]
intents = y.unique().tolist()

ex_texts, ex_labels = [], []
for intent in intents:
  y_temp = y[y == intent]
  sample_indexes = y_temp.sample(n=int(len(X)/2), random_state=42).index
  ex_texts += X[sample_indexes].tolist()
  ex_labels += y[sample_indexes].tolist()

examples = list()
for txt, lbl in zip(ex_texts,ex_labels):
  examples.append(Example(txt,lbl))

print(classify_text('''import mysql.connector

user_input = input("Enter a user ID: ")

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="mydatabase"
)

cursor = db.cursor()

query = "SELECT * FROM users WHERE id = %s"
cursor.execute(query, (user_input,))

result = cursor.fetchall()

print(result)
''', examples))