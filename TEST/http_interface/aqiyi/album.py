#coding=utf-8
import requests




class FyTopListVO:
    def __init__(self):
        self._cid = 15
        self._dim = 'hour'
        self._page =1
        self._size =10
        self._list_type = 'realTime'

    def get_vo(self):
        vo = {
            "cid": self._cid,
            "dim":self._dim,
            "page":self._page,
            "size": self._size,
            "type":self._list_type
        }
        return vo

    @property
    def dim(self):
        return self._dim
    @dim.setter
    def dim(self ,dim):
        self._dim = dim


    @property
    def cid(self):
        return self._cid
    @cid.setter
    def cid(self ,cid):
        self._cid = cid

    @property
    def page(self):
        return self._page
    @page.setter
    def page(self ,page):
        self._page = page

    @property
    def size(self):
        return self._size
    @size.setter
    def size(self ,size):
        self._size = size


def get_album_fy_top_list(fy_top_list_vo):
    uri = "https://pcw-api.iqiyi.com/album/album/fytoplist"
    resp = requests.get(uri, params=fy_top_list_vo, verify=False)
    print(resp.json())
    return resp


def tools_of_get_category_name_by_id(category_id = 31020):
    resp = get_album_fy_top_list(FyTopListVO().get_vo())
    for category_info in resp.json()['data'][0]['categories']:
        if category_info['id'] == category_id:
            print(category_info['name'])
            return category_info['name']

if __name__ == '__main__':
    # fy_top_list_vo  = FyTopListVO()
    # get_album_fy_top_list(fy_top_list_vo.get_vo())
    # fy_top_list_vo.size = 1
    # fy_top_list_vo.cid = 16
    # get_album_fy_top_list(fy_top_list_vo.get_vo())
    tools_of_get_category_name_by_id()


