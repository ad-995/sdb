<p align="center">
  <img alt="sdb" src="https://i.imgur.com/M6H5l2o.png" height="140" />
  <p align="center">
    <a href="https://github.com/mez0cc/sdb/releases/latest"><img alt="Release" src="https://img.shields.io/github/release/mez0cc/sdb.svg?style=flat-square"></a>
    <a href="https://github.com/mez0cc/sdb/blob/master/LICENSE"><img alt="Software License" src="https://img.shields.io/badge/license-MIT-brightgreen.svg?style=flat-square"></a>
    <a href="https://github.com/mez0cc/sdb/issues"><img alt="GitHub issues" src="https://img.shields.io/github/issues/mez0cc/sdb.svg?style=flat-square"></a>
    </p>
</p>

<h5 align="center"><i>Periodically query for subdommains</i></h5>

***

`sdb`,  `Subdomain Database`, is a Python applciation to query various APIs for DNS entries. It has the ability to be backgrounded and can query on any interval. The aim of this particular project is to be able to afk a bit of recon. There are several other techniques and queries to add, but as of now, this is fine for me.

Thanks to [michaelranaldo](https://github.com/michaelranaldo) for contributing!

## Installing

```
pip3 install -r requirements
```

## Help Page

```
usage: sdb.py [-h] [-d] [-n] [-i] [-s] [-q] [--single]

Monitor subdomains for changes.

optional arguments:
  -h, --help        show this help message and exit
  -d , --domain     Domain to monitor
  -n , --name       Name of the database file
  -i , --interval   Seconds between runs. 3 hrs = 10800
  -s, --silent      Turn console output off
  -q, --query       Extract all subdomains
  --single          Run sdb once
```

## Usage

### Run every 3 hours

```
sdb.py --domain groups.yahoo.com --name subdomains.db --interval 10800
```

### Run once

```
sdb.py --domain groups.yahoo.com --name subdomains.db --single
```

### Pull results

```
sdb.py --domain groups.yahoo.com --name subdomains.db --query
```

