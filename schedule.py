import csv 
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

    def find_by_subject(self, subject: str) -> list:
        """Returns a list of courses that match the given subject."""
        # List comprehension filtering by subject
        return [course for course in self.courses.values() if course.subject == subject]

    def find_by_subject_catalog(self, subject: str, catalog: str) -> list:
        """Returns a list of courses that match both subject and catalog."""
        # List comprehension checking two conditions
        return [course for course in self.courses.values() if course.subject == subject and course.catalog == catalog]

    def find_by_instructor_last_name(self, last_name: str) -> list:
        """Returns a list of courses taught by an instructor with the given last name."""
        return [course for course in self.courses.values() if course.instructor.startswith(last_name)]
    
    def load_data(self, filename: str):
        """Reads the CSV file and populates the dictionary with ScheduleItem objects."""
        with open(filename, encoding='utf-8-sig', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            
            for row in reader:
                item = ScheduleItem(
                    subject=row['Subject'],
                    catalog=row['Catalog'],
                    section=row['Section'],
                    component=row['Component'],
                    session=row['Session'],
                    units=int(row['Units']),
                    tot_enrl=int(row['TotEnrl']),
                    cap_enrl=int(row['CapEnrl']),   
                    instructor=row['Instructor']
                )
                
                self.add_entry(item)