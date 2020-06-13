import requests

def refresh():
    burp0_url = "https://www.pythonanywhere.com:443/user/bottwittetins/schedule/task/160725/extend"
    burp0_cookies = {"sessionid": "pavn7gjspzleo6qgxlfjnd2m63kd0wd6", "cookie_warning_seen": "True", "csrftoken": "bmDvb4RpicUwkdemFh0p1XuUBZoHWBs7phTNIUpHrpyTltuMD3gHZ9SZPKlsyEtV", "_ga": "GA1.2.1785059359.1591999259", "_gid": "GA1.2.928083924.1591999259"}
    burp0_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0", "Accept": "application/json", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate", "Referer": "https://www.pythonanywhere.com/user/bottwittetins/tasks_tab/", "X-CSRFToken": "MCGoL5XWn3W6OvxG2ytC63BCKnmtHyb90xWGiVvewgAtPLN60kJU4fZHY8jejBcX", "Content-Type": "application/json", "Origin": "https://www.pythonanywhere.com", "Connection": "close"}
    r = requests.post(burp0_url, headers=burp0_headers, cookies=burp0_cookies)
    print(r.status_code)
    if r.status_code == 200:
        print("refresht succesfully")
    else: 
        print("did not refresh succesfully")

