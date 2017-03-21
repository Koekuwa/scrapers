#coding:utf-8

"""
cron起動用スクリプト
"""

import puller as pull

if __name__ == "__main__":
    pull.PullRate().sendToSQL()
