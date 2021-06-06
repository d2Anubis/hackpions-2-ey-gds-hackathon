import importlib
from utils import load_exceptions
from utils.fuzzy import get_fuzzy_score
import random
from sent2vec.vectorizer import Vectorizer
vectorizer = Vectorizer()

importlib.reload(load_exceptions)

# loading the Exception module and datasets
e = load_exceptions.Exceptions()
exception, sys_exc, bus_exc = e.get_data()

# changing all data into simple array
exception_val = e.exception.Exception.values.tolist()
sys_exc_val = e.system.Exception.values.tolist()
bus_exc_val = e.business.Exception.values.tolist()
_l = len(exception_val)


class Classify():
    ''' module to classify and update exceptions into database
    '''

    def __init__(self, e):
        self.e = e
        self.index = None

    def match_from_database(self):
        try:
            self.index = exception_val.index(self.e)
            return('Error exists at index', self.index)

        except:
            # check from existing tags of business and system errors
            for tag in sys_exc_val:
                if tag in self.e:
                    self.index = {'tag': 'Sytem Exception'}
                    print("Exception found from direct keyword match")
                    return self.index

            for tag in bus_exc_val:
                if tag in self.e:
                    self.index = {'tag': 'Business Exception'}
                    print("Exception found from direct keyword match")
                    return self.index

            self.index = []
            for i in range(_l):
                fuzz_score = get_fuzzy_score(
                    self.e,
                    e.exception.loc[i, "Exception"])

                if fuzz_score >= 0.85:
                    self.index.append([i, fuzz_score])
            return('Error exists at index', self.index)

    def update_to_database(self, tag="", kind=""):
        global exception_val
        global e
        if type(self.index) == list and len(self.index) > 0:
            # get the max match score for the exception
            _i, _f = sorted(self.index, key=lambda x: x[1], reverse=True)[0]

            # generating a random ID to store the exception in database
            id = int(random.random()*100000000)
            while id in e.exception.ID.values:
                id = int(random.random()*100000000)

            # saving the exception into the database
            e.exception = e.save_exceptions(
                {'ID': id, 'Exception': self.e, 'Category': e.exception.loc[_i, 'Category']})

            print("Created Exception with ID : ", id)

            # make the exception array index list global to allow other functions to access it across code
            exception_val = e.exception.Exception.values.tolist()

        elif type(self.index) == int:
            # show error ID for already existing Exception
            print("Similar error already exists with Exception ID : ",
                  e.exception.loc[self.index, "ID"], ". Duplication avoided.")

        elif type(self.index) == dict:

            exception_val = e.exception.Exception.values.tolist()

            try:
                _in = exception_val.index(self.e)
                print("Similar error already exists with Exception ID : ",
                      e.exception.loc[_in, "ID"], ". Duplication avoided.")
            except:
                # generate a random id for the exception to store in dataset
                id = int(random.random()*100000000)
                while id in e.exception.ID.values:
                    id = int(random.random()*100000000)

                # saving the exception into the database
                e.exception = e.save_exceptions(
                    {'ID': id, 'Exception': self.e, 'Category': self.index['tag']})

                print("Created Exception with ID : ", id)

                # make the exception array index list global to allow other functions to access it across code
                exception_val = e.exception.Exception.values.tolist()

        # condition for loading ML models and predict for cases where its not possible to use fuzzy logic
        elif type(self.index == list) and len(self.index) == 0:
            print("ML model loaded up")


class Update_tags:
    ''' 
    Code to update the tags for business and system tags
    '''

    def __init__(self, error, tag):
        self.error = error
        self.tag = tag

    def update(self):
        global sys_exc_val
        global bus_exc_val

        try:
            temp = None
            global e

            if self.tag == "Business Exception":
                temp = e.business.Exception.values.tolist()
            else:
                temp = e.system.Exception.values.tolist()

            _i = temp.index(self.error)
            print("Error already exists in Database. Duplication avoided.")

        except Exception as exc:
            if self.tag == 'System Exception':
                e.system = e.save_sys_exceptions({'Exception': self.error})
                sys_exc_val = e.system.Exception.values.tolist()
            else:
                e.business = e.save_bus_exceptions({'Exception': self.error})
                bus_exc_val = e.business.Exception.values.tolist()

            print("Exception added to database")
