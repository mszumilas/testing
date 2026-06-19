from pages.cookies_banner import CookiesBanner

def test_customize_and_accept_selected(page):
    page.goto("https://www.ing.pl")

    cookies = CookiesBanner(page)

    cookies.open_customization()
    cookies.enable_analytical()
    cookies.accept_selected()
    page.reload()
    cookies = page.context.cookies()
    analytical_prefixes = [
        "_ga",
        "_gid",
        "_gat"
    ]

    found = {prefix: False for prefix in analytical_prefixes}

    for cookie in cookies:
        for prefix in analytical_prefixes:
            if cookie["name"].startswith(prefix):
                found[prefix] = True
    assert any(found.values()), f"Brak cookies analitycznych! Znaleziono: {cookies}"
    
    forbidden_prefixes = [
        "_fbp",
        "_gcl",
        "_uet"
    ]

    for cookie in cookies:
        for prefix in forbidden_prefixes:
            assert not cookie["name"].startswith(prefix), \
                f"Cookie {cookie['name']} NIE powinno być ustawione!"
