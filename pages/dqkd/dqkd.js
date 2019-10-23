var app = getApp();
Page({
  data: {
    hidden:true,
    openid:''
  },
  onPullDownRefresh: function() {
    console.log('onPullDownRefresh', '下拉刷新....');

    wx.stopPullDownRefresh();
    this.onLoad();
  },
  onLoad:function(option){
    var abcoepnid = app.globalData;
    //  console.log(abcoepnid);
    var that = this;
    wx.request({
      url: 'http://127.0.0.1:8080/dqkd',
      data: "",
      method: "POST",
      header: {
        //设置参数内容类型为x-www-form-urlencoded
        'content-type': 'application/json'
      },
      success: function (res) {
        console.log(res)

        //  res.data 是包含以上定义的两条记录的数组
          if(res.data.length==0){
            that.data.hidden = false;
   //         console.log(that.data.hidden)
            that.setData({
              hidden:that.data.hidden
            })
          }else{
            that.data.hidden =true;
            that.setData({
              hidden: that.data.hidden
            })
          }
          that.setData({
            userList: res.data,
          })
        }
      
    }),
    wx.login({
      success: function (res) {
        //请求自己后台获取用户openid
        wx.request({
          url: 'https://30paotui.com/user/wechat',
          data: {
            appid: 'wxb3f10259e8a20499',
            secret: 'bb9ae3ab1575d3e23364d0df24010119',
            code: res.code
          },
          success: function (response) {
            var openid = response.data.openid;
            abcoepnid = response.data.openid;
            //      console.log(abcoepnid);
            that.data.openid = response.data.openid;
            //console.log(that.data.aopenid);
            //可以把openid存到本地，方便以后调用
            //  wx.setStorageSync('openid', openid);
            that.data.openid = openid;
            that.setData({
              openid: openid
            })
          }
        })
      }
    })
  },
  // onLoad: function(option) {
  //   var abcoepnid = app.globalData;
  // //  console.log(abcoepnid);
  //   var that = this;
  //   wx.cloud.init();
  //   const db = wx.cloud.database();
  //   db.collection('Waimai').where({
  //       done: "false",
  //     })
  //     .get({
  //       success(res) {
  //      //   console.log(res);
          
  //         // res.data 是包含以上定义的两条记录的数组
  //         if(res.data.length==0){
  //           that.data.hidden = false;
  //  //         console.log(that.data.hidden)
  //           that.setData({
  //             hidden:that.data.hidden
  //           })
  //         }else{
  //           that.data.hidden =true;
  //           that.setData({
  //             hidden: that.data.hidden
  //           })
  //         }
  //         that.setData({
  //           userList: res.data,
  //         })
  //       }
  //     })
  //   //获取openid不需要授权
  //   wx.login({
  //     success: function(res) {
  //       //请求自己后台获取用户openid
  //       wx.request({
  //         url: 'https://30paotui.com/user/wechat',
  //         data: {
  //           appid: 'wxb3f10259e8a20499',
  //           secret: 'bb9ae3ab1575d3e23364d0df24010119',
  //           code: res.code
  //         },
  //         success: function(response) {
  //           var openid = response.data.openid;
  //           abcoepnid = response.data.openid;
  //     //      console.log(abcoepnid);
  //           that.data.openid = response.data.openid;
  //           //console.log(that.data.aopenid);
  //           //可以把openid存到本地，方便以后调用
  //           //  wx.setStorageSync('openid', openid);
  //           that.data.openid = openid;
  //           that.setData({
  //             openid: openid
  //           })
  //         }
  //       })
  //     }
  //   })
  // },

  getOpenid: function() {

    // console.log(openid)
  },


  a: function(event){
    var that = this;
    var a = app.globalData;
    console.log(event.currentTarget.dataset.postid);
    var c = {
      w: a.openid,
      id: event.currentTarget.dataset.postid,
    }
    wx.showModal({
      title: '领取任务',
      content: '是否领取',
      success: function (res) {
        if (res.confirm) {
          wx.request({
            url: 'http://127.0.0.1:8080/confirm',
            data: c,
            method: "POST",
            header: {
              //设置参数内容类型为x-www-form-urlencoded
              'content-type': 'application/json'
            },
            success: function (res) {
              console.log(res)

            //   //  res.data 是包含以上定义的两条记录的数组
              if (res.data.length == 0) {
                that.data.hidden = false;
                //         console.log(that.data.hidden)
                that.setData({
                  hidden: that.data.hidden
                })
              } else {
                that.data.hidden = true;
                that.setData({
                  hidden: that.data.hidden
                })
              }
              that.setData({
                userList: res.data,
              })
              // console.log('更新数据成功')
              that.onLoad();
              wx.showToast({
                title: '领取成功',
              })
            }

          })

        }
      }
    })
  },
  // a: function(event) {
  //   wx.cloud.init();
  //   var that = this;
  //   var db = wx.cloud.database();
  //   wx.showModal({
  //     title: '领取任务',
  //     content: '是否领取',
  //     success: function(res) {
  //       if (res.confirm) {

  //         wx.cloud.callFunction({
  //           name: 'sum',
  //           data: {
  //             _id: event.target.dataset.postid,
  //             backlogid: that.data.openid
  //           },
  //           success: res => {
  //             console.log('更新数据成功')
  //             that.onLoad();
  //             wx.showToast({
  //               title: '领取成功',
  //             })
  //           }
  //         })
  //       }
  //     }
  //   })

  // },

  // onAccept: function(event) {
  //   wx.cloud.callFunction({
  //     // 云函数名称
  //     name: 'sum',
  //     // 传给云函数的参数
  //     data: {
  //       a: 1,
  //       b: 2,
  //     },
  //     success(res) {
  //   //    console.log(res.result.sum) // 3
  //     },
  //     fail: console.error
  //   })
  // }

})