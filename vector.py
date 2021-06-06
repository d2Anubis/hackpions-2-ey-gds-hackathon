import pickle
from sent2vec.vectorizer import Vectorizer
import pandas as pd
import warnings
warnings.filterwarnings('ignore')
vectorizer = Vectorizer()
df = pd.read_excel("./data/exceptions.xlsx")


def create_vector(sent):
    vectorizer.bert(sent)
    return vectorizer.vectors


def save_vector():
    global df
    df = df.to_dict('list')
    vec = df['Exception']
    df['Exception'] = create_vector(vec)

    # saving as pickle file
    with open('./data/vectors.pickle', 'wb') as handle:
        pickle.dump(df, handle,
                    protocol=pickle.HIGHEST_PROTOCOL)
