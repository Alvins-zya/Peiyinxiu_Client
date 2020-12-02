# coding: utf-8
check = ['上传一个带频道的作品', '分享作品至朋友圈', '收听语聊10分钟', '用钻石曝光1个作品', '看完5个作品','评论5个曝光区作品']
for j in range(len(check)):
    result = ('{0}, {1}'.format(j, check[j]))
    print(result)
    num = int(result[0])
    print(num)