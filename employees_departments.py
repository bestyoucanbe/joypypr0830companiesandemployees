# Create an Employee type that contains information about employees of a company. Each employee must have a name, job title, and employment start date.


class Employee:

    def __init__(self, name, job_title, start_date):
        self.name = name
        self.job_title = job_title
        self.emp_start_date = start_date

# Create a Company type that employees can work for. A company should have a business name, address, and industry type.


class Company:

    def __init__(self):
        self.business_name = ""
        self.address = ""
        self.industry_type = ""
        self.employees = list()

# Create two companies, and 5 people who want to work for them.
# Assign 2 people to be employees of the first company.
# Assign 3 people to be employees of the second company.
# Output a report to the terminal the displays a business name, and its employees.
# For example:

# Acme Explosives is in the chemical industry and has the following employees
#    * Michael Chang
#    * Martina Navritilova

# Jetways is in the transportation industry and has the following employees
#    * Serena Williams
#    * Roger Federer
#    * Pete Sampras


Acme_Explosives = Company()
Acme_Explosives.business_name = "Acme Explosives"
Acme_Explosives.address = "101 Wile E. Coyote Drive"
Acme_Explosives.industry_type = "Explosives"

Virgin_Spaceways = Company()
Virgin_Spaceways.business_name = "Virgin Spaceways"
Virgin_Spaceways.address = "202 Moon Flyby Drive"
Virgin_Spaceways.industry_type = "Private Space Company"

Acme_Employee1 = Employee("Bugs Bunny", "Chief Funny Guy", "08/30/2019")
Acme_Employee2 = Employee("Porky Pig", "Wabbit Hunter", "08/30/1919")
Acme_Employee3 = Employee("Road Runner", "Bleep Bleep", "01/01/2000")

Virgin_Employee1 = Employee("Space Cowboy", "Chief wrangler", "09/01/2019")

Virgin_Employee2 = Employee("Deanna Troy", "Doctor", "09/02/2019")

Acme_Explosives.employees.append(Acme_Employee1)
Acme_Explosives.employees.append(Acme_Employee2)
Acme_Explosives.employees.append(Acme_Employee3)

Virgin_Spaceways.employees.append(Virgin_Employee1)
Virgin_Spaceways.employees.append(Virgin_Employee2)

print(
    f'Acme Explosives is in the {Acme_Explosives.industry_type} business and has the following employees:')
print("")
for eachemployee in Acme_Explosives.employees:
    print(eachemployee.name)

print("------------")
print(
    f'Virgin Spaceways is a {Virgin_Spaceways.industry_type} business and has the following employees:')
print("")
for eachemployee in Virgin_Spaceways.employees:
    print(eachemployee.name)
