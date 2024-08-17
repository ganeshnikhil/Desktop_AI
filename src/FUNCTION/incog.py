from subprocess import call , run 


def open_chrome_incognito(url):
    chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"  # Adjust the path if needed
    run([chrome_path, '--incognito', url])
    
def open_firefox_private(url):
    firefox_path = r"C:\Program Files\Mozilla Firefox\firefox.exe"  # Adjust the path if needed
    run([firefox_path, '-private-window', url])
    
    
def incog_mode(url:str) -> None:
    applescript_code = f'''
    tell application "Google Chrome"
    activate
        tell (make new window with properties {{mode:"incognito"}})
            set URL of active tab to "{url}"
        end tell
    end tell'''
    run(['osascript', '-e', applescript_code])
    return  