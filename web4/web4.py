# -*- coding:gbk -*-
import web
import copy
import time
import pymysql
#�������ÿ��Է��ʵ�ҳ��
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
#i Ϊ�û���� �� usernameΪ�û�����dingdanhaoΪ���ɵĶ������
i = 0
dingdanhao = 0
first = 0
username = ""
gonghuo = 'true'
#����ʵ��
app = web.application(urls, globals())
#���õ���ģ���λ��
render = web.template.render('templates/')
#�������ݿ�
db = web.database(dbn='mysql',user='beta1025',db='stu',host="152.136.15.161",pw="123456",charset='gbk')
#�ڽ����ݿ��ʱ����Ҫͳһ���룬������������

#δ֧���Ķ���
class nopay:
    def GET(self):
        sql = "select * from orders,orderdetail where pay='NO' AND orders.ordnum=orderdetail.ordnum"
        dingdan = db.query(sql)
        dingdanxiangqing = db.select('orderdetail')
        return render.comorder(dingdan, dingdanxiangqing)

#�����ڸ��˶��������֧���Ķ���
class payment:
    def POST(self):
        i = web.input()
        sql = "update orders set pay=" + "'" + "YES" + "'" + " where ordnum=" + "'" + i.ordnum + "'"
        db.query(sql)
        return "<script>alert('pay successful');window.location='/myorder';</script>"

#����֧���Ķ���
class propay:
    def POST(self):
        i = web.input()
        sql = "update orders set pay="+"'"+"YES"+"'"+" where ordnum="+"'"+i.ordnum+"'"
        db.query(sql)
        return "<script>alert('pay successful');window.location='/goods';</script>"

#ɾ����Ʒ
class delete:
    def POST(self):
        i = web.input()
        sql = "delete from goods where xingming="+"'"+i.xingming1+"'"
        db.query(sql)
        return "<script>alert('delete successful');window.location='/lookgoods';</script>"

#���������Ʒ
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

#������Ʒ
class modifygoods:
    def GET(self):
        sql = "select * from fac"
        a = db.query(sql)
        return render.modifygoods(a)

#�û��鿴�ҵĶ���
class myorder:
    def GET(self):
#        insert into a values('a','b','c')
        #ʹ��֮ǰ����ĵ�usernamne
        global username
        sql0 = "select * from custome where cusname = " + "'"+username + "'"
        yonghu1 = db.query(sql0)
        for yonghu in yonghu1:
            print(yonghu)
        sql = "select * from orders where cuscode = " + "'"+yonghu.cuscode+ "'"
        dingdan = db.query(sql)

        return render.myorder(dingdan,username)

#����Ա��������
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

#�û����¸�����Ϣ����
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
        #����֮��ˢ�±�ҳ��
        raise web.seeother('/message')

#�û��鿴������Ϣ����
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

#����Ա�鿴����ɶ���ҳ��
class comorder:
    def GET(self):
        sql = "select * from orders,orderdetail where sendgoods = 'true' AND orders.ordnum=orderdetail.ordnum"
        dingdan = db.query(sql)
        dingdanxiangqing = db.select('orderdetail')
        return render.comorder(dingdan, dingdanxiangqing)

#����Ա�鿴δ��ɶ���ҳ��
class noprocess:
    def GET(self):
        sql = "select * from orders,orderdetail where sendgoods = 'false' AND orders.ordnum=orderdetail.ordnum"
        dingdan = db.query(sql)
        dingdanxiangqing = db.select('orderdetail')
        return render.noprocess(dingdan, dingdanxiangqing)
#����Ա�����û��ύ�Ķ�������
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

#����Ա��½�ɹ�ҳ��
class system:
    def GET(self):
        #w = web.input()
        return render.system()

#�û���½����
class index:

    def GET(self):
        #email = db.select('user')
        #��ת��addҳ����Ϊ��ȡ�û����룬����addʵ���ϲ������ڣ���ת֮��������ת����ҳ�棨�൱��ˢ�¹��ܣ�
        # �����û���½��Ϣ
        global username
        username = ""
        return render.index1()

#�����û�ע�����Ϣ
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
#�ж�������û����Ƿ�Ϊ�Ѿ����ڵ�
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

#�û������½��ť���ж��û����������Ƿ����
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

#�û���½�ɹ�����
class user:
    def GET(self):
        global username
        return render.user(username)

#�û�ע�����
class sign:
    def GET(self):
        return render.sign()

#�����Ʒ���µ�����
class goods:
    def GET(self):
        s = db.select('goods')
        b = db.select('goods')
        global username
        return render.goods(s,username,b)

#�û�����ύ����֮�����ɵĶ���ҳ��
class down:
    def POST(self):
        global dingdanhao
        dingdanhao = dingdanhao + 1
        dingdanhao1 = str(dingdanhao)
        global username
        i = web.input()
        #��ȡ��Ʒ����Ϊ �û��������Ʒ
        sql1 = "select * from goods where xingming =" +"'"+ i.xingming+"'"
        goods = db.query(sql1)

        #��ȡ��ǰ��½���û�����Ϣ
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
        #�ж��û�ѡ��������Ƿ���Թ���
        if (a>c):
            return "<script>alert('sum is not enough');window.history.back(-1);</script>"
        else:
            if(a>2):
                yunfee = 0

            else:
                yunfee = 20
                a = c - a

        transfee = str(yunfee)

        #�˴��������ݿ��б�����Ƿ��ǹؼ��ֵ�����!!!!!!!!!!!!!!!!!
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

        #�������������ݿ�
        db.query(sql)
        #��������ܼ�
        db.query(sqlq)
        a = int(a)
        danjia = int(zzz.unitfee)
        num1 = danjia * b + yunfee
        num = str(num1)
        # ��������������ݿ�
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
        #���û����룬��ǰ��½�Ŀͻ���Ϣ���ܷ񹩻��������ţ��˷ѣ��ܼ۴���
        return render.down(i, kehu, zzz, gonghuo, wuwu[0],yunfee,num,shijian,pay)

#����Ա�����û���������
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

#����������
class lookgoods:
    def GET(self):
        s = db.select('goods')
        d = db.select('goods')
        return render.lookgoods(s,d)

if __name__ == "__main__":
    app.run()