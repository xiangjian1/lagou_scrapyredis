#coding:utf8
import json
import redis
import MySQLdb

def main():
    # 指定redis数据库信息
    try:
        rediscli = redis.StrictRedis(host='192.168.101.128', port=6379, db=0)
        # 指定mysql数据库
        mysqlcli = MySQLdb.connect(host='127.0.0.1', user='root', passwd='', db = 'practice', port=3306, charset='utf8')
    except Exception,e:
        print '数据库连接失败'
        print str(e)
        exit()

    while True:
        source, data = rediscli.blpop(["lagou:items"])
        # print source # redis里的键
        # print data # 返回的数据
        item = json.loads(data)

        try:
            # 使用cursor()方法获取操作游标
            cur = mysqlcli.cursor()
            # 使用execute方法执行SQL INSERT语句
            # sql = "insert ignore into lagou(url,company,position,salary_min,salary_max,location,work_years,degree,position_type,tags,pub_date,position_desc,work_address)" \
            #   "values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s',) "% (item['url'],item['company'], item['position'], item['salary_min'],item['salary_max'],item['location'],item['work_years'],item['degree'],item['position_type'],item['tags'],item['pub_date'],item['position_desc'],item['work_address'])
            sql = 'insert ignore into lagou(url,company,position,salary,location,work_years,degree,position_type,tags,pub_date,position_desc,work_address) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            cur.execute(sql, (item['url'], item['company'], item['position'], item['salary'], item['location'],item['work_years'], item['degree'], item['position_type'], item['tags'], item['pub_date'],item['position_desc'], item['work_address']))


            # sql = "insert into truelove(nick, age,crawled, spider,url) values('%s',%s, '%s', '%s','%s') on duplicate key update " \
            #       "nick=values(nick),age=values(age),crawled=values(crawled),spider=values(spider)" % (item['nick'], item['age'], item['crawled'], item['spider'],item['url'])
            #

            # cur.execute(sql)
            # 提交sql事务
            mysqlcli.commit()
            #关闭本次操作
            cur.close()
            print "inserted %s" % item['url']
        except Exception,e:
            print '插入失败'
            print str(e)

if __name__ == '__main__':
    main()