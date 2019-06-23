# -*- coding: UTF-8 -*-
# @LastAuthor: TakanashiKoucha
# @Date: 2018-02-21 17:17:59
import random
import easygui


def main():
    choices = []
    while 1:
        buff = easygui.enterbox(
            '''Input One Choice To Add Coice Or 'done' To Next Step:''')
        if buff == 'done':
            break
        else:
            choices.append(buff)
    try:
        randomnum = random.randint(0, len(choices)-1)
        finalchoice = choices[randomnum]
        easygui.msgbox(finalchoice)
    except:
        easygui.msgbox('No Choice')


if __name__ == '__main__':
    main()
