from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import messagebox
from PIL import ImageTk
import PIL
import auto_game
import threading
import sys
import os
import time,re

root = Tk()
root.title("Auto_aknight")

width, height = 600, 500  # 窗口大小
mouse_coord = [0, 0]  # 初始化鼠标位置
# y居中显示
root.geometry('%dx%d+%d+%d' %
              (width, height, 0, (root.winfo_screenheight() - height) / 2))
root.overrideredirect(True)
root.resizable(width=False, height=False)
root.config(bg='white')

style = ttk.Style()
style.map('TButton', background=[('disabled', '#d9d9d9'), ('active', '#FFFFFF')], foreground=[
          ('disabled', '#a3a3a3')], relief=[('pressed', '!disabled', 'sunken')])
# 窗口部件
label = Label(root, text="auto_knight", bg='#FFAEB9', fg='white',
              font=("微软雅黑", 14), anchor=W, justify=LEFT)
label.pack(fill=X, side='top')


def shutdown():
    root.destroy()


button_shutdown = ttk.Button(label, text=" X ", command=shutdown,)
button_shutdown.pack(side='right')


def iconify():
    root.overrideredirect(False)
    root.iconify()


button_iconify = ttk.Button(label, text=" — ", command=iconify)
button_iconify.pack(side='right')
# 左侧部件
left_frame = Frame(width=500, height=470, bg='#FFE4C4')
left_frame.pack(side='left')
label_text = Label(
    left_frame, text='--------------- 任务列表 ---------------', bg='#FFE4C4')
label_text.place(relx=0.5, rely=0, anchor=N)
misson_list = Listbox(left_frame, width=60, height=14, bd=2, relief=FLAT,)
misson_list.place(relx=0.5, rely=0.04, anchor=N)

label_text2 = Label(
    left_frame, text='---------------- 调试窗口 ----------------', bg='#FFE4C4')
label_text2.place(relx=0.5, rely=0.62, anchor=N)
text2 = scrolledtext.ScrolledText(
    left_frame, width=59, height=10, bd=2, relief=FLAT, wrap=NONE)
text2.place(relx=0.5, rely=0.66, anchor=N)
text2.config(state=DISABLED)  # 默认设定为不可gai

'''Y轴scroller，已被替代
scrollbar_y = Scrollbar(text2,command=text2.yview)
scrollbar_y.place(relx=1, rely=0,anchor=NE,relheight=1)
text2.configure(yscrollcommand=scrollbar_y.set)
''X轴scroller，直接增加了宽度
scrollbar_x = Scrollbar(text2,command=text2.xview,orient=HORIZONTAL,)
scrollbar_x.place(relx=0, rely=1,anchor=SW,relwidth=0.98)
text2.configure(xscrollcommand=scrollbar_x.set)
''text2自动滚动好像多此一举了
def modified(event):
    text2.see(END)  # tkinter.END if you use namespaces
text2.bind('<<Modified>>', modified)'''
global misson_sequence  # 初始化任务顺序
misson_sequence = 1


def text_insert(msg):
    text2['state'] = 'normal'
    text2.insert('end', msg)
    text2['state'] = 'disabled'
    text2.see(END)


def connect():
    text_insert('正在尝试连接模拟器...大约需要10s...\n')
    button0_1['state'] = 'disabled'
    os.popen("adb kill-server", "r")
    time.sleep(2)
    f = os.popen("adb connect 127.0.0.1:7555", "r")
    console = f.read()
    f.close()
    text_insert(console)
    if console.find('unable') == -1:
        text_insert('连接成功\n')
        button0_2 = Button(right_frame, text="断开模拟器", command=lambda: set_a_new_thread(
            disconnect), padx=2, relief=GROOVE,)
        button0_2.place(relx=0.4, rely=0.04, anchor=N)
    else:
        text_insert('连接失败,请再次尝试\n')
        button0_1['state'] = 'normal'


def disconnect():
    # button0_2['state']='disabled'  noneed
    os.popen("adb kill-server", "r")
    text_insert('已停止adb server\n ')
    button0_1 = Button(right_frame, text="连接模拟器", command=lambda: set_a_new_thread(
        connect), padx=2, relief=GROOVE,)
    button0_1.place(relx=0.4, rely=0.04, anchor=N)


