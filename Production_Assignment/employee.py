import production_worker


def main():
    print("Enter following Details of the Employee:")
    print("---------------------------------------")
    name = input("Employee's name: ")
    number = input("Employee's number: ")
    shift = input("Employee's shift: ")
    pay = input("Employee's pay rate: ")
    worker = production_worker.ProductionWorker(name, number, shift, pay)
    print("---------------------------------------")
    print("\nEmployee name: " + worker.get_employee_name() + "\nEmployee's number: " + worker.get_employee_number()
          + "\nEmployee's shift: " + worker.get_shift() + "\nEmployee's pay rate: " + worker.get_pay_rate())


main()
