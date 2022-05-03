# pip install -i https://pypi.tuna.tsinghua.edu.cn/simple matplotlib
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['simsun']


def example_1():
    # 简单示例 Axes对象绘制
    import matplotlib.pyplot as plt
    import numpy as np
    # 注册全局字体
    plt.rcParams['font.sans-serif'] = ['simsun']
    # plt.rcParams['font.family'] = ['simsun']

    # subplots 方法 :Create a figure and a set of subplots.
    fig, ax = plt.subplots()
    # Axes.plot 方法 :Plot y versus x as lines and/or markers.
    ax.plot(np.array([0, 10]), np.array([5, 20]), label="数据_1")
    ax.plot(np.array([0, 20]), np.array([50, 200]), label="label_2")
    # 设置X轴和Y轴的标题
    ax.set_xlabel("X轴")
    ax.set_ylabel("Y轴")
    # 设置标题
    ax.set_title("example_1")
    # 添加legend
    ax.legend()
    # plt.show 方法 :Display all open figures.
    plt.show()


# example_1()


def example_2():
    # 简单示例 plt对象绘制
    # 注册字体
    from matplotlib.font_manager import FontProperties
    font_simsun = FontProperties(fname="./fonts/simsun.ttc")
    import matplotlib.pyplot as plt
    import numpy as np
    plt.figure()
    plt.plot(np.array([0, 10]), np.array([5, 20]), label="label_1")
    plt.plot(np.array([0, 20]), np.array([50, 200]), label="label_2")
    plt.xlabel("X 轴", fontproperties=font_simsun)
    plt.ylabel("Y 轴", fontproperties=font_simsun)
    plt.title("example_2")
    plt.legend()
    plt.show()


# example_2()

def example_3():
    # 支持所有可索引访问数据的对象 利用plot的data参数进行传递数据
    import matplotlib.pyplot as plt
    import numpy as np
    data_dict = {
        "X_label": np.arange(0, 10),
        "Y_label": np.arange(0, 10)}
    fig, ax = plt.subplots()
    ax.plot("X_label", "Y_label", data=data_dict)
    plt.show()


# example_3()


def example_4():
    # 生成多个Axes
    # 一个figure包含多个Axes
    import matplotlib.pyplot as plt
    import numpy as np

    # matplotlib.pyplot.subplots(nrows=1, ncols=1, *, sharex=False, sharey=False, squeeze=True, subplot_kw=None, gridspec_kw=None, **fig_kw)
    # plt.subplots方法 返回一个figure对象和一组Axes
    # 2*2的一组Axes
    fig, axs = plt.subplots(2, 2)
    # 通过下标访问单个Axes
    axs[0][0].plot([0, 1, 2], [2, 1, 0])
    axs[0][0].set_title("axs[0][0]")
    axs[0][1].plot([2, 3, 4], [4, 3, 2])
    axs[0][1].set_title("axs[0][1]")

    # matplotlib.pyplot.subplot_mosaic(mosaic, *, sharex=False, sharey=False, subplot_kw=None, gridspec_kw=None, empty_sentinel='.', **fig_kw)
    # plt.subplot_mosaic方法
    # mosaic
    mosaic = [['upleft', '.', 'upright'],
              ['.', 'center', '.'],
              ['lowleft', '.', 'lowright'], ]
    fig, axd = plt.subplot_mosaic(mosaic)
    # 通过下标访问Axes
    axd["upleft"].set_title("upleft")

    plt.show()


example_4()
# Line2D
if __name__ == "__main__":
    pass
