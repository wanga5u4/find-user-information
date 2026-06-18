import requests
name=input("输入名称:")
url=f"https://api.github.com/users/{name}"
respones=requests.get(url)
date=respones.json()
if "login" in date:
    print("用户名:",date["login"])
    print("粉丝数量:",date["followers"])
    print("公开仓库:",date["public_repos"])
    print("关注数:",date["following"])
    print("创建时间:",date["created_at"])
    print("简介:",date["bio"])
    print("所在地:",date["location"])
else:
    print("用户不存在")