# kiln-stats

reports and graphs a kiln run

requires output in daemon.log from kiln run

```
sudo apt-get install sqlite3 pdftk
sudo ln -s /usr/bin/sqlite3 /usr/bin/sqlite
git clone git@github.com:jbruce12000/kiln-stats.git
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
cd scripts
./go
```

produces [pdf with a few graphs](https://github.com/jbruce12000/kiln-stats/blob/main/output/final.pdf) and a report.
