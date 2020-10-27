import production_worker


def main():
    print("Enter following Details of the Employee:")
    print("---------------------------------------")
    name = input("Employee name: ")
    number = input("Employee number: ")
    shifts = input("Shift: ")
    pay = float(input("Pay rate: "))
    worker = production_worker.ProductionWorker(name, number, shifts, pay)
    print(worker)


main()
