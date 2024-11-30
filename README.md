## Inspiration

Telegram bot with full control over your ai-necklace, what can improve your life better?

## What it does

Have your ever imagined that you can manage all the conversations around you in your favorite messenger? With OmiTelebot this becomes possible!

1. **Receive your memories in telegram.**
Receive summary of your business conversations just in telegram. Recap and share with friends your insights! Download the full version of conversation if needed

2. **Day summary.**
Get texted by bot about your results of the day

3. **Capture voice message or dictate the text just in your necklace.**
Type /voice command to the bot, dictate a message and receive it to telegram!

4. **Recap geo-positions of your talks.**
Check out positions of your talks on the map

## Setup
1. Create .env file with the content shown in .env.example file
2. Fill env variables `BOT_TOKEN`, `MONGO_URL`, `MONGO_INITDB_ROOT_USERNAME`, `MONGO_INITDB_ROOT_PASSWORD`


## Commands
### Run bot
1. Launch bot with `docker-compose up bot`

### Run webhook api handler
1. Launch bot with `docker-compose up api_server`

### Collect strings for localization
1. Collect strings with `docker-compose up collect_strings`

### Compile strings for localization
1. Compile strings with `docker-compose up compile_strings`
