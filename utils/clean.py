# importing regex for data cleaning
import re


def cleaning_data(text):
    # converting text to lower case
    text = text.lower()

    # removing text between brackets
    text = re.sub("([\(\[]).*?([\)\]])", "\g<1>\g<2>", text)

    # removing all characters except letters
    text = re.sub(r'[^a-zA-Z ]+', '', text)

    # removing extra white spaces
    text = re.sub("\s+", " ", text)

    return text
