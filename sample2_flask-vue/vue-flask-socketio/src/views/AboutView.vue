<template>
  <div>
    <span>flask返回的数据:</span>
    <br>
    <span>{{ data }}</span>
  </div>
</template>

<script>
import io from 'socket.io-client'; // 导入 socket.io-client 库
export default {
  data() {
    return {
      data: {},   // 获取后端发送的消息
    }
  },
  created() {
    this.socket = io('http://localhost:5000/dcenter');
    // 监听后端发送的事件，例如 'dcenter' 事件
    this.socket.on('dcenter', (res) => {
      console.log(res); // 处理接收到的数据
      this.data = res.data
      // 在这里可以对接收到的数据进行处理，例如更新组件的 data 属性等
    });

    // 监听连接成功事件
    this.socket.on('connect', () => {
      console.log('连接成功'); // 处理连接成功后的操作
    });

    // 监听连接断开事件
    this.socket.on('disconnect', () => {
      console.log('连接断开'); // 处理连接断开后的操作
    });
  },
  // sockets: {    // socket.io携带，与watch/create/data等同级
  //   connect: function () {
  //     console.log('连接成功')   // 判断是否正确连接上后端
  //   },

  //   dcenter: function (data) {    // api为对应后端发出的信息接口，可自行更换
  //     console.log(data);
  //     this.data = data      // 获取后端发出的信息

  //   }
  // },

  // mounted() {    // 在组件开始渲染时进行调用
  //   this.$socket.connect() // socket连接
  //   // this.$socket.emit('/my_event')  // 发送消息:对应后端test测试函数
  //   console.log('连接中')
  // },

  destroyed() {    // 当离开组件时，结束调用
    if (this.$socket) this.$socket.disconnect()  // 如果socket连接存在，销毁socket连接
    console.log('连接已断开')
  }

}
</script>


