Page({
  data: {
    //用户个人信息
    userInfo: {
      avatarUrl: "",//用户头像
      nickName: "",//用户昵称
    }
  },

  me_issue:function(event){
    wx.navigateTo({
        url:'/pages/me/me-issue/me-issue'
      })
  },
  me_order: function (event) {
    wx.navigateTo({
      url: '/pages/me/me-order/me-order'
    })
  },


  onLoad: function () {
    var that = this;
    wx.getUserInfo({
      success: function (res) {
        console.log(res);
        var avatarUrl = 'userInfo.avatarUrl';
        var nickName = 'userInfo.nickName';
        that.setData({
          [avatarUrl]: res.userInfo.avatarUrl,
          [nickName]: res.userInfo.nickName,
        })
      }
    })
  },

  onShareAppMessage: function () {

    return {

      title: '自定义分享标题',

      desc: '自定义分享描述',

      path: '/page/user?id=123'

    }

  },

    address: function(event) {
      wx.navigateTo({
        url: '/pages/address/address',
      })
    
  }

})


/**
<view class='content'>
  <view class='common'>
    <view class='hr'>
      <text>我的发布</text>
    </view>
  </view>

  <view class='common'>
    <view class='hr'>
      <text>我的接单</text>
    </view>
  </view>
  <view class="classname">1.预约人:
    <text>{{orderInfo.username}}</text>
  </view>

</view> 

.yuansu{
  background-color:azure;
  height: 100vh;
  display: flex;
  flex-direction: column;
  justify-content:space-around;
  align-items: center;
}

.content{
  width:100%;
  height:100%;
  background: #f2f2f2;
  font-family: "宋体";
}
.common{
  position: relative;
  padding:40rpx;
  font-size:28rpx;
  font-family: "微软雅黑";
}
.hr
{
  height:0fr;
  background: #cecece;
}
.hr text{
  position:absolute;
  width:200rpx;
  text-align:center;
  background: #eeeeee;
  left:37%;
  top:20rpx;
}
*/

/**
<view class='content'>
  <view class='common'>
    <view class='hr'>
     <button class='common' catchtap='me_issue'>我的发布</button>
    </view>
  </view>

  <view class='common'>
    <view class='hr'>
      <button class='common' catchtap='me_order'>我的接单</button>
    </view>
  </view>
</view>  */