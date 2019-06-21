# -*- coding: utf-8 -*-
# 摘自 pyecharts 文档  https://pyecharts.org/#/zh-cn/quickstart?id=_5-%E5%88%86%E9%92%9F%E4%B8%8A%E6%89%8B


from pyecharts.charts import Bar


bar = Bar()
bar.add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
bar.add_yaxis("商家A", [5, 20, 36, 10, 75, 90])
# render 会生成本地 HTML 文件，默认会在当前目录生成 render.html 文件
# 也可以传入路径参数，如 bar.render("mycharts.html")
bar.render()

