import requests
import keyboard

hostName = 'localhost'
port = '5000'

url_home = 'http://'+hostName+':'+port+'/'

response_home = requests.get(url_home)

print(response_home,'\n\n')
print("Press Enter To Generate Number!!",'\n')

def on_press(event):
    if event.name == 'enter':
        url_generate = url_home
        response_generate = requests.get(url_generate)
        print(response_generate.content)
        return

keyboard.on_press(on_press)

keyboard.wait()