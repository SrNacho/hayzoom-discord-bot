<div align="center">Suggestions are welcomed</div>
<br>
---
# hayzoom-discord-bot
Discord bot that reads an excel with dates and sends a message when you have an equity with the day
## How it works
It checks every 20 seconds if there's a date that equals with the actual date from the timezone GMT-3 Buenos Aires. If there's an equity, it will send a message to the channel where it was initialized.
## Setting up.
#### 1 - set up your bot token, channels and timezone in the .env file. for a full timezone list [here](https://gist.github.com/heyalexej/8bf688fd67d7199be4a1682b3eec7568)

#### 2 - install the required libs
* discord
* python-dotenv
* asyncio
* schedule
* pytz
* pandas
* openpyxl
#### 3 - set up your schedulements at the horarios.xlsx file 
with the format of:
#
|      Dia       |         Materia          |     Hora      |
|----------------|--------------------------|---------------|
| DD/MM/YY:00:00 | Message you want to send | Schedule time |
#

In the **Dia** column you will set up the Day, Month and Year.

### **DO NOT CHANGE THE NAME HEADERS `Dia, Materia and Hora`**

### **DO NOT CHANGE THE :00:00 PARAMETER IF YOU WANT TO RECEIVE IT AT START OF THE DAY**

#### 3 - py main.py
<br>

# KNOWN ISSUES
* If you a message in another channel with the `!list` command, it will execute the command (doesn't matter if the bot is in `n` servers amount and you type it in one of this)