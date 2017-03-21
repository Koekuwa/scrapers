#coding:utf-8

"""
cron起動用スクリプト
"""
from argparse import ArgumentParser
import puller as pull
import sys

argparser = ArgumentParser()
argparser.add_argument('--create','-c',help='create table.',action="store_true")
args = argparser.parse_args()






if __name__ == "__main__":

    if args.create:
        pull.PullRate().createTableSQL()
        sys.exit()
    else:
        pull.PullRate().sendToSQL()
