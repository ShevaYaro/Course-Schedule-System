from schedule import Schedule

def print_search_results(my_schedule, results):
    """A helper function to neatly print the list of courses returned from a search."""
    if not results:
        print("\nNo courses found matching your criteria.")
    else:
        print(f"\n--- Found {len(results)} result(s) ---")
        my_schedule.print_header()
        for course in results:
            course.print()

def main():
    print("Loading course data into trees...")
    
    
    bst_schedule = Schedule(tree_type="BST")
    bst_schedule.load_data('courses_2023.csv') 
    
    # 2. Create and load the Self-Balancing AVL Tree
    avl_schedule = Schedule(tree_type="AVL")
    avl_schedule.load_data('courses_2023.csv')

    print("Data loaded successfully into both BST and AVL backends!")

    while True:
        print("\n" + "="*35)
        print("   COURSE SCHEDULE SYSTEM (TREES)")
        print("="*35)
        print("1. Display all courses")
        print("2. Search by subject")
        print("3. Search by subject and catalog")
        print("4. Search by instructor last name")
        print("5. Compare Tree Heights (BST vs AVL)") # TASK 5
        print("6. Quit")
        
        choice = input("\nEnter your choice (1-6): ")

        if choice == '1':
            print("\n--- Full Schedule ---")
            avl_schedule.print()
            
        elif choice == '2':
            subject = input("Enter subject (e.g., BIO): ").upper()
            results = avl_schedule.find_by_subject(subject)
            print_search_results(avl_schedule, results)

        elif choice == '3':
            subject = input("Enter subject (e.g., BIO): ").upper()
            catalog = input("Enter catalog (e.g., 141): ")
            results = avl_schedule.find_by_subject_catalog(subject, catalog)
            print_search_results(avl_schedule, results)

        elif choice == '4':
            last_name = input("Enter instructor's last name: ").title()
            results = avl_schedule.find_by_instructor_last_name(last_name)
            print_search_results(avl_schedule, results)

        elif choice == '5':
            # TASK 6: Compare heights
            print("\n--- Tree Height Comparison ---")
            print(f"Unbalanced BST Height:  {bst_schedule.get_tree_height()}")
            print(f"Self-Balancing AVL Height: {avl_schedule.get_tree_height()}")
            print("\n(Note: The AVL tree should be significantly shorter because it balances itself!)")

        elif choice == '6':
            print("\nExiting the Course Schedule System. Goodbye!")
            break
            
        else:
            print("\nInvalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()