from pages.base_page import BasePage

class CookiesBanner(BasePage):

    customize_btn = "button.js-cookie-policy-main-settings-button:visible"

    accept_selected_btn = "button.js-cookie-policy-settings-decline-button:visible"
    
    @property
    def analytical_switch(self):
        return self.page.locator("[name='CpmAnalyticalOption'][role='switch']")
    
    def customization_button_is_visible(self):
        return self.is_visible(self.customize_btn)

    def open_customization(self):
        self.click(self.customize_btn)

    def accept_selected(self):
        self.click(self.accept_selected_btn)

    def enable_analytical(self):
        if self.analytical_switch.get_attribute("aria-checked") == "false":
            self.analytical_switch.click()
