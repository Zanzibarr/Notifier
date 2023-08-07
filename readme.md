# Telegram_Python_Notifier
This python application, will send messages on telegram, to the chat id specified, from the bot specified by the token.  
Currently it is configured to send text messages, markdown text messages, documents, photos, video and audio.  

We also added a simple listener so that you can send messages to the bot (edit the <a href="https://github.com/Zanzibarr/Telegram_Python_Notifier/blob/main/listener.py">listener.py</a> to customize the responses).  

Feel free to suggest us new improvements or to report some bugs/problems by opening an <a href="https://github.com/Zanzibarr/Telegram_Python_Notifier/issues">Issue</a>.  

#### STILL A WORK IN PROGRESS

# Configuration
Clone this repo into a folder of your choice (the folder must be kept into the system for the app to work).  

To create your bot and view his token you can use the @BotFather (follow this <a href="https://www.youtube.com/watch?v=aNmRNjME6mE">tutorial</a>); to see your chat id you can use the @RawDataBot (follow this <a href="https://www.youtube.com/watch?v=UPC5Ck1oU6k">tutorial</a>).  
Once you created your bot, start a chat with it (without this step, the application will run, but you won't recieve any message).  

You won't need to edit any file, just open a terminal inside the cloned folder and run the command  
```shell
sudo python3 setup.py develop
```

Follow the steps and then you're ready to go!

### IF YOU NEED THE LISTENER:  
To configure the listener, you will need to install the python packages for telegram:
```shell
pip install python-telegram-bot
```
Then you will need to insert your bot token and authorized chat id's in the <a href="https://github.com/Zanzibarr/Telegram_Python_Notifier/blob/main/listener.py">listener.py</a> file.  

(The listener must be running for it to work)

# Edit build

If you edit some files and want to build the application again, you have to locate the build first and delete it.

To locate the current build you can use the command  
```shell
whereis notify
```
then  
```shell
sudo rm /path/to/file/notify
```

Once you've done this, you can apply your changes, then repeat the setup command used during the initial configuration:
```shell
sudo python3 setup.py develop
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


# Credits
Authors: <a href="https://github.com/Zanzibarr">@Zanzibarr</a> <a href="https://github.com/RickSrick">@RickSrick</a>
