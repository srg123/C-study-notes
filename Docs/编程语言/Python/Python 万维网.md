# Python之万维网


## 客户端爬虫


```python
import urllib.request

# 目标网页地址，就是URL
url = "https://www..."

# 向服务器发送请求，拿到返回的网页数据
with urllib.request.urlopen(url) as response:
    # read拿到字节，decode转成字符串html源码
    html = response.read().decode("utf-8")
# 打印前300个字符看看
print(html[:300])

```


 ## 服务端框架flask\Django\fastAPI


### 总结

 -  客户端：Python 作为 web 客户端，模拟浏览器拿网页。如果网页里面有图片链接，提取链接就能下载图片做 CV 数据集
-  Selenium、Playwright，模拟真实浏览器运行 JS，拿到渲染完成后的页面
-  mod_python 改进：Python 解释器一直挂在 Apache 里面，不用反复启动，速度比 CGI 快
-  现在做 Python Web，直接用 Flask/Django + uWSGI/gunicorn
-  训练好的图像识别模型，包装成 Web 服务。别人上传图片，调用这个服务，服务跑 CV 模型，返回识别结果。
这个就是工业机器视觉


