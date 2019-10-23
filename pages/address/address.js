// pages/address/address.js
Page({
  data: {

  },

  onLoad: function (options) {

  },

  submitdate:function(event){
    var that = this;
    var boss = event.detail.value;
    console.log(event.detail.value);
    if (event.detail.value.username!=""&&boss.phone!=""&&boss.address!=""){
      wx.setStorage({
        key: 'address',
        data: event.detail.value,
      })
      that.onLoad();
      that.setData({
        information: "",
      })
      wx.showToast({
        title: '提交成功',
        icon: 'succes',
        duration: 1000,
        mask: true
      })
    }
    else{
      wx.showToast({
        title: '有信息为空，请重新输入信息',
        image: '/images/6.png',
        duration: 2000
      })
    }
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