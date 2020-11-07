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

### Receive update notifications in Telegram

```yaml
version: "3.8"
services:
  watchtower:
    environment:
      WATCHTOWER_NOTIFICATIONS: shoutrrr
      WATCHTOWER_NOTIFICATION_URL: "telegram://bot_token@telegram?channels=user_id"
```
