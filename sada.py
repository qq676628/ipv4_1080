from git import Repo

# 本地仓库路径
repo_path = 'L:\\Mr.Chen 设计环境\\影视相关\\ipv4'

# 打开仓库
repo = Repo(repo_path)

# 添加所有更改的文件
repo.git.add('--all')

# 提交更改
repo.index.commit("提交消息")

# 推送到远程仓库
origin = repo.remote(name='origin')
origin.push()
