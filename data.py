import pandas


class Data:
    def __init__(self, path):
        """
        initialize variables, load data from
        csv file to dictionary.
        :param path: path to csv file.
        """
        self.path = path
        self.data = {}
        df = pandas.read_csv(path)
        self.data = df.to_dict(orient="list")

    def get_all_districts(self):
        """
        :return: list that contains all the distinct districts.
        """
        districts = self.data["denominazione_region"]
        distinct_districts = []
        for district in districts:
            if district not in distinct_districts:
                distinct_districts.append(district)
        return distinct_districts

    def set_districts_data(self, districts):
        """
        create a new dictionary that is a sub-dictionary of self.data.
        :param districts: list of districts that the new dictionary will contain.
        :return:the new dictionary.
        """
        new_data = {}
        for key in self.data:
            new_data[key] = []
        for i in range(0, len(self.data["denominazione_region"])):
            if self.data["denominazione_region"][i] in districts:
                for key in self.data:
                    new_data[key].append(self.data[key][i])
        self.data = new_data
