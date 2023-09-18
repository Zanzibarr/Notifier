# Telegram_Python_Notifier
This python application, will send messages on telegram, to the chat id specified, from the bot specified by the token.  
Currently it is configured to send text messages, markdown text messages, documents, photos, video and audio.  

Current version: 1.6  
For informations about versions, read the <a href="https://github.com/Zanzibarr/Telegram_Python_Notifier/blob/main/change_log.md">change_log</a>.    

Feel free to suggest us new improvements or to report some bugs/problems by opening an <a href="https://github.com/Zanzibarr/Telegram_Python_Notifier/issues">Issue</a>.  

#### STILL ADDING FEATURES

# Configuration
To create your bot and view his token you can use the @BotFather (follow this <a href="https://www.youtube.com/watch?v=aNmRNjME6mE">tutorial</a>); to see your chat id you can use the @RawDataBot (follow this <a href="https://www.youtube.com/watch?v=UPC5Ck1oU6k">tutorial</a>).  
Once you created your bot, start a chat with it (without this step, the application will run, but you won't recieve any message).  

Make sure you have already installed the requests module:
```shell
python3 pip -m install requests
```
To download and install properly notify, open a terminal and run the command  
```shell
git clone https://github.com/Zanzibarr/Telegram_Python_Notifier temp/ && python3 temp/setup.py
```

Once you're done you will be ready to go (on a freshly opened terminal)  

This setup works by editing the ~/.bashrc (or ~/.zshrc) file.  

Please note that notify will work only on python3, if you wish you can change the setup.py and notify_app.py by replacing all python3 commands with python commands.  

If any problems occur, let me know by opening an <a href="https://github.com/Zanzibarr/Telegram_Python_Notifier/issues">Issue</a>.  

# Update build
To get the latest version of notify:
```shell
notify -update
```

# Python lib use
You can use the application as a python library:
```python
import notify
```

First of all, you must setup the bot token and chat id:
```python
notify.set_env(token="your_bot_token", i_chat_id="your_chat_id")
```

Then you can use all the methods from the library.  

# Command line use
Open a terminal and write:
```shell
notify -h
```
to get the list of commands.

# Uninstall
To uninstall just run the command
```shell
notify -uninstall
```

# Credits
Authors: <a href="https://github.com/Zanzibarr">@Zanzibarr</a> <a href="https://github.com/RickSrick">@RickSrick</a>
