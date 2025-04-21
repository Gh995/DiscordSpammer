import requests

channelID = "YOUR_CHANNEL_ID"
HEADERS = {"AUTHORIZATION":"YOUR_AUTHORIZATION_TOKEN"}

file = open("spam.txt", "r")
lines = file.readlines() 

for line in lines:
    requests.post (f"https://discord.com/api/v9/channels/{channelID}/messages", headers=HEADERS, json={"content":line})
