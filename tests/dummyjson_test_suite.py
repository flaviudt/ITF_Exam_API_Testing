import unittest
import HtmlTestRunner

from tests.test_products import TestProductsRequests
from tests.test_carts import TestCartsRequests
from tests.test_users import TestUsersRequests
from tests.test_posts import TestPostsRequests
from tests.test_comments import TestCommentsRequests
from tests.test_todos import TestTodosRequests
from tests.test_quotes import TestQuotesRequests


class TestSuite(unittest.TestCase):

    def test_suite(self):

        suita_teste = unittest.TestSuite()

        suita_teste.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(TestProductsRequests),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestUsersRequests),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestCartsRequests),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestPostsRequests),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestCommentsRequests),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestTodosRequests),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestQuotesRequests)
        ])

        runner = HtmlTestRunner.HTMLTestRunner(
            combine_reports=True,
            report_title="API test report",
            report_name="Dummyjson API Test Results"
        )

        runner.run(suita_teste)

