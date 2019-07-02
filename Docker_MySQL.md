# Docker_MySQL

## 下载运行MySQL

`docker run --name mysql01 -e MYSQL_ROOT_PASSWORD=root -p 3306:3306 --restart=always -v /data/volumes/mysql:/var/lib/mysql:rw --privileged=true -d mysql/mysql-server (mysql:5.7)`

`如果已经启动了则可以使用如下命令：`

```
docker update --restart=always <CONTAINER ID>
```

## 进入docker mysql容器

`docker exec -it mysql01 mysql -uroot -p`

## 配置MySQL远程访问

    update user set host = "%" where user = "root";
    FLUSH PRIVILEGES；
    ALTER USER 'root'@'%' IDENTIFIED WITH mysql_native_password BY 'root';
    FLUSH PRIVILEGES；
    GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' WITH GRANT OPTION；
    FLUSH PRIVILEGES；


