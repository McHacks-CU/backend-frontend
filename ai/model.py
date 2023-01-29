import cohere
from cohere.classify import Example
from dotenv import load_dotenv
import pandas as pd
import os

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
  return (classifications.classifications[0].prediction == 'safe')

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

# print(classify('''"Codec ORACLE_CODEC = new OracleCodec();
# String query = ""SELECT user_id FROM user_data WHERE user_name = '""
# + ESAPI.encoder().encodeForSQL( ORACLE_CODEC, req.getParameter(""userID""))
# + ""' and user_password = '""
# + ESAPI.encoder().encodeForSQL( ORACLE_CODEC, req.getParameter(""pwd"")) +""'"";"'''))

