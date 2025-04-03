from catuo import *

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

def test_pic():
    history = load_history()
    # var_model = pmb.prompt("输入机种型号:", default=history.get('model', ''))
    # var_class = pmb.confirm("EMI标准:", buttons=["Class A", "Class B"])
    # var_sn = pmb.prompt("输入SN:", default=history.get('sn', ''))
    # var_power = pmb.prompt("输入单体的Vac:", default=history.get('power', ''))
    # var_load = pmb.prompt("输入单体负载:", default=history.get('load', ''))
    # history['model'] = var_model
    # history['class'] = var_class
    # history['sn'] = var_sn
    # history['power'] = var_power
    # history['load'] = var_load
    # save_history(history)
    
    var_model = history.get('model', '')
    var_class = history.get('class', '')
    var_sn = history.get('sn', '')
    var_power = history.get('power', '')
    var_load = history.get('load', '')
    
    """
    if var_class == "Class A":
        pic_class = r".\\Pic_lib\\ClassA.png"
    else:
        pic_class = r".\\Pic_lib\\ClassB.png"
    moveTo_image(pic_class)
    pg.click(clicks=2)
    
    pg.keyDown('ctrl')
    pg.press('s')
    pg.keyUp('ctrl')
    
    pic_peijian = r".\\Pic_lib\\PeijianSheZhi.png"
    moveTo_image(pic_peijian)
    pg.click()
    
    pic_ceshixinxi = r".\\Pic_lib\\CeShiXinXi_closed.png"
    moveTo_image(pic_ceshixinxi)
    pg.click()
    
    pic_model = r".\\Pic_lib\\Model.png"
    moveTo_image(pic_model, ['left', (200,0)])
    pg.click()
    pg.typewrite(var_model)
    
    pic_sn = r".\\Pic_lib\\SN.png"
    moveTo_image(pic_sn, ['left', (200,0)])
    pg.click()
    pg.typewrite(var_sn)
    
    pic_power = r".\\Pic_lib\\Power.png"
    moveTo_image(pic_power, ['left', (200,0)])
    pg.click()
    pg.typewrite(var_power)
    
    pic_load = r".\\Pic_lib\\Load.png"
    moveTo_image(pic_load, ['left', (200,0)])
    pg.click()
    pg.typewrite(var_load)
    
    pic_run = r".\\Pic_lib\\Run.png"
    moveTo_image(pic_run)
    pg.click()

    pic_queren = r".\\Pic_lib\\QueRen1.png"
    moveTo_image(pic_queren)
    pg.click()
    
    pic_queren = r".\\Pic_lib\\QueRen1.png"
    moveTo_image(pic_queren)
    pg.click()
    """
    
    pic_queren = r".\\Pic_lib\\QueRen1.png"
    moveTo_image(pic_queren)
    pg.click()

    #TODO: 图像拽取
    
    

if __name__ == '__main__':
    test_pic()
