from pages.cookies_banner import CookiesBanner

def test_customize_and_accept_selected(page):
    page.goto("https://www.ing.pl")

    cookies = CookiesBanner(page)

    cookies.open_customization()

    cookies.accept_selected()

    cookies = page.context.cookies()

    forbidden_prefixes = [
        "_fbp",
        "_gcl",
        "_uet"
    ]

    for cookie in cookies:
        for prefix in forbidden_prefixes:
            assert not cookie["name"].startswith(prefix), \
                f"Cookie {cookie['name']} NIE powinno być ustawione!"