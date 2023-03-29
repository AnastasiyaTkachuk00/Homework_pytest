from page_site import SearchHelper


def test_check_cart(browser):
    site_main_page = SearchHelper(browser)
    site_main_page.go_to_site()
    site_main_page.click_on_the_cart()
    element = site_main_page.check_empty_cart_page()
    assert "Your shopping cart is empty." in element


def test_check_login_page(browser):
    site_main_page = SearchHelper(browser)
    site_main_page.go_to_site()
    site_main_page.click_on_the_login_button()
    assert 'Login - My Store' in browser.title


def test_check_search_page(browser):
    site_main_page = SearchHelper(browser)
    site_main_page.go_to_site()
    site_main_page.click_on_the_search_field()
    site_main_page.send_keys('Test')
    site_main_page.click_on_the_search_button()
    assert 'Search - My Store' in browser.title


def test_check_contact_us_page(browser):
    site_main_page = SearchHelper(browser)
    site_main_page.go_to_site()
    site_main_page.click_on_the_contact_us_button()
    assert 'Contact us - My Store' in browser.title


def test_check_woman_page(browser):
    site_main_page = SearchHelper(browser)
    site_main_page.go_to_site()
    site_main_page.click_on_the_women_button()
    assert 'Women - My Store' in browser.title
