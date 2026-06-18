import pytest
from playwright.sync_api import sync_playwright

def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="append",
        default=["chromium"],
        help="Browsers to run tests against: chromium, firefox, webkit",
    )

@pytest.fixture(scope="session")
def playwright_instance():
    with sync_playwright() as p:
        yield p

@pytest.fixture(scope="session")
def browser_type(request, playwright_instance):
    browsers = request.config.getoption("--browser")
    return [getattr(playwright_instance, b) for b in browsers]

@pytest.fixture(params=["chromium", "firefox"])
def browser(request, playwright_instance):
    return getattr(playwright_instance, request.param)

@pytest.fixture
def page(browser):
    context = browser.launch(headless=True).new_context()
    page = context.new_page()
    yield page
    context.close()
