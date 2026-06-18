from pages.base_page import BasePage

class CookiesBanner(BasePage):

    banner = ".js-cookie-policy-main"
    customize_btn = "button.js-cookie-policy-main-settings-button:visible"

    accept_selected_btn = "button.js-cookie-policy-settings-decline-button:visible"

    def banner_is_visible(self):
        return self.is_visible(self.banner)
    
    def customization_button_is_visible(self):
        return self.is_visible(self.customize_btn)

    def open_customization(self):
        self.click(self.customize_btn)

    def accept_selected(self):
        self.click(self.accept_selected_btn)
