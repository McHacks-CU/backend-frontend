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

def classify(code, nltk):
  if not init:
      initialize()
      
  classifications = co.classify(
      model='large',
      inputs=[code, nltk],
      examples=examples
    )
  if (classifications.classifications[0].prediction != classifications.classifications[1].prediction):
    return "Tests are inconclusive, please enter mode code, or change your code to be more precise"
  elif (classifications.classifications[0].prediction == 'safe'):
    return "Your code is safe"
  response = respond(code)
  if (response == ""):
    return "You should use prepared statements in order to escape your queries as well as validating your input"
  return "Your code is unsafe, here are some ways you can try to fix your code: \n" + response
  

def initialize():

  load_dotenv()

  global co
  co = cohere.Client(os.getenv("API_KEY"))

  df = pd.read_csv('/Users/aekus/Documents/code/McHacks/ai/dataset.csv', names=['query','intent'])

  X, y = df["query"], df["intent"]
  intents = y.unique().tolist()

  ex_texts, ex_labels = [], []
  for intent in intents:
      y_temp = y[y == intent]
      sample_indexes = y_temp.sample(n=127, random_state=42).index
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
# ''', 'String query = "SELECT account_balance FROM user_data WHERE user_name = ? ";'))