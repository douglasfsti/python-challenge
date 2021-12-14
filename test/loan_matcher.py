from unittest import TestCase

from challenge.customer import Customer
from challenge.loan_matcher import LoanMatcher
from challenge.loan import PersonalLoan, CollateralizedLoan, PayrollLoan


class LoanMatcherTest(TestCase):
    def setUp(self) -> None:
        self.loan_matcher = LoanMatcher()
        self.loan_matcher.register(PersonalLoan())
        self.loan_matcher.register(CollateralizedLoan())
        self.loan_matcher.register(PayrollLoan())

    def test_returns_personal_loan_when_customer_income_is_under_3000(self):
        customer = Customer("Erikaya", "123.456.789-10", 29, "BH", 2500.)
        response = self.loan_matcher.loan_matcher(customer)

        assert len(response.loans) == 1
        assert response.loans[0].loan_type == 'EMPRESTIMO_PESSOAL'

    def test_returns_personal_loan_and_collateralized_loan_when_income_is_under_3000(self):
        customer = Customer("Erikaya", "123.456.789-10", 29, "SP", 2500.)
        response = self.loan_matcher.loan_matcher(customer)

        assert len(response.loans) == 2
        assert response.loans[0].loan_type == 'EMPRESTIMO_PESSOAL'
        assert response.loans[1].loan_type == 'EMPRESTIMO_GARANTIA'

    def test_returns_personal_loan_when_income_in_range_3000_5000(self):
        customer = Customer("Erikaya", "123.456.789-10", 29, "BH", 4500.)
        response = self.loan_matcher.loan_matcher(customer)

        assert len(response.loans) == 1
        assert response.loans[0].loan_type == 'EMPRESTIMO_PESSOAL'

    def test_returns_personal_loan_and_collateralized_loan_when_income_in_range_3000_5000(self):
        customer = Customer("Erikaya", "123.456.789-10", 29, "SP", 4500.)
        response = self.loan_matcher.loan_matcher(customer)

        assert len(response.loans) == 2
        assert response.loans[0].loan_type == 'EMPRESTIMO_PESSOAL'
        assert response.loans[1].loan_type == 'EMPRESTIMO_GARANTIA'

    def test_retunrs_personal_loan_collateralized_loan_payroll_loan_when_income_is_above_5000(self):
        customer = Customer("Erikaya", "123.456.789-10", 29, "BH", 6500.)
        response = self.loan_matcher.loan_matcher(customer)

        assert len(response.loans) == 3
        assert response.loans[0].loan_type == 'EMPRESTIMO_PESSOAL'
        assert response.loans[1].loan_type == 'EMPRESTIMO_GARANTIA'
        assert response.loans[2].loan_type == 'EMPRESTIMO_CONSIGNADO'
