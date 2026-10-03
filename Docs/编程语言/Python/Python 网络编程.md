# Python 网络编程

[[网络编程是干啥的]]
[[Socket（套接字)]]
[[服务端和客户端]]
[Python2模块]
[Socketserver]
[Twisted]

#### 网络编程是干啥的

**让两台电脑之间互相发消息、传数据,IP 地址 + 端口号**.

#### Socket（套接字)

 **网络通信的管道,两个电脑程序想聊天，就得各自建一个 socket，管道接通之后，就能来回传字节数据**.
 - TCP（可靠传输）
像打电话：接通之后，一对一聊天；消息不会丢、不乱序。
很多场景用 TCP：传图片、文件、摄像头数据流，工业视觉设备通信常用。
 - UDP（不可靠传输）
像发短信：直接扔数据包出去，不用先建立连接；不保证对方一定收到。
优点速度快；缺点丢包了也不会重传。直播、视频流偶尔会用。

#### 服务端 和 客户端

 - 服务端：一直待命，开好 socket，监听端口，等着别人连过来;
 - 客户端：主动发起连接，去找服务端


#### Python2模块

**专门用来写网络客户端，去网上拿资源（网页、图片）的工具包**，相当于封装好的简易浏览器**
- urllib：负责打开链接、下载文件、编码 url 参数
- urllib2：增强版，支持自定义请求头、处理网页登录、处理网页报错（404 这类）
- Python3 把这俩合并成了一个包：**urllib.request**，不再有 urllib2。
- 共同点：拼网址、发送请求、下载网页源码、下载图片。
- 缺点：功能简单，不支持 JS 渲染（拿不到动态网页内容）。
- 
#### Socketserver
**简化 socket 服务端代码的工具**
 - 前面讲原生 socket，写服务端要写 bind、listen、accept，代码繁琐。
 - Socketserver 把这些底层操作打包封装好了，你只需要写：收到消息之后怎么处理。

 - 原生 socket：要自己写全套接待流程（开门、等人、接消息）
 - Socketserver：房子大门、排队系统都给你建好，你只写客人来了之后干啥。

 - 支持两种：TCP 服务、UDP 服务。
 - 特点：默认**多线程 / 多进程**，可以同时接待多个客户端连接。

 - CV 场景：
 - 写简单图像接收服务，相机设备上传图片到你的程序，用它快速搭服务。
 - - 现状：属于标准库自带模块，Python3 还保留，小型测试工具能用，大型项目一般不用

#### Twisted
**老牌、功能强大的异步网络框架，用来写网络服务**
 - 普通 socket：排队处理，一个客户端任务没干完，后面的人等着（阻塞）。
 - Twisted：不用傻傻等待，在等待网络数据的时候，程序可以去处理别的任务
  - - 能干什么：TCP 服务、网页服务、自定义通信协议


```python

# 服务端
# =====服务端代码（等待别人连我）=====
import socket

# 创建tcp socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 绑定本机IP和端口
server_socket.bind(("127.0.0.1", 8888))
# 开始监听，最多排队5个连接
server_socket.listen(5)
print("等待客户端连接...")
# 等待客户端上门，拿到连接
conn, addr = server_socket.accept()
print("客户端来了", addr)

# 接收客户端发来的数据
data = conn.recv(1024)
print("收到消息：", data.decode("utf8"))
# 返回消息给客户端
conn.send("收到！".encode("utf8"))

# 关闭连接
conn.close()
server_socket.close()


# 客户端
# =====客户端代码（主动去连服务端）=====
import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 连接服务端
client_socket.connect(("127.0.0.1", 8888))
# 发送数据，网络传输必须是bytes字节
client_socket.send(b"你好，我是客户端")
# 接收返回信息
res = client_socket.recv(1024)
print(res.decode("utf8"))
client_socket.close()

```

### 用例总结

1. 服务端：开门，守在端口等连接（bind 绑定端口 → listen 监听）
2. 客户端：上门发起连接 connect
3. 服务端 accept，接受连接，管道打通
4. 两边 send 发数据，recv 接收数据
5. 通信结束，关闭 socket

### 应用场景

1. 工业相机：相机采集图像，通过网络把图片传给电脑上的视觉程序（底层就是 socket）
2. 多机部署：A 电脑采集图片，发给 B 电脑跑 CV 检测算法
3. 摄像头视频流传输
   

### 技术分析
1. urllib+urllib2：**客户端**，主动去网上拉网页、下载文件（Python2 模块，Python3 合并）
2. Socketserver：**简化版 socket 服务端**，快速写 TCP/UDP 服务器，适合简单场景
3. Twisted：**老牌异步网络框架**，高性能网络服务，旧项目多见，新项目很少用
4. 要做 CV 模型部署、图像上传接口，现在一般用 Flask/FastAPI，底层已经帮你封装好了，不需要手写 Socketserver、Twisted