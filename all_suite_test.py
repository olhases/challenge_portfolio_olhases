import unittest

from unittest.loader import makeSuite

from test_cases.framework import Test
from test_cases.login_to_the_system import TestLoginPage
from test_cases.test_add_player import TestAddPlayerPage
from test_cases.test_add_matches import TestAddMatchesPage
from test_cases.test_change_language import TestChangeLanguagePage
from test_cases.test_remind_password import TestRemindPasswordPage
from test_cases.test_sign_out import TestSignOutPage


def full_suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest((makeSuite(Test)))
    test_suite.addTest(makeSuite(TestLoginPage))
    test_suite.addTest(makeSuite(TestAddPlayerPage))
    test_suite.addTest(makeSuite(TestAddMatchesPage))
    test_suite.addTest(makeSuite(TestChangeLanguagePage))
    test_suite.addTest(makeSuite(TestRemindPasswordPage))
    test_suite.addTest(makeSuite(TestSignOutPage))

    return test_suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(full_suite())
