//index.js
//获取应用实例
var app = getApp()
Page({
  data: {
    informations: {
      time: "请输入时间",
      contacts: "请输入联系人",
      phone: "请输入电话",
      address: "请输入地址",
      yangshi: "请输入样式"
    }
  },
  //事件处理函数
  submitdate: function (event) {
    var that = this;
    var abc = event.detail.value;
    console.log(abc)
    //获取用户的oepnid
    var abcoepnid = app.globalData;
    //传入字典
    abc['usernames'] = abcoepnid.openid
    if (abc.date == '' || abc.phone == '') {
      that.setData({
        information:""
      });
      wx.showToast({
        title: '信息不符合要求，请重新输入信息',
        image: '/images/6.png',
        duration: 2000
      })

    }
    else {
      wx.request({
        url: 'http://127.0.0.1:8080/',
        data: abc,
        method: "POST",
        header: {
          //设置参数内容类型为x-www-form-urlencoded
          'content-type': 'application/json'
        },
        success: function (res) {
          console.log(res.data)
          that.setData({
            items: res.data
          })
        }
      })
      that.setData({
        information: ""
      })
    }

    // wx.cloud.init();
    // var db = wx.cloud.database();
    // if (abc.other != '' || abc.phone != '') {
    //   wx.cloud.callFunction({
    //         name: 'add',
    //         data: {
    //           a:abc
    //         },
    //         success: res => {
    //           console.log('更新数据成功')
    //           that.onLoad();
    //           that.setData({
    //             information: "",
    //            })
    //          }
    //         })/*
    //   db.collection('waimai').add({
    //     data: {
    //       a,
    //       done: 'false',
    //       backlogid: null
    //     }

    //   })
    //   //通过数据绑定，每次提交之后，清空input输入的值
    //   that.setData({
    //     information: "",
    //   });
    //   */
    //   wx.showToast({
    //     title: '提交成功',
    //     icon: 'succes',
    //     duration: 1000,
    //     mask: true
    //   })
    // } else {
    //   wx.showToast({
    //     title: '信息不符合要求，请重新输入信息',
    //     image:'/images/6.png',
    //     duration:2000
    //   })
    //   console.log("请重新输入数据");
    //   this.onLoad();
    // }
  }
})