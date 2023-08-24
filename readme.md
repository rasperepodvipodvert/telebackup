![](assets/logo.png)
>Backup to telegram your sites archive

## Install

```shell
git clone https://github.com/rasperepodvipodvert/telebackup.git
cd telebackup
```

Create `.env` and past your data from: https://my.telegram.org/apps

```ini
API_ID = '5195065'
API_HASH = 'f933114319f9a650f669e91ccf995165'
```

Create venv

```shell
apt install python3-venv        # if need
python3 -m venv venv
venv\Scripts\activate           # windows
source venv/bin/activate        # linux
pip install -r requirements.txt
```

## How to use

```shell
python3 app.py -u "@ifilatov" -f "./readme.md"
```

## Fetches

- Upload more than 50mb

## TODO

- Split large files
- ~~comandline args~~