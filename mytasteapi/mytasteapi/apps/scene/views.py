from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination

from .serializers import *
from .models import *


class Pagination(PageNumberPagination):
    """
    分页
    """
    page_query_param = "page"
    page_size_query_param = "page_size"
    max_page_size = 100
    page_size = 1


class ScenesSummaryAPIView(ListAPIView):
    """
    国、省、市景点公用首页缩略图展示
    """

    serializer_class = SceneSummarySerializer

    def get_queryset(self):
        province_id = self.request.query_params.dict().get('province')
        city_id = self.request.query_params.dict().get('city')

        queryset = Scene.objects.filter().order_by('-hot')
        if province_id:
            queryset = queryset.filter(province=province_id)
        if city_id:
            queryset = queryset.filter(city=city_id)
        queryset = queryset[:8]
        return queryset


class CityScenesAPIView(APIView):
    """
    景点筛选展示
    """

    def get(self, request, *args, **kwargs):
        city_id = kwargs.get('pk')
        scene_type = request.query_params.dict().get('scene_type', '')
        scene_grade = request.query_params.dict().get('scene_grade', '')
        scene_order = request.query_params.dict().get('scene_order', '')
        page = Pagination()
        scenes_queryset = Scene.objects.filter(city_id=city_id).order_by('-hot')

        if scene_type:
            scenes_queryset = scenes_queryset.filter(type=scene_type)
        if scene_grade:
            scenes_queryset = scenes_queryset.filter(grade=scene_grade)
        if scene_order:
            scenes_queryset = scenes_queryset.order_by(scene_order)

        page_scenes = page.paginate_queryset(queryset=scenes_queryset, request=request, view=self)
        ser_obj = SceneSerializer(page_scenes, many=True)
        return page.get_paginated_response(ser_obj.data)


class SceneAPIView(RetrieveAPIView):
    """
    单个景点详细展示
    """
    queryset = Scene.objects.all()
    serializer_class = SceneSerializer


class CityAPIView(RetrieveAPIView):
    """
    获取单个城市信息
    """
    queryset = City.objects.all()
    serializer_class = CitySerializer


class SceneCommentAPIView(APIView):
    """
    景点评论展示
    """

    def get(self, request, *args, **kwargs):
        scene_id = kwargs.get('pk')
        page = Pagination()
        comments_queryset = SceneComment.objects.filter(scene_id=scene_id).order_by('-created_time')
        page_comments = page.paginate_queryset(queryset=comments_queryset, request=request, view=self)
        ser_obj = SceneCommentSerializer(page_comments, many=True)
        return page.get_paginated_response(ser_obj.data)


class SceneCommentCreateAPIView(CreateAPIView):
    """
    新增景点评论
    """
    queryset = SceneComment
    serializer_class = SceneCommentSerializer


class ScenesSearchAPIVIew(ListAPIView):
    """
    首页景点模糊搜索
    """
    serializer_class = ScenesSearchSerializer

    def get_queryset(self):
        query_string = self.request.query_params.dict().get('search', '')
        queryset = Scene.objects.filter(name__contains=query_string)

        return queryset


class CitiesSearchAPIVIew(ListAPIView):
    """
    首页目的地模糊搜索
    """
    serializer_class = CitySerializer

    def get_queryset(self):
        query_string = self.request.query_params.dict().get('search', '')
        queryset = City.objects.filter(name__contains=query_string)

        return queryset


