import logging, os, argparse, subprocess
from logging import handlers

# Globals with defaults
_sublist = 'yute_subscriptions.csv'
_outfolder = 'yute-videos'
_logName = 'yute.log'
# Parse Args
parser = argparse.ArgumentParser(description='')
parser.add_argument('-i', 
	help="Input file (should be csv with url in position 0). default is \
	yute_subscriptions.csv.")
parser.add_argument('-o', help="Output folder. Default is 'yute-videos'.")
parser.add_argument('-v', help="Enable verbose (console) logging. Useful for \
	debugging. By default yute.py does not print anything (but exceptions).")
args = parser.parse_args()

if args.i:
	_sublist = args.i

if args.o:
	_outfolder = args.o

# initialize logs.
logger = logging.getLogger('yuteLogger')
logger.setLevel(logging.DEBUG)

fh = handlers.RotatingFileHandler(_logName, maxBytes=200000) #20kByte
fh.setLevel(logging.DEBUG)
fh_formatter = logging.Formatter('%(asctime)s: %(message)s')
fh.setFormatter(fh_formatter)
logger.addHandler(fh)

if args.v:
	ch = logging.StreamHandler()
	ch.setLevel(logging.DEBUG)
	ch_formatter = logging.Formatter(
		'%(asctime)s [%(name)s][%(levelname)s] %(message)s')
	ch.setFormatter(ch_formatter)
	logger.addHandler(ch)


def yexit(why=''):
	logger.info("----- Stopping Yute ----- \n %s" % why)
	logging.shutdown()
	exit(0)


def main():
	print("Go Fuck Yourself.")
	#todo
	yexit()


if __name__ == '__main__':
	logger.info("----- Starting yute. -----")
	main()