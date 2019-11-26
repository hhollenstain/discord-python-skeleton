# Discord python Bot


## How to develop?

The makefile is your friend, but have a few perquisites you will need to cover first.
You will need pipenv, make, gcc (linux) for compiling fun. This readme will not go
over all this, but should be straight forward. Some info about [pipenv](https://realpython.com/pipenv-guide/#pipenv-introduction)



### Running commands

#### make init
does the base install of the source package through pipenv that should already be installed,
if a local pipenv isn't yet setup this is when it will happen (python 3.6.8)

#### make check
Designed to do linting and pipenv checking for dependencies and such

#### make test
This is designed to install bot package and testing packages if I ever decided to write tests for it :shrug:

#### make dist
Makes is dist package for system built on.

#### make live
This run only on image builds in my CI/CD pipeline just install the package in the image and pushes into image repo.


### After installing fakah-bot what do?

You will need to copy example.env to .env and update the value inside

| ENV Variable | Description | Required | Default |
| :----------- | :---------: | -------: | :-----: |
| `APP_ID`     | APP ID of your discordapp | NO | N/A |
| `TOKEN`      | Token for your bots api access to discord | YES | N/A |

### Now Running the bot locally
run:
```bash
pipenv run bot
```

```bash
pipenv run bot                                                                                                                                                                  
Loading .env environment variables...
[2019-11-25 19:58:03][INFO] [bot.bot.main:50] Bot brewing coffee. Just a moment
[2019-11-25 19:58:03][DEBUG] [asyncio.__init__:54] Using selector: EpollSelector
[2019-11-25 19:58:03][WARNING] [discord.client.__init__:189] PyNaCl is not installed, voice will NOT be supported
[2019-11-25 19:58:03][INFO] [bot.lib.plugin.load:19] Loaded extension: bot.lib.plugins.server
[2019-11-25 19:58:03][INFO] [bot.lib.plugin.load:19] Loaded extension: bot.lib.plugins.example
[2019-11-25 19:58:03][INFO] [discord.client.login:399] logging in using static token
[2019-11-25 19:58:03][INFO] [discord.gateway.from_client:241] Created websocket connected to wss://gateway.discord.gg?encoding=json&v=6&compress=zlib-stream
[2019-11-25 19:58:03][INFO] [discord.gateway.identify:320] Shard ID 0 has sent the IDENTIFY payload.
[2019-11-25 19:58:03][INFO] [discord.gateway.received_message:411] Shard ID 0 has connected to Gateway: ["gateway-prd-main-cp9z",{"micros":68385,"calls":["discord-sessions-prd-1-5",{"micros":66985,"calls":["start_session",{"micros":60218,"calls":["api-prd-main-608j",{"micros":53409,"calls":["get_user",{"micros":9485},"add_authorized_ip",{"micros":5},"get_guilds",{"micros":2057},"coros_wait",{"micros":1}]}]},"guilds_connect",{"micros":1,"calls":[]},"presence_connect",{"micros":6456,"calls":[]}]}]}] (Session ID: 8115c14c8301ff1a009f687a6712545c).
[2019-11-25 19:58:05][INFO] [bot.lib.plugins.server.on_ready:18] Logged in as Test-boot
[2019-11-25 19:58:05][INFO] [bot.lib.utils.list_servers:75] Current servers: []
[2019-11-25 19:58:05][INFO] [bot.lib.utils.list_users:87] Number Of clients: 0

```


## Okay I got it running so?
Either fix things or change things you want. This runs on the discordpy API documentation [here](https://discordpy.readthedocs.io/en/latest/index.html)
If you want to fix things or just improve it go ahead and submit PRs against the repo, I will welcome any changes!
