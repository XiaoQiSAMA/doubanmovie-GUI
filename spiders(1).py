from multiprocessing.pool import Pool
import requests
import re
import pymysql
from urllib.parse import quote
import time
import _thread

from bs4 import BeautifulSoup

headers = {
    # 'cookies':'Cookie: ll="118183"; bid=zksOhnJp1UE; __yadk_uid=79PXDbNAk6o41loW7xQCUod4zei6f20e; __gads=ID=1719db48b4f4af7f:T=1560474098:S=ALNI_MYV1qPZiBvWaz-GV3lNaahA8e1SXw; _vwo_uuid_v2=D1C45CA091D224E98D7FC83878F5EDFA3|67438f7abd57e0dbe057ff800cecaf7e; trc_cookie_storage=taboola%2520global%253Auser-id%3Db36e206c-3aa0-4f47-9952-3ad42e83aab7-tuct3fc77a4; __utmz=30149280.1560474755.2.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmc=30149280; __utmc=223695111; __utmz=223695111.1560746134.8.4.utmcsr=baidu|utmccn=(organic)|utmcmd=organic|utmctr=%E8%B1%86%E7%93%A3; ap_v=0,6.0; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1560755066%2C%22https%3A%2F%2Fwww.baidu.com%2Fs%3Fwd%3D%25E8%25B1%2586%25E7%2593%25A3%26rsv_spt%3D1%26rsv_iqid%3D0xa9fc078b000000c9%26issp%3D1%26f%3D8%26rsv_bp%3D1%26rsv_idx%3D2%26ie%3Dutf-8%26tn%3Dbaiduhome_pg%26rsv_enter%3D1%26rsv_sug3%3D5%26rsv_sug1%3D3%26rsv_sug7%3D100%26rsv_t%3Dd0c6J%252B45dZ%252Fn8nTGJ%252F%252BgwR2TjMN0%252Bt9X%252FlC%252FjF3m8UbaHBvWz%252B9pxVMnI4h2c4lpS2jR%22%5D; _pk_ses.100001.4cf6=*; __utma=30149280.811583953.1560474086.1560749801.1560755066.10; __utma=223695111.1293088587.1560474086.1560749801.1560755066.10; __utmb=223695111.0.10.1560755066; ct=y; douban-fav-remind=1; __utmt=1; __utmb=30149280.7.5.1560756202026; dbcl2="198086965:HYJ+U3GJ9yQ"; ck=VE6I; push_noty_num=0; push_doumail_num=0; _pk_id.100001.4cf6=9bec1a1ba7cef6be.1560474086.11.1560757039.1560752528.',
    # 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.90 Safari/537.36'
}
lastdy = 0
lastactor = 0
dbname = 'spiders'
moviedb = pymysql.connect(host='localhost', user='root', password='13021910302', port=3306, db=dbname)
cursor = moviedb.cursor()


def get_movie_detail(url):
    html = requests.get(url).text
    pname = 'v:itemreviewed">(.*?)</span>.*?</div>'
    pdaoyan = '<div id="info">.*?导演.*?">(.*?)</a>.*?</div>'
    pactor = 'v:starring">(.*?)</a>'
    psort = 'v:genre">(.*?)</span>.*?</div>'
    pcountrys = '制片国家/地区:</span> (.*?)<br/>.*?</div>'
    planguages = '语言:</span> (.*?)<br/>.*?</div>'
    ptimes = 'v:initialReleaseDate.*?content.*?>(.*?)</span>.*?</div>'
    plongs = '<div id="info">.*?片长.*?</span>.*?([0-9 ]+分钟.*?)<br/>.*?</div>'
    pimdbs = 'IMDb.*?">(tt.*?)</a><br>.*?</div>'
    preview = 'v:summary".*?>(.*?)</span>.*?</div>'
    paverage = '"ratingValue":.*?"(.*?)"'

    pdirectorids = '"director".*?\[.*?celebrity/(.*?)/.*?\]'
    pactorsids = '"actor".*?\[.*?celebrity/(.*?)/.*?\]'

    try:
        name = re.findall(pname, html, re.S)
        daoyan = re.findall(pdaoyan, html, re.S)
        actors = re.findall(pactor, html, re.S)
        # del actors[2:len(actors)]
        sorts = re.findall(psort, html, re.S)
        countrys = re.findall(pcountrys, html, re.S)
        languages = re.findall(planguages, html, re.S)
        times = re.findall(ptimes, html, re.S)
        longs = re.findall(plongs, html, re.S)
        average = re.findall(paverage, html, re.S)
        if longs:
            longs = re.sub('</span>', '', longs[0])
        else:
            longs = ''
        imdbs = re.findall(pimdbs, html, re.S)
        review = re.findall(preview, html, re.S)
        if review:
            review = re.sub(' ', '', review[0])
            review = re.sub('\n', '', review)
            review = re.sub('<br>', '', review)
            review = re.sub('<br/>', '', review)
            review = re.sub('\u3000', '', review)
        else:
            review = ''
    except:
        print('error')
        return {}

    try:

        directorids = re.findall(pdirectorids, html, re.S)
        actorsids = re.findall(pactorsids, html, re.S)

        for directorid in directorids:
            insertdb({'idindou': directorid}, 'daoyanid')
        for actorsid in actorsids:
            insertdb({'idindou': actorsid}, 'actorid')
    except:
        print('getdaoyan or actors id error')


    return {
        'name': name,
        'daoyan': daoyan,
        'actor': actors,
        'sort': sorts,
        'contury': countrys,
        'language': languages,
        'time': times,
        'chang': longs,
        'imdb': imdbs,
        'review': review,
        'average': average
    }


