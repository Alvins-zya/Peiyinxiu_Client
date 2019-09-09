#coding=utf-8
from Peiyinxiu_Client.Circle_Society.Society import Corporation
from Peiyinxiu_Client.Circle_Society.Circle import Home_Circle
from Peiyinxiu_Client.Circle_Society.Entry_Community import Communitys


def main():
    Tiezi_home = Home_Circle()#圈子
    Corp = Corporation()#社团
    # Communitys()  # 启动应用并切换到社区主界面
    # Tiezi_home.History()#圈子历史记录
    # Tiezi_home.Topic_search()#话题搜索
    # Tiezi_home.Circle_home()#圈子主页
    # Tiezi_home.Topic_detail()#话题详情
    # Tiezi_home.Posting()#发帖
    Corp.Corp_Home()#社团主界面
    # Corp.Corp_Search()#社团搜索
    Corp.Corp_My()#我的社团
    Corp.Corp_Recommend()#推荐社团




if __name__=="__main__":
    main()