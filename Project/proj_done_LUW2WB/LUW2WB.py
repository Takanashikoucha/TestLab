# -*- coding: UTF-8 -*-
# @LastAuthor: TakanashiKoucha
# @Date: 2018-03-01 15:38:31
# Look Up Words To WordBook
import codecs
import requests
import easygui
from playsound import playsound


def main():
    while 1:
        buff = easygui.enterbox(
            '''请输入要查询的单词:''')
        try:
            Data = requests.get('https://api.shanbay.com/bdc/search/?word=' +
                                buff).json()
            CN = Data['data']['cn_definition']['defn']
            Audio = requests.get(Data['data']['audio'])
            with open('audio.mp3', 'wb') as f:
                f.write(Audio.content)
            with codecs.open('wordbook.md', 'a+', 'utf-8') as f:
                f.write('- ' + buff + '        ' + CN + '\n')
            easygui.msgbox(CN)
            playsound('audio.mp3')
        except:
            easygui.msgbox('卧槽,查不到中文哇.')
            break


if __name__ == '__main__':
    main()