'''
import random


import requests
from io import BytesIO
from lxml import etree
from urllib.request import urlopen
from multiprocessing.dummy import Pool

from django.core.files import File
from django.http import HttpResponse

from .models import City, Province, Scene

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"
}

start_urls = [
    'https://you.ctrip.com/sight/beijing1/s0-p{page}.html#sightname',
    'https://you.ctrip.com/sight/tianjin154/s0-p{page}.html#sightname',
    'https://you.ctrip.com/sight/shanghai2/s0-p{page}.html#sightname',
    'https://you.ctrip.com/sight/chongqing158/s0-p{page}.html#sightname',
    'https://you.ctrip.com/sight/hebei100059.html',
    'https://you.ctrip.com/sight/shanxi100056.html',
    'https://you.ctrip.com/sight/taiwan100076.html',
    'https://you.ctrip.com/sight/liaoning100061.html',
    'https://you.ctrip.com/sight/jilinshi267/s0-p{page}.html#sightname',
    'https://you.ctrip.com/sight/heilongjiang100055.html',
    'https://you.ctrip.com/sight/jiangsu100066.html',
    'https://you.ctrip.com/sight/zhejiang100065.html',
    'https://you.ctrip.com/sight/anhui100068.html',
    'https://you.ctrip.com/sight/fujian100038.html',
    'https://you.ctrip.com/sight/jiangxi100054.html',
    'https://you.ctrip.com/sight/shandong100039.html',
    'https://you.ctrip.com/sight/henan100058.html',
    'https://you.ctrip.com/sight/hubei100067.html',
    'https://you.ctrip.com/sight/hunan100053.html',
    'https://you.ctrip.com/sight/guangdong100051.html',
    'https://you.ctrip.com/sight/gansu100060.html',
    'https://you.ctrip.com/sight/sichuan100009.html',
    'https://you.ctrip.com/sight/guizhou100064.html',
    'https://you.ctrip.com/sight/hainan100001.html',
    'https://you.ctrip.com/sight/yunnan100007.html',
    'https://you.ctrip.com/sight/qinghai100032.html',
    'https://you.ctrip.com/sight/shanxi100057.html',
    'https://you.ctrip.com/sight/guangxi100052.html',
    'https://you.ctrip.com/sight/tibet100003.html',
    'https://you.ctrip.com/sight/ningxia100063.html',
    'https://you.ctrip.com/sight/xinjiang100008.html',
    'https://you.ctrip.com/sight/innermongolia100062.html',
    'https://you.ctrip.com/sight/macau39/s0-p{page}.html#sightname',
    'https://you.ctrip.com/sight/hongkong38/s0-p{page}.html#sightname',
]

def push(request):
    pool1 = Pool(10)
    pool2 = Pool(10)
    paramss1 = []
    paramss2 = []
    for index, url in enumerate(start_urls, 1):
        if index in [1, 2, 3, 4, 9, 33, 34]:
            params = (url, index)
            paramss1.append(params)
        else:
            params = (url, index)
            paramss2.append(params)
    pool1.map(get_city, paramss1)
    pool2.map(get_province, paramss2)
    pool1.close()
    pool1.join()
    pool2.close()
    pool2.join()
    return HttpResponse('ok')


def get_province(params):
    """
    从省份分解到城市
    :param url: 省份url
    :param index: 省份索引
    :return:
    """
    (url_, index) = params
    page_text = requests.get(url_, headers=headers).text
    tree = etree.HTML(page_text)
    city_div_list = tree.xpath('/html/body/div[4]/div/div[2]/div[2]/div[2]/div')
    for i in range(10):
        div = city_div_list[i]
        city_link_place = 'https://you.ctrip.com' + div.xpath('./div/a/@href')[0]
        # https://you.ctrip.com/place/guangdong100051.html  ——
        #                                                     |
        # https://you.ctrip.com/sight/guangdong100051.html <——
        city_link_sight = city_link_place.replace('place', 'sight').replace('.html', '/s0-p{page}.html#sightname')
        params = (city_link_sight, index)
        get_city(params)


def get_city(params):
    """
    从城市分解到景点
    :param url_: 城市url
    :param index: 省份索引
    :return:
    """
    # 爬取10页景点内容
    (url_, index) = params
    for i in range(1, 3):
        url = url_.format(page=i)
        page_text = requests.get(url=url, headers=antiantispider()).text
        tree = etree.HTML(page_text)
        # 获取当前网页的景点div标签列表
        scene_div_list = tree.xpath('/html/body/div[4]/div/div[2]/div/div[3]/div')
        # 景点所在城市名称
        city_name = tree.xpath('/html/body/div[2]/div[2]/div[1]/div[1]/h1/a/text()')[0]
        for div_i, div in enumerate(scene_div_list, 1):
            if div_i not in [6, 17]:
                # 景点详情页链接
                detail_link = 'https://you.ctrip.com' + div.xpath('./div/a/@href')[0]
                # 景点主展示图片链接
                img_link = div.xpath('./div/a/img/@src')[0] or 'https://dimg05.c-ctrip.com/images/fd/tg/g2/M02/C5/09/Cghzf1W7IBCAU1soAAA1rXNRb5g042_C_220_140.jpg'
                # 景点门票
                t = div.xpath('./div[2]/dl/dd/span[@class="price"]/text()')
                ticket = str(t[0] if t else '').strip()
                # 获取详细数据并存入数据库
                get_detail(detail_link, ticket, index, city_name, img_link)


def get_detail(url, ticket, province_id, city_name, img_link):
    """
    获取一个景点的全部信息并存入数据库
    :param url: 景点url
    :param ticket: 票价
    :param province_id: 省份id
    :param city_name: 城市名
    :param img_link: 主展示图片链接
    :return:
    """
    # 获得对应城市索引的方法，如果有重名或者不存在，设为“未知城市（id392）”，后续手动修改
    city_id = None
    citys = City.objects.filter(name__startswith=city_name)
    if citys.count() == 1:
        city_id = citys.first().id
    else:
        city_id = 393
    # 该景点在携程网站上对应的id，用于爬取热度
    # https://you.ctrip.com/sight/beijing1/229.html
    ctrip_scene_id = url.split('/')[-1].split('.')[0]

    page_text = requests.get(url, headers=headers).text
    tree = etree.HTML(page_text)
    # 中文名称
    name = tree.xpath('/html/body/div[2]/div[2]/div/div[1]/h1/a/text()')[0].strip()
    # 英文名称
    t = tree.xpath('/html/body/div[2]/div[2]/div/div[1]/p/text()')
    ename = str(t[0] if t else '').strip()
    # 图片io，为末尾存入做准备
    img_content = urlopen(img_link)
    io = BytesIO(img_content.read())
    # 评分
    score = tree.xpath(
        '/html/body/div[3]/div/div[1]/div[1]/ul/li[1]/span/b/text() | /html/body/div[3]/div/div[1]/div[1]/ul/li[1]/span/text()')[
        0].strip()
    # 评论数
    t = tree.xpath('//*[@id="hrefyyDp"]/span/text()')
    comment_num = int(t[0]) if t else 0
    # 攻略数，携程网没有，0
    travelbook_num = 0
    # 景点类型，携程网没有，默认为1，其他类型
    type = 1
    # 景点概述
    t = tree.xpath('/html/body/div[3]/div/div[1]/div[5]/div[2]/div[1]/div/text()')
    summary = str(t[0] if t else '').strip()

    # 因为景点等级、联系电话、官方网址在ul>li列表中，且数量不规则，所以详细判断
    grade = 1
    phone = ''
    website = ''
    li_list = tree.xpath('/html/body/div[3]/div/div[2]/div[@class="s_sight_infor"]/ul/li')
    if len(li_list) != 0:
        for li in li_list:
            # 若有等级存在
            label = li.xpath('./span[1]/text()')[0].strip()
            grade_or_phone = li.xpath('./span[2]/text()')[0].strip()
            if label == '等        级：':
                grade_detail = grade_or_phone
                grade = get_scene_grade(grade_detail)
            # 若有电话存在
            if label == '电        话：':
                phone = grade_or_phone
            # 若有网站存在
            if label == '官方网站：':
                website = li.xpath('./span/a/text()')[0]
    # 开放时间
    t = tree.xpath('/html/body/div[3]/div/div[2]/div[@class="s_sight_infor"]/dl/dd/text()')
    open_time = str(t[0] if t else '').strip()
    # 详细地址
    t = tree.xpath('/html/body/div[3]/div/div[2]/div[@class="s_sight_infor"]/p/text()')
    address = str(t[0] if t else '').strip()
    # 交通指南，携程没有
    traffic = ''
    # 建议游玩时间，携程没有
    advice_time = ''
    # 小提示
    t = tree.xpath('/html/body/div[3]/div/div[1]/div[5]/div[3]/div[1]/div/text()')
    tips = str(t[0] if t else '').strip()
    # 热度，动态加载出来
    data = {
        'Resource': ctrip_scene_id,
        'pageType': 'Sight',
        'rank': '0.7893706684189208'
    }
    hot = get_scene_hot(data=data)
    # 存入数据库
    if not Scene.objects.filter(name=name, city_id=city_id):
        scene = Scene.objects.create(name=name, ename=ename, city_id=city_id, province_id=province_id, address=address,
                                     hot=hot, score=score, comment_num=comment_num, travelbook_num=travelbook_num,
                                     type=type, summary=summary, phone=phone, website=website, open_time=open_time,
                                     ticket=ticket, traffic=traffic, grade=grade, advice_time=advice_time, tips=tips)
        scene.main_photo.save('{city}_{name}.jpg'.format(city=city_name, name=name), File(io))
        print(name + 'ok！')


def get_scene_grade(grade_detail):
    """
    根据等级描述获取等级索引
    :param grade_detail: 等级描述
    :return: 索引
    """
    grade = 1
    if grade_detail == 'A':
        grade = 2
    elif grade_detail == 'AA':
        grade = 3
    elif grade_detail == 'AAA':
        grade = 4
    elif grade_detail == 'AAAA':
        grade = 5
    elif grade_detail == 'AAAAA':
        grade = 6
    return grade


def get_scene_hot(data):
    """
    获取景点热度
    :param data: post请求数据，景点id
    :return: 热度
    """
    url = 'https://you.ctrip.com/Destinationsite/SharedComm/ShowGowant'
    result = requests.post(url, headers=headers, data=data).json()
    return result['WantTimes'] + result['WentTimes']


def antiantispider():
    user_agent_list = [
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 "
        "(KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
        "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 "
        "(KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 "
        "(KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 "
        "(KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 "
        "(KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 "
        "(KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
        "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 "
        "(KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 "
        "(KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 "
        "(KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
    ]
    return {"User-Agent": random.choice(user_agent_list)}
'''
