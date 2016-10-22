# yute
Feed Youtube less.

# Description

Yute reads a list of youtube channels (youtube.com/user/videos) and downloads any new videos.

# List of files

 - `Yute.py`
  - Main. This file does everything.
 - `yute_subscriptions.csv`
  - List of youtube channels to check
 - `yute.sh`
  - For a chron job.
 - `*.log` or `*.log.*`
  - The fuck do you think
 - `/yute-videos/`
  - Output folder. Will be created by Yute if it doesn't exist.

# Setup

## Youtube-dl
Install [youtube-dl](https://github.com/rg3/youtube-dl)

	brew install youtube-dl

or (this works on older osx):

	sudo pip install --upgrade youtube-dl

or:

	sudo curl -L https://yt-dl.org/downloads/latest/youtube-dl -o /usr/local/bin/youtube-dl
	sudo chmod a+rx /usr/local/bin/youtube-dl

## This Repo

	git clone https://github.com/639zw/yute

## Cron

## Apache
Make a symlink to `yute-videos` and allow directory listing.