def get_moive_id(tag):
    html = requests.get('https://movie.douban.com/j/search_subjects?type=movie&tag=' + quote(
        tag) + '&sort=recommend&page_limit=1000&page_start=0', headers=headers).text
    print('https://movie.douban.com/j/search_subjects?type=movie&tag=' + quote(
        tag) + '&sort=recommend&page_limit=1000&page_start=0')
    p = 'id":"(.*?)"'
    result = re.findall(p, html)
    return result


def get_daoyan_detail(daoyanid):
    headers = {
        # 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0'
    }
    url = 'https://movie.douban.com/celebrity/' + daoyanid
    html = requests.get(url, headers=headers).text
    directors_info = {
        'name': '',
        'sex': '',
        'birthday': '',
        'birthplace': '',
        'imdb': '',
        'discribtion': '',
        'zuoping': ''
    }
    soup = BeautifulSoup(html, 'lxml')
    directors_info['name'] = soup.h1.string
    info = soup.find_all(class_='info')
    directors_info['sex'] = re.search('男|女', str(info)).group(0)
    print(directors_info)


def insertdb(param, tname):
    table = tname

    keys = ', '.join(param.keys())
    values = ', '.join(['%s'] * len(param))

    for key in param.keys():
        if key == 'chang' or key == 'review':
            continue
        param[key] = ', '.join(param[key])
    sql = 'INSERT INTO {table}({keys}) VALUES ({values})'.format(table=table, keys=keys, values=values)
    try:
        if cursor.execute(sql, tuple(param.values())):
            print('Successful')
            moviedb.commit()
    except:
        print('Failed')
        moviedb.rollback()


def searchdb(searchkey, tname):
    sql = 'select * from ' + str(tname) + ' where name = \'' + str(searchkey) + '\''
    print(sql)
    try:
        cursor.execute(sql)
        if cursor.fetchall():
            print('exsits')
            return 1
        else:
            print('new movie')
            return 0
    except:
        print('failed')


def create_table(sql):
    try:
        cursor = moviedb.cursor()
        cursor.execute(sql)
        print('creat_table')
    except:
        print('creat_table error')


def drop_table(sql):
    try:
        cursor = moviedb.cursor()
        cursor.execute(sql)
        print('drop_table')
    except:
        print('drop_table error')


def get_tags():
    html = requests.get('https://movie.douban.com/j/search_tags?type=movie&source=', headers=headers).text
    tp = '"(.*?)"'
    re.compile(tp)
    tags = re.findall(tp, html)
    tags.remove('tags')
    return tags


def finish_daoyan():
    global lastdy
    try:
        number = cursor.execute('SELECT * FROM spiders.movies;')
        for i in range(lastdy, number):
            idindou = cursor.execute('select * from  daoyanid where  id = ' + str(i))
            dy = get_daoyan_detail(idindou)
            print(dy)
            insertdb(dy, 'daoyan')
            print('for daoyan sleep 0.5')
            time.sleep(2)
        lastdy = number
    except:
        print('error in daoyan')
        lastdy = i + 1
        return finish_daoyan()



def finish_movies(tag):
    movieids = get_moive_id(str(tag))
    print(movieids)
    for movieid in movieids:
        url = 'https://movie.douban.com/subject/' + movieid + '/'
        print(url)
        md = get_movie_detail(url)
        if md == {}:
            print('for error sleep 0.5')
            time.sleep(0.1)
            continue
        # 依据电影名判断查重电影
        print(md)
        if searchdb(md['name'][0], 'movies') == 0:
            insertdb(md, 'movies')
            print('for succeed sleep 0.5')
            time.sleep(2)
        else:
            print('for exsits sleep 0.5')
            time.sleep(2)



#
# def finish_actor():
#     global lastactor
#     try:
#         for i in range(lastactor, cursor.execute('SELECT * FROM spiders.movies;')):
#             id = cursor.execute('select * from  where id = ' + str(i))
#             ac = get_daoyan_detail(id)
#             print(ac)
#             insertdb(ac, 'actor')
#             print('for daoyan sleep 0.5')
#             time.sleep(2)
#         lastdy=
#     except:
#         print('error in daoyan')
#         lastdy = i + 1
#
#
#
# def main():


if __name__ == '__main__':
    # 连接数据库
    drop_table('drop table if exists ' + 'movies')
    create_table(
        'create table if not exists ' + 'movies' + ' ( id int primary key AUTO_INCREMENT,name varchar(255), daoyan varchar(100), actor varchar(1000), sort varchar(255), contury varchar(255)' \
                                                   ', language varchar(255), time varchar(255), chang varchar(255), imdb varchar(255) , review varchar(1000),average varchar(5)) ')
    create_table('create table if not exists daoyanid (id int primary key AUTO_INCREMENT,id_in_dou int)')
    create_table('create table if not exists actorid (id int primary key AUTO_INCREMENT,id_in_dou int)')


    #
    # create_table('create table if not exists daoyan (id int primary key AUTO_INCREMENT,number int)')
    # create_table('create table if not exists actor (id int primary key AUTO_INCREMENT,number int)')
    #
    tags = get_tags()
    pool = Pool()
    pool.map(main, [tags[i] for i in range(0, len(tags))])
    moviedb.close()
