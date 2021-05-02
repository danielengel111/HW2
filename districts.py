class Districts:
    def __init__(self, dataset):
        self.dataset = dataset

    def filter_districts(self, letters):
        districts=self.dataset.get_all_districts()
        filtered_districts=[]
        for district in districts:
            for letter in letters:
                if(district[0]==letter):
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
        x= {}
        for line in self.dataset:
            if(line["resigned_healed"]-line["new_positives"]>0):
                x.update({"day_type": 1})
            else:
                x.update({"day_type":0})
        self.dataset.data.update(x)

    def get_districts_class(self):
        pass

