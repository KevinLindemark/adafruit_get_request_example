import urequests as requests

def do_connect():
    """connects to Wifi"""
    import network
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        # Update the credentials!!
        wlan.connect('YOUR_SSID', 'YOUR_PASSWORD')
        while not wlan.isconnected():
            pass
    print('network config:', wlan.ifconfig())

do_connect()

# tutorial about python requests
# https://realpython.com/python-requests/
# tutorial about python and JSON
# https://realpython.com/python-json/

# link to Denmark timezone datetime
timestamp_link = "http://worldtimeapi.org/api/timezone/Europe/Copenhagen"
time_response = requests.get(timestamp_link)

time_response = time_response.json() # deserialize response 
datetime = time_response["datetime"] #get datetime from
datetime_list = datetime.split("T") # split date and time to returned list
date = datetime_list[0] # assign date value from list to variable
# store hours, minutes, seconds in seperate variables
hours = datetime_list[1][:2]
minutes = datetime_list[1][3:5]
seconds = datetime_list[1][6:8]

# Doumentation for adafruit pagination headers
# https://io.adafruit.com/api/docs/#pagination-headers

# some values needs to be URL encoded - check link below
# https://www.url-encode-decode.com/

# example link, change to your own adafruit username and feedname
adafruit_feed_link = f"https://io.adafruit.com/api/v2/KEA_ITTEK/feeds/mapfeed/data?end_time={date}+{hours}%3A{minutes}%3A{seconds}+UTC&limit=10"
response = requests.get(adafruit_feed_link)
print(response.text,"\n")
print(response.json())