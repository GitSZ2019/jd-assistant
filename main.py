#!/usr/bin/env python
# -*- coding:utf-8 -*-
from jd_assistant import Assistant
from util import parse_sku_id
import threading

if __name__ == '__main__':
    """
    重要提示：此处为示例代码之一，请移步下面的链接查看使用教程👇
    https://github.com/tychxn/jd-assistant/wiki/1.-%E4%BA%AC%E4%B8%9C%E6%8A%A2%E8%B4%AD%E5%8A%A9%E6%89%8B%E7%94%A8%E6%B3%95
    """

    sku_ids = '100006394713:1,100011551632:1'  # 商品id
    area = '19_1607_3639_59699'  # 区域id
    asst = Assistant()  # 初始化
    asst.login_by_QRcode()  # 扫码登陆
    items_dict = parse_sku_id(sku_ids)
    threads = []
    for sku_id in items_dict:
        th = threading.Thread(target=asst.exec_seckill_proc, args=(sku_id, '2020-03-19 20:00:00.000', 4, 4, 1,))
        threads.append(th)
        th.start()

    for t in threads:
        t.join()
    #asst.buy_item_in_stock(sku_ids=sku_ids, area=area, wait_all=False, stock_interval=5)  # 根据商品是否有货自动下单
    # 6个参数：
    # sku_ids: 商品id。可以设置多个商品，也可以带数量，如：'1234' 或 '1234,5678' 或 '1234:2' 或 '1234:2,5678:3'
    # area: 地区id
    # wait_all: 是否等所有商品都有货才一起下单，可选参数，默认False
    # stock_interval: 查询库存时间间隔，可选参数，默认3秒
    # submit_retry: 提交订单失败后重试次数，可选参数，默认3次
    # submit_interval: 提交订单失败后重试时间间隔，可选参数，默认5秒
