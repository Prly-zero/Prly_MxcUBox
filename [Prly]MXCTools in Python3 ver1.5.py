'''
-*- encoding: utf-8 -*-
Project-MXCTools in Python3 ver1.5
请使用pip install pyperclip 命令安装pyperclip模块以支持程序功能正常运行安装后删除代码前注释符#以保证程序功能实现
当然,在此之前你需要安装完整的python3运行环境以及pip
安装完成后删除"import pyperclip","pyperclip.copy(ComText)"和“print("内容已复制到粘贴板")”这些代码前的#号
by.Prly_Zero
需要的支持库:(安装指令)
pip install pyperclip
pip install pyttsx3
'''
import pyttsx3
import pyperclip
import os
print("欢迎来到Prly.汐翎的世界")
print("接下来我将会用最简单的方法来帮助你")
print("由于开发进度有限,功能也将有限")
print("让我们开始吧！")
print("\033[33m请键入以下选项(填数字)“1.高级指令助手(1.12)“\033[0m")
def addp():
    if ComText[-1]!="{" and ComText[-1]!=",":
        return ","
    else:
        return ""
def che():
    while True:
        finput = input("请输入数字:")
        try:
            x=eval(finput)
            if type(x)==int:break
        except:pass
    return finput
option1=int(che())
def opt2(x):
    if x==1:
        Text="ench:["
        print("盔甲：【0】保护、【1】火焰保护、【2】摔落保护、【3】爆炸保护、【4】弹射物")
        print("保护、【5】水下呼吸、【6】水下速倔、【7】荆棘、【8】深海探索者、【9】冰霜行者")
        print("剑：【16】锋利、【17】亡灵杀手、【18】截肢杀手、【19】击退、【20】火焰附加、【21】抢夺、【22】横扫之刃")
        print("镐子：【32】效率、【33】精准采集、【34】耐久、【35】时运")
        print("弓：【48】力量、【49】冲击、【50】火矢、【51】无限")
        print("鱼竿：【61】海之眷顾、【62】饵钓")
        print("其他：【70】经验修补、【10】绑定诅咒、【71】消失诅咒")
        stop=0
        while stop==0:
            print("\033[33m是否添加(1/0)\033[0m")
            option2f1=int(che())
            if option2f1==1:
                enchid=input("\033[33m请输入附魔ID\033[0m")
                print("\033[33m请输入附魔等级\033[0m")
                enchlvl =che()
                if Text!="ench:[":
                    Text=Text+","
                Text=Text+"{id:"+enchid+",lvl:"+enchlvl+"}"
            else:
                Text=Text+"]"
                return Text
    else:
        return ""
def opt3(x):
    if x==1:
        return "Unbreakable:1b"
    else:
        return ""
def opt4(x):
    if x==1:
        name=input("\033[33m请输入物品的名称:\033[0m")
        Text = "display:{Name:\""+name+"\""
        print("\033[33m是否添加备注?(True:1/False:0)\033[0m")
        option4f1=int(che())
        if option4f1==1:
            Text=Text+",Lore:["
            LoreText=""
            stop=0
            while stop==0:
                input("\033[33m是否添加?(True:1/False:0)\033[0m")
                option4f2=int(che())
                if option4f2==1:
                    lore=input("\033[33m请输入内容:\033[0m")
                    if LoreText!="":
                        LoreText=LoreText+","
                    LoreText=LoreText+"\""+lore+"\""
                else:
                    Text=Text+LoreText+"]}"
                    return Text
        else:
            return Text+"}"
    else:
        return ""
def opt5(x):
    if x==1:
        print("{HideFlags:1-32}")
        print("1 = 附魔")
        print("2 = 属性修改器")
        print("4 = 不能破坏")
        print("8 = 能破坏的方块")
        print("16 = 能放在的方块")
        print("32 = 其他, 比如药水效果")
        print("如果要隐藏多个标签，你需要把那些标签的数值加起来")
        print("\033[33m请输入值:\033[0m")
        f=che()
        return "HideFlags:"+f
    else:
        return ""
ComText="/give @p "
if option1==1:
    ItemID=input("\033[33m请输入物品ID(自动填充“minecraft:”):\033[0m")
    ComText=ComText+"minecraft:"+ItemID+" 1 0 "
    print("\033[33m需要添加附魔吗?输入数字(True:1/False:0)\033[0m")
    option2=int(che())
    ComText=ComText+"{"+opt2(option2)
    print("\033[33m需要添加无法破坏吗?输入数字(True:1/False:0)\033[0m")
    option3=int(che())
    ComText = ComText + addp() + opt3(option3)
    print("\033[33m需要添加展示信息吗?输入数字(True:1/False:0)\033[0m")
    option4=int(che())
    ComText = ComText + addp() + opt4(option4)
    print("\033[33m需要隐藏标签吗?输入数字(True:1/False:0)\033[0m")
    option5=int(che())
    ComText = ComText + addp() + opt5(option5)
    #待补充
    ComText=ComText+"}"
    print(ComText)
    pyperclip.copy(ComText)
    print("\033[33m内容已复制到粘贴板\033[0m")
    engine = pyttsx3.init()
    engine.say("内容已复制到粘贴板")
    engine.runAndWait()
    os.system("pause")
else:
    os.system("pause")



