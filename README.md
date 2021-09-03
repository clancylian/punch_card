## 厦门大学自动健康打卡

​		本脚本适用于厦门大学学生健康打卡，只是为了方便大家打卡，以免有时忘记重零开始。请**中高风险**的同学**谨慎使用**，按实际情况填报，如出问题，概不负责。

重要事情说三遍：

​    &emsp;   **中高风险地区同学谨慎使用！**
 
​    &emsp;  	**中高风险地区同学谨慎使用！**

​    &emsp;   **中高风险地区同学谨慎使用！**

​		 &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;         发布日期：2021-09-03

### 浏览器插件下载

脚本使用谷歌浏览器，通过[chrome://version/](chrome://version/)查看自己电脑的浏览器版本：

```
Google Chrome	92.0.4515.159 (正式版本) （32 位） (cohort: Stable)
修订版本	0185b8a19c88c5dfd3e6c0da6686d799e9bc3b52-refs/branch-heads/4515@{#2052}
操作系统	Windows 10 OS Version 1909 (Build 18363.1734)
JavaScript	V8 9.2.230.29
```

然后在http://chromedriver.storage.googleapis.com/index.html 下载对应版本插件，替换当前的浏览器版本。

### 依赖安装

脚本需要在有python环境的电脑运行。

脚本依赖于Web应用程序测试的工具Selenium，如果执行发现缺少依赖，另行安装。

```bash
pip3 install selenium
```

### 配置文件修改

修改目录下的配置文件config.json：

```json
{
  // 校园网登录账号密码
  "username" : "xxxx",
  "password" : "xxxxx",
  // 发送邮箱和接收邮箱，本脚本限制使用qq邮箱
  "email" : "xxx@qq.com",
  // 授权码在QQ邮箱 -> 设置 -> 账号里面生成授权码
  "auth" : "ixbcnumplshkbchsad"
}
```

### 修改批处理文件

修改为脚本实际的目录

```bash
@echo off
E:
cd E:\punch_card
start python punch_card.py
exit
```

### 定时任务设置

从 计算机管理 -> 系统工具 -> 任务计划程序 -> 创建基本任务，具体操作可自行百度。

### 注意事项

- 部署完成后，可以先自行测试一下。

- 如果网页内容更新，脚本需要相应修改。

### 目录

```
├─logs
│  └─ log_test.txt  日志文件
├─chromedriver      浏览器插件
├─config.json       配置文件
├─punch_card.py     打卡脚本
├─start.bat         批处理文件
└─README.md         说明文档
```

