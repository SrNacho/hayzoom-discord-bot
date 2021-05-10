# hayzoom-discord-bot
Discord bot that reads an excel with dates and sends a message when you have an equity with the day
## How it works
It checks every 20 seconds if there's a date that equals with the actual date from the timezone GMT-3 Buenos Aires. If there's an equity, it will send a message to the channel where it was initialized.
## Setting up.
#### 1 - set up your bot token in the .env file
#### 2 - install the requirement libs
#### 3 - py main.py
#### 4 - do !startt in the channel where you want to send the notifications, remember to add your dates to the excel file with the format DD/MM/YY:00:00 (00:00 actually means 00:00 am of the day)
