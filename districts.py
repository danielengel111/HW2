class Districts:
    def __init__(self, dataset):
        self.dataset = dataset

    def filter_districts(self, letters):
        districts=self.dataset.get_all_districts()
        filtered_districts=[]
        for district in districts:
            for letter in letters:
                if district[0]==letter:
                    filtered_districts.append(district)
        self.dataset.set_districts_data(filtered_districts)

    def print_details(self, features, statistic_functions):
        for feature in features:
            print("{}: ".format(feature), end="")
            feat_list = self.dataset[feature]
            for x in range(len(statistic_functions) - 1):
                print("{}, ".format(statistic_functions[x](feat_list)), end="")
            print("{} ".format((float)(statistic_functions[len(statistic_functions) - 1](feat_list))))

    def determine_day_type(self):
        self.dataset.data['day_type'] = []
        for i in range(len(self.dataset.data["resigned_healed"])):
            if self.dataset.data["resigned_healed"][i] - self.dataset.data["new_positives"][i] > 0:
                self.dataset.data['day_type'].append(1)
            else:
                self.dataset.data['day_type'].append(0)

    def get_districts_class(self):
        pass

