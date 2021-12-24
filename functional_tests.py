from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith has heard about a cool new online to-do app. she goes to check its homepage
        self.browser.get('http://localhost:8000')

        # she notices the page title and header mention to-do lists.
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')

        # she is invited to enter a to-do item straight away

        # she types "buy peacock feathers into a text box

        # when she hits enter, the page updates and now the page lists
        # 1: buy peacock feathers as an item on the to-do list

        # there is still a text box for Edith to add another item
        # she enters "use peacock feathers to make a fly"

        # the page updates again and now shows both items on her list.

        # Edith wonders whether the site will remember her list. then she sees
        # that the site has generated a unique URL for her -- there is some explanatory text to that effect.

        # she visits that URL - her to-do list is still there

        # satisfied, she goes back to sleep.


if __name__ == '__main__':
    unittest.main(warnings='ignore')
