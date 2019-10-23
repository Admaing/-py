// pages/me/me-order/me-order.js
var app = getApp();
Page({

  data: {
    hidden: true
  },

  onLoad: function (options) {
    var a = app.globalData;
    console.log(a.openid);
    var c = {
      w: a.openid
    }
    var that = this;
    wx.request({
      url: 'http://127.0.0.1:8080/me_issue',
      data: c,
      method: "POST",
      header: {
        //设置参数内容类型为x-www-form-urlencoded
        'content-type': 'application/json'
      },
      success: function (res) {
        console.log(res)

        //  res.data 是包含以上定义的两条记录的数组
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
      }

    })
  },
  //   onLoad: function (options) {
  //     var a = app.globalData;
  //  //   console.log(a.openid);
  //     var that = this;
  //     wx.cloud.init();
  //     const db = wx.cloud.database();
  //     db.collection('Waimai').where({
  //       backlogid: a.openid,
  //     })
  //       .get({
  //         success(res) {
  //           // res.data 是包含以上定义的两条记录的数组
  //           //      console.log(res.data)
  //           if (res.data.length == 0) {
  //             that.data.hidden = false;
  //    //         console.log(that.data.hidden)
  //             that.setData({
  //               hidden: that.data.hidden
  //             })
  //           } else {
  //             that.data.hidden = true;
  //             that.setData({
  //               hidden: that.data.hidden
  //             })
  //           }
  //           that.setData({
  //             userList: res.data,
  //           })
  //         }
  //       })
  //   },



  // onReady: function () {

  // },

  deleted: function (event) {

    wx.cloud.init();
    var that = this;
    //   console.log(that.data.aopenid)
    var db = wx.cloud.database();
    wx.showModal({
      title: '删除任务',
      content: '是否删除',
      success: function (res) {
        if (res.confirm) {

          wx.cloud.callFunction({
            name: 'delete',
            data: {
              _id: event.target.dataset.postid
              //    backlogid: that.data.aopenid
            },
            success: res => {
              that.onLoad();
              wx.showToast({
                title: '删除成功',
              })
              console.log('更新数据成功')
            }
          })
        }
      }
    })
  },


  onShow: function () {

  },

  /**
   * 生命周期函数--监听页面隐藏
   */
  onHide: function () {

  },

  /**
   * 生命周期函数--监听页面卸载
   */
  onUnload: function () {

  },

  /**
   * 页面相关事件处理函数--监听用户下拉动作
   */
  onPullDownRefresh: function () {

  },

  /**
   * 页面上拉触底事件的处理函数
   */
  onReachBottom: function () {

  },

  /**
   * 用户点击右上角分享
   */
  onShareAppMessage: function () {

  }
})