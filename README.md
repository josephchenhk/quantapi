Local debug:

```shell
> docker run -itd --name mongo -v ./mongo/data/db:/data/db -p 27017:27017 mongo --auth
```

Deployment in docker:

```shell
> docker-compose up -d --build (第一次运行)
> docker-compose up -d
```
