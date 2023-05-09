from dotenv import dotenv_values
import datetime as dt
import requests

# Environment variables that holds secret keys
discord_config = {
    **dotenv_values(".env.secret")
}

# Bot token used in Discord
discord_token = discord_config["DISCORD_TOKEN"]

# Personal channel in Discord
discord_channel_id = discord_config["DISCORD_CHANNEL_ID"]

# List of friends' birthday
birthdays = {
    'riza': dt.date(1991, 2, 27),
    'pogi': dt.date(1991, 3, 25),
    'daniel': dt.date(1991, 4, 15),
    'jacob': dt.date(1991, 5, 11),
    'gel': dt.date(1990, 5, 24),
    'sel': dt.date(1992, 9, 30),
    'norbs': dt.date(1991, 10, 7),
    'xtian': dt.date(1991, 10, 18),
    'jay': dt.date(1991, 11, 7)
}

# Checks the date today and find match on the birthday list
def check_birthdays():
    today = dt.date.today()

    for name, dob in birthdays.items():
        if dob.month == today.month and dob.day == today.day:
            message = f"Today is {name.capitalize()}'s birthday. Send a message"
            return message
    else:
        message = "No one has birthday today"
        return message
    
# Send notification to Discord
def send_reminder(birthday):
    payload = {"content": birthday, "tts": False}
    r = requests.post(f"https://discord.com/api/webhooks/{discord_channel_id}/{discord_token}", data=payload)
    return r.text

# Call the functions
bday = check_birthdays()
send_reminder(bday)
        
