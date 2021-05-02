import sys
import data
import statistics
import districts

def main(argv):
    dataset = data.Data(argv[0])
    D = districts.Districts(dataset)
    D.filter_districts({'L', 'S'})

    print("Question 1:")
    arr = D.dataset['hospitalized_with_symptoms']
    mean = statistics.mean(arr)
    median = statistics.median(arr)
    print(f"hospitalized_with_symptoms: {mean}, {median}")

    arr = D.dataset['intensive_care']
    mean = statistics.mean(arr)
    median = statistics.median(arr)
    print(f"intensive_care: {mean}, {median}")

    arr = D.dataset['total_hospitalized']
    mean = statistics.mean(arr)
    median = statistics.median(arr)
    print(f"total_hospitalized: {mean}, {median}")

    arr = D.dataset['home_insulation']
    mean = statistics.mean(arr)
    median = statistics.median(arr)
    print(f"home_insulation: {mean}, {median}")



    dataset = data.Data(argv[0])
    distinct_districts = dataset.Data.get_all_districts()
    print("Question 2:")
    print(f"Number of districts: {len(distinct_districts)}")
    print(f"Number of not green districts: {}")
    print(f"Will a lockdown be forced on whole of Italy?: {}")




if __name__ == '__main__':
    main(sys.argv)
