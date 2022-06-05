import application.salary
import application.db.people


def main():
	application.salary.calculate_salary()
	application.db.people.get_employees()

if __name__ == '__main__':
	main()