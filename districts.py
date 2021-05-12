class Districts:
    def __init__(self, dataset):
        """
        initialize variables.
        :param dataset: Data object that contains the data
        """
        self.dataset = dataset

    def filter_districts(self, letters):
        """

        :param letters:
        :return:
        """
        districts = self.dataset.get_all_districts()
        filtered_districts = []
        for district in districts:
            for letter in letters:
                if district[0] == letter:
                    filtered_districts.append(district)
        self.dataset.set_districts_data(filtered_districts)

    def print_details(self, features, statistic_functions):
        """

        :param features:
        :param statistic_functions:
        :return:
        """
        for feature in features:
            print("{}: ".format(feature), end="")
            feat_list = self.dataset.data[feature]
            for x in range(len(statistic_functions) - 1):
                print("{}, ".format(statistic_functions[x](feat_list)), end="")
            print("{} ".format((statistic_functions[len(statistic_functions) - 1](feat_list))))

    def determine_day_type(self):
        """
        adds a new key:value to the self.dataset.data dictionary,
        which classifies each day as a "good day" or "not good day".
        """
        self.dataset.data['day_type'] = []
        for i in range(len(self.dataset.data['denominazione_region'])):
            if self.dataset.data['resigned_healed'][i] - self.dataset.data['new_positives'][i] > 0:
                self.dataset.data['day_type'].append(1)
            else:
                self.dataset.data['day_type'].append(0)

    def get_districts_class(self):
        """
        creates a dictionary where one key points to the list of all "green" districts
        and the second key points to the list of all "not green" districts.
        :return:the new dictionary.
        """
        distinct_districts = self.dataset.get_all_districts()
        self.determine_day_type()
        new_dict = {}
        new_dict['green'] = []
        new_dict['not_green'] = []

        for district in distinct_districts:
            green_days = 0
            for i in range(len(self.dataset.data['hospitalized_with_symptoms'])):
                if self.dataset.data['denominazione_region'][i] == district and self.dataset.data['day_type'][i] == 1:
                    green_days += 1
            if green_days > 340:
                new_dict['green'].append(district)
            else:
                new_dict['not_green'].append(district)
        return new_dict
