import sys
import data
import statistics
import districts


def main(argv):
    dataset = data.Data(argv[1])
    district = districts.Districts(dataset)
    district.filter_districts({'L', 'S'})

    print("Question 1:")
    statistic_methods = [statistics.mean, statistics.median]
    for key in ["hospitalized_with_symptoms", "intensive_care", "total_hospitalized", "home_insulation"]:
        district.print_details([key], statistic_methods)

    dataset = data.Data(argv[1])
    distinct_districts = dataset.get_all_districts()
    print("\nQuestion 2:")
    print(f"Number of districts: {len(distinct_districts)}")

    district = districts.Districts(dataset)
    dict = district.get_districts_class()

    print(f"Number of not green districts: {len(dict['not_green'])}")
    if len(dict['not_green']) > 10:
        answer = "Yes"
    else:
        answer = "No"
    print(f"Will a lockdown be forced on whole of Italy?: {answer}")


if __name__ == '__main__':
    main(sys.argv)
