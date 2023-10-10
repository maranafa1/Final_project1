from Final_project1.stepit.model import dress

def test_dressa_e2e():
    # Open the site in full window
    dress.site_open()
    # Log in and enter email and password
    dress.auth_site()
    # Check my profile for my First and Last name
    dress.check_auth()
    # Select in main menu "В'язаний одяг" Category and Subcategory "Шапки"
    dress.choose_category()
    # Select product
    dress.select_product()
    # Add in to the cart
    dress.add_to_cart()
    # Increase quantity
    dress.counter_add()
    # Check full cart
    dress.check_full_cart()
    # Remove product
    dress.remove_product()
    # Check empty cart
    dress.check_empty_cart()
    # Go to the main page
    dress.head_page()
    # Enter search text
    dress.search_text('Взуття')
    # Check search
    dress.check_search()
    # Change name
    dress.change_name()
    # Check change name
    dress.check_change_name()
    # logout account
    dress.logout_account()
    # Incorrect mail
    dress.incorrect_mail()
    # Incorrect password
    dress.incorrect_password()




