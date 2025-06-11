from catuo import *
from change_lang import change_language

import pygetwindow as gw
import json
import time
import sys


def load_history():
    try:
        with open("history.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return {}


def save_history(history):
    try:
        with open("history.json", "w", encoding="utf-8") as f:
            json.dump(history, f, ensure_ascii=False, indent=4)
        return True
    except:
        return False


def foreground(title="ELEKTRA "):
    """将窗口前置。

    Args:
        title (str, optional): 窗口标题. 默认值: "ELEKTRA ".
    """
    try:
        window = gw.getWindowsWithTitle(title)[0]
        window.activate()
        window.maximize()
    except:
        pmb.alert(f"找不到窗口:{title}", "错误")
        sys.exit()


class ELEKTRA:
    def __init__(self):
        self.init_pic()
        self.init_var()

    def init_pic(self):
        """初始化图片"""
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
        """初始化变量"""
        self.var_first: bool = True

        self.var_model: str = None
        self.var_class: str = None
        self.var_sn: list = None
        self.var_power: list = None
        self.var_load: list = None
        self.var_lisn: list = None
        self.var_exclude: list = None

    def input_testConfig(self):
        """输入测试配置"""
        input_method = pmb.confirm(
            title="测试条件顺序",
            buttons=["SN_LOAD_POWER", "LOAD_SN_POWER", "SN_POWER_LOAD"],
        )
        if not input_method:
            pmb.alert("未选择测试条件顺序", "退出")
            sys.exit()

        loaded_history = load_history()
        if input_method in loaded_history:
            self.history = loaded_history[input_method]
        else:
            self.history = {}

        default_model: str = self.history.get("model", "")
        default_class: str = self.history.get("class", "")
        default_sn: list = self.history.get("sn", [])
        default_power: list = self.history.get("power", [])
        defualt_load: list = self.history.get("load", [])
        defualt_lisn: list = self.history.get("lisn", [])
        defualt_exclude: list = self.history.get("exclude", [""])

        input_class = (
            pmb.confirm(title="测试标准:", buttons=["Class A", "Class B"])
            or default_class
        )
        input_model = pmb.prompt(title="机种型号:", default=default_model)
        input_sn = pmb.prompt(title="SN:", rows=6, default=default_sn)
        input_power = pmb.prompt(title="单体的Vac:", default=default_power)
        input_load = pmb.prompt(title="单体负载:", default=defualt_load)
        input_lisn = pmb.prompt(title="LISN顺序:", default=defualt_lisn)
        input_exclude = pmb.prompt(
            title="排除已测试条件:", rows=6, default="".join(defualt_exclude)
        )

        self.history["class"] = self.var_class = input_class
        self.history["model"] = self.var_model = input_model
        self.history["sn"] = self.var_sn = input_sn.split()
        self.history["power"] = self.var_power = input_power.split(" ")
        self.history["load"] = self.var_load = input_load.split(" ")
        self.history["lisn"] = self.var_lisn = input_lisn.split(" ")
        self.history["exclude"] = self.var_exclude = input_exclude.split()

        loaded_history[input_method] = self.history
        save_history(loaded_history)

        if input_method == "SN_LOAD_POWER":
            self.SN_LOAD_POWER()
        elif input_method == "LOAD_SN_POWER":
            self.LOAD_SN_POWER()
        elif input_method == "SN_POWER_LOAD":
            self.SN_POWER_LOAD()
        else:
            pmb.alert("未知的测试条件顺序", "错误")

    def set_testConfig(self):
        """设置测试配置"""
        click_image(self.pic_saveTest)

        if self.var_class == "Class A":
            self.pic_class = self.pic_classA
        else:
            self.pic_class = self.pic_classB

        click_image(self.pic_class, clicks=2)
        click_image(self.pic_peijian, wait_time=0.6)
        click_image(self.pic_ceshixinxi)
        pg.scroll(-2)
        pg.scroll(-2)
        pg.scroll(-2)

        change_language("EN")
        click_image(self.pic_model, ["left", (600, 0)])

        pg.typewrite(self.var_model)

    def SN_LOAD_POWER(self):
        """ """
        foreground()

        powerNoChange = False
        loadNoChange = False
        snNoChange = False

        # return
        self.set_testConfig()

        for sn in self.var_sn:
            click_image(self.pic_sn, ["left", (600, 0)])

            pg.typewrite(sn)
            self.movetoQueRen()
            pmb.confirm("确认已切换到" + sn, "确认窗口", ["已确认"])

            for load in self.var_load:
                if not loadNoChange:
                    click_image(self.pic_load, ["left", (600, 0)])

                    pg.typewrite(load)
                    self.movetoQueRen()
                    pmb.confirm("确认已切换到" + load, "确认窗口", ["已确认"])
                else:
                    loadNoChange = False

                for power in self.var_power:
                    if not powerNoChange:
                        click_image(self.pic_power, ["left", (600, 0)])
                        pg.typewrite(power)
                        self.movetoQueRen()
                        pmb.confirm("确认已切换到" + power, "确认窗口", ["已确认"])
                    else:
                        powerNoChange = False
                    self.loop_lisn(sn, load, power)

                self.var_power.reverse()
                powerNoChange = True
            self.var_load.reverse()
            loadNoChange = True

    def LOAD_SN_POWER(self):
        """ """
        foreground()

        powerNoChange = False
        loadNoChange = False
        snNoChange = False

        # return
        self.set_testConfig()

        for load in self.var_load:
            click_image(self.pic_load, ["left", (600, 0)])
            pg.typewrite(load)
            self.movetoQueRen()
            pmb.confirm("确认已切换到" + load, "确认窗口", ["已确认"])

            for sn in self.var_sn:
                if not snNoChange:
                    click_image(self.pic_sn, ["left", (600, 0)])
                    pg.typewrite(sn)
                    self.movetoQueRen()
                    pmb.confirm("确认已切换到" + sn, "确认窗口", ["已确认"])
                else:
                    snNoChange = False

                for power in self.var_power:
                    if not powerNoChange:
                        click_image(self.pic_power, ["left", (600, 0)])
                        pg.typewrite(power)
                        self.movetoQueRen()
                        pmb.confirm("确认已切换到" + power, "确认窗口", ["已确认"])
                    else:
                        powerNoChange = False

                    self.loop_lisn(sn, load, power)

                self.var_power.reverse()
                powerNoChange = True
            self.var_sn.reverse()
            snNoChange = True

    def SN_POWER_LOAD(self):
        foreground()

        powerNoChange = False
        loadNoChange = False
        snNoChange = False

        # return
        self.set_testConfig()
        for sn in self.var_sn:
            click_image(self.pic_sn, ["left", (600, 0)])
            pg.typewrite(sn)
            self.movetoQueRen()
            pmb.confirm("确认已切换到" + sn, "确认窗口", ["已确认"])

            for power in self.var_power:
                if not powerNoChange:
                    click_image(self.pic_power, ["left", (600, 0)])
                    pg.typewrite(power)
                    self.movetoQueRen()
                    pmb.confirm("确认已切换到" + power, "确认窗口", ["已确认"])
                else:
                    powerNoChange = False

                for load in self.var_load:
                    if not loadNoChange:
                        click_image(self.pic_load, ["left", (600, 0)])
                        pg.typewrite(load)
                        self.movetoQueRen()
                        pmb.confirm("确认已切换到" + load, "确认窗口", ["已确认"])
                    else:
                        loadNoChange = False

                    self.loop_lisn(sn, load, power)

                self.var_load.reverse()
                loadNoChange = True
            self.var_power.reverse()
            powerNoChange = True

    def loop_lisn(self, sn, load, power):
        """LISN循环"""
        for lisn in self.var_lisn:
            self.testItem = f"{sn}-{power}-{load}-{lisn}"
            if self.testItem in self.var_exclude:
                pmb.alert(
                    f"{self.testItem} 已测试过，跳过", "测试提示", timeout=ALERT_TIMEOUT
                )
                continue

            foreground()
            minTime = 0.2
            if (
                lisn == "L"
                and exists_image(self.pic_ln_n, minTime)
                or lisn == "N"
                and exists_image(self.pic_ln_l1, minTime)
            ):
                click_image(self.pic_lisn_n, wait_time=0.3)
                click_image(self.pic_lisn_l, wait_time=0.1)
                lisn_changed = True
            else:
                lisn_changed = False

            if lisn_changed:
                self.movetoQueRen()
                pmb.confirm("请切换到" + lisn, "确认窗口", ["已确认"])

            self.selectPoint(lisn_changed)
            self.saveReport()

        self.var_lisn.reverse()

    def selectPoint(self, lisn_changed):
        """选择测试点"""
        click_image(self.pic_zhongyaodian, clicks=2)
        click_image(self.pic_run)

        if lisn_changed:
            click_image(self.pic_qingchu)

        click_image(self.pic_queren)
        click_image(self.pic_queren)

        # TODO: 图像拽取
        while True:
            PT_OK = pmb.confirm(
                "重要点选择完成？",
                position="+1200+500",
                topmost=True,
                title="重要点选取",
                buttons=["是", "否"],
            )
            if PT_OK == "是":
                point_region = (300, 500, 700, 1000)
                minTime = 0.2
                foreground()
                if exists_image(self.seven_1, minTime, point_region) or exists_image(
                    self.seven_2, minTime, point_region
                ):
                    pmb.alert(
                        "请最多选取六个重要点", "重要点选取过多", timeout=ALERT_TIMEOUT
                    )
                    continue
                if exists_image(self.six_1, minTime, point_region) or exists_image(
                    self.six_2, minTime, point_region
                ):
                    break
                else:
                    pmb.alert(
                        "请选择六个重要点", "重要点选取过少", timeout=ALERT_TIMEOUT
                    )

        click_image(self.pic_qujian, ["bottom", (0, 20)])
        pg.typewrite("1\n2\n3\n4\n5\n6\n")

    def saveReport(self):
        """保存报告"""
        click_image(self.pic_saveTest)
        click_image(self.pic_saverp)
        click_image(self.pic_exportrp, ["left", (10, 0)], timeout=10)
        click_image(self.pic_exportrp, ["right", (-10, 0)])

        if self.var_first:
            self.var_first = False
            pmb.confirm("请选择保存位置", "选择位置", ["已完成"])
        foreground()
        change_language("EN")
        click_image(self.pic_wenjianming, ["right", (100, 0)])

        pg.keyDown("ctrl")
        pg.press("a")
        pg.keyUp("ctrl")
        pg.typewrite(self.testItem)
        pg.press("enter")

        click_image(self.pic_class)
        pg.click(clicks=2)

    def movetoQueRen(self):
        """移动鼠标到信息窗口的确认按钮位置。"""
        pg.moveTo(520, 290)


def TimeCount(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        end_time = time.time()
        print(f"程序运行时间：{end_time - start_time:.2f}秒")

    return wrapper


@TimeCount
def main():
    ato = ELEKTRA()
    ato.input_testConfig()


if __name__ == "__main__":
    main()
