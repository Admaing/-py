App({

  globalData: {
    openid: ''
  },
  onLaunch: function() {
    var that = this;
    if (!wx.cloud) {
      console.error('请使用 2.2.3 或以上的基础库以使用云能力')
    } else {
      wx.cloud.init({
        traceUser: true,
      })
    }
    wx.login({
      success: function(res) {
        //请求自己后台获取用户openid
        wx.request({
          url: 'https://30paotui.com/user/wechat',
          data: {
            appid: 'wxb3f10259e8a20499',
            secret: 'bb9ae3ab1575d3e23364d0df24010119',
            code: res.code
          },
          success: function(response) {
            //     console.log(response.data.openid);
            //可以把openid存到本地，方便以后调用
            //  wx.setStorageSync('openid', openid);
            that.globalData.openid = response.data.openid;
          }
        })
      }
    })
  },

  /**
   * 当小程序启动，或从后台进入前台显示，会触发 onShow
   */
  onShow: function(options) {

  },

  /**
   * 当小程序从前台进入后台，会触发 onHide
   */
  onHide: function() {

  },

  /**
   * 当小程序发生脚本错误，或者 api 调用失败时，会触发 onError 并带上错误信息
   */
  onError: function(msg) {

  }
})