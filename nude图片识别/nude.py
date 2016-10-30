# -*- coding: utf-8 -*-
"""
程序的关键步骤如下:
1.遍历每个像素，检测像素颜色是否为肤色
2.将相邻的肤色像素归为一个皮肤区域，得到若干个皮肤区域
3.剔除像素数量极少的皮肤区域

我们定义非色情图片的判定规则如下（满足任意一个判定为真）：
1.皮肤区域的个数小于3 个
2.皮肤区域的像素与图像所有像素的比值小于 15%
3.最大皮肤区域小于总皮肤面积的 45%
4.皮肤区域数量超过60个

像素肤色判定

"""

import sys
import os
import _io
from collections import namedtuple
from PIL import Image


class Nude(object):
    Skin = namedtuple("Skin", "id skin region x y")
    
    def __init__(self, path_or_image):
        # 若 path_or_image 为 Image.Image 类型的实例，直接赋值
        if isinstance(path_or_image, Image.Image):
            self.image = path_or_image
        # 若 path_or_image 为 str 类型的实例，打开图片
        elif isinstance(path_or_image, str):
            self.image = Image.open(path_or_image)

        # 获得图片所有颜色通道
        bands = self.image.getbands()
        # 判断是否为单通道图片（也即灰度图），是则将灰度图转换为 RGB 图
        if len(bands) == 1:
            # 新建相同大小的 RGB 图像
            new_img = Image.new("RGB", self.image.size)
            # 拷贝灰度图 self.image 到 RGB图 new_img.paste （PIL 自动进行颜色通道转换）
            new_img.paste(self.image)
            f = self.image.filename
            # 替换 self.image
            self.image = new_img
            self.image.filename = f

        # 存储对应图像所有像素的全部 Skin 对象
        self.skin_map = []
        # 检测到的皮肤区域，元素的索引即为皮肤区域号，元素都是包含一些 Skin 对象的列表
        self.detected_regions = []
        # 元素都是包含一些 int 对象（区域号）的列表
        # 这些元素中的区域号代表的区域都是待合并的区域
        self.merge_regions = []
        # 整合后的皮肤区域，元素的索引即为皮肤区域号，元素都是包含一些 Skin 对象的列表
        self.skin_regions = []
        # 最近合并的两个皮肤区域的区域号，初始化为 -1
        self.last_from, self.last_to = -1, -1
        # 色情图像判断结果
        self.result = None
        # 处理得到的信息
        self.message = None
        # 图像宽高
        self.width, self.height = self.image.size
        # 图像总像素
        self.total_pixels = self.width * self.height
        
def resize(self, maxwidth=1000, maxheight=1000, res=True):

    ret = 0
    if res:
        if self.width > maxwidth or :
            wpercent = (maxwidth / self.width)
            hsize = int((self.height * wpercent))
            fname = self.image.filename
            # Image.LANCZOS 是重采样滤波器，用于抗锯齿
            self.image = self.image.resize((maxwidth, hsize), Image.LANCZOS)
            self.image.filename = fname
            self.width, self.height = self.image.size
            self.total_pixels = self.width * self.height
            ret += 1
        if self.height > maxheight:
            hpercent = (maxheight / float(self.height))
            wsize = int((float(self.width) * float(hpercent)))
            fname = self.image.filename
            self.image = self.image.resize((wsize, maxheight), Image.LANCZOS)
            self.image.filename = fname
            self.width, self.height = self.image.size
            self.total_pixels = self.width * self.height
            ret += 2
    return ret