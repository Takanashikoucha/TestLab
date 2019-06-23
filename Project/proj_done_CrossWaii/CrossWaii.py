# -*- coding: UTF-8 -*-
# @Author: TakanashiKoucha
# @Date: 2017-09-03 22:29:03

import os
import requests


def downloadHosts(url):
    file = open('./hosts.txt', 'wb')
    data = requests.get(url)
    file.writelines(data)
    file.close()


def crosswaii():
    try:
        os.system(
            r'copy %SystemRoot%\System32\drivers\etc\hosts  %SystemRoot%\System32\drivers\etc\hosts_bak'
        )
        print('backup down')
        os.system(r'copy hosts.txt %SystemRoot%\System32\drivers\etc\hosts')
        print('copy down')
        os.system(r'ipconfig /flushdns')
        print('dnsflush down')
        print('It\'s done and Try your browser!')
    except Exception as e:
        print(e)


if __name__ == '__main__':
    url = 'https://raw.githubusercontent.com/googlehosts/hosts/master/hosts-files/hosts'
    downloadHosts(url=url)
    print('Hosts update success!')
    crosswaii()
    print('Hosts replaced success! Try to cross the wall!')
