# Telegram Notifier bot

This a simple Telegram bot that can send you notifications about events in a Linux based system.
For example, it can be called from an automatic updates script or from a download manager when something happens.

# Usage
* Install [Telepot](https://github.com/nickoala/telepot). You can use `pip`: `pip install telepot`
* Clone this repository
* Create a bot contacting [@BotFather](https://t.me/BotFather)
* Copy the token code inside the `config.EDIT.py` file and rename it to `config.py`
* Run the `test.py` script and send some messages to the bot. You should see, on the terminal, a log of them. The `ID` of the sender is the last field.
* Copy the above into the `IDS` array inside config.py
* You can use the command `./tg_notify.py PROGRAM_NAME TEXT` to send some notifications. 
* You can create a wrapping script performing some operations on the text before sending it: see `aria2.py` for an example.

Note that any message written to the bot will never been received.

# License
The code on this repository is licensed under the GNU Public License v3, see [LICENSE](LICENSE) for more informations.
