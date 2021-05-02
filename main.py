import sys
import districts as districts
import data as data_set

def main(argv):
    covid_data = argv[1]
    data = data_set.Data(covid_data)
    district = districts.Districts(data)
    print(district.filter_districts(['B']))
    pass




if __name__ == '__main__':
    main(sys.argv)
