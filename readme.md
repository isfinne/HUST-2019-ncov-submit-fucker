# HUST 健康状况上报 auto fucker 

项目参考[HUST-2019-ncov-submit-fucker](https://git.recolic.net/recolic-hust/hust-2019-ncov-submit-fucker)

效果如下图所示
![效果图](https://cdn.jsdelivr.net/gh/misaka7690/My_GitHub_CDN/img/2020/03/12/09-00-47.png)
做了以下改进

- 每日邮件提醒
- 异常处理(出现错误时发送邮件,以免没填)
- 随机体温和随机填报时间
- 无头浏览器(chrome版)安装环境(自带chromedriver)
- 可选择每日手动提交和全自动提交两种模式

## 使用方法

环境: 阿里云Ubuntu服务器

这里我为了方便用了`python2`.

首先配置无头浏览器环境

```bash
sudo bash install_chrome.sh
```

然后再修改`config.py`中的邮箱,校园网账号等信息.配置信息如下
- family_name: 你的同居住的家人的名字,由于只填一个就行了,我这里只写了一个,两个以上去源码增加
- m_uid: 学号,类似U201714***
- m_password: hust认证密码
- m_qq_pwd: QQ第三方客户端授权码
- m_sender_email: 发送的QQ邮箱
- m_receiver_email: 接受邮件的邮箱

如果嫌配置邮箱麻烦,也可以不用邮箱,fucker.py最后注释有说明...

最后以下命令运行即可(建议在`tmux`建一个session).

```bash
python fucker.py
```

## 声明

仅作学习用途.
