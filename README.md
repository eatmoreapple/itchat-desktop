# itchat-desktop

itchat-desktop 是 itchat 的一个补丁，使得 itchat 可以支持更多的用户登录。

## 安装

```bash
pip install itchat-desktop
```

## 使用

```python
import itchat_desktop

import itchat

itchat_desktop.patch()

itchat.auto_login()

itchat.send('Hello, filehelper', toUserName='filehelper')
```

## 说明

在你的项目开始的时候，调用 `itchat_desktop.patch()` 即可。别的地方不需要做任何修改。