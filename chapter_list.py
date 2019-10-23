'chapter_list_module'

__author__ = 'DSKaowu'

chapter_list=[]
class chapter:
    def __init__(self):
        self.add1()
    def add1(self):
        global chapter_list
        chapter_list.append('chapter_start')
'''二级目录'''
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

class chapter_pr(chapter):
    def __init__(self):
        super(chapter_pr,self).__init__()
        self.add2()
    def add2(self):
        global chapter_list
        chapter_list.append('chapter_pr')

class chapter_jm(chapter):
    def __init__(self):
        super(chapter_jm,self).__init__()
        self.add2()
    def add2(self):
        global chapter_list
        chapter_list.append('chapter_jm')

'''三级目录'''
# 主线
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
# 物资
class chapter_wz_ls(chapter_wz):
    def __init__(self):
        super(chapter_wz_ls,self).__init__()
        self.add3()
    def add3(self):
        global chapter_list
        chapter_list.append('chapter_wz_ls')
class chapter_wz_ap(chapter_wz):
    def __init__(self):
        super(chapter_wz_ap,self).__init__()
        self.add3()
    def add3(self):
        global chapter_list
        chapter_list.append('chapter_wz_ap')
class chapter_wz_ce(chapter_wz):
    def __init__(self):
        super(chapter_wz_ce,self).__init__()
        self.add3()
    def add3(self):
        global chapter_list
        chapter_list.append('chapter_wz_ce')
class chapter_wz_ca(chapter_wz):
    def __init__(self):
        super(chapter_wz_ca,self).__init__()
        self.add3()
    def add3(self):
        global chapter_list
        chapter_list.append('chapter_wz_ca')
class chapter_wz_sk(chapter_wz):
    def __init__(self):
        super(chapter_wz_sk,self).__init__()
        self.add3()
    def add3(self):
        global chapter_list
        chapter_list.append('chapter_wz_sk')
        
# 芯片
class chapter_pr_a(chapter_pr):
    def __init__(self):
        super(chapter_pr_a,self).__init__()
        self.add3()
    def add3(self):
        global chapter_list
        chapter_list.append('chapter_pr_a')
class chapter_pr_b(chapter_pr):
    def __init__(self):
        super(chapter_pr_b,self).__init__()
        self.add3()
    def add3(self):
        global chapter_list
        chapter_list.append('chapter_pr_b')
class chapter_pr_c(chapter_pr):
    def __init__(self):
        super(chapter_pr_c,self).__init__()
        self.add3()
    def add3(self):
        global chapter_list
        chapter_list.append('chapter_pr_c')
class chapter_pr_d(chapter_pr):
    def __init__(self):
        super(chapter_pr_d,self).__init__()
        self.add3()
    def add3(self):
        global chapter_list
        chapter_list.append('chapter_pr_d')

# 剿灭
class chapter_jm_qc(chapter_jm):
    def __init__(self):
        super(chapter_jm_qc,self).__init__()
        self.add3()
    def add3(self):
        global chapter_list
        chapter_list.append('chapter_jm_qc')
class chapter_jm_wh(chapter_jm):
    def __init__(self):
        super(chapter_jm_wh,self).__init__()
        self.add3()
    def add3(self):
        global chapter_list
        chapter_list.append('chapter_jm_wh')
class chapter_jm_sq(chapter_jm):
    def __init__(self):
        super(chapter_jm_sq,self).__init__()
        self.add3()
    def add3(self):
        global chapter_list
        chapter_list.append('chapter_jm_sq')
        
'''四级目录'''
#主线
class chapter_2_4(chapter_2):
    def __init__(self):
        super(chapter_2_4,self).__init__()
        self.add4()
    def add4(self):
        global chapter_list
        chapter_list.append('chapter_2_4')
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


# 物资
class chapter_wz_ls_5(chapter_wz_ls):
    def __init__(self):
        super(chapter_wz_ls_5,self).__init__()
        self.add4()
    def add4(self):
        global chapter_list
        chapter_list.append('chapter_wz_ls_5')
class chapter_wz_ap_5(chapter_wz_ap):
    def __init__(self):
        super(chapter_wz_ap_5,self).__init__()
        self.add4()
    def add4(self):
        global chapter_list
        chapter_list.append('chapter_wz_ap_5')
class chapter_wz_ce_5(chapter_wz_ce):
    def __init__(self):
        super(chapter_wz_ce_5,self).__init__()
        self.add4()
    def add4(self):
        global chapter_list
        chapter_list.append('chapter_wz_ce_5')
class chapter_wz_ca_3(chapter_wz_ca):
    def __init__(self):
        super(chapter_wz_ca_3,self).__init__()
        self.add4()
    def add4(self):
        global chapter_list
        chapter_list.append('chapter_wz_ca_3')
class chapter_wz_ca_5(chapter_wz_ca):
    def __init__(self):
        super(chapter_wz_ca_5,self).__init__()
        self.add4()
    def add4(self):
        global chapter_list
        chapter_list.append('chapter_wz_ca_5')
class chapter_wz_sk_3(chapter_wz_sk):
    def __init__(self):
        super(chapter_wz_sk_3,self).__init__()
        self.add4()
    def add4(self):
        global chapter_list
        chapter_list.append('chapter_wz_sk_3')
class chapter_wz_sk_5(chapter_wz_sk):
    def __init__(self):
        super(chapter_wz_sk_5,self).__init__()
        self.add4()
    def add4(self):
        global chapter_list
        chapter_list.append('chapter_wz_sk_5')

# 芯片
class chapter_pr_a_1(chapter_pr_a):
    def __init__(self):
        super(chapter_pr_a_1,self).__init__()
        self.add4()
    def add4(self):
        global chapter_list
        chapter_list.append('chapter_pr_1')
class chapter_pr_b_1(chapter_pr_b):
    def __init__(self):
        super(chapter_pr_b_1,self).__init__()
        self.add4()
    def add4(self):
        global chapter_list
        chapter_list.append('chapter_pr_1')
class chapter_pr_c_1(chapter_pr_c):
    def __init__(self):
        super(chapter_pr_c_1,self).__init__()
        self.add4()
    def add4(self):
        global chapter_list
        chapter_list.append('chapter_pr_1')
class chapter_pr_d_1(chapter_pr_d):
    def __init__(self):
        super(chapter_pr_d_1,self).__init__()
        self.add4()
    def add4(self):
        global chapter_list
        chapter_list.append('chapter_pr_1')
class chapter_pr_a_2(chapter_pr_a):
    def __init__(self):
        super(chapter_pr_a_2,self).__init__()
        self.add4()
    def add4(self):
        global chapter_list
        chapter_list.append('chapter_pr_2')
class chapter_pr_b_2(chapter_pr_b):
    def __init__(self):
        super(chapter_pr_b_2,self).__init__()
        self.add4()
    def add4(self):
        global chapter_list
        chapter_list.append('chapter_pr_2')
class chapter_pr_c_2(chapter_pr_c):
    def __init__(self):
        super(chapter_pr_c_2,self).__init__()
        self.add4()
    def add4(self):
        global chapter_list
        chapter_list.append('chapter_pr_2')
class chapter_pr_d_2(chapter_pr_d):
    def __init__(self):
        super(chapter_pr_d_2,self).__init__()
        self.add4()
    def add4(self):
        global chapter_list
        chapter_list.append('chapter_pr_2')