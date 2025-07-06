import requests

login_url = "http://52.203.72.116:8080/login"
mutuals_url = "http://localhost:8080/get-mutuals"

login_data = {
    "User_mail": "allan",
    "password": "1234"
}

login_response = requests.post(login_url, json=login_data)

if login_response.status_code == 200:
    token = login_response.json().get("token")

    if not token:
        print("Not found token.")
    else:
        print("Token:", token)

        headers = {"Authorization": f"Bearer {token}"}
        mutuals_response = requests.get(mutuals_url, headers=headers)

        print("Status:", mutuals_response.status_code)
        print("Response", mutuals_response.json())

else:
    print("Error to login:", login_response.status_code)
    print("➡️", login_response.json())
