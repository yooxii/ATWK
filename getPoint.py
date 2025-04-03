import cv2
import numpy as np
from scipy.signal import find_peaks
import matplotlib.pyplot as plt
 
def process_image(img):
    # 读取图像
    img = cv2.imread(img)
    # 将图像转换为灰度图像
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    cv2.imshow("gray", gray)
    cv2.waitKey(0)
    
    # 对灰度图像进行二值化处理
    _, binary = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)
    
    cv2.imshow("binary", binary)
    cv2.waitKey(0)
    
    # 创建一个3x3的结构元素，用于形态学操作
    kernel = np.ones((5,5), np.uint8)
    # 对二值图像进行开运算，去除小的噪声点
    binary = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel)
    
    cv2.imshow("opened", binary)
    cv2.waitKey(0)
    
    # 查找二值图像中的轮廓
    contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
     
    data_contours = []
    # 遍历每个轮廓，筛选出符合条件的轮廓
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 10:
            points = cnt.squeeze()
            y_std = np.std(points[:,1])
            if y_std > 10:
                data_contours.append(cnt)
 
    # 如果检测到的轮廓数量不为2，则抛出异常
    if len(data_contours) != 2:
        raise ValueError("未检测到两条数据曲线")
     
    all_extremes = []
    # 对每个符合条件的轮廓进行处理，找出每个区域的极值点
    for cnt in data_contours:
        points = points[points[:, 0].argsort()]
        x = points[:, 0].astype(float)
        y = points[:, 1].astype(float)
         
        num_zones = 6
        zone_length = len(x) // num_zones
        zone_extremes = []
         
        for i in range(num_zones):
            start = i * zone_length
            end = (i+1) * zone_length
             
            x_part = x[start:end]
            y_part = y[start:end]
             
            max_idx = np.argmax(y_part)
             
            max_point = (x_part[max_idx], y_part[max_idx])
             
            zone_extremes.append(max_point)
         
        all_extremes.append(zone_extremes)
     
    # 创建输出图像
    output = img.copy()
    colors = [(0, 0, 255), (0, 255, 0)]
    # 在输出图像上绘制极值点
    for i, extremes in enumerate(all_extremes):
        for point in extremes:
            cv2.circle(output, (int(point[0]), int(point[1])), 5, colors[i], -1)
     
    return output
 
if __name__ == '__main__':
    # 定义输入图像路径
    img = r".\\test.png"
    # 处理图像并获取输出图像
    output = process_image(img)
    # 显示输出图像
    cv2.imshow("output", output)
    # 等待用户按键
    cv2.waitKey(0)
    # 保存输出图像
    cv2.imwrite(r".\\output.png", output)