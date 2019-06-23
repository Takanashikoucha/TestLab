# -*- coding: UTF-8 -*-
# @LastAuthor: TakanashiKoucha
# @Date: 2019-05-10 19:05:15
import configparser

import easygui
import requests


def mainloop():
    i = 0
    try:
        if i < 3:
            list = requests.get(
                r"https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_best.txt",
                timeout=2.5)
            trackers = list.text
            finalTrackers = trackers.replace("\n\n", ",")
    except:
        i = i + 1
    filepath = easygui.fileopenbox(msg="请定位aria2配置文件位置",
                                   title="Aria2_BestTrackers",
                                   filetypes="*.conf")
    cf = configparser.ConfigParser()
    cf.read(filepath)
    cf.set("all", "bt-trackers", finalTrackers)
    cf.write(open(filepath, "w"))


try:
    mainloop()
except:
    easygui.msgbox(
        msg="失败,请退出重试",
        title="异常",
        ok_button='退出',
    )
