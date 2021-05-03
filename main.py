import sys
import data
import statistics
import districts

def main(argv):
    dataset = data.Data(argv[1])
    D = districts.Districts(dataset)
    D.filter_districts({'L', 'S'})

    print("Question 1:")
    for key in D.dataset.data:
        if key == 'data' or key == 'region_code' or key == 'denominazione_region' or key == 'new_positives' or key == 'resigned_healed':
            continue
        arr = D.dataset.data[key]
        mean = statistics.mean(arr)
        median = statistics.median(arr)
        print(f"{key}: {mean}, {median}")
    print()

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
