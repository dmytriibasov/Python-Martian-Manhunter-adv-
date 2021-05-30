import unittest
from unittest.mock import patch
from employee import Employee


class MockTestTrue:
    text = 'response.ok = True'
    status_code = 200
    elapsed = 100
    ok = True

    def __init__(self, *args, **kwargs):
        pass


class MockTestFalse:
    text = 'response.ok = False'
    status_code = 400
    elapsed = 100
    ok = False

    def __init__(self, *args, **kwargs):
        pass


class TestEmployee(unittest.TestCase):

    def setUp(self):
        self.employee_1 = Employee('Tomas', 'Anderson', 120000)
        self.employee_2 = Employee('Morpheus', 'Nebuchadnezzar', 100000)
        self.employee_3 = Employee('Cypher', 'Reagan', 50000)

    def test_email(self):
        self.assertEqual(self.employee_1.email.lower(), 'tomas.anderson@email.com')
        self.assertEqual(self.employee_2.email.lower(), 'morpheus.nebuchadnezzar@email.com')
        self.assertEqual(self.employee_3.email.lower(), 'cypher.reagan@email.com')

    def test_fullname(self):
        self.assertEqual(self.employee_1.fullname.lower(), 'tomas anderson')
        self.assertEqual(self.employee_2.fullname.lower(), 'morpheus nebuchadnezzar')
        self.assertEqual(self.employee_3.fullname.lower(), 'cypher reagan')

    def test_apply_raise(self):
        self.employee_1.apply_raise()
        self.assertEqual(self.employee_1.pay, 126000.0)
        self.assertEqual(self.employee_1.pay, 126000)
        self.employee_2.apply_raise()
        self.assertEqual(self.employee_2.pay, 105000)
        self.employee_3.apply_raise()
        self.assertEqual(self.employee_3.pay, 52500)

    @patch('employee.requests.get')
    def test_monthly_schedule(self, mocker):
        mocker.side_effect = MockTestTrue
        self.assertEqual(self.employee_1.monthly_schedule('May'), 'response.ok = True')
        self.assertEqual(self.employee_2.monthly_schedule('June'), 'response.ok = True')
        self.assertEqual(self.employee_3.monthly_schedule('July'), 'response.ok = True')

        mocker.side_effect = MockTestFalse
        self.assertEqual(self.employee_1.monthly_schedule('January'), 'Bad Response!')
        self.assertEqual(self.employee_2.monthly_schedule('February'), 'Bad Response!')
        self.assertEqual(self.employee_3.monthly_schedule('March'), 'Bad Response!')


if __name__ == '__main__':

    unittest.main()
