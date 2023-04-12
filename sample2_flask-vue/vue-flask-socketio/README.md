# vue-flask-socketio

## Project setup
```
npm install
```

### Compiles and hot-reloads for development
```
npm run serve
```
### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).

```
socketio写在About页面
在python后端中，需要注意的两个点是 命名空间 namespace 和 事件 event_name
命名空间相当于一个虚拟路由，在后端中socketio通过emit向前端实时发送数据
socketio.emit(event_name, {'data': 'data'}, namespace=name_space)
```

```
在vue中配置socketio有两种用法，一种是在main.js全局配置，另一种在.vue文件中配置
这里我们选择第二种

import io from 'socket.io-client'; // 导入 socket.io-client 库

创建created，需要指定命名空间接受（发送）数据
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
```
