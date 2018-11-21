#-*- coding: UTF-8 -*-
# @Author  : countofdane
# @Email   : countofdane@163.com
# @Blog    ：https://blog.csdn.net/countofdane

import datetime,time,calendar

class  TimeMachine(object):

    def convert_to_datetime(self,datetime_str):
        # nowdate = '2017-05-02 12:34:40'
        date1 = time.strptime(datetime_str, "%Y-%m-%d %H:%M:%S")
        day1 = datetime.datetime(date1[0], date1[1], date1[2], date1[3], date1[4], date1[5])
        # print(day1)
        # print(type(day1))
        return day1

    #时间转换为时间戳
    def convert_to_stamp(self,nowdate):
        ret = 0;
        if type(nowdate) == str :
            date1 = time.strptime(nowdate, "%Y-%m-%d %H:%M:%S")
            day1 = datetime.datetime(date1[0], date1[1], date1[2], date1[3], date1[4], date1[5])
            ret = int(time.mktime(day1.timetuple()))
        else:
            ret = int(time.mktime(nowdate.timetuple()))
        return ret

    #获取当前标准格式时间
    def get_now_datetime(self):
        return  time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))


    def stamp_convert_to_datetime(self,stamp):
        return time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(int(stamp)))

    #回到过去的月份
    def back_month_ago(self,nowdate,count):
        print("回到过去的月份")
        print(nowdate)
        print(count)
        if type(nowdate) == str :
            nowdate = time.strptime(nowdate, "%Y-%m-%d %H:%M:%S")
            nowdate = datetime.datetime(nowdate[0], nowdate[1], nowdate[2], nowdate[3], nowdate[4], nowdate[5])
        year = nowdate.year
        month = nowdate.month
        day = nowdate.day
        flag = 0
        if count > 0:
            while(count>0):
                month-=1
                count-=1
                if (month<1):
                    year-=1
                    month=12
                dayofthismonth = int(calendar.monthrange(year,month)[1])#获得当前月份的天数，以便区别此月是28，29，30，31天？
                if (day<dayofthismonth):
                    flag = 1 # 为1表示制造过程正常；
                else:
                    flag = 0 #为0表示此种情况不存在；
            if  flag > 0 :
                date = datetime.datetime(year, month, day, nowdate.hour, nowdate.minute, nowdate.second)
            else:
                date = datetime.datetime(1970, 1, 1, 0, 0, 0)
        else:
            date = datetime.datetime(year, month, day, nowdate.hour, nowdate.minute, nowdate.second)
            flag = 1
        return [flag,date]


    #穿越到未来的月份
    def to_future_month(self,nowdate,count):
        year = nowdate.year
        month = nowdate.month
        day = nowdate.day
        while (count > 0):
            month+=1
            if (month >=13 ):
                year+=1
                month = 1
            count =count - 1
            dayofthismonth = int(calendar.monthrange(year,month)[1])#获得当前月份的天数，以便区别此月是28，29，30，31天？
            if (day > dayofthismonth):
                day = dayofthismonth
        date = datetime.datetime(year, month, day, nowdate.hour, nowdate.minute, nowdate.second)
        return [1,date]

    #回到过去的几天
    def back_days_ago(self,nowdate,backday):
        if type(nowdate) == str :
            nowdate = time.strptime(nowdate, "%Y-%m-%d %H:%M:%S")
            nowdate = datetime.datetime(nowdate[0], nowdate[1], nowdate[2], nowdate[3], nowdate[4], nowdate[5])
        backdayAgo = (nowdate - datetime.timedelta(days= int(backday)))
        # 转换为时间戳:
        #timeStamp = int(time.mktime(threeDayAgo.timetuple()))
        # 转换为其他字符串格式:
        backdaytime = backdayAgo.strftime("%Y-%m-%d %H:%M:%S")
        return [1,backdaytime]

    #穿越到未来几天
    def to_future_day(self,nowdate,day):
        if type(nowdate) == str :
            nowdate = time.strptime(nowdate, "%Y-%m-%d %H:%M:%S")
            nowdate = datetime.datetime(nowdate[0], nowdate[1], nowdate[2], nowdate[3], nowdate[4], nowdate[5])
        backdayAgo = (nowdate + datetime.timedelta(days= day))
        # 转换为时间戳:
        #timeStamp = int(time.mktime(threeDayAgo.timetuple()))
        # 转换为其他字符串格式:
        backdaytime = backdayAgo.strftime("%Y-%m-%d %H:%M:%S")
        return [1,backdaytime]



    #处理时间的总函数
    def handle_datetime(self,nowdate, month=0, days=0):
        month = int(month)
        days = int(days)
        date = time.strptime(nowdate, "%Y-%m-%d %H:%M:%S")
        nowdate = datetime.datetime(date[0], date[1], date[2], date[3], date[4], date[5])
        flag = [1, nowdate]
        if month < 0:
            month = 0-month
            flag = back_month_ago(nowdate, month)
        elif month > 0:
            flag = to_future_month(nowdate, month)
        if flag[0]> 0:
            days = 0-days
            flag =  back_days_ago(flag[1], days)
        return flag

    #计算两个日期之间的天数差    day1>day2
    def count_days(self,day1, day2):
        if type(day1) == str :
            date1 = time.strptime(day1, "%Y-%m-%d %H:%M:%S")
            day1 = datetime.datetime(date1[0], date1[1], date1[2], date1[3], date1[4], date1[5])
        if type(day2) == str :
            date2 = time.strptime(day2, "%Y-%m-%d %H:%M:%S")
            day2 = datetime.datetime(date2[0], date2[1], date2[2], date2[3], date2[4], date2[5])
        return (day2-day1).days


    #回到几个小时之前
    def back_hours_ago(self,nowdate,backhours):
        backhourAgo = (nowdate - datetime.timedelta(hours= backhours))
        # 转换为时间戳:
        #timeStamp = int(time.mktime(threeDayAgo.timetuple()))
        # 转换为其他字符串格式:
        backhourtime = backhourAgo.strftime("%Y-%m-%d %H:%M:%S")
        return backhourtime


    #穿越到几个小时之后
    def to_future_hour(self,nowdate,hour):
        futurehourAgo = (nowdate + datetime.timedelta(hours= hour))
        # 转换为时间戳:
        #timeStamp = int(time.mktime(threeDayAgo.timetuple()))
        # 转换为其他字符串格式:
        futuretime = futurehourAgo.strftime("%Y-%m-%d %H:%M:%S")
        return futuretime


    #调整时间的函数
    def tune_time(self,nowdate,hours):
        date1 = time.strptime(nowdate, "%Y-%m-%d %H:%M:%S")
        day1 = datetime.datetime(date1[0], date1[1], date1[2], date1[3], date1[4], date1[5])
        hours = int(hours)
        if hours < 0:
            hours = 0 - hours
            flag = back_hours_ago(day1,hours)
        else:
            flag = to_future_hour(day1,hours)
        return flag


    #获取时间的小时部分
    def get_hour_time(self,nowdate):
        print("********----------************************")
        print(nowdate)
        print(type(nowdate))
        if type(nowdate) == str:
            nowdate = time.strptime(nowdate, "%Y-%m-%d %H:%M:%S")
            nowdate = datetime.datetime(nowdate[0], nowdate[1], nowdate[2], nowdate[3], nowdate[4], nowdate[5])
        hour_time_str = nowdate.strftime("%H:%M:%S")
        print("********----------************************")
        print(nowdate)
        print(type(nowdate))
        print(hour_time_str)
        ret = {'hour_time':hour_time_str}
        return ret

    #获取时间的日期部分
    def get_day_time(self,nowdate):
        if type(nowdate) == str:
            nowdate = time.strptime(nowdate, "%Y-%m-%d %H:%M:%S")
            nowdate = datetime.datetime(nowdate[0], nowdate[1], nowdate[2], nowdate[3], nowdate[4], nowdate[5])
        day_time_str = nowdate.strftime("%Y-%m-%d")
        ret = {'day_time':day_time_str}
        return ret




# tm = TimeMachine()
# print("------**********--------")
# he = tm.get_now_datetime()
# print(he)
# print(tm.get_hour_time(he))
