from schedule_item import ScheduleItem

class Schedule:
    def __init__(self):
        self.courses = {}

    def add_entry(self, item: ScheduleItem):
        """Adds a ScheduleItem to the dictionary using its unique key."""
        key = item.get_key()
        self.courses[key] = item

    def print_header(self):
        """Prints the column headers for the schedule report."""
        print(f"{'Subject':<8} {'Catalog':<8} {'Section':<8} {'Component':<10} {'Session':<8} {'Units':<7} {'TotEnrl':<8} {'CapEnrl':<8} {'Instructor'}")

    def print(self):
        """Prints the full schedule."""
        self.print_header()
        
        # 5. Loop through all the values (the ScheduleItem objects) in our dictionary
        for course in self.courses.values():
            # Call the print() method we defined inside the ScheduleItem class
            course.print()