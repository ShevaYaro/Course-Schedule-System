from schedule import Schedule

def print_search_results(my_schedule, results):
    if not results:
        print("\nNo courses found matching your criteria.")
    else:
        print(f"\n--- Found {len(results)} result(s) ---")
        my_schedule.print_header()
        for course in results:
            course.print()

def main():
    # 1. Instantiate the Schedule class
    my_schedule = Schedule()
    
    # 2. Load the data from the CSV file
    print("Loading course data...")
    my_schedule.load_data('courses.csv')
    print("Data loaded successfully!")

    # 3. Create the interactive user menu
    while True:
        print("\n" + "="*30)
        print("   COURSE SCHEDULE SYSTEM")
        print("="*30)
        print("1. Display all courses")
        print("2. Search by subject")
        print("3. Search by subject and catalog")
        print("4. Search by instructor last name")
        print("5. Quit")
        
        choice = input("\Enter your choice (1-5): ")

        # 4. Handle the user's choice
        if choice == '1':
            print("\n--- Full Schedule ---")
            my_schedule.print()
            
        elif choice == '2':
            subject = input("Enter subject (e.g., BIO): ").upper()
            results = my_schedule.find_by_subject(subject)
            print_search_results(my_schedule, results)

        elif choice == '3':
            subject = input("Enter subject (e.g., BIO): ").upper()
            catalog = input("Enter catalog (e.g., 141): ")
            results = my_schedule.find_by_subject_catalog(subject, catalog)
            print_search_results(my_schedule, results)

        elif choice == '4':
            last_name = input("Enter instructor's last name: ").title()
            results = my_schedule.find_by_instructor_last_name(last_name)
            print_search_results(my_schedule, results)

        elif choice == '5':
            print("\nExiting the Course Schedule System. Goodbye!")
            
        else:
            print("\nInvalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()