#encoding: utf-8
'''
@author:alvin.zhu
@file:test_Video_detail.py
@time:2020/11/6 14:45
@Description:

'''
import time
from Public.Unittest_import import Dubbing

class Video_detail(Dubbing):
    def test_a(self):
        self.V.Into_video()
        self.V.Head_into_zoom_back()
        self.V.Video_follow()
        self.V.Video_good()
        self.V.Video_exposure_touch()
        self.V.Video_exposure_gold()
        self.V.Video_exposure_freevip()
        self.V.Video_exposure_diamond()
        self.V.Video_comments()
        self.V.Video_comment_send()
        self.V.Video_comment_report()
        self.V.Video_comments_load()
        self.V.Video_Coor_dubbing()
        self.V.Video_source()
        self.V.Video_share()
        self.V.Video_switch()
