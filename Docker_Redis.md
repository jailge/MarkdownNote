# Docker_Redis

## 下载redis镜像

`docker pull redis`

## 配置data、conf

    mkdir -p ./docker/redis/data
    mkdir -p ./docker/redis/conf

## redis.conf

配置外网访问

    #bind 127.0.0.1
    protected-mode no
    appendonly yes//持久化
    requirepass yourpassword

## 启动redis

### 创建并运行一个名为 myredis 的容器

    docker run \
    -p 6379:6379 \ # 端口映射 宿主机:容器
    -v /root/docker/redis/data:/data:rw \ # 映射数据目录 rw 为读写
    -v /root/docker/redis/conf/redis.conf:/etc/redis/redis.conf:ro \ # 挂载配置文件 ro 为readonly
    --privileged=true \ # 给与一些权限
    --name myredis \ # 给容器起个名字
    -d redis redis-server /etc/redis/redis.conf # deamon 运行 服务使用指定的配置文件

## 查看状态

    docker ps
