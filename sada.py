import subprocess
import os
# 仓库路径
repo_path = 'L:/Mr.Chen 设计环境/影视相关/ipv4'

# 切换到仓库目录
os.chdir(repo_path)

# 添加文件
subprocess.run(["git", "add", "--all"])

# 提交更改
subprocess.run(["git", "commit", "-m", "提交消息"])

# 推送到远程仓库
subprocess.run(["git", "push", "origin", "main"])
