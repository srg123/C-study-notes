
- 当安装 Flask 时，以下配套软件会被自动安装。

- - Werkzeug 用于实现 WSGI ，应用和服务之间的标准 Python 接口。

- - Jinja 用于渲染页面的模板语言。

- - MarkupSafe 与 Jinja 共用，在渲染页面时用于避免不可信的输入，防止注 入攻击。

- - ItsDangerous 保证数据完整性的安全标志数据，用于保护 Flask 的 session cookie.

- - Click 是一个命令行应用的框架。用于提供 flask 命令，并允许添加 自定义管理命令。

- - Blinker 提供对于 信号 的支持。




- 以下配套软件不会被自动安装。如果安装了，那么 Flask 会检测到这些软件。

- - python-dotenv 当运行 flask 命令时为 通过 dotenv 设置环境变量 提供支持。

- - Watchdog 为开发服务器提供快速高效的重载。