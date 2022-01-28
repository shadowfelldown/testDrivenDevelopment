from django.conf import settings
from .server_tools import create_session_on_server
from .management.commands.create_session import create_pre_authenticated_session

from .base import FunctionalTest


class MyListsTest(FunctionalTest):

    def create_pre_authenticated_session(self, email):
        if self.staging_server:
            session_key = create_session_on_server(self.staging_server, email)
        else:
            session_key = create_pre_authenticated_session(email)

        self.browser.get(self.live_server_url + "/404_no_such_url/")
        self.browser.add_cookie(dict(
            name = settings.SESSION_COOKIE_NAME,
            value = session_key,
            path = '/',
        ))
    
    def test_logged_in_users_lists_are_saved_as_my_lists(self):
        email = 'edith@example.com'
        
        # Edith is a logged in user
        self.create_pre_authenticated_session(email)
        # she goes to the the home page and starts a list
        self.browser.get(self.live_server_url)
        self.add_list_item('Reticulating splines')
        self.add_list_item('Immanentize eschaton')
        first_list_url = self.browser.current_url

        # she notices a my lists link for the first time.
        self.browser.find_element_by_link_text('My lists').click()

        #she sees that the list is in there, named according to its first list item
        self.wait_for(
            lambda: self.browser.find_element_by_link_text('Reticulating splines')
        )
        self.browser.find_element_by_link_text('Reticulating splines').click()
        self.wait_for(
            lambda: self.assertEqual(self.browser.current_url, first_list_url)
        )

        # she decides to start another list just to see.
        self.browser.get(self.live_server_url)
        self.add_list_item('Click cows')
        second_list_url = self.browser.current_url

        # Under "my lists" her new list appears
        self.browser.find_element_by_link_text('My lists').click()
        self.wait_for(
            lambda: self.browser.find_element_by_link_text('Click cows')
        )
        self.browser.find_element_by_link_text('Click cows').click()
        self.wait_for(
            lambda: self.assertEqual(self.browser.current_url, second_list_url)
        )

        # she logs out. the 'My lists' option disappears
        self.browser.find_element_by_link_text('Log out').click()
        self.wait_for(lambda: self.assertEqual(self.browser.find_elements_by_link_text('My lists'), []))
