# EY GDS Hackpions 2.0 - Hackathon

**NLP-based tagging solution**

**Overview**

The Intelligent Automation team manually processes a large volume of exception data. The manual process includes examining the exception reasons and categorizing them broadly into business or technical issues, which is time consuming and increases turnaround time. 

We have build an intelligent solution, to auto label exceptions as they occur.

**Proposed Solution**

An AI operations model which will autolabel the exceptions and provide the solution without any user intervention. Following are the features of the proposed solution:
- Categorizing exceptions
- Finding similar occurring exceptions
- Updating database with incoming exceptions with unique Exception ID
- Exception Validation to avoid duplication in database

Categorizing the exceptions via two ways:
- Direct Lookup Table
- Using Fuzzy Logic
- Classification using Word vectors (BERT) for exceptions that are tough to classify


**Submission**

A UI based exception tagger with a API backend that can be utilised separately

**How to run the app**
- download the complete repo
- open anaconda command prompt and run ```streamlit run app.py```

**Python package Requirements**
- python >= 3
- pandas
- bert
- streamlit
- fuzzywuzzy
