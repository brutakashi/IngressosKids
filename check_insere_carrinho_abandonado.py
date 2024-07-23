import requests

def check_email_status():
    url = "https://www.ingressoskids.com/schedule/InsereCarrinhoAbandonado.aspx"
    response = requests.get(url)
    if response.status_code == 200:
        print("Success: Email status checked.")
    else:
        print(f"Failed: Status code {response.status_code}")

if __name__ == "__main__":
    check_email_status()
