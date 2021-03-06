# -*- coding: utf-8 -*-
# 摘自 pyecharts 文档  https://pyecharts.org/#/zh-cn/3d_charts


from example.commons import Faker
from pyecharts import options as opts
from pyecharts.charts import Bar3D
import random


def bar3d_base() -> Bar3D:
    data = [(i, j, random.randint(0, 12)) for i in range(6) for j in range(24)]
    c = (
        Bar3D()  # 类
        .add(  # 实例方法  # 这种写法需要在外面加 ()
            "",  # 传参
            [[d[1], d[0], d[2]] for d in data],
            xaxis3d_opts=opts.Axis3DOpts(Faker.clock, type_="category"),
            yaxis3d_opts=opts.Axis3DOpts(Faker.week_en, type_="category"),
            zaxis3d_opts=opts.Axis3DOpts(type_="value"),
        )
        .set_global_opts(  # 实例方法
            visualmap_opts=opts.VisualMapOpts(max_=20),  # 传参
            title_opts=opts.TitleOpts(title="Bar3D-基本示例"),
        )
    )
    return c


if __name__ == '__main__':
    bar3d = bar3d_base()
    bar3d.render()

