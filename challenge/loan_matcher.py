from .customer import Customer
from .loan import Loan, LoanResponse


class LoanMatcher(object):
    def __init__(self):
        self.loans = []

    def register(self, loan: Loan):
        self.loans.append(loan)

    def loan_matcher(self, customer: Customer) -> LoanResponse:
        response = LoanResponse(customer)
        for loan in self.loans:
            if loan.validate(customer):
                response.add(loan)

        return response
