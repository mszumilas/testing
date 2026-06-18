class BasePage:
    def __init__(self, page):
        self.page = page

    def click(self, locator):
        self.page.locator(locator).click()

    def is_visible(self, locator):
        return self.page.locator(locator).is_visible()
