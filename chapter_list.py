'chapter_list_module'

__author__ = 'DSKaowu'

chapter_list=[]
class chapter:
    def __init__(self):
        self.add1()
    def add1(self):
        global chapter_list
        chapter_list.append('chapter_start')
#二级目录
class chapter_zx(chapter):
    def __init__(self):
        super(chapter_zx,self).__init__()
        self.add2()
    def add2(self):
        global chapter_list
        chapter_list.append('chapter_zx')
        
class chapter_wz(chapter):
    def __init__(self):
        super(chapter_wz,self).__init__()
        self.add2()
    def add2(self):
        global chapter_list
        chapter_list.append('chapter_wz')

class chapter_xp(chapter):
    def __init__(self):
        super(chapter_xp,self).__init__()
        self.add2()
    def add2(self):
        global chapter_list
        chapter_list.append('chapter_xp')

class chapter_jm(chapter):
    def __init__(self):
        super(chapter_jm,self).__init__()
        self.add2()
    def add2(self):
        global chapter_list
        chapter_list.append('chapter_jm')

#三级目录

class chapter_2(chapter_zx):
    def __init__(self):
        super(chapter_2,self).__init__()
        self.add3()
    def add3(self):
        global chapter_list
        chapter_list.append('chapter_2')
class chapter_3(chapter_zx):
    def __init__(self):
        super(chapter_3,self).__init__()
        self.add3()
    def add3(self):
        global chapter_list
        chapter_list.append('chapter_3')
class chapter_4(chapter_zx):
    def __init__(self):
        super(chapter_4,self).__init__()
        self.add3()
    def add3(self):
        global chapter_list
        chapter_list.append('chapter_4')
class chapter_5(chapter_zx):
    def __init__(self):
        super(chapter_5,self).__init__()
        self.add3()
    def add3(self):
        global chapter_list
        chapter_list.append('chapter_5')

#四级目录
class chapter_2_10(chapter_2):
    def __init__(self):
        super(chapter_2_10,self).__init__()
        self.add4()
    def add4(self):
        global chapter_list
        chapter_list.append('chapter_2_10')


class chapter_3_1(chapter_3):
    def __init__(self):
        super(chapter_3_1,self).__init__()
        self.add4()
    def add4(self):
        global chapter_list
        chapter_list.append('chapter_3_1')
class chapter_3_2(chapter_3):
    def __init__(self):
        super(chapter_3_2,self).__init__()
        self.add4()
    def add4(self):
        global chapter_list
        chapter_list.append('chapter_3_2')
class chapter_3_3(chapter_3):
    def __init__(self):
        super(chapter_3_3,self).__init__()
        self.add4()
    def add4(self):
        global chapter_list
        chapter_list.append('chapter_3_3')
class chapter_3_4(chapter_3):
    def __init__(self):
        super(chapter_3_4,self).__init__()
        self.add4()
    def add4(self):
        global chapter_list
        chapter_list.append('chapter_3_4')
class chapter_3_8(chapter_3):
    def __init__(self):
        super(chapter_3_8,self).__init__()
        self.add4()
    def add4(self):
        global chapter_list
        chapter_list.append('chapter_3_8')


class chapter_S4_1(chapter_4):
    def __init__(self):
        super(chapter_S4_1,self).__init__()
        self.add4()
    def add4(self):
        global chapter_list
        chapter_list.append('chapter_S4_1')
class chapter_S4_6(chapter_4):
    def __init__(self):
        super(chapter_S4_6,self).__init__()
        self.add4()
    def add4(self):
        global chapter_list
        chapter_list.append('chapter_S4_6')
class chapter_4_2(chapter_4):
    def __init__(self):
        super(chapter_4_2,self).__init__()
        self.add4()
    def add4(self):
        global chapter_list
        chapter_list.append('chapter_4_2')
class chapter_4_4(chapter_4):
    def __init__(self):
        super(chapter_4_4,self).__init__()
        self.add4()
    def add4(self):
        global chapter_list
        chapter_list.append('chapter_4_4')
class chapter_4_5(chapter_4):
    def __init__(self):
        super(chapter_4_5,self).__init__()
        self.add4()
    def add4(self):
        global chapter_list
        chapter_list.append('chapter_4_5')
class chapter_4_6(chapter_4):
    def __init__(self):
        super(chapter_4_6,self).__init__()
        self.add4()
    def add4(self):
        global chapter_list
        chapter_list.append('chapter_4_6')
class chapter_4_7(chapter_4):
    def __init__(self):
        super(chapter_4_7,self).__init__()
        self.add4()
    def add4(self):
        global chapter_list
        chapter_list.append('chapter_4_7')
class chapter_4_8(chapter_4):
    def __init__(self):
        super(chapter_4_8,self).__init__()
        self.add4()
    def add4(self):
        global chapter_list
        chapter_list.append('chapter_4_8')
class chapter_4_9(chapter_4):
    def __init__(self):
        super(chapter_4_9,self).__init__()
        self.add4()
    def add4(self):
        global chapter_list
        chapter_list.append('chapter_4_9')
class chapter_4_10(chapter_4):
    def __init__(self):
        super(chapter_4_10,self).__init__()
        self.add4()
    def add4(self):
        global chapter_list
        chapter_list.append('chapter_4_10')

        
class chapter_5_3(chapter_5):
    def __init__(self):
        super(chapter_5_3,self).__init__()
        self.add4()
    def add4(self):
        global chapter_list
        chapter_list.append('chapter_5_3')        
class chapter_5_8(chapter_5):
    def __init__(self):
        super(chapter_5_8,self).__init__()
        self.add4()
    def add4(self):
        global chapter_list
        chapter_list.append('chapter_5_8')        
class chapter_5_10(chapter_5):
    def __init__(self):
        super(chapter_5_10,self).__init__()
        self.add4()
    def add4(self):
        global chapter_list
        chapter_list.append('chapter_5_10')

