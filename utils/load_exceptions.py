import pandas as pd


class Exceptions:
    def __init__(self):
        self.exception = None
        self.system = None
        self.business = None

    def get_data(self):
        self.exception = pd.read_excel("./data/exceptions.xlsx")

        self.system = pd.read_excel("./data/system_exception.xlsx")
        self.business = pd.read_excel("./data/business_exception.xlsx")

        return self.exception, self.system, self.business

    def save_exceptions(self, e):
        self.exception = self.exception.append(e, ignore_index=True)
        self.exception.to_excel("./data/exceptions.xlsx", index=False)
        return self.exception

    def save_sys_exceptions(self, e):
        self.system = self.system.append(e, ignore_index=True)
        self.system.to_excel("./data/system_exception.xlsx", index=False)
        return self.system

    def save_bus_exceptions(self, e):
        self.business = self.business.append(e, ignore_index=True)
        self.business.to_excel("./data/business_exception.xlsx", index=False)
        return self.business
