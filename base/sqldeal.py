import pymysql
from loguru import logger


def sqldeal(host='182.61.131.173', port=51006,database='sass',user='root',password='tahJoh3U',sql=''):
    try:
        db = pymysql.connect(host=host, port=port, user=user, password=password, database=database,
                             charset='utf8')
        cursor = db.cursor()
        cursor.execute(sql)
        db.commit()
        logger.info("sql执行成功，sql语句为：{}".format(sql))

    except :
        logger.warning("数据库连接或执行sql语句失败")


    #查询数据
    # lst_data = cursor.fetchall()
    # cursor.close()  # 关闭游标
    # db.close()  # 关闭数据库连接
    # return lst_data
