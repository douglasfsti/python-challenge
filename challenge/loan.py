import abc
from .customer import Customer


class Loan(metaclass=abc.ABCMeta):
    def __init__(self, loan_type, interest_rate):
        self.loan_type = loan_type
        self.interest_rate = interest_rate

    @abc.abstractmethod
    def validate(self, customer: Customer) -> bool:
        pass


class PersonalLoan(Loan):
    def __init__(self):
        super().__init__("EMPRESTIMO_PESSOAL", 4.)

    def validate(self, customer: Customer) -> bool:
        return True


class CollateralizedLoan(Loan):
    def __init__(self):
        super().__init__("EMPRESTIMO_GARANTIA", 3.)

    def validate(self, customer: Customer) -> bool:
        if customer.income <= 3000 and customer.age < 30 and customer.location == "SP":
            return True

        if customer.income in range(3000, 5000) and customer.location == "SP":
            return True

        if customer.income >= 5000:
            return True

        return False


class PayrollLoan(Loan):
    def __init__(self):
        super().__init__("EMPRESTIMO_CONSIGNADO", 2.)

    def validate(self, customer: Customer) -> bool:
        return customer.income >= 5000


class LoanResponse(object):
    def __init__(self, customer: Customer):
        self.customer = customer.name
        self.loans = []

    def add(self, loan: Loan):
        if loan is not None:
            self.loans.append(loan)
