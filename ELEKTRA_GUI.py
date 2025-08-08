from ELEKTRA_autoTest import *
from ui_GUI import *

from PySide6.QtWidgets import QFileDialog

import json


class ELEKTRA_GUI(QDialog, Ui_Dialog):
    history_files = []

    def __init__(self, parent=None):
        super().__init__()
        self.setupUi(self)
        self.loadHistoryModel()
        self.model_name.addItems(self.history_files)
        self.loadConfig()
        self.ato = ELEKTRA()

        self.model_name.editTextChanged.connect(self.modelUpdate)
        self.btn_start.clicked.connect(self.startTest)
        self.btnSavepath.clicked.connect(self.selectSavePath)

    def selectSavePath(self):
        save_path = QFileDialog.getExistingDirectory(self, "Select Save Path")
        if save_path:
            self.pathEdit.setText(save_path)

    def modelUpdate(self):
        self.loadConfig()

    def loadHistoryModel(self):
        if not os.path.exists("history"):
            return
        self.history_files = [
            f.split(".")[0] for f in os.listdir("history") if f.endswith(".json")
        ]

    def saveConfig(self):
        power = []
        lisn = []
        if self.power_110V.isChecked():
            power.append("110V")
        if self.power_220V.isChecked():
            power.append("220V")
        if self.lisn_l.isChecked():
            lisn.append("L")
        if self.lisn_n.isChecked():
            lisn.append("N")
        config = {
            "save_path": self.pathEdit.text(),
            "model": self.model_name.currentText(),
            "class": self.classbtns.checkedButton().text(),
            "method": self.methodbtns.checkedButton().objectName().upper(),
            "power": power,
            "lisn": lisn,
            "sn": self.sn.toPlainText(),
            "load": self.load.text(),
            "excludes": self.exclude_items.toPlainText(),
        }
        if not os.path.exists("history"):
            os.mkdir("history")
        with open(f"history/{self.model_name.currentText()}.json", "w") as f:
            json.dump(config, f, indent=4)
        return config

    def loadConfig(self):
        if not os.path.exists("history"):
            return
        config_path = f"history/{self.model_name.currentText()}.json"
        if os.path.exists(config_path):
            with open(config_path, "r") as f:
                config = json.load(f)

                if config.get("class", "Class A") == "Class A":
                    self.class_a.setChecked(True)
                else:
                    self.class_b.setChecked(True)

                if config.get("method", "POWER_LOAD_UUT") == "POWER_LOAD_UUT":
                    self.power_load_uut.setChecked(True)
                elif config.get("method", "POWER_LOAD_UUT") == "LOAD_POWER_UUT":
                    self.load_power_uut.setChecked(True)
                elif config.get("method", "POWER_LOAD_UUT") == "POWER_UUT_LOAD":
                    self.power_uut_load.setChecked(True)

                if "110V" not in config.get("power", []):
                    self.power_110V.setChecked(False)
                if "220V" not in config.get("power", []):
                    self.power_220V.setChecked(False)
                if "L" not in config.get("lisn", []):
                    self.lisn_l.setChecked(False)
                if "N" not in config.get("lisn", []):
                    self.lisn_n.setChecked(False)

                self.sn.setPlainText(config.get("sn", ""))
                self.load.setText(config.get("load", ""))
                self.exclude_items.setPlainText(config.get("excludes", ""))
                self.pathEdit.setText(config.get("save_path", ""))

    def startTest(self):
        self.hide()
        config = self.saveConfig()
        self.ato.inputTestConfig(config)
        self.show()


@TimeCount
def main():
    app = QApplication(sys.argv)
    window = ELEKTRA_GUI()
    window.show()
    app.exec()


if __name__ == "__main__":
    main()
