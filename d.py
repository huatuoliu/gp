import urllib
import urllib2
import time
import sys
import os
import re
import json
import datetime

def getkey(mytuple):
    return mytuple[2]

def getreply(url):
    response = urllib2.urlopen(url)
    html = response.read().decode('gb2312').encode('utf-8')
    return html

def print_stock():
    testInfo = {}
    while True:
        dateStr = str(datetime.datetime.now().strftime("%Y-%m-%d"))
        fileName = "foo"+dateStr+".txt"
        fo = open(fileName, "a+")
        while True:
            if not(113001 > int(time.strftime("%H%M%S")) > 92500 or 150101 > int(time.strftime("%H%M%S")) > 130000):
                time.sleep(60)
                if 90000 > int(time.strftime("%H%M%S")) > 70000:
                    testInfo = {}
                continue
            else:
                break
        try:
            stocklist=['sh000001','sz399006','sh601989',"sz002460","sh601088"]
            stocks=','.join(stocklist)
            url = 'http://hq.sinajs.cn/list='+stocks
            html = getreply(url)
            linelist=html.split(';')

            stockinfolist=[]
            for line in linelist:
                line=line[4:-1]
                kvlist=line.split('=')
                if len(kvlist)<2:
                    continue
                #print kvlist
                dataline=kvlist[1]
                datalist=dataline.split(',')
                name=datalist[0][1:100]
                current=datalist[3]
                percent=(float(datalist[3])-float(datalist[2]))/float(datalist[2])*100
                stockinfolist.append((name,current,percent))


            linenb = 1
            sortedstock=sorted(stockinfolist,None,getkey,True)
            for info in sortedstock:
                name=info[0]
                current=info[1]
                percent=info[2]
                if len(name)==3:
                    name=name+'  '
                if percent<0:
                    strpercent=str(percent)[0:5]+'%'

                else:
                    strpercent=' '+str(percent)[0:4]+'%'

                mystockinfo = name+'  '+current+ '   '+strpercent
                if not testInfo.has_key(name):
                    testInfo[name]={"list":[]}
                    testInfo[name]["list"].append(float(current))
                    testInfo[name]["percent"] = strpercent
                else:
                    testInfo[name]["list"].append(float(current))
                    testInfo[name]["percent"] = strpercent
                maxV = max(testInfo[name]["list"])
                minV = min(testInfo[name]["list"])
                printStr = name+'|  cur:'+current+'| '+strpercent+'| max:'+str(maxV)[0:5]+'| perMax:'+str((float(current)/float(maxV)-1)*100)[0:5]+'| min:'+str(minV)[0:5]+'| perMin:'+str((float(current)/float(minV)-1)*100)[0:5]
                fo.write( "%s\n" % printStr )
                fo.flush()
                '''
                if abs(float(percent)) > 1:
                    print printStr
               '''
                if '-' == strpercent[0]:
                    #print mystockinfo
                    pass
                else:
                    #print mystockinfo
                    pass
                linenb+=1
            timeStr = "------------"+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            fo.write( "%s\n" % timeStr )
            fo.flush()
            #print timeStr
        except Exception as inst:
            s=sys.exc_info()
            print "Error '%s' happened on line %d" % (s[1],s[2].tb_lineno)
            print inst
        time.sleep(30)
        fo.close()

def daemonize(noout=False):
    if noout:
        fd = open(os.devnull, 'w')
        sys.stdout = fd
        sys.stderr = fd
        os.dup2(fd.fileno(), 0)
        os.dup2(fd.fileno(), 1)
        os.dup2(fd.fileno(), 2)
    pid = os.fork()
    if pid > 0:
        sys.exit(0)
    os.setsid()
    os.umask(0)
    pid = os.fork()
    if pid > 0:
        sys.exit(0)


if __name__ == '__main__':
    daemonize(True)
    print_stock()