def _add_mission():

    def chapter_zx():
        zx = Toplevel()
        zx.geometry('1144x610+0+%d' % ((root.winfo_screenheight()-610)/2))
        zx.resizable(width=False, height=False)
        zx.overrideredirect(1)
        im = PIL.Image.open('images/material.png')
        global img
        img = ImageTk.PhotoImage(im)
        mt = Canvas(zx, width=1200, height=610)
        mt.place(x=0, y=0)
        mt.create_image(0, 0, image=img, anchor=NW)
        lf = ttk.LabelFrame(mt, text='ready2add', width=150, height=200)
        lf.place(x=900, y=160)
        st = scrolledtext.ScrolledText(lf, width=20, height=15)
        st.place(x=0, y=0)
        st['state'] = 'disabled'

        b_plus = PIL.Image.open('images/material/plus.png')
        global img_b_plus
        img_b_plus = ImageTk.PhotoImage(b_plus)
        ready2add = {}

        chapter_name = {0: '4-9', 1: '3-2', 2: '4-8', 3: '3-1', 4: 'S4-1', 5: '3-4', 6: '4-4', 7: '3-8', 8: '4-2',
                        9: '4-7', 10: '4-5', 11: '4-10', 12: '5-3', 13: 'S4-6', 14: '2-10', 15: '3-3', 16: '4-6', 17: '5-8', 18: '5-10'}

        def ready(_name, times):
            global misson_sequence
            ready2add[misson_sequence] = '[' + \
                str(misson_sequence)+']'+chapter_name[_name]+' ^ '+str(times)
            st['state'] = 'normal'
            st.insert('end', ready2add[misson_sequence]+'\n')
            st['state'] = 'disabled'
            misson_sequence += 1

        spinbox = {}
        button_box = {}  # 字典批量生成19个spinbox和buttom
        xy = [[420, 47], [420, 104], [420, 162], [420, 282], [420, 338], [420, 396], [420, 454], [420, 511], [420, 569], [
            600, 104], [600, 282], [600, 396], [600, 511], [730, 569], [780, 47], [780, 162], [780, 220], [780, 282], [780, 396]]

        def get_spin(i): return ready(i, spinbox[i].get())
        button_box[0] = ttk.Button(
            mt, image=img_b_plus, command=lambda: get_spin(0))
        button_box[1] = ttk.Button(
            mt, image=img_b_plus, command=lambda: get_spin(1))
        button_box[2] = ttk.Button(
            mt, image=img_b_plus, command=lambda: get_spin(2))
        button_box[3] = ttk.Button(
            mt, image=img_b_plus, command=lambda: get_spin(3))
        button_box[4] = ttk.Button(
            mt, image=img_b_plus, command=lambda: get_spin(4))
        button_box[5] = ttk.Button(
            mt, image=img_b_plus, command=lambda: get_spin(5))
        button_box[6] = ttk.Button(
            mt, image=img_b_plus, command=lambda: get_spin(6))
        button_box[7] = ttk.Button(
            mt, image=img_b_plus, command=lambda: get_spin(7))
        button_box[8] = ttk.Button(
            mt, image=img_b_plus, command=lambda: get_spin(8))
        button_box[9] = ttk.Button(
            mt, image=img_b_plus, command=lambda: get_spin(9))
        button_box[10] = ttk.Button(
            mt, image=img_b_plus, command=lambda: get_spin(10))
        button_box[11] = ttk.Button(
            mt, image=img_b_plus, command=lambda: get_spin(11))
        button_box[12] = ttk.Button(
            mt, image=img_b_plus, command=lambda: get_spin(12))
        button_box[13] = ttk.Button(
            mt, image=img_b_plus, command=lambda: get_spin(13))
        button_box[14] = ttk.Button(
            mt, image=img_b_plus, command=lambda: get_spin(14))
        button_box[15] = ttk.Button(
            mt, image=img_b_plus, command=lambda: get_spin(15))
        button_box[16] = ttk.Button(
            mt, image=img_b_plus, command=lambda: get_spin(16))
        button_box[17] = ttk.Button(
            mt, image=img_b_plus, command=lambda: get_spin(17))
        button_box[18] = ttk.Button(
            mt, image=img_b_plus, command=lambda: get_spin(18))
        for i in range(0, 19):
            spinbox[i] = ttk.Spinbox(mt, from_=1, to=99, increment=1, width=2)
            eval('spinbox['+str(i)+'].set(1)')  # 初始化spinbox
            button_box[i].place(x=((xy[i][0])+40), y=(xy[i][1])-4)
            spinbox[i].place(x=xy[i][0], y=xy[i][1])

        def add_comfirm():
            if messagebox.askyesno(message='确定添加关卡吗？', icon='question', title='确认', parent=zx):
                for key in ready2add:
                    misson_list.insert(END, ready2add[key])
                zx.destroy()
                am.destroy()
                root.lift()

        def add_cancel():
            ready2add.clear()
            st['state'] = 'normal'
            st.delete('1.0', 'end')
            st['state'] = 'disabled'
            global misson_sequence
            misson_sequence = 1
            zx.destroy()

        def add_rescind():
            global misson_sequence
            if misson_sequence == 1:
                messagebox.showinfo(message="待添加列表为空")
            else:
                misson_sequence -= 1
                del ready2add[misson_sequence]
                st['state'] = 'normal'
                st.delete('end-2 lines', 'end')
                if misson_sequence != 1:
                    st.insert('end', '\n')
                st['state'] = 'disabled'
        ttk.Button(mt, text='撤销添加', command=add_rescind).place(x=900, y=370)
        ttk.Button(mt, text='√添加完成', command=add_comfirm).place(x=900, y=570)
        ttk.Button(mt, text='×取消并返回上页',
                   command=add_cancel).place(x=1000, y=570)

    am = Toplevel()
    am.title('添加任务')
    am.geometry('1100x200+0+%d' % (root.winfo_screenheight()/2))
    am.resizable(width=False, height=False)
    im1 = PIL.Image.open('images/chapter_zx.png')
    im2 = PIL.Image.open('images/chapter_wz.png')
    im3 = PIL.Image.open('images/chapter_xp.png')
    im4 = PIL.Image.open('images/chapter_jm.png')
    global img_zx, img_wz, img_xp, img_jm
    img_zx = ImageTk.PhotoImage(im1)
    img_wz = ImageTk.PhotoImage(im2)
    img_xp = ImageTk.PhotoImage(im3)
    img_jm = ImageTk.PhotoImage(im4)
    button1 = ttk.Button(am, image=img_zx, command=chapter_zx)
    button2 = ttk.Button(am, image=img_wz)
    button3 = ttk.Button(am, image=img_xp)
    button4 = ttk.Button(am, image=img_jm)
    button1.grid(column=0, row=0)
    button2.grid(column=1, row=0)
    button3.grid(column=2, row=0)
    button4.grid(column=3, row=0)


