# clipboard-to-qbwebui
Monitor clipboard in real time and send magnet link to qBittorrent WebUi.  
实时监控剪贴板，并将磁力链接发送到qBittorrent WebUi下载。
# 运行
依赖`qbittorrentapi`、`PySide6`。  
直接运行`clipboard qb.pyw`即可。  
首次运行会自动创建`config.json`文件保存用户配置。  
# 使用  
运行软件后，软件会尝试连接qBittorrent webui，成功登录后会开始监控剪贴板，失败则会退出。  
程序驻留在系统托盘以后台运行，并监控剪贴板中的磁力链接，如需退出请从托盘退出。  
只需要将磁力链接复制到剪贴板，软件会自动获取并询问用户是否推送到qBittorrent webui下载，下载后会显示通知。  
# 设置  
## config.json  
所有设置选项全部由`config.json`配置。  
```
{  
    "qb_adress": "127.0.0.1",
    # qBittorrent webui的域名，如果是https需要加上
    "qb_port": 8080,
    # 域名端口，默认是8080
    "qb_user_name": "admin",
    # 填写webui的用户名
    "qb_user_pwd": "adminadmin",
    # 填写webui的用户密码
    "enable": true,
    # 是否启用软件功能
    "download_msgbox": true,
    # 检测到剪贴板中磁力链接后是否弹窗询问下载
    # 如果该项是false，则不弹窗询问，直接下载
    "download_notify": true
    # 下载后是否显示下载通知
    # 成功下载会显示磁力链接，失败会显示错误信息
}
```
# 使用环境
PySide6 3.6.0  
Python 3.10  
更低版本或许兼容。