from dataclasses import dataclass

@dataclass
class ScheduleItem:
    # 1. Define the fields and their data types
    subject: str
    catalog: str
    section: str
    component: str
    session: str
    units: int
    tot_enrl: int
    cap_enrl: int
    instructor: str
    
    # 2 Implement the get_key() method
    def get_key(self) -> str:
        return f"{self.subject}_{self.catalog}_{self.section}"

    # 3. Implement the print() method
    def print(self):
        print(f"{self.subject:<8} {self.catalog:<8} {self.section:<8} {self.component:<10} {self.session:<8} {self.units:<7} {self.tot_enrl:<8} {self.cap_enrl:<8} {self.instructor}")