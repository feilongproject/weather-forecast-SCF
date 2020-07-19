import requests,json
 
desp,status='',''
sckey='这里是你的sckey值存放位置'
city='这里是你的城市编号'
 
def getweather():
    global desp,city,status
    url=('http://t.weather.sojson.com/api/weather/city/%s'%city)
    weather_res=requests.get(url=url).text
    weather_res=json.loads(weather_res)
    status=weather_res['status']
    citys=weather_res['cityInfo']['city']
    nowdatetime=weather_res['time']
    data=weather_res['data']
    shidu=data['shidu']
    pm25=data['pm25']
    pm10=data['pm10']
    quality=data['quality']
    weather=data['forecast']
    todayweather=weather[0]
    today_aqi=todayweather['aqi']
    today_ymd=todayweather['ymd']
    today_week=todayweather['week']
    today_high=todayweather['high']
    today_low=todayweather['low']
    today_fx=todayweather['fx']
    today_fl=todayweather['fl']
    today_type=todayweather['type']
    today_notice=todayweather['notice']
    desp=(
        '\n'+'#### ————— '+citys+' —————'+'\n'
        '#####'+nowdatetime+'——'+today_week+'\n'
        '#####空气质量：'+str(quality)+'\n'
        '#####AQI指数：'+str(today_aqi)+'\n'
        '#####pm2.5：'+str(pm25)+'\n'
        '#####pm10：'+str(pm10)+'\n'
        '####——————————————'+'\n'
        '####天气状况：\n'
        '#####'+str(today_low)+'~'+str(today_high)+'\n'
        '#####'+str(today_type)+'\n'
        '#####'+str(today_notice)+'\n'
        '#####'+str(today_fx)+str(today_fl)+'\n'
        '####——————————————'+'\n')
 
 
def upserver():
    global desp,sckey
    data={
        'text':'天气预报',
        'desp':desp
    }
    url=('https://sc.ftqq.com/%s.send'%sckey)
    server=requests.post(url=url,data=data)
 
def main_handler(event, context):
    global status,city,sckey
    getweather()
    if status != 200:
        status = '获取失败'
        print(status)
        url = ('https://sc.ftqq.com/%s.send'%sckey)
        data = {
            'text':'天气预报推送失败',
            'desp':'天气预报推送失败'
        }
        server=requests.post(url=url,data=data)
    else:
        upserver()
