# discord-py-bot

Written during one of my development streams. This is just a freeform project that can go anywhere. I aim for this to be an active bot in my own streaming Discord.

## installing and running

* clone the repository
* create a new Python virtual environment
* (you may need to see the footnote for this section first) run the activate script to enter the virtual environment, usually found in `env/Scripts/activate{.bat|.ps1|}`
* run `pip install -r requirements.txt` 

I used to be able to get a .env file in the root folder working with just the virtual environment, but something changed in it. What I did was append a line in one of the activation scripts to add the "DISCORD_TOKEN" and "CMD_SYMBOL" environment variables, then restart the environment. Not ideal, but it works.

## features

* dynamic command loading