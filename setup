import requests

server_url = 'http://localhost:5000'

def send_command(command):
    response = requests.post(f'{server_url}/command', json={'command': command})
    return response.json()

def report_data(data):
    response = requests.post(f'{server_url}/report', json={'data': data})
    return response.json()

# Example usage
command_response = send_command('ls')
print(command_response)

report_response = report_data('some data')
print(report_response)
