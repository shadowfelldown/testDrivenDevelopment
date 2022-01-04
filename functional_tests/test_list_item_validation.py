from selenium.webdriver.common.keys import Keys
from unittest import skip
from .base import FunctionalTest

class ItemValidationTest(FunctionalTest):
    def test_cannot_add_empty_list_items(self):
        # Edith goes to the home page and accidentally tries to submint
        # an empty list item. she hits enter on the empty input box

        # The home page refreshes, and there is an error message saying that
        # entries cannot be blank

        # she tries again with some text for the entry, which now works

        # she decides to submit a second empty list item

        # she receives a similar warning on the list page

        # she corrects it by filling some text in
        self.fail('Write Me!')
