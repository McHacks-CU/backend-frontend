import cohere
from cohere.classify import Example
from dotenv import load_dotenv
import pandas as pd
import os
from response import respond

global init
init = False

# def classify_text(text,examples):
#   classifications = co.classify(
#     model='large',
#     inputs=[text],
#     examples=examples
#     )
#   return classifications.classifications[0].prediction

def classify(text):
  if not init:
      initialize()
      
  classifications = co.classify(
      model='large',
      inputs=[text],
      examples=examples
    )
  if (classifications.classifications[0].prediction == 'safe'):
    return "Your code is safe"
  return respond(text)
  

def initialize():

  load_dotenv()

  global co
  co = cohere.Client(os.getenv("API_KEY"))

  df = pd.read_csv('/Users/aekus/Documents/code/McHack/ai/dataset.csv', names=['query','intent'])

  X, y = df["query"], df["intent"]
  intents = y.unique().tolist()

  num_tests = 15
  ex_texts, ex_labels = [], []
  for intent in intents:
      y_temp = y[y == intent]
      sample_indexes = y_temp.sample(n=num_tests, random_state=42).index
      ex_texts += X[sample_indexes].tolist()
      ex_labels += y[sample_indexes].tolist()

  global examples
  examples = list()
  for txt, lbl in zip(ex_texts,ex_labels):
      examples.append(Example(txt,lbl))

# print(classify('''String userInput = request.getParameter("user_id");
# String query = "SELECT * FROM users WHERE id = " + userInput;
# Statement stmt = conn.createStatement();
# ResultSet rs = stmt.executeQuery(query);
# '''))