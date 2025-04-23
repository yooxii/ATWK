from catuo import *
from change_lang import change_language

import pygetwindow as gw
import json

def load_history():
    try:
        with open('history.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except:
        return {}
    
def save_history(history):
    try:
        with open('history.json', 'w', encoding='utf-8') as f:
            json.dump(history, f, ensure_ascii=False, indent=4)
        return True
    except:
        return False

def foreground(title = "ELEKTRA "):
    try:
        window = gw.getWindowsWithTitle(title)[0]
        window.activate()
        window.maximize()
    except:
        pmb.alert("找不到ELEKTRA窗口", "错误")
        sys.exit()

class ELEKTRA:
    def __init__(self):
        self.init_pic()
        self.init_var()
        
    def init_pic(self):
        self.pic_saveTest = ".\\Pic_lib\\SaveTest.png"
        self.pic_classA = ".\\Pic_lib\\ClassA.png"
        self.pic_classB = ".\\Pic_lib\\ClassB.png"
        self.pic_peijian = ".\\Pic_lib\\PeijianSheZhi.png"
        self.pic_ceshixinxi = ".\\Pic_lib\\CeShiXinXi_closed.png"
        self.pic_neirong = ".\\Pic_lib\\NeiRong.png"
        self.pic_model = ".\\Pic_lib\\Model.png"
        self.pic_sn = ".\\Pic_lib\\SN.png"
        self.pic_power = ".\\Pic_lib\\Power.png"
        self.pic_load = ".\\Pic_lib\\Load.png"
        self.pic_run = ".\\Pic_lib\\Run.png"
        self.pic_ln_l1 = ".\\Pic_lib\\NL_L.png"
        self.pic_ln_n = ".\\Pic_lib\\NL_N.png"
        self.pic_lisn_l = ".\\Pic_lib\\L1.png"
        self.pic_lisn_n = ".\\Pic_lib\\N.png"
        self.pic_zhongyaodian = ".\\Pic_lib\\ZhongYaodian.png"
        self.pic_qingchu = ".\\Pic_lib\\QingChu.png"
        self.pic_queren = ".\\Pic_lib\\QueRen1.png"
        self.pic_qujian = ".\\Pic_lib\\QuJian.png"
        self.pic_saverp = ".\\Pic_lib\\SaveRp.png"
        self.pic_wenjianming = ".\\Pic_lib\\WenJianMing.png"
        self.six_1 = ".\\Pic_lib\\Six_1.png"
        self.six_2 = ".\\Pic_lib\\Six_2.png"
        self.seven_1 = ".\\Pic_lib\\seven_1.png"
        self.seven_2 = ".\\Pic_lib\\seven_2.png"
        self.pic_exportrp = ".\\Pic_lib\\ExportRp.png"
        
    def init_var(self):
        self.var_first = True
        
        self.history = load_history()
        
        self.var_model:str = self.history.get('model', '')
        self.var_class:str = self.history.get('class', '')
        self.var_sn:list = self.history.get('sn', [])
        self.var_power:list = self.history.get('power', [])
        self.var_load:list = self.history.get('load', [])
        self.var_lisn:list = self.history.get('lisn', [])
        self.var_exclude:list = self.history.get('exclude', [''])

    def input_testConfig(self):
        input_method = pmb.confirm(title="测试条件顺序", buttons=["SN-LOAD-POWER", "LOAD-SN-POWER", "POWER-SN-LOAD"])
        
        input_model = pmb.prompt(title="机种型号:", default=self.var_model)
        input_class = pmb.confirm(title="测试标准:", buttons=["Class A", "Class B"])
        input_sn = pmb.prompt(title="SN:",rows=len(self.var_sn), default=self.var_sn)
        input_power = pmb.prompt(title="单体的Vac:", default=self.var_power)
        input_load = pmb.prompt(title="单体负载:", default=self.var_load)
        input_lisn = pmb.prompt(title="LISN顺序:", default=self.var_lisn)
        input_exclude = pmb.prompt(title="排除已测试条件:",rows=4, default=''.join(self.var_exclude))
        
        self.history['model'] = self.var_model = input_model
        self.history['class'] = self.var_class = input_class
        self.history['sn'] = self.var_sn = input_sn.split()
        self.history['power'] = self.var_power = input_power.split(' ')
        self.history['load'] = self.var_load = input_load.split(' ')
        self.history['lisn'] = self.var_lisn = input_lisn.split(' ')
        self.history['exclude'] = self.var_exclude = input_exclude.split()
        save_history(self.history)
        
        if input_method == "SN-LOAD-POWER":
            self.SN_LOAD_POWER()
        elif input_method == "LOAD-SN-POWER":
            self.LOAD_SN_POWER()
        elif input_method == "POWER-SN-LOAD":
            self.POWER_SN_LOAD()
        else:
            pmb.alert("未知的测试条件顺序", "错误")

    def set_testConfig(self):
        if self.var_class == "Class A":
            self.pic_class = self.pic_classA
        else:
            self.pic_class = self.pic_classB
        moveTo_image(self.pic_class)
        pg.click(clicks=2)
        
        moveTo_image(self.pic_saveTest)
        pg.click()
        
        moveTo_image(self.pic_peijian,wait_time=0.6)
        pg.click()
        
        moveTo_image(self.pic_ceshixinxi)
        pg.click()
        
        moveTo_image(self.pic_neirong)
        pg.scroll(-2)
        pg.scroll(-2)
        pg.scroll(-2)
        
        change_language("EN")
        moveTo_image(self.pic_model, ['left', (600,0)])
        pg.click()
        pg.typewrite(self.var_model)
        
    def SN_LOAD_POWER(self):
        """
        """
        foreground()
        
        powerNoChange = False
        loadNoChange = False
        snNoChange = False
        
        # return
        self.set_testConfig()
        
        for sn in self.var_sn:
            moveTo_image(self.pic_sn, ['left', (600,0)])
            pg.click()
            pg.typewrite(sn)
            self.movetoQueRen()
            pmb.confirm("确认已切换到"+sn, "确认窗口",["已确认"])
            
            for load in self.var_load:
                if not loadNoChange:
                    moveTo_image(self.pic_load, ['left', (600,0)])
                    pg.click()
                    pg.typewrite(load)
                    self.movetoQueRen()
                    pmb.confirm("确认已切换到"+load, "确认窗口",["已确认"])
                else:
                    loadNoChange = False
            
                for power in self.var_power:
                    if not powerNoChange:
                        moveTo_image(self.pic_power, ['left', (600,0)])
                        pg.click()
                        pg.typewrite(power)
                        self.movetoQueRen()
                        pmb.confirm("确认已切换到"+power, "确认窗口",["已确认"])
                    else:
                        powerNoChange = False
                    
                    self.loop_lisn(sn, load, power)
                    
                self.var_power.reverse()
                powerNoChange = True
            self.var_load.reverse()
            loadNoChange = True

    def LOAD_SN_POWER(self):
        """
        """
        foreground()
        
        powerNoChange = False
        loadNoChange = False
        snNoChange = False
        
        # return
        self.set_testConfig()
        
        for load in self.var_load:
            moveTo_image(self.pic_load, ['left', (600,0)])
            pg.click()
            pg.typewrite(load)
            self.movetoQueRen()
            pmb.confirm("确认已切换到"+load, "确认窗口",["已确认"])
            
                
            for sn in self.var_sn:
                if not snNoChange:
                    moveTo_image(self.pic_sn, ['left', (600,0)])
                    pg.click()
                    pg.typewrite(sn)
                    self.movetoQueRen()
                    pmb.confirm("确认已切换到"+sn, "确认窗口",["已确认"])
                else:
                    snNoChange = False
                    
                for power in self.var_power:
                    if not powerNoChange:
                        moveTo_image(self.pic_power, ['left', (600,0)])
                        pg.click()
                        pg.typewrite(power)
                        self.movetoQueRen()
                        pmb.confirm("确认已切换到"+power, "确认窗口",["已确认"])
                    else:
                        powerNoChange = False
                    
                    self.loop_lisn(sn, load, power)
                
                self.var_power.reverse()
                powerNoChange = True
            self.var_sn.reverse()
            snNoChange = True

    def POWER_SN_LOAD(self):
        """
        """
        foreground()
        
        powerNoChange = False
        loadNoChange = False
        snNoChange = False
        
        # return
        self.set_testConfig()
        
        for power in self.var_power:
            moveTo_image(self.pic_power, ['left', (600,0)])
            pg.click()
            pg.typewrite(power)
            self.movetoQueRen()
            pmb.confirm("确认已切换到"+power, "确认窗口",["已确认"])
            
                
            for sn in self.var_sn:
                if not snNoChange:
                    moveTo_image(self.pic_sn, ['left', (600,0)])
                    pg.click()
                    pg.typewrite(sn)
                    self.movetoQueRen()
                    pmb.confirm("确认已切换到"+sn, "确认窗口",["已确认"])
                else:
                    snNoChange = False
                    
                for load in self.var_load:
                    if not loadNoChange:
                        moveTo_image(self.pic_load, ['left', (600,0)])
                        pg.click()
                        pg.typewrite(load)
                        self.movetoQueRen()
                        pmb.confirm("确认已切换到"+load, "确认窗口",["已确认"])
                    else:
                        loadNoChange = False
                    
                    self.loop_lisn(sn, load, load)
                
                self.var_load.reverse()
                loadNoChange = True
            self.var_sn.reverse()
            snNoChange = True

    def loop_lisn(self, sn, load, power):
        for lisn in self.var_lisn:
            self.testItem = f"{sn}-{power}-{load}-{lisn}"
            if self.testItem in self.var_exclude:
                pmb.alert(f"{sn}-{power}-{load}-{lisn} 已测试过，跳过","测试提示",timeout=ALERT_TIMEOUT)
                continue

            foreground()
            minTime = 0.2
            if lisn == "L" and exists_image(self.pic_ln_n,minTime) or lisn == "N" and exists_image(self.pic_ln_l1,minTime):
                moveTo_image(self.pic_lisn_n,wait_time=0.3)
                pg.click()
                moveTo_image(self.pic_lisn_l,wait_time=0.1)
                pg.click()
                lisn_changed = True
            else:
                lisn_changed = False
                        
            if lisn_changed:
                self.movetoQueRen()
                pmb.confirm("请切换到"+lisn, "确认窗口",["已确认"])
                        
            self.selectPoint(lisn_changed)
            self.saveReport()
                        
        self.var_lisn.reverse()

    def selectPoint(self, lisn_changed):
        moveTo_image(self.pic_zhongyaodian)
        pg.click(clicks=2)
        
        moveTo_image(self.pic_run)
        pg.click()

        if lisn_changed:
            moveTo_image(self.pic_qingchu)
            pg.click()
        moveTo_image(self.pic_queren)
        pg.click()
                        
        moveTo_image(self.pic_queren)
        pg.click()

        #TODO: 图像拽取
        while True:
            PT_OK = pmb.confirm("重要点选择完成？",topmost=True,title="重要点选取",buttons=["是", "否"])
            if PT_OK == "是":
                point_region = (300,500,700,1000)
                minTime = 0.2
                foreground()
                if exists_image(self.seven_1, minTime, point_region) or exists_image(self.seven_2, minTime, point_region):
                    pmb.alert("请最多选取六个重要点","重要点选取过多",timeout=ALERT_TIMEOUT)
                    continue
                if exists_image(self.six_1,minTime,point_region) or exists_image(self.six_2,minTime,point_region):
                    break
                else:
                    pmb.alert("请选择六个重要点","重要点选取过少",timeout=ALERT_TIMEOUT)
                        
        moveTo_image(self.pic_qujian, ["bottom", (0, 20)])
        pg.click()
        pg.typewrite("1\n2\n3\n4\n5\n6\n")
            
        moveTo_image(self.pic_saverp)
        pg.click()
                        
        moveTo_image(self.pic_exportrp,["left", (10,0)],timeout=10)
        pg.click()
                        
        moveTo_image(self.pic_exportrp,["right", (-10,0)])
        pg.click()
        
    def saveReport(self):
        if self.var_first:
            self.var_first= False
            pmb.confirm("请选择保存位置","选择位置",["已完成"])
        foreground()
        moveTo_image(self.pic_wenjianming,["right",(100,0)])
        pg.click()
        pg.keyDown('ctrl')
        pg.press('a')
        pg.keyUp('ctrl')
        pg.typewrite(self.testItem)
        pg.press('enter')
                            
        moveTo_image(self.pic_class)
        pg.click(clicks=2)
                        
        moveTo_image(self.pic_saveTest)
        pg.click()

    def movetoQueRen(self):
        pg.moveTo(520,290)
        

if __name__ == '__main__':
    ato = ELEKTRA()
    ato.input_testConfig()