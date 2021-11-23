# -*- coding:gbk -*-
import web
import copy
import time
import pymysql
#用于配置可以访问的页面
urls = (
    '/', 'index',
    '/add', 'add',
    '/user','user',
    '/system','system',
    '/manager','manager',
    '/user1','user1',
    '/goods','goods',
    '/yemian','yemian',
    '/sign','sign',
    '/down','down',
    '/proorder','proorder',
    '/lookgoods','lookgoods',
    '/operation','operation',
    '/noprocess','noprocess',
    '/comorder','comorder',
    '/message','message',
    '/updateuser','updateuser',
    '/update','update',
    '/myorder','myorder',
    '/modifygoods','modifygoods',
    '/addgoods','addgoods',
    '/delete','delete',
    '/propay','propay',
    '/payment','payment',
    '/nopay','nopay'
)
#i 为用户编号 ， username为用户名，dingdanhao为生成的订单编号
i = 0
dingdanhao = 0
first = 0
username = ""
gonghuo = 'true'
#生成实例
app = web.application(urls, globals())
#配置调用模板的位置
render = web.template.render('templates/')
#配置数据库
db = web.database(dbn='mysql',user='beta1025',db='stu',host="152.136.15.161",pw="123456",charset='gbk')
#在建数据库的时候需要统一编码，否则会出现问题

#未支付的订单
class nopay:
    def GET(self):
        sql = "select * from orders,orderdetail where pay='NO' AND orders.ordnum=orderdetail.ordnum"
        dingdan = db.query(sql)
        dingdanxiangqing = db.select('orderdetail')
        return render.comorder(dingdan, dingdanxiangqing)

#处理在个人订单中完成支付的订单
class payment:
    def POST(self):
        i = web.input()
        sql = "update orders set pay=" + "'" + "YES" + "'" + " where ordnum=" + "'" + i.ordnum + "'"
        db.query(sql)
        return "<script>alert('pay successful');window.location='/myorder';</script>"

#处理支付的订单
class propay:
    def POST(self):
        i = web.input()
        sql = "update orders set pay="+"'"+"YES"+"'"+" where ordnum="+"'"+i.ordnum+"'"
        db.query(sql)
        return "<script>alert('pay successful');window.location='/goods';</script>"

#删除商品
class delete:
    def POST(self):
        i = web.input()
        sql = "delete from goods where xingming="+"'"+i.xingming1+"'"
        db.query(sql)
        return "<script>alert('delete successful');window.location='/lookgoods';</script>"

#处理添加商品
class addgoods:
    def POST(self):
        i = web.input()
        sql0 = "select * from goods"
        w = db.query(sql0)
        first = []
        for z in w:
            first.append(z.xingming)
        if i.xingming in first:
                return "<script>alert('goods is exist');window.history.back(-1);</script>"
        else:
            sql = "insert into goods(classifynum,facnum,xingming,unitfee,num) values ("+"'"+i.classifynum+"'"+","+"'"+i.facnum+"'"+","+"'"+i.xingming+"'"+","+"'"+i.unitfee+"'"+","+"'"+i.num+"'"+")"
            db.query(sql)
            return "<script>alert('add successful');window.location='/lookgoods';</script>"

#新增商品
class modifygoods:
    def GET(self):
        sql = "select * from fac"
        a = db.query(sql)
        return render.modifygoods(a)

#用户查看我的订单
class myorder:
    def GET(self):
#        insert into a values('a','b','c')
        #使用之前定义的的usernamne
        global username
        sql0 = "select * from custome where cusname = " + "'"+username + "'"
        yonghu1 = db.query(sql0)
        for yonghu in yonghu1:
            print(yonghu)
        sql = "select * from orders where cuscode = " + "'"+yonghu.cuscode+ "'"
        dingdan = db.query(sql)

        return render.myorder(dingdan,username)

#管理员补货界面
class update:
    def POST(self):
        i = web.input()
        num1 = int(i.num)
        sql1 = "select * from goods where xingming="+"'"+i.xingming+"'"
        print(sql1)
        a = db.query(sql1)
        print(a)
        for z in a:
            print(z.num)

        c = int(z.num)
        num =c+num1
        num = str(num)
        a = i.xingming
        sql = "update goods set num = "+"'"+ num +"'"+ "where xingming = " +"'"+i.xingming+"'"
        print(sql)
        db.query(sql)
        raise web.seeother('/lookgoods')

