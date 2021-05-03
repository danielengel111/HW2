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
    print(f"hospitalized_with_symptoms: {D.print_details({'hospitalized_with_symptoms'},[statistics.mean,statistics.median])}")
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

    D = districts.Districts(dataset)
    dict = D.get_districts_class()

    print(f"Number of not green districts: {len(dict['not_green'])}")
    if len(dict['not_green']) > 10:
        answer = "Yes"
    else:
        answer = "No"
    print(f"Will a lockdown be forced on whole of Italy?: {answer}")




if __name__ == '__main__':
    main(sys.argv)