def add_mission():
    _add_mission()


def cancel_mission():
    misson_list.delete('end')
    global misson_sequence
    if misson_sequence == 1:
        messagebox.showinfo(message="任务列表为空")
    else:
        misson_sequence -= 1


def clean_mission():
    misson_list.delete(0, 'end')
    global misson_sequence
    misson_sequence = 1


def get_name(i): 
    name=misson_list.get(i)
    matchObj = re.match( r'(.*)](.*?) .*', name, re.M|re.I)
    print(matchObj.group(2))
    return matchObj.group(2)
def get_times(i): 
    name=misson_list.get(i)
    matchObj = re.match( r'(.*) ^ (.*?) .*', name, re.M|re.I)
    print(matchObj.group(2))
    return matchObj.group(2)


def star_mission():
    auto_game.run_state='running'
    num=misson_list.size()+1
    for i in range(1,num):
        auto_game.chapter_selet(get_name(i))
        auto_game.chapter_run(get_times(i))
    auto_game.run_state='over'


# 右侧部件
right_frame = Frame(width=100, height=470, bg='#FFE4C4')
right_frame.pack(side='right')
button0_1 = Button(right_frame, text="连接模拟器", command=lambda: set_a_new_thread(
    connect), padx=2, relief=GROOVE,)
button0_1.place(relx=0.4, rely=0.04, anchor=N)

button1 = Button(right_frame, text="增加任务",
                 command=add_mission, padx=9, relief=GROOVE)
button1.place(relx=0.4, rely=0.14, anchor=N)
button2 = Button(right_frame, text="删除最后项",
                 command=cancel_mission, padx=3, relief=GROOVE)
button2.place(relx=0.4, rely=0.24, anchor=N)
button3 = Button(right_frame, text="清空任务",
                 command=clean_mission, padx=9, relief=GROOVE)
button3.place(relx=0.4, rely=0.34, anchor=N)
button4 = Button(right_frame, text="开始任务",
                 command=clean_mission, padx=9, relief=GROOVE)
button4.place(relx=0.4, rely=0.44, anchor=N)
button5 = Button(right_frame, text="暂停任务",
                 command=clean_mission, padx=9, relief=GROOVE)
button5.place(relx=0.4, rely=0.54, anchor=N)
right_frame_1 = Frame(right_frame, width=80, height=100,
                      bg='#FFE4C4', relief=GROOVE, bd=3)
right_frame_1.place(relx=0.41, rely=0.95, anchor=S)
# 新建线程


def set_a_new_thread(fun_name, args_name=()):
    th = threading.Thread(target=fun_name, args=args_name)
    th.setDaemon(True)  # 守护线程
    th.start()


# root.winfo_x()获取当前窗口位置x
def windows_move(event):
    time.sleep(0.01)
    root.geometry('%dx%d+%d+%d' % (width, height, (root.winfo_x()+(event.x -
                                                                   mouse_coord[0])/2), (root.winfo_y()+(event.y-mouse_coord[1])/2)))
    root.update()

# 获取当前鼠标位置


def get_mouse(event):
    global mouse_coord
    mouse_coord = [event.x, event.y]
    print(mouse_coord)

# frame.bind("<Motion>",callback),使用bind获取点击事件


def monitor():
    while True:
        label.bind("<Button-1>", get_mouse)
        label.bind("<B1-Motion>", windows_move)
        label.update()


root.update()

set_a_new_thread(monitor)
root.mainloop()
