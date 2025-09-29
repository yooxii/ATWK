import typing
from catuo import *
from change_lang import change_language

import pygetwindow as gw
import tkinter as tk
import json
import time
import sys
import os
import logging

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("atwk.log", encoding="utf-8"),
        logging.StreamHandler(),
    ],
)
logger = logging.getLogger(__name__)


def TimeCount(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        logger.info(f"开始执行 {func.__name__}")
        func(*args, **kwargs)
        end_time = time.time()
        total_time = end_time - start_time
        logger.info(
            f"{func.__name__} 执行完成，耗时 {total_time//60:.0f}分{total_time%60:.2f}秒"
        )
        pmb.confirm(
            f"程序运行时间：{total_time//60:.0f}分{total_time%60:.2f}秒",
            "运行时间",
            ["已完成"],
        )

    return wrapper


def load_history():
    try:
        with open("history.json", "r", encoding="utf-8") as f:
            history = json.load(f)
            logger.info("历史配置加载成功")
            return history
    except Exception as e:
        logger.error(f"加载历史配置失败: {e}")
        return {}


def saveHistory(history):
    try:
        with open("history.json", "w", encoding="utf-8") as f:
            json.dump(history, f, ensure_ascii=False, indent=4)
        logger.info("历史配置保存成功")
        return True
    except Exception as e:
        logger.error(f"保存历史配置失败: {e}")
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
        logger.info(f"窗口 '{title}' 已前置")
    except Exception as e:
        error_msg = f"找不到窗口: {title}"
        logger.error(error_msg)
        pmb.alert(error_msg, "错误")
        sys.exit()


class ELEKTRA:
    def __init__(self):
        self.init_pic()
        self.init_var()
        logger.info("ELEKTRA 实例初始化完成")

    def init_pic(self):
        """初始化图片"""
        self.pic_ceshixinxi = ".\\Pic_lib\\CeShiXinXi_closed.png"
        self.pic_classA = ".\\Pic_lib\\ClassA.png"
        self.pic_classB = ".\\Pic_lib\\ClassB.png"
        self.pic_exportcsv = ".\\Pic_lib\\ExportCsv.png"
        self.pic_exportrp = ".\\Pic_lib\\ExportRp.png"
        self.pic_lisn_l = ".\\Pic_lib\\L1.png"
        self.pic_lisn_n = ".\\Pic_lib\\N.png"
        self.pic_ln_l1 = ".\\Pic_lib\\NL_L.png"
        self.pic_ln_n = ".\\Pic_lib\\NL_N.png"
        self.pic_load = ".\\Pic_lib\\Load.png"
        self.pic_model = ".\\Pic_lib\\Model.png"
        self.pic_neirong = ".\\Pic_lib\\NeiRong.png"
        self.pic_peijian = ".\\Pic_lib\\PeijianSheZhi.png"
        self.pic_power = ".\\Pic_lib\\Power.png"
        self.pic_qingchu = ".\\Pic_lib\\QingChu.png"
        self.pic_queren = ".\\Pic_lib\\QueRen1.png"
        self.pic_qujian = ".\\Pic_lib\\QuJian.png"
        self.pic_result_table = ".\\Pic_lib\\ResultTable.png"
        self.pic_run = ".\\Pic_lib\\Run.png"
        self.pic_save_as = ".\\Pic_lib\\SaveAs.png"
        self.pic_saverp = ".\\Pic_lib\\SaveRp.png"
        self.pic_saveTest = ".\\Pic_lib\\SaveTest.png"
        self.pic_sn = ".\\Pic_lib\\SN.png"
        self.pic_wenjianming = ".\\Pic_lib\\WenJianMing.png"
        self.pic_zhongyaodian = ".\\Pic_lib\\ZhongYaodian.png"
        self.pic_zuizhongjieguo = ".\\Pic_lib\\ZuiZhongJieGuo.png"
        self.pic_seven_1 = ".\\Pic_lib\\seven_1.png"
        self.pic_seven_2 = ".\\Pic_lib\\seven_2.png"
        self.pic_six_1 = ".\\Pic_lib\\Six_1.png"
        self.pic_six_2 = ".\\Pic_lib\\Six_2.png"
        self.pic_testpass = ".\\Pic_lib\\TestPass.png"
        logger.debug("图片路径初始化完成")

    def init_var(self):
        """初始化变量"""
        self.var_first: bool = True
        self.stop = False

        self.var_model = ""
        self.var_class = ""
        self.var_sn = []
        self.var_power = []
        self.var_load = []
        self.var_lisn = []
        self.var_exclude = []
        logger.debug("变量初始化完成")

    def inputTestConfig(self, info: dict = None):
        """输入测试配置"""
        if info is None:
            input_method = pmb.confirm(
                title="测试条件顺序",
                buttons=["POWER_LOAD_UUT", "LOAD_POWER_UUT", "POWER_UUT_LOAD"],
            )
            if not input_method:
                logger.warning("未选择测试条件顺序，程序退出")
                pmb.alert("未选择测试条件顺序", "退出")
                sys.exit()
            self.method = input_method

            loaded_history = load_history()
            if input_method in loaded_history:
                self.history = loaded_history[input_method]
            else:
                self.history = {}

            default_model = self.history.get("model", "")
            default_class = self.history.get("class", "")
            default_sn = self.history.get("sn", [])
            default_power = self.history.get("power", [])
            defualt_load = self.history.get("load", [])
            defualt_lisn = self.history.get("lisn", [])
            defualt_exclude = self.history.get("exclude", [""])

            input_model = pmb.prompt(title="机种型号:", default=default_model)
            input_class = (
                pmb.confirm(title="测试标准:", buttons=["Class A", "Class B"])
                or default_class
            )
            input_sn = pmb.prompt(title="SN:", rows=6, default=default_sn)
            input_power = pmb.prompt(title="单体的Vac:", default=default_power)
            input_load = pmb.prompt(title="单体负载:", default=defualt_load)
            input_lisn = pmb.prompt(title="LISN顺序:", default=defualt_lisn)
            input_exclude = pmb.prompt(
                title="排除已测试条件:", rows=6, default="".join(defualt_exclude)
            )
            if None in [
                input_class,
                input_model,
                input_sn,
                input_power,
                input_load,
                input_lisn,
            ]:
                logger.error("输入参数不能为空")
                pmb.alert("输入参数不能为空", "错误")
                sys.exit()
            self.history["class"] = self.var_class = input_class
            self.history["model"] = self.var_model = input_model
            self.history["sn"] = self.var_sn = input_sn.split()
            self.history["power"] = self.var_power = input_power.split(" ")
            self.history["load"] = self.var_load = input_load.split(" ")
            self.history["lisn"] = self.var_lisn = input_lisn.split(" ")
            self.history["exclude"] = self.var_exclude = input_exclude.split()

            loaded_history[input_method] = self.history
            saveHistory(loaded_history)
            logger.info(
                f"测试配置输入完成: 模型={self.var_model}, 标准={self.var_class}"
            )
        else:
            self.save_path = info["save_path"]
            self.var_model = info["model"]
            self.var_class = info["class"]
            self.var_sn = info["sn"].split()
            self.var_power = info["power"]
            self.var_load = [
                l for l in info["load"].split() if l not in ["", "\n", "\t"]
            ]
            self.var_lisn = info["lisn"]
            self.var_exclude = info["excludes"]
            self.method = info["method"]
            self.save_path = os.path.join(self.save_path, self.var_model)
            os.makedirs(self.save_path, exist_ok=True)
            # 如果这个路径下存在任何测试结果文件，则提示用户是否覆盖
            already_result = []
            for root, dirs, files in os.walk(self.save_path):
                for file in files:
                    already_uutsn = file.split("-")[0]
                    if already_uutsn in self.var_sn:
                        already_result.append(file.split(".")[0])
                        logger.warning(f"已存在测试结果文件: {file}")
            if already_result:
                already_result_str = "\n".join(already_result[:6]) + "..."
                overwrite = pmb.confirm(
                    title="已存在测试结果",
                    text=f"已存在测试结果: \n{already_result_str}\n是否覆盖(会删除所有已测试结果)？",
                    buttons=["覆盖", "跳过"],
                )
                if overwrite == "覆盖":
                    for file in os.listdir(self.save_path):
                        if file.split(".")[0] in already_result:
                            os.remove(os.path.join(self.save_path, file))
                            logger.info(f"已删除: {file}")
                else:
                    self.var_exclude += "\n".join(already_result)
                    logger.info("跳过已测试结果")

            logger.info(f"使用传入配置: 模型={self.var_model}, 路径={self.save_path}")

    @TimeCount
    def startTest(self, method=None):
        self.stop = False
        if method is None:
            method = self.method
        logger.info(f"开始执行测试，模式: {method}")
        if method == "POWER_LOAD_UUT":
            self.POWER_LOAD_UUT()
        elif method == "LOAD_POWER_UUT":
            self.LOAD_POWER_UUT()
        elif method == "POWER_UUT_LOAD":
            self.POWER_UUT_LOAD()
        else:
            error_msg = f"未知的测试条件顺序: {method}"
            logger.error(error_msg)
            pmb.alert(error_msg, "错误")

    def setTestConfig(self):
        """设置测试配置"""
        logger.info("开始设置测试配置")
        click_image(self.pic_saveTest)

        if self.var_class == "Class A":
            self.pic_class = self.pic_classA
        else:
            self.pic_class = self.pic_classB

        click_image(self.pic_class, clicks=2)
        click_image(self.pic_peijian, wait_time=0.6)
        click_image(self.pic_ceshixinxi)
        for _ in range(5):
            pg.scroll(-2)

        change_language("EN")
        click_image(self.pic_model, ["left", (600, 0)])

        pg.typewrite(self.var_model)
        logger.info(f"测试配置设置完成: 单体={self.var_model}, 标准={self.var_class}")

    def POWER_LOAD_UUT(self):
        """POWER_LOAD_UUT 测试流程"""
        logger.info("执行 POWER_LOAD_UUT 测试流程")
        foreground()

        powerNoChange = False
        loadNoChange = False
        snNoChange = False
        message = "已切换到 "

        self.setTestConfig()

        for sn in self.var_sn:
            click_image(self.pic_sn, ["left", (600, 0)])
            pg.typewrite(sn)
            message += f"- {sn} "
            logger.info(f"切换到 SN: {sn}")

            for load in self.var_load:
                if self.stop:
                    logger.info("收到停止信号，结束测试")
                    return
                if not loadNoChange:
                    click_image(self.pic_load, ["left", (600, 0)])
                    pg.typewrite(load)
                    self.clickSpace()
                    message += f"- {load} "
                    logger.info(f"切换到 负载: {load}")
                else:
                    loadNoChange = False

                for power in self.var_power:
                    if self.stop:
                        logger.info("收到停止信号，结束测试")
                        return
                    if not powerNoChange:
                        click_image(self.pic_power, ["left", (600, 0)])
                        pg.typewrite(power)
                        self.clickSpace()
                        message += f"- {power} "
                        logger.info(f"切换到 电源: {power}")
                    else:
                        powerNoChange = False

                    self.movetoQueRen()
                    pmb.confirm(
                        message,
                        "确认窗口",
                        ["已确认"],
                    )
                    self.loop_lisn(sn, load, power)
                    message = "已切换到 "
                    if self.stop:
                        return

                self.var_power.reverse()
                powerNoChange = True
            self.var_load.reverse()
            loadNoChange = True

    def POWER_UUT_LOAD(self):
        """POWER_UUT_LOAD 测试流程"""
        logger.info("执行 POWER_UUT_LOAD 测试流程")
        foreground()

        powerNoChange = False
        loadNoChange = False
        snNoChange = False
        message = "已切换到 "

        self.setTestConfig()

        for load in self.var_load:
            click_image(self.pic_load, ["left", (600, 0)])
            pg.typewrite(load)
            self.clickSpace()
            message += f"- {load} "
            logger.info(f"切换到 负载: {load}")

            for sn in self.var_sn:
                if self.stop:
                    logger.info("收到停止信号，结束测试")
                    return
                if not snNoChange:
                    click_image(self.pic_sn, ["left", (600, 0)])
                    pg.typewwrite(sn)
                    self.clickSpace()
                    message += f"- {sn} "
                    logger.info(f"切换到 SN: {sn}")
                else:
                    snNoChange = False

                for power in self.var_power:
                    if self.stop:
                        logger.info("收到停止信号，结束测试")
                        return
                    if not powerNoChange:
                        click_image(self.pic_power, ["left", (600, 0)])
                        pg.typewrite(power)
                        self.clickSpace()
                        message += f"- {power} "
                        logger.info(f"切换到 电源: {power}")
                    else:
                        powerNoChange = False

                    self.movetoQueRen()
                    pmb.confirm(
                        message,
                        "确认窗口",
                        ["已确认"],
                    )
                    self.loop_lisn(sn, load, power)
                    message = "已切换到 "
                    if self.stop:
                        return

                self.var_power.reverse()
                powerNoChange = True
            self.var_sn.reverse()
            snNoChange = True

    def LOAD_POWER_UUT(self):
        """LOAD_POWER_UUT 测试流程"""
        logger.info("执行 LOAD_POWER_UUT 测试流程")
        foreground()

        powerNoChange = False
        loadNoChange = False
        snNoChange = False
        message = "已切换到 "

        self.setTestConfig()
        for sn in self.var_sn:
            click_image(self.pic_sn, ["left", (600, 0)])
            pg.typewrite(sn)
            self.clickSpace()
            message += f"- {sn} "
            logger.info(f"切换到 SN: {sn}")

            for power in self.var_power:
                if self.stop:
                    logger.info("收到停止信号，结束测试")
                    return
                if not powerNoChange:
                    click_image(self.pic_power, ["left", (600, 0)])
                    pg.typewrite(power)
                    self.clickSpace()
                    message += f"- {power} "
                    logger.info(f"切换到 电源: {power}")
                else:
                    powerNoChange = False

                for load in self.var_load:
                    if self.stop:
                        logger.info("收到停止信号，结束测试")
                        return
                    if not loadNoChange:
                        click_image(self.pic_load, ["left", (600, 0)])
                        pg.typewrite(load)
                        self.clickSpace()
                        message += f"- {load} "
                        logger.info(f"切换到 负载: {load}")
                    else:
                        loadNoChange = False

                    self.movetoQueRen()
                    pmb.confirm(
                        message,
                        "确认窗口",
                        ["已确认"],
                    )
                    self.loop_lisn(sn, load, power)
                    message = "已切换到 "
                    if self.stop:
                        return

                self.var_load.reverse()
                loadNoChange = True

            self.var_power.reverse()
            powerNoChange = True

    def loop_lisn(self, sn, load, power):
        """LISN循环"""
        for lisn in self.var_lisn:
            logger.info(f"LISN循环开始: {sn}-{power}-{load}-{lisn}")
            if self.stop:
                logger.info("收到停止信号，结束LISN循环")
                return
            self.testItem = f"{sn}-{power}-{load}-{lisn}"
            if self.testItem in self.var_exclude:
                logger.warning(f"{self.testItem} 已测试过，跳过")
                pmb.alert(
                    f"{self.testItem} 已测试过，跳过",
                    "测试提示",
                    timeout=ALERT_TIMEOUT,
                )
                continue

            foreground()
            if (lisn == "L" and not exists_image(self.pic_ln_l1, confidence=0.93)) or (
                lisn == "N" and not exists_image(self.pic_ln_n, confidence=0.93)
            ):
                click_image(self.pic_lisn_n, wait_time=0.3)
                click_image(self.pic_lisn_l, wait_time=0.1)
                lisn_changed = True
            else:
                lisn_changed = False

            if lisn_changed:
                self.movetoQueRen()
                pmb.confirm("请切换到" + lisn, "确认窗口", ["已确认"])

            if self.stop:
                return
            self.selectPoint(lisn_changed)
            if self.stop:
                return
            self.saveReport()

        self.var_lisn.reverse()
        logger.info("LISN循环完成")

    def selectPoint(self, lisn_changed):
        """选择测试点"""
        import utils

        logger.info(f"开始选择测试点, LISN变化: {lisn_changed}")
        click_image(self.pic_zhongyaodian, clicks=2)
        flag_testpass = False

        while True:
            if self.stop:
                logger.info("收到停止信号，结束选择测试点")
                return
            isPass = True
            if not flag_testpass:
                try:
                    click_image(self.pic_run)
                    if lisn_changed:
                        click_image(self.pic_qingchu)
                    click_image(self.pic_queren)
                    click_image(self.pic_queren)
                    if self.var_first:
                        click_image(self.pic_queren)
                except:
                    isPass = False

                # pg.sleep(1)
                # self.saveExportcsv()
                # pg.sleep(0.5)

                # isPass = utils.checkTestPass(self.save_path)
                if not isPass:
                    click_image(self.pic_zuizhongjieguo, clicks=2)
                    click_image(self.pic_qujian, ["left", (-10, 35)], clicks=1)
                    pg.keyDown("ctrl")
                    pg.press("a")
                    pg.keyUp("ctrl")
                    pg.press("del")
                    click_image(self.pic_zhongyaodian, clicks=2)
                    click_image(self.pic_qujian, ["left", (-10, 35)], clicks=1)
                    pg.keyDown("ctrl")
                    pg.press("a")
                    pg.keyUp("ctrl")
                    pg.press("del")

                click_image(self.pic_result_table, ["bottom", (0, 9)], clicks=2)
                self.saveOverview()
                click_image(self.pic_zhongyaodian, clicks=2)
                freq = utils.findmin(self.save_path, 0.2)
                click_image(self.pic_qujian, ["bottom", (80, 20)])
                pg.typewrite(freq)
                flag_testpass = True

            PT_OK = pmb.confirm(
                "选择此次测试结果？",
                position="+1200+500",
                topmost=True,
                title="测试完成确认",
                buttons=["是", "重试"],
            )

            if PT_OK == "重试":
                flag_testpass = False
                logger.info("用户选择重试")
                continue
            elif PT_OK == "是":
                flag_testpass = True
                logger.info("用户确认测试结果")

            if self.stop:
                return
            point_region = (300, 500, 700, 1000)
            minTime = 0.2
            foreground()
            if exists_image(self.pic_seven_1, minTime, point_region) or exists_image(
                self.pic_seven_2, minTime, point_region
            ):
                logger.warning("重要点选取过多")
                pmb.alert(
                    "请最多选取六个重要点",
                    "重要点选取过多",
                    timeout=ALERT_TIMEOUT,
                )
                continue
            if exists_image(self.pic_six_1, minTime, point_region) or exists_image(
                self.pic_six_2, minTime, point_region
            ):
                utils.delete_csv(self.save_path)
                logger.info(f"删除临时测试数据完成")
                break
            else:
                logger.warning("重要点选取过少")
                pmb.alert(
                    "请选择六个重要点",
                    "重要点选取过少",
                    timeout=ALERT_TIMEOUT,
                )
        logger.info("测试点选择完成")

    def saveReport(self):
        """保存报告"""
        logger.info("开始保存报告")
        click_image(self.pic_saveTest)
        click_image(self.pic_saverp)
        click_image(self.pic_exportrp, ["left", (10, 0)], timeout=10)
        click_image(self.pic_exportrp, ["right", (-10, 0)])
        foreground()
        change_language("EN")
        if self.var_first:
            click_image(self.pic_save_as, ["top", (70, -36)])
            pg.typewrite(str(self.save_path).replace("*", ""))
            pg.press("enter")
            self.var_first = False
        click_image(self.pic_wenjianming, ["right", (100, 0)])
        pg.keyDown("ctrl")
        pg.press("a")
        pg.keyUp("ctrl")
        pg.typewrite(str(self.testItem).replace("*", ""))
        pg.press("enter")
        click_image(self.pic_class)
        pg.click(clicks=2)
        logger.info(f"报告保存完成: {self.testItem}")

    def movetoQueRen(self):
        """移动鼠标到信息窗口的确认按钮位置。"""
        pg.moveTo(520, 290)
        logger.debug("鼠标移动到确认按钮位置")

    def clickSpace(self):
        """移动鼠标到信息窗口的空白位置。"""
        pg.click(1520, 800)
        logger.debug("点击空白区域")

    def saveOverview(self):
        """保存概览数据"""
        logger.info("开始保存概览数据")
        foreground()
        click_image(self.pic_result_table, ["bottom", (0, 9)], clicks=2)
        click_image(self.pic_exportcsv, ["top", (-20, -25)])
        if self.var_first:
            change_language("EN")
            click_image(self.pic_save_as, ["top", (70, -36)])
            pg.typewrite(self.save_path)
            pg.press("enter")
            click_image(self.pic_wenjianming, ["right", (100, 0)])
            self.var_first = False
        pg.sleep(0.5)
        pg.press("enter")
        pg.press("enter")
        logger.info("概览数据保存完成")

    def saveExportcsv(self):
        """保存导出CSV"""
        logger.info("开始保存导出CSV")
        foreground()
        click_image(self.pic_exportcsv, ["top", (55, -25)])
        if self.var_first:
            change_language("EN")
            click_image(self.pic_save_as, ["top", (70, -36)])
            pg.typewrite(self.save_path)
            pg.press("enter")
            click_image(self.pic_wenjianming, ["right", (100, 0)], confidence=0.9)
            self.var_first = False
        pg.sleep(0.5)
        pg.press("enter")
        pg.press("enter")
        logger.info("导出CSV保存完成")


def main():
    logger.info("程序启动")
    ato = ELEKTRA()
    # ato.input_testConfig()
    ato.clickSpace()
    logger.info("程序执行结束")


if __name__ == "__main__":
    main()
