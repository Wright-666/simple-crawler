#!/usr/bin/python
# -*- coding:UTF-8 -*-
import requests


def main():
    url = "https://www.bilibili.com/v/popular/rank/all"
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0",
               "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
               "Accept-Language":"zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
               "Connection":"keep-alive",
               "Cookie": "_uuid=704AD34D-2E11-4603-8CBF-953389E685CD68050infoc; sid=6284zoar; fingerprint=26cd7161a61b8ab14f10570cb3e564bb; buvid_fp=bd0945e463932c980166ada44ba73b97; buvid_fp_plain=undefined; PVID=1; CURRENT_FNVAL=4048; blackside_state=0; rpdid=|(u)~mkRR|mY0J'uYkkJYkRu); buvid3=8DD8D352-2121-774C-6F3E-67F9B169784373152infoc; CURRENT_BLACKGAP=0; CURRENT_QUALITY=80; LIVE_BUVID=AUTO5216294639208554; bp_t_offset_169905728=640862369647427639; bp_video_offset_169905728=640862369647427600; video_page_version=v_old_home; b_ut=5; i-wanna-go-back=-1; DedeUserID=169905728; DedeUserID__ckMd5=cc2305e2c4f51d71; SESSDATA=bf961ed7%2C1653997174%2C143bb*c1; bili_jct=7df0ce46fbf5195fca6bc21d6d5b42ed; buvid4=09E0EFE9-1F78-0BA5-DA01-F11146FC2C4E10640-022012016-bK5ysmawZ6WvPiFjG8cuRg%3D%3D; fingerprint3=e472ccb65649c4263fdd33e95779695c; is-2022-channel=1; nostalgia_conf=-1; innersign=0; b_lsid=AB10A1F59_17FB9E97AE2",
               "Host":"www.bilibili.com"}
    # 请求对应的url
    responses = requests.get(url,headers=headers)
    print(responses.content)
    pass


if __name__ == '__main__':
    main()
