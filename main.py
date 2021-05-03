import sys
import data
import statistics
import districts
import pandas
def main(argv):
    dataset = data.Data(argv[1])
    D = districts.Districts(dataset)
    D.filter_districts({'L', 'S'})

    print("Question 1:")
    arr = D.dataset.data['hospitalized_with_symptoms']
    mean = statistics.mean(arr)
    median = statistics.median(arr)
    print(f"hospitalized_with_symptoms: {mean}, {median}")

    arr = D.dataset.data['intensive_care']
    mean = statistics.mean(arr)
    median = statistics.median(arr)
    print(f"intensive_care: {mean}, {median}")

    arr = D.dataset.data['total_hospitalized']
    mean = statistics.mean(arr)
    median = statistics.median(arr)
    print(f"total_hospitalized: {mean}, {median}")

    arr = D.dataset.data['home_insulation']
    mean = statistics.mean(arr)
    median = statistics.median(arr)
    print(f"home_insulation: {mean}, {median}\n")



    dataset = data.Data(argv[1])
    distinct_districts = dataset.get_all_districts()
    print("Question 2:")
    print(f"Number of districts: {len(distinct_districts)}")

    D.determine_day_type()
    not_green_districts = 0
    for district in distinct_districts:
        green_days = 0
        for i in range(len(dataset.data['hospitalized_with_symptoms'])):
            if dataset.data['denominazione_region'] == district and dataset.data['day_type'][i] == 1:
                green_days += 1
        if green_days <= 340:
            not_green_districts += 1

    print(f"Number of not green districts: {not_green_districts}")
    if not_green_districts > 10:
        answer = "Yes"
    else:
        answer = "No"
    print(f"Will a lockdown be forced on whole of Italy?: {answer}")




if __name__ == '__main__':
    main(sys.argv)
