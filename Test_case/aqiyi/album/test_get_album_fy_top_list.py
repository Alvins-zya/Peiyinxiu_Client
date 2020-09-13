#coding=utf-8
import unittest

from TEST.http_interface.aqiyi.album import FyTopListVO, get_album_fy_top_list


class TestGetAlbumFyTopList(unittest.TestCase):

    def test_with_temp(self):
        resp =get_album_fy_top_list(FyTopListVO().get_vo())
        self.assertEqual(200, resp.status_code)

    def test_with_cid_is_0(self):
        fy_top_list_vo = FyTopListVO()
        fy_top_list_vo.cid =  0
        resp = get_album_fy_top_list(fy_top_list_vo.get_vo())
        self.assertEqual(200, resp.status_code)
        self.assertEqual('A00002', resp.json()['code'])
        self.assertEqual("未找到数据", resp.json()['data'])

    def test_with_cid_is_str(self):
        fy_top_list_vo = FyTopListVO()
        fy_top_list_vo.cid = "XX"
        resp = get_album_fy_top_list(fy_top_list_vo.get_vo())
        self.assertEqual(200, resp.status_code)
        self.assertEqual('A00001', resp.json()['code'])
        self.assertEqual("参数错误", resp.json()['data'])

