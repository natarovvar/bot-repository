#  Bot for telegram
My first Python project, an example of a telegram chatbot and as admin-helper in our community chats. based
on the asynchronous aiogram framework.

## What this bot can do?

 * Admin control panel `/apanel`

  ![apanel](https://user-images.githubusercontent.com/111649346/221408007-f0982ac5-4c54-4b98-92ac-abed13060dc5.jpg)
 * Filtering out some obscene words
 * Chat Admin Notifier (a command that sends a message to all administrators when someone has logged in as an administrator)

>adding an administrator,
>active administrator status,
>uploading some images with a description

![Без имени](https://user-images.githubusercontent.com/111649346/221408721-486810e9-4af8-45f9-8438-bcef9d98478d.png)


* You can transfer your geolocation, which will then be saved in the database `/getlocation`
* Uploading photos and adding some description to them in the form of a sentence `/load` (available to authorized administrators)
* Unloading and editing data from a database (available to authorized administrators in the admin panel `/p`)
 ![image](https://user-images.githubusercontent.com/111649346/221410129-089c0611-ab39-4bbc-a648-f2ec4d48e149.png)
## Development
### System dependencies
* Python 3.7
* Aiogram
* pipenv
* SQlite3 

### ⚙️ Project structure
* The  `database` file contains methods for editing and writing
* `handlers`, contains all event handlers for clients and administrators
* `keyboards`, buttons to use
*  in the `create.py` it contains the main methods of launching the bot, and also stores the transferred token
*  `dbot.py` checking the correct launch of the bot and database
*  `mat.json` some obscene words encoded in unicode
## Deployment
Here is a brief instruction on how to launch the bot
* Create a virtual environment in a place convenient for you
* Aiogram Installation`$ pipenv install aiogram`
* Create a bot using `@BotFather ` and get a `TOKEN`
* Use the `run.bat` to launch the bot, put your token in the `API_TOKEN` field
```python
@echo off

call D:\bot_repository-master\venv\Scripts\activate

cd D:\bot_repository-master

set API_TOKEN = ........... 
set CHANNEL_ID = ..........
python dbot.py

pause 
```
* In order to make the user the administrator of the bot, you need to create a separate chat group and add the ID of this group to the variable `channel_id` `channel_id = os.getenv('CHANNEL_ID') ` in the file `create.py`

```python
from aiogram import Bot, Dispatcher
import os 
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()

bot = Bot(token = os.getenv('TOKEN')) # объект бота
channel_id = os.getenv('CHANNEL_ID')
dp = Dispatcher(bot, storage = storage) # объект диспетчера
```
