# Octo-Tg-Bot Compose file

This repository contains file for quick deployment of [Octo-Tg-Bot](https://github.com/octo-tg-bot/octobotv4)

## Quickstart

1. Make config file and write your stuff in it
    ```bash
    cp settings.base.toml settings.toml
    nano settings.toml
    ```
2. Make preimport file
    ```bash
    cp preimport-example.py preimport.py
    ```
3. (Optional) Customize preimport file
   ```bash
   nano preimport.py
   ```
4. Run the bot
   ```bash
   docker-compose up
   ```

5. The bot should send you message with results from booting up if you set everything up correctly.

## Extra cool stuff!

You can add that stuff by creating docker-compose.override.yml and putting that stuff into it

### Automatically update bot with watchtower on webhook

```yaml
watchtower:
    command:  --http-api-update --debug --scope octobot
    ports:
      - 8080:8080
    environment:
      WATCHTOWER_HTTP_API_TOKEN: "PUT SUPER SECURE TOKEN HERE!"
```

Make sure to set following secrets if you use the same deployment GitHub action:

- WT_URL - url to update. For example: http://server:8080/v1/update
- WT_TOKEN - your super secure token

### Receive update notifications in Telegram

```yaml
watchtower:
  environment:
    WATCHTOWER_NOTIFICATIONS: shoutrrr
    WATCHTOWER_NOTIFICATION_URL: "telegram://bot_token@telegram?channels=user_id"
```

### Self-hosted bot API

> :warning: **If you are using the watchtower Telegram notifications, use different token in WATCHTOWER_NOTIFICATION_URL**. Bot API blocks out access to bot API after the the different endpoint is getting used, so Watchtower will fail when trying to send notifications

```yaml
version: "3.8"
services:
  botapi:
    image: ghcr.io/octo-tg-bot/tgbotapi:latest
    environment: 
      TELEGRAM_API_ID: PUT THE API ID HERE
      TELEGRAM_API_HASH: PUT THE API HASH HERE
    labels:
      - "com.centurylinklabs.watchtower.scope=octobot"
    logging:
      driver: "none"
    volumes:
      - botapi-files:/file
  bot:
    entrypoint: 'python3 main.py'
    environment:
      ob_telegram_base_url: "http://botapi/bot"
    depends_on: 
      - botapi
      - redis
    volumes:
      - botapi-files:/file
volumes:
  botapi-files:
```