#用户更新个人信息界面
class updateuser:
    def POST(self):
        i = web.input()
        global username
        sql0 = "update custome set name=" + "'" + i.name + "'" + "," + "mail=" + "'" + i.mail + "'" + "," + "tel=" + "'" + i.tel + "'" + "," + "address=" + "'" + i.address + "' " + "where cuscode=" + " '" + username + "'"
        sql2 = "update user set password=" + "'" + i.password + "' " + "where username=" + " '" + username + "'"
        print(sql2)
        print(sql0)
        db.query(sql0)
        db.query(sql2)
        #更新之后刷新本页面
        raise web.seeother('/message')

#用户查看个人信息界面
class message:
    def GET(self):
        global username
        sql = "select * from custome where cusname = "+ "'"+username+ "'"
        a1 = db.query(sql)
        sql2 = "select * from user where username = "+ "'"+username+ "'"
        b1 = db.query(sql2)
        # for a in a1:
        #     print(a)
        # for b in b1:
        #     print(b)
        return render.message(a1, b1, username)

#管理员查看已完成订单页面
class comorder:
    def GET(self):
        sql = "select * from orders,orderdetail where sendgoods = 'true' AND orders.ordnum=orderdetail.ordnum"
        dingdan = db.query(sql)
        dingdanxiangqing = db.select('orderdetail')
        return render.comorder(dingdan, dingdanxiangqing)

#管理员查看未完成订单页面
class noprocess:
    def GET(self):
        sql = "select * from orders,orderdetail where sendgoods = 'false' AND orders.ordnum=orderdetail.ordnum"
        dingdan = db.query(sql)
        dingdanxiangqing = db.select('orderdetail')
        return render.noprocess(dingdan, dingdanxiangqing)
#管理员处理用户提交的订单的类
class operation:
    def POST(self):
        shijian = time.strftime('%Y-%m-%d', time.localtime(time.time()))

        i = web.input()
        sql = "update orders set sendgoods = 'true' where ordnum =" + i.ordnum
        sql1 = "update orders set transdate = "+"'"+shijian+ "'" +"where ordnum = "+"'"+i.ordnum+"'"
        print(sql)
        db.query(sql1)
        db.query(sql)
        return render.operation()

#管理员登陆成功页面
class system:
    def GET(self):
        #w = web.input()
        return render.system()

#用户登陆界面
class index:

    def GET(self):
        #email = db.select('user')
        #跳转到add页面是为获取用户输入，但是add实际上并不存在，跳转之后马上跳转回主页面（相当于刷新功能）
        # 保存用户登陆信息
        global username
        username = ""
        return render.index1()

#处理用户注册的信息
class manager:

    def POST(self):
        name = db.select('user')
        global i
        i = i + 1
        shijian2 = time.time()
        shijian2 = str(shijian2)
        wuwu = shijian2.split('.')
        zidian = {}
         #render.add()
        for me in name:
           zidian[me.username] = me.password

        w = web.input()
        www = str(w.cusname)
#判断输入的用户名是否为已经存在的
        if w.cusname in zidian:
            return "<script>alert('user is exist');window.history.back(-1);</script>"
        else:
            a = str(i)
            #sql = "insert into orders values ("+"'"+wuwu[0]+"'"+","+"'"+w.cusname+"'"+","+"'"+w.name+"'"+","+"'"+w.address+"'"+","+"'"+w.mail+"'"+","+"'"+w.tel+"'"
            #sql = "insert into orders(ordnum,cuscode,lable,transfee,feelist,sendgoods,orddate,need)values (" + "'" +wuwu[0] + "'" + "," + "'" + kehu.cuscode + "'" + "," + "'" + gonghuo + "'" + "," + "'" + transfee + "'" + ",'" + xingming + "','" + "false" + "'" + "," + "'" + shijian + "'" + "," + "'" + i.need + "'" + ")"
            #db.query(sql)
            db.insert('custome',cuscode=wuwu[0], cusname=w.cusname, name=w.name, address=w.address, mail=w.mail, tel=w.tel)
            db.insert('user',username=w.cusname, password = w.password)
            return "<script>alert('sign successful,after 0 seconds,Jump to Home');</script><meta http-equiv='refresh' content='0;url=/'>"
            raise web.seeother('/')
        #return render.manager()

#用户点击登陆按钮后判断用户名和密码是否存在
class add:
    def POST(self):
        name = db.select('user')
        i = web.input()
        zidian = {}
      #  render.add()
        global username

        for w in name:
            zidian[w.username] = w.password

        if i.username in zidian:
            username = i.username
            if(zidian[i.username]==i.password):
                if i.username=='system':
                    raise web.seeother('/system')
                else:
                    raise web.seeother('/user')
            else:
                return "<script>alert('password is wrong');window.history.back(-1);</script>"
        else:
            return "<script>alert('user is not exsixt');window.history.back(-1);</script>"

