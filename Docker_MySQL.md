# Docker_MySQL

## 下载运行MySQL

`docker run --name mysql01 -e MYSQL_ROOT_PASSWORD=root -p 33066:3306 -d mysql/mysql-server`

## 进入docker mysql容器

`docker exec -it mysql01 mysql -uroot -p`

## 配置MySQL远程访问

    update user set host = "%" where user = "root";
    FLUSH PRIVILEGES；
    ALTER USER 'root'@'%' IDENTIFIED WITH mysql_native_password BY 'root';
    FLUSH PRIVILEGES；
    GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' WITH GRANT OPTION；
    FLUSH PRIVILEGES；


