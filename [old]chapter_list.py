'chapter_list_module'

__author__ = 'DSKaowu'

screen_now = ()


def chapter_1():
    pass
def chapter_2():
    pass
def chapter_3():
    pass
def chapter_4():
    pass
def chapter_5():
    pass
def chapter_zx(x):
    selet_chapter_zx = {'':'chapter_zx', '1':'chapter_1', '2':'chapter_2', '3':'chapter_3', '4':'chapter_4', '5':'chapter_5'}
    global screen_now
    screen_now=selet_chapter_zx['']
    return selet_chapter_zx[x]
def chapter_wz_yx():
    pass
def chapter_wz_hp():
    pass
def chapter_wz_t():
    pass
def chapter_wz_lmb():
    pass
def chapter_wz_book():
    pass
def chapter_wz(x):
    selet_chapter_wz = {'':'chapter_wz', '1':'chapter_wz_yx', '2':'chapter_wz_hp', '3':'chapter_wz_t', '4':'chapter_wz_lmb', '5':'chapter_wz_book'}
    global screen_now
    screen_now=selet_chapter_wz['']
    return selet_chapter_wz[x]

def chapter_xp_ssjj():
    pass
def chapter_xp_fzxf():
    pass
def chapter_xp_tzjw():
    pass
def chapter_xp_ylzz():
    pass

def chapter_xp(x):
    selet_chapter_xp = {'':'chapter_xp', '1':'chapter_xp_ssjj', '2':'chapter_xp_fzxf', '3':'chapter_xp_tzjw', '4':'chapter_xp_ylzz'}
    global screen_now
    screen_now=selet_chapter_xp['']
    return selet_chapter_xp[x]

def chapter_jm_qc():
    pass
def chapter_jm_wh():
    pass
def chapter_jm_sq():
    pass

def chapter_jm(x):
    selet_chapter_jm = {'':'chapter_jm', '1':'chapter_jm_qc', '2':'chapter_jm_wh', '3':'chapter_jm_sq'}
    global screen_now
    screen_now=selet_chapter_jm['']
    return selet_chapter_jm[x]
'''
def of_6(x):

    return 'end'

def of_7(x):

    return 'end'

def of_8(x):

    return 'end'

def special_chapter_stage_1(x):
    selet_special_chapter_stage_1 = {'6':'of_6' ,'7':'of_7' ,'8':'of_8'}
    return selet_special_chapter_stage_1[x]

def of_f3(x):
    return 'end'

def of_f4(x):

    return 'end'

def special_chapter_stage_2(x):
    selet_special_chapter_stage_2 = {'3':'of_f3' ,'4':'of_f4'}
    return selet_special_chapter_stage_2[x]

def special_chapter(x):
    selet_special_chapter = {'':'special_chapter', '1':'special_chapter_stage_1', '2':'special_chapter_stage_2'}

    global screen_now
    screen_now=selet_special_chapter['']

    return selet_special_chapter[x]
'''
def chapter_start(x) :
    selet_chapter_start = {'':'chapter_start', '1':'chapter_zx' , '2':'chapter_wz' , '3':'chapter_xp' , '4':'chapter_jm' ,'5': 'special_chapter' }
    global screen_now
    screen_now=selet_chapter_start['']
    return selet_chapter_start[x]#selet_chapter_start.get(x, 'end')()

