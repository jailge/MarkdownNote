# Docker\_监控 - cadvisor+influxdb+grafana

## cadvisor+influxdb+grafana介绍

| 框架名称     | 框架名称                                                                                                         |                                                          框架名称 |
| -------- | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------: |
| cadvisor | Google开源的用于监控基础设施应用的工具，可以零配置运行在docker主机上来监控Docker主机以及Docker容器。其为但节点监控，只能监控一个主机。多节点监控可参考Google的Kubernetes。    |                                作为docker服务的监控数据收集器，提供给influxdb |
| influxdb | InfluxDB 是用Go语言编写的一个开源分布式时序、事件和指标数据库，无需外部依赖、提供管理界面。提供基于时间序列，基于事件的可度量的实时计算功能。                                 |         作为数据存储器以及分析函数支持，与elk中elasticsearch作用类似，但此数据库偏向存储实时数据。 |
| grafana  | Grafana可视化大型测量数据的开源程序，有灵活丰富的图形化选项，可以混合多种风格，多个数据源例如Graphite、zabbix、InfluxDB、Prometheus、mysql和OpenTSDB 详见配置页面。 | 作为数据分析的可视化展示，与influxdb配合实现监控目的。与elk中kibana类似，但此可视化偏向实时监控数据展示。 |

## 架构图

![20180630171521270]($resource/20180630171521270.png)

> docker多节点监控
> 备注：每个docker主机上均部署多个tomcat容器，以及docker主机的监控服务cadvisor。
> influxdb以及grafana根据监控压力配置。
> 数据流向： docker主机+docker容器-->cadvisor-->influxdb-->granfana-->web页面

## 搭建

### 创建虚拟网卡（为了网络环境隔离）

`docker network create docker-monitor #为docker主机创建一个网卡名为docker-monitor`

> 备注：容器启动可以设置使用改网卡 即使用 --net 网卡名指定 若不指定则默认使用docker主机默认网卡docker0 其后所有步骤不需指定 --net

### 部署influxdb

`docker run --name influxdb --net docker-monitor -p 8083:8083 -p 8086:8086 -d tutum/influxdb`

> 备注：

    -d:守护线程运行
    --name:容器名influxdb
    --net:加入到网络docker-monitor
    -p:   主机端口(自己分配):容器端口  8083为infuxdb后台控制端口，8086是infuxdb的数据端口 
    tutum/influxdb:默认会在docker官方仓库pull下来influxdb镜像

`http://docker主机的ip:容器映射出来host`
![TIM截图20190701101511]($resource/TIM%E6%88%AA%E5%9B%BE20190701101511.png)
添加管理员角色，创建数据库（作为后续存储）
```
CREATE USER "root" WITH PASSWORD 'root' WITH ALL PRIVILEGES ##创建管理员角色 root 密码 root 供使用
CREATE DATABASE "cadvisor"                                  ##创建数据库 cadvisor 用于接收cadvisor的监控数据
```
### 部署cadvisor
`docker run --privileged=true --net docker-monitor --volume=/:/rootfs:ro --volume=/var/run:/var/run:rw --volume=/sys:/sys:ro --volume=/var/lib/docker:/var/lib/docker:ro --volume=/sys/fs/cgroup:/sys/fs/cgroup:ro -p 8087:8080 --detach=true --name=cadvisor google/cadvisor -storage_driver=influxdb -storage_driver_db=cadvisor -storage_driver_host=influxdb:8086`

> 备注:

```
docker run 
--privileged=true           ：设置挂载目录权限为最大 否则挂载出错
--net docker-monitor        ：设置加入docker-monitor网络
--volume=/:/rootfs:ro       ：将容器/rootfs目录挂载到docker /
--volume=/var/run:/var/run:rw :将容器/var/run 挂载到docker /var/run
--volume=/sys:/sys:ro         ：rw表示读写  ro表示只读
--volume=/var/lib/docker:/var/lib/docker:ro 
--volume=/sys/fs/cgroup:/sys/fs/cgroup:ro 
-p 8087:8080                  ：设置cadvisor端口映射  由于8080被我使用oracle  我分配8087
--detach=true                 ：是否后台运行容器服务
--name=cadvisor google/cadvisor :容器服务名 为cadvisor  从docker默认仓库 下载google/cadvisor镜像
-storage_driver=influxdb        ：绑定存储驱动 为 influxdb
-storage_driver_db=cadvisor     ：数据库为  cadvisor  请对应
-storage_driver_host=influxdb:8086 ：绑定数据库管理地址  容器名:容器端口
```


`http://docker主机的ip:容器映射出来host 本来为8080 修改为8087`

![TIM截图20190701104207]($resource/TIM%E6%88%AA%E5%9B%BE20190701104207.png)

### 部署grafana
`docker run -d --name grafana --net docker-monitor -p 3000:3000 grafana/grafana`

> 备注：

```
docker run 
-d                    ：后台运行
--name grafana        ：容器别名
--net docker-monitor  ：加入docker-monitor网络
-p 3000:3000          ：端口映射
grafana/grafana       ：默认docker仓库下载grafana镜像
```

`http://docker主机的ip:容器映射出来host 默认帐号admin admin`

## 简单使用
### 登录grafana
### 设置数据源
![20180630183640163]($resource/20180630183640163.png)
### 设置添加面板
![TIM截图20190701104512]($resource/TIM%E6%88%AA%E5%9B%BE20190701104512.png)

