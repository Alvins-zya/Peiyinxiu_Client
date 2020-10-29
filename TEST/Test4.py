# coding: utf-8

check = ['上传一个带频道的作品','分享作品至朋友圈','收听语聊10分钟','用钻石曝光1个作品','评论5个曝光区作品','看完5个作品']
check1 = ['分享作品至朋友圈','上传一个带频道的作品','收听语聊10分钟','用钻石曝光1个作品','评论5个曝光区作品','看完5个作品']


for i in range(len(check)):
    result = ('({0}, {1})'. format(i, check[i]))
    num = int(result[1])
    if check[num] == '上传一个带频道的作品':
        print(i)
    elif check[num] == '分享作品至朋友圈':
        print(i)
    elif check[num] == '收听语聊10分钟':
        print(i)
    elif check[num] == '用钻石曝光1个作品':
       print(i)
    elif check[num] == '评论5个曝光区作品':
        print(i)
    elif check[num] == '看完5个作品':
        print(i)

