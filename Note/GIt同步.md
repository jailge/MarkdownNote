---
enable html: true
---
# Git同步文件夹

1. 安装Git
2. 打开Git Bash
3. 创建ssh-key
`ssh-keygen -t rsa -C "XXX@XXX.COM"`
4. 打开id_rsa.pub（默认c:\用户\administrator\.ssh）
5. github网站上去配置一下 ssh key，验证一下是否设置成功,在**git bash**下输入如下命令：
`ssh –T git@github.com`
6. 配置一下用户名和邮箱：
`git config –-global user.name “用户名”`
`git config –-global user.email “邮箱”`
7. 本机新建项目文件夹，Git中打开该路径并初始化
`git init`
8. 增加对我们github上创建的仓库的管理
`git remote add origin git@github.com:jailge/MarkdownNote.git`
9. 由于我建立仓库的时候创建README.md之时，已经算一次提交了，我需要先在本地同步一下仓库的内容
`git pull git@github.com:jailge/MarkdownNote.git`
