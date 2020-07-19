import requests,json
 
body,status='',''
key='这里是你的key值存放位置'
city='这里是你的城市编号'
 
def gettianqi():
    global body,city,status
    url=('http://t.weather.sojson.com/api/weather/city/%s'%city)
    tianqi_res=requests.get(url=url).text
    tianqi_res=json.loads(tianqi_res)
    status=tianqi_res['status']
    citys=tianqi_res['cityInfo']['city']
    nowdatetime=tianqi_res['time']
    data=tianqi_res['data']
    shidu=data['shidu']
    pm25=data['pm25']
    pm10=data['pm10']
    quality=data['quality']
    tianqi=data['forecast']
    jintiantianqi=tianqi[0]
    jintian_aqi=jintiantianqi['aqi']
    jintian_ymd=jintiantianqi['ymd']
    jintian_week=jintiantianqi['week']
    jintian_high=jintiantianqi['high']
    jintian_low=jintiantianqi['low']
    jintian_fx=jintiantianqi['fx']
    jintian_fl=jintiantianqi['fl']
    jintian_type=jintiantianqi['type']
    jintian_notice=jintiantianqi['notice']
    body=(
        '\n'+' ————— '+citys+' —————'+'\n'
        +nowdatetime+'——'+jintian_week+'\n'
        '空气质量：'+str(quality)+'\n'
        'AQI指数：'+str(jintian_aqi)+'\n'
        'pm2.5：'+str(pm25)+'\n'
        'pm10：'+str(pm10)+'\n'
        '——————————————'+'\n'
        '天气状况：\n'
        +str(jintian_low)+'~'+str(jintian_high)+'\n'
        +str(jintian_type)+'\n'
        +str(jintian_notice)+'\n'
        +str(jintian_fx)+str(jintian_fl)+'\n'
        '——————————————'+'\n')
 
def upserver():
    global key,body
    data={
        'key':key,
        'head':'天气预报',
        'body':body
    }
    url=('http://push.ijingniu.cn/send')
    server=requests.post(url=url,data=data)
 
def main_handler(event, context):
    global status,city,key
    gettianqi()
    if status != 200:
        status = '获取失败'
        print(status)
        url = ('http://push.ijingniu.cn/send?key=%s'%key)
        data = {
            'text':'天气预报推送失败',
            'desp':'天气预报推送失败'
        }
        server=requests.post(url=url,data=data)
    else:
        upserver()
