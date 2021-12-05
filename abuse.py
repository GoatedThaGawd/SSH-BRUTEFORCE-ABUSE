import requests
import os
import socket

url = 'https://api.abuseipdb.com/api/v2/report'

socketname = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

socketname.bind(("",22))
socketname.listen()

while True:
  connection, address = socketname.accept() #address is the ip
  address = str(address).split("'")
  address = address[1]

  params = {
    'ip':str(address),
    'categories':'18,20',
    'comment':'SSH login attempts with user root.'
  }

  headers = {
    'Accept': 'application/json',
    'Key': 'YOUR_ABUSEIPDB_API_KEY_HERE'
  }

  response = requests.request(method='POST', url=url, params=params, headers=headers)

  discord_webhook_url = 'YOUR_WEBHOOK_URL_HERE'
  Message = {
  "content": "Attempted SSH Login From IP Address: " + str(address) + " Automatically Reporting To AbuseIPDB.com."
}
  requests.post(discord_webhook_url, data=Message)
  
  print(response.status_code)
  if response.status_code == 429:
    print("IP Already reported - You must wait 15 minutes")
  else:
    pass
  print("User reported, IP: " + str(address))
  connection.close()