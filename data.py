import pandas


class Data:
    def __init__(self, path):
        self.path = path
        self.data = {}
        df = pandas.read_csv(path)
        self.data = df.to_dict(orient="list")

    def get_all_districts(self):
        """

        :return:
        """
        districts = self.data["denominazione_region"]
        distinct_districts = []
        for district in districts:
            if district not in distinct_districts:
                distinct_districts.append(district)
        return distinct_districts

    def set_districts_data(self, districts):
        """

        :param districts:
        :return:
        """
        new_data = {}
        for key in self.data:
            new_data[key] = []
        for i in range(0, len(self.data["denominazione_region"])):
            if self.data["denominazione_region"][i] in districts:
                for key in self.data:
                    new_data[key].append(self.data[key][i])
        self.data = new_data
