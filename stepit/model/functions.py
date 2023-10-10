from selene import by, have
from selene.support.shared import browser
from selene.support.shared.jquery_style import s, ss
import time


class DressaTest:
    def __init__(self):
        self.site_URL = 'https://dressa.com.ua/uk/'

    def site_open(self):
        browser.driver.maximize_window()
        browser.open('https://dressa.com.ua/uk/')
        return self

    def auth_site(self):
        ss("//div[@id='profile__button']")[0].click()
        time.sleep(2)
        ss(by.text('Увійти / Зареєструватися'))[0].click()
        time.sleep(2)
        s("#regularUserLogin").type("irina071165@gmail.com").press_tab()
        time.sleep(2)
        s("#regularUserPassword").type("n!vw47Y").press_enter()
        time.sleep(5)
        return self

    def check_auth(self):
        ss("//div[@id='profile__button']")[0].click()
        s('.link__profile_popup .popup__profile').click()
        ss('//div[@class="description ng-star-inserted"]')[0].should(have.exact_text('Ірина Хричева'))
        return self

    def choose_category(self):
        ss('.header__nav .ng-tns-c32-0.ng-star-inserted')[12].click()
        ss('.categories__inner_item.ng-star-inserted')[0].click()
        time.sleep(2)
        return self

    def select_product(self):
        s('.ng-star-inserted [dressavendor="56133"]').click()
        time.sleep(2)
        return self

    def add_to_cart(self):
        s('.button__inner.button__inner--buy').click()
        time.sleep(2)
        s("//div[@class='link__shopping_title']").click()
        time.sleep(2)
        s('.button__inner.button__inner--white').click()
        return self

    def counter_add(self):
        ss(".counter__add")[0].click()
        return self

    def check_full_cart(self):
        s('.item__quantity_counter .counter__quantity').should(have.exact_text('2'))
        return self

    def remove_product(self):
        s("//div[@class='icon__trash']").click()
        return self

    def check_empty_cart(self):
        ss('div.title')[1].should(have.exact_text('КОШИК ПОРОЖНІЙ'))
        return self

    def head_page(self):
        s('.link .header__logo').click()
        time.sleep(2)
        return self

    def search_text(self, dress: str):
        ss('#search__field_input')[0].type(dress).press_enter()
        time.sleep(3)
        return self

    def check_search(self):
        s("h1.container__not-found-products_text").should(have.exact_text('ПРОДУКТИ НЕ ЗНАЙДЕНІ'))
        time.sleep(3)
        return self

    def change_name(self):
        ss("//div[@id='profile__button']")[0].click()
        s('.link__profile_popup .popup__profile').click()
        ss(by.text('Змінити'))[0].click()
        ss("#name")[0].double_click().type('Ірен')
        time.sleep(1)
        # s('input#name.input__field .ng-pristine .ng-valid .ng-touched').type('Iryna')
        # time.sleep(1)
        s('div#default_button.button__inner.button__inner--color').click()
        return self

    def check_change_name(self):
        ss("//div[@id='profile__button']")[0].click()
        s('.link__profile_popup .popup__profile').click()
        ss('//div[@class="description ng-star-inserted"]')[0].should(have.exact_text('Ірен Хричева'))
        time.sleep(3)
        return self

    def logout_account(self):
        ss("//div[@id='profile__button']")[0].click()
        time.sleep(2)
        s('.popup__logout.ng-star-inserted').click()
        return self

    def incorrect_mail(self):
        ss("//div[@id='profile__button']")[0].click()
        time.sleep(2)
        ss(by.text('Увійти / Зареєструватися'))[0].click()
        time.sleep(2)
        s("#regularUserLogin").type("irina071165@gmail.").press_tab()
        time.sleep(2)
        s("#regularUserPassword").type("n!vw47Y").press_enter()
        time.sleep(2)
        s('div.notification.ng-star-inserted').should(have.exact_text('Неверный e-mail или пароль'))
        time.sleep(3)
        s('div.close').click()
        return self

    def incorrect_password(self):
        ss("//div[@id='profile__button']")[0].click()
        time.sleep(2)
        ss(by.text('Увійти / Зареєструватися'))[0].click()
        time.sleep(2)
        s("#regularUserLogin").type("irina071165@gmail.com").press_tab()
        time.sleep(2)
        s("#regularUserPassword").type("n!vw47Y8888").press_enter()
        time.sleep(2)
        s('div.notification.ng-star-inserted').should(have.exact_text('Неверный e-mail или пароль'))
        time.sleep(3)
        s('div.close').click()
        return self
