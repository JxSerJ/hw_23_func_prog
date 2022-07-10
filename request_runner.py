import requests

url = "http://127.0.0.1:5000/perform_query"
payload = {
    'file_name': 'apache_logs.txt',
    'cmd1': 'filter',
    'value1': 'GET',
    'cmd2': 'map',
    'value2': '0'
}

response = requests.request("POST", url, data=payload)
print(f'Response: \n{response.text}\nStatus code: {response.status_code}\n')


payload = {
    'file_name': 'apache_logs.txt',
    'cmd1': 'map',
    'value1': '0',
    'cmd2': 'unique',
    'value2': ''
}

response = requests.request("POST", url, data=payload)
print(f'Response: \n{response.text}\nStatus code: {response.status_code}\n')


payload = {
    'file_name': 'apache_logs.txt',
    'cmd1': 'limit',
    'value1': '3',
    'cmd2': 'col',
    'value2': '0'
}

response = requests.request("POST", url, data=payload)
print(f'Response: \n{response.text}\nStatus code: {response.status_code}\n')


payload = {
    'file_name': 'apache_logs.txt',
    'cmd1': 'filter',
    'value1': 'GET',
    'cmd2': 'map',
    'value2': '0'
}

response = requests.request("POST", url, data=payload)
print(f'Response: \n{response.text}\nStatus code: {response.status_code}\n')


payload = {
    'file_name': 'apache_logs.txt',
    'cmd1': 'filter',
    'value1': 'GET',
    'cmd2': 'map',
    'value2': '0'
}

response = requests.request("POST", url, data=payload)
print(f'Response: {response.text}\nStatus code: {response.status_code}\n')
