# telegram-SJP
## Telegram Słownik Języka Polskiego bot
This is a simple bot for telegram written in python and using [telethon](https://github.com/LonamiWebs/Telethon) library.
It allows you to search for words definitions from https://sjp.pwn.pl (internet polish dictionary).
It works both in normal bot mode and inline mode. If you want to see it in action it _should_ currently work if you try using [@slownikbot](https://t.me/slownikbot).
### Normal mode
Simply send message with a word or part of the word to the bot - 
it will reply with definition (if it finds it) or give you suggestions for the complete word.
This mode will probably get a little improved in some time.
### Inline mode (recommended and more useful)
Use @[BotName] in any conversation and start typing a word, you will get the suggestions of definitions that you can click on.
The definition will be sent as a message **via @[Botname]**.
### Example
![example](https://i.imgur.com/AyfscOo.png) ![second example](https://i.imgur.com/oYLwZmI.png)
## Setup
If you want to set your own bot based on this code you will (of course) need to create a bot (look https://core.telegram.org/bots up).
You will need an **API ID**, **API hash** and **bot token** parsed to the bot.py for it to work correctly.
Project supports docker and recommended option is to use it and create an .env file with these as variables.
Generally - if you get bot.py running correctly in any way, bot will work.
