#
# Description: matplotlib test
# Create: 2025-03-13
#

import os
import random
import matplotlib.pyplot as plt


# matplotlib 画图表使用方式测试
def matplotlib_test():
    # 随机构造一组点集(二维)
    # 生成10个随机整数点，每个坐标在 [0, 10) 范围内
    points = [(random.randint(0, 10), random.randint(0, 10)) for _ in range(10)]
    x_list = [point[0] for point in points]
    y_list = [point[1] for point in points]

    # plt默认会在同一个图上绘制所有信息，可以通过创建新的图标，或者清除当前图表来避免
    # 创建新的图表
    plt.figure()
    # 清除当前图表
    # plt.clf()

    # scatter用于绘制散点图的函数，可以用于二维数据点的可视化
    '''
    plt.scatter(x点坐标， y点坐标， color='颜色', s=点的大小(默认10), marker=点的形状('o'原型,'s'方形, 默认实心圆形)
                alpha=设置点的透明度(0 到 1 之间), edgecolors=点的边缘颜色)
    '''
    plt.scatter(x_list, y_list, color='blue', s=5)

    test_str = 'test'
    # plt.title()添加标题
    plt.title(f'saved_{test_str}')
    # 添加x和y的标签
    plt.xlabel(f'X-axis_{test_str}')
    plt.ylabel(f'Y-axis_{test_str}')

    # plt.legend()显示图例
    # plt.legend()
    '''
    如果pycharm中show()报错:
    1. 打开PyCharm的设置File -> Settings
    2. 导航到Tools -> Python Scientific
    3. 取消勾选Show plots in tool window。
    '''
    plt.show()

    # image_name = 'plt_test.png'
    # dir_path = r'D:\TempFile'
    # 将图片保存到指定位置
    # plt.savefig(os.path.join(dir_path, image_name), dpi=300, bbox_inches="tight")


if __name__ == "__main__":
    matplotlib_test()
