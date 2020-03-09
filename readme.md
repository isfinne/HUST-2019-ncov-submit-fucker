# HUST 健康状况上报 auto fucker 

项目参考[HUST-2019-ncov-submit-fucker](https://git.recolic.net/recolic-hust/hust-2019-ncov-submit-fucker)

做了以下改进

- 每日邮件提醒
- 异常处理(出现错误时发送邮件,以免没填)
- 随机体温和随机填报时间
- 无头浏览器(chrome版)安装环境(自带chromedriver)

## 使用方法

环境: 阿里云Ubuntu服务器

这里我为了方便用了`python2`.

首先配置无头浏览器环境

```bash
sudo bash install_chrome.sh
```

然后再修改`fucker.py`中的邮箱,校园网账号等信息.

最后以下命令运行即可(建议在`tmux`建一个session).

```bash
python fucker.py
```

## 声明

仅作学习用途.