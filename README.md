# kiln-stats

reports and graphs a kiln run

requires output in daemon.log from kiln run.

libatlas-base-dev only needed if you plan to run this on a raspberry pi.
**warning**... this runs slow on a raspberry pi.

```
sudo apt-get install sqlite3 pdftk libatlas-base-dev
sudo ln -s /usr/bin/sqlite3 /usr/bin/sqlite
git clone git@github.com:jbruce12000/kiln-stats.git
python3 -m venv
source venv/bin/activate
pip install -r requirements.txt
cd scripts
./go
```

```
cd ../output; python3 -m http.server
```

Then go to any machine on the network and download final.pdf, assuming your kiln is at ip address 10.0.0.148...

http://10.0.0.148:8000/

Here is an example [pdf with a few graphs](https://github.com/jbruce12000/kiln-stats/blob/main/output/final.pdf)
