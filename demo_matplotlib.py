# pip install -i https://pypi.tuna.tsinghua.edu.cn/simple matplotlib
import sys
print(sys.path)


def example():
    # 简单示例
    import matplotlib.pyplot as plt
    import numpy as np
    # subplots :Create a figure and a set of subplots.
    fig, ax = plt.subplots()
    # Axes.plot :Plot y versus x as lines and/or markers.
    ax.plot(np.array([0, 10]), np.array([5, 20]))
    # plt.show :Display all open figures.
    # plt.show()


# example()


def the_figure():
    import matplotlib.pyplot as plt
    # Figure对象：
    fig = plt.figure()  # 空白的figure
    fig.show()


the_figure()

if __name__ == "__main__":
    pass
