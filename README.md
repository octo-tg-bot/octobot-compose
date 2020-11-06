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