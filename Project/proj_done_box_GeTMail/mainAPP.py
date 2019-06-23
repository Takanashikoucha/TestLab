# -*- coding: UTF-8 -*-
# @Author: TakanashiKoucha
# @Date: 2017-09-27 23:15:41

import os
import subprocess
import threading
import Tkinter
import ttk

import re
import requests
import xlwt

groupnamelist = []
groupnamenum = []

if os.path.exists(os.getcwd() + '/save'):
    pass
else:
    os.makedirs(os.getcwd() + '/save')

proc = subprocess.Popen('qqbot')


def remove_invalid_utf8(data):
    new_data = re.subn(
        '|([xC0xC1]|[xF0-xFF])[x80-xBF]*' +
        '|[xC2-xDF]((?![x80-xBF])|[x80-xBF]{2,})' +
        '|[xE0-xEF](([x80-xBF](?![x80-xBF]))|(?![x80-xBF]{2})|[x80-xBF]{3,})',
        '', data)
    new_data = re.subn(
        'xE0[x80-x9F][x80-xBF]' + '|xED[xA0-xBF][x80-xBF]', '', new_data)
    return new_data.replace(' ', '').replace('/', '')


def getgroupname():
    global tnamedict
    namedata = requests.get('http://127.0.0.1:8188/list/group')
    namedict = namedata.json()['result']
    for i in range(0, len(namedict)):
        if namedict[i]['qq'] not in groupnamenum:
            groupnamenum.append(namedict[i]['qq'])
        if namedict[i]['name'] not in groupnamelist:
            groupnamelist.append(namedict[i]['name'])
    tnamedict = dict(zip(groupnamenum, groupnamelist))


def getmail(groupnum):
    global tnamedict
    data = requests.get('http://127.0.0.1:8188/list/group-member/' + groupnum)
    result = data.json()['result'][0]['membs']['r']
    workbook = xlwt.Workbook()
    table = workbook.add_sheet(groupnum, cell_overwrite_ok=True)
    first_col = table.col(0)
    sec_col = table.col(1)
    first_col.width = 256 * 30
    sec_col.width = 256 * 30
    for i in range(0, len(result)):
        table.write(i, 0, result[i]['nick'])
        table.write(i, 1, result[i]['qq'] + '@qq.com')
        workbook.save(os.getcwd() + '/save/' +
                      remove_invalid_utf8(tnamedict[groupnum]) + '.xls')


root = Tkinter.Tk()
root.resizable(False, False)
root.title("GetMail")


def getall():
    for num in groupnamenum:
        getmail(num)
    textbox.insert(Tkinter.END, '所有群的邮件表格全部下载完成\n')
    textbox.update()


def begin():
    try:
        getgroupname()
        t = threading.Thread(target=getall)
        t.start()
    except:
        pass
    start.config(text='再来一次')
    textbox.insert(Tkinter.END, 'fine,查看save文件夹下的文件\n')
    textbox.update()


start = ttk.Button(root, text="开始", command=begin)
start.grid(column=1, row=0, columnspan=2)

photo = Tkinter.PhotoImage(file='logo.png')
imgLabel = Tkinter.Label(root, imag=photo)
imgLabel.grid(column=0, row=0, rowspan=2)

textbox = Tkinter.Text(root, width=35)
textbox.grid(column=1, row=1, columnspan=2)


def quit():
    proc.terminate()
    os.system('taskkill /f /t /im qqbot.exe')
    root.quit()


root.protocol("WM_DELETE_WINDOW", quit)

textbox.insert(Tkinter.END, '扫码登陆后点击开始,耐心等待完成\n')
root.mainloop()