#用户登陆成功界面
class user:
    def GET(self):
        global username
        return render.user(username)

#用户注册界面
class sign:
    def GET(self):
        return render.sign()

#浏览商品并下单界面
class goods:
    def GET(self):
        s = db.select('goods')
        b = db.select('goods')
        global username
        return render.goods(s,username,b)

#用户点击提交订单之后生成的订单页面
class down:
    def POST(self):
        global dingdanhao
        dingdanhao = dingdanhao + 1
        dingdanhao1 = str(dingdanhao)
        global username
        i = web.input()
        #获取商品姓名为 用户输入的商品
        sql1 = "select * from goods where xingming =" +"'"+ i.xingming+"'"
        goods = db.query(sql1)

        #获取当前登陆的用户的信息
        sql2 = 'select * from custome where cusname = ' +"'"+ username+"'"
        kehu1 = db.query(sql2)
        for zzz in goods:
            print(zzz)
        for kehu in kehu1:
            print(kehu)

        a = int(i.num)
        b = a
        global gonghuo

        c = int(zzz.num)
        #判断用户选择的数量是否可以购买
        if (a>c):
            return "<script>alert('sum is not enough');window.history.back(-1);</script>"
        else:
            if(a>2):
                yunfee = 0

            else:
                yunfee = 20
                a = c - a

        transfee = str(yunfee)

        #此处存在数据库中表的名是否是关键字的问题!!!!!!!!!!!!!!!!!
        a = str(a)
        shijian = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        shijian2 = time.time()
        print(shijian2)
        print(shijian)
        shijian2 = str(shijian2)
        wuwu = shijian2.split('.')
        nms = shijian2.split('.')
        print(nms[0])
        pay = "NO"
        xingming = str(i.xingming)
        sql = "insert into orders(ordnum,cuscode,lable,transfee,feelist,sendgoods,orddate,need,pay)values ("+"'"+wuwu[0]+"'"+","+"'"+kehu.cuscode+"'"+","+"'"+gonghuo+"'"+","+"'"+transfee+"'"+",'"+xingming+"','"+"false"+"'"+","+"'"+shijian+"'"+","+"'"+i.need+"'"+","+"'"+pay+"'"+")"
        sqlq = "update goods set num=" + "'"+ a+"'"+"where xingming="+"'"+ i.xingming+"'"

        #将订单插入数据库
        db.query(sql)
        #计算货物总价
        db.query(sqlq)
        a = int(a)
        danjia = int(zzz.unitfee)
        num1 = danjia * b + yunfee
        num = str(num1)
        # 订单详情插入数据库
        facnum = str(zzz.facnum)

        selectfac = "select * from fac where facnum = "+ "'"+ facnum +"'"
        print(selectfac)
        fac = db.query(selectfac)
        print(fac)
        first = []
        for fac2 in fac:
            first.append(fac2)
            print(fac2)

        facname = str(first[0].facname)
        classifynum = str(zzz.classifynum)
        shuliang = str(i.num)
        sumfee = str(num)
        sql3 = "insert into orderdetail(detailnum,ordnum,classifynum,facname,num,sumfee) values("+"'"+wuwu[0]+"'"+','+"'"+wuwu[0]+"'"+','+"'"+classifynum+"'"+','+"'"+facname+"'"+','+"'"+shuliang+"'"+','+"'"+sumfee+"'"+")"
        db.query(sql3)

        first.clear()
        #将用户输入，当前登陆的客户信息，能否供货，订单号，运费，总价传入
        return render.down(i, kehu, zzz, gonghuo, wuwu[0],yunfee,num,shijian,pay)

#管理员处理用户订单界面
class proorder:
    def GET(self):
        i = 0
        sql = "select * from orders,orderdetail where sendgoods = 'false' AND pay='YES' AND orders.ordnum=orderdetail.ordnum "
        dingdan = db.query(sql)
        x = db.query(sql)
        y = db.query(sql)
        #x = copy.deepcopy(dingdan)
        dingdanxiangqing = db.select('orderdetail')
        for www in x:
            i = i+ 1
        if(i<1):
            return "<script>alert('All orders have been processed,will be back');window.location='/system'</script>"
        else:
            return render.proorder(dingdan, dingdanxiangqing,y)

#补充货物界面
class lookgoods:
    def GET(self):
        s = db.select('goods')
        d = db.select('goods')
        return render.lookgoods(s,d)

if __name__ == "__main__":
    app.run()