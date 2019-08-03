# Docker_RabbitMQ

> 注意获取镜像的时候要获取management版本的，不要获取last版本的，management版本的才带有管理界面。

##  获取镜像
```
docker pull rabbitmq:management
```


## 运行镜像

```
docker run -p 5672:5672 -p 15672:15672 --name rabbitmq -d rabbitmq:management
```

## 访问管理界面

访问管理界面的地址就是 http://[宿主机IP]:15672，可以使用默认的账户登录，用户名和密码都guest

