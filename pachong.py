import requests

def main():
    '''url="http://www.huayunsys.com"
    responses=requests.get(url)
    #print(responses.content.decode("utf-8"))   #源码
    #print(responses.request.headers)    #查看请求头，爬虫的本尊形态是python开头，可以伪装成浏览器
    #print(responses.headers)            #响应头
    print(responses.url)                #响应地址
    #print(responses.request.url)'''

    '''url = "http://www.baidu.com"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36",
               "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
               "Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8",
               "Connection": "keep-alive",
               "Cookie": "BIDUPSID=B6EA7C9B05DAB3C37B715A2AB92BD08B; PSTM=1629100955; BD_UPN=12314753; BDUSS=BZfm55ay0tT29PaUlaSjR-clhFbTJ-Q2RpTEROWm4yMlhSWXR3ZXpQZzZxVUZoSUFBQUFBJCQAAAAAAAAAAAEAAADK2ualc3VubnnJscbGwMcwMgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADocGmE6HBphSF; BDUSS_BFESS=BZfm55ay0tT29PaUlaSjR-clhFbTJ-Q2RpTEROWm4yMlhSWXR3ZXpQZzZxVUZoSUFBQUFBJCQAAAAAAAAAAAEAAADK2ualc3VubnnJscbGwMcwMgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADocGmE6HBphSF; __yjs_duid=1_bbe39be9ba12597a6659dac18a1b797c1629101225013; BAIDUID=1936181143C7F0483CC02E5F3FF01DFA:FG=1; H_WISE_SIDS=107313_110085_127969_131861_168388_176398_177985_178384_178530_178605_179345_179448_180276_181106_181398_181588_181709_182000_182243_182531_182663_183030_183223_183328_183536_183611_184010_184246_184267_184319_184735_184809_184892_185029_185037_185268_185519_185726_185873_185879_186039_186206_186313_186317_186411_186446_186558_186597_186636_186644_186665_186841_186898_187022_187062_187086_187188_187214_187282_187292_187326_187356_187421_187488_187533_187643_187828_187912_187928_187965_188049_8000055_8000116_8000125_8000139_8000144_8000153_8000173_8000178_8000182_8000186; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; H_PS_645EC=89aapjNplXzERMiuXfrHu6bPOP8WIi4KAa8H7TGQpgtmVqlAEosq6cH8iNos1Lz2xPBv; delPer=0; BD_CK_SAM=1; PSINO=5; COOKIE_SESSION=6_0_9_9_8_18_0_0_9_8_1_0_62691_0_0_0_1642985536_0_1642986547%7C9%233211939_107_1642076303%7C9; BDRCVFR[OmkpXC8mjrc]=mk3SLVN4HKm; BD_HOME=1; H_PS_PSSID=31253_26350; BDRCVFR[ZX8MhTrnJan]=mk3SLVN4HKm; BA_HECTOR=858l8l800l2la42lhl1gus07b0r",
               "Host": "www.baidu.com"}
    responses = requests.get(url,headers=headers)
    print(responses.content.decode("UTF-8"))'''

    '''url="http://sqlilabs.njhack.xyz/Less-20/index.php"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
        "Connection": "keep-alive",
        "Cookie": "uname=Dumb; tj95eceba51d1749cd98415c14e7456b=1",
        "Host": "sqlilabs.njhack.xyz"}
    responses=requests.get(url,headers=headers)
    print(responses.content.decode("UTF-8"))'''

    '''url = "http://sqlilabs.njhack.xyz/Less-20/index.php"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
        "Connection": "keep-alive",
        "Host": "sqlilabs.njhack.xyz",}
    data={"uname":"Dumb","passwd":"Dumb","submit":"Submit"}
    responses = requests.post(url, headers=headers,data=data)
    print(responses.content.decode("UTF-8"))'''

    '''input_id=int(input("输入待查询id："))
    url = "http://sqlilabs.njhack.xyz/Less-1/index.php?id={}".format(input_id)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
        "Connection": "keep-alive",
        "Host": "sqlilabs.njhack.xyz", }

    for i in range(3):
        params={"id":i}
        responses = requests.get(url, headers=headers,params=params)
        print(responses.content.decode("UTF-8"))
        
    '''
    '''responses = requests.get(url, headers=headers)
    print(responses.content.decode("UTF-8"))'''








    

if __name__=="__main__":
    main()   
