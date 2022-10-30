You can either build and push it by using 
```
make
```
but you may need to change your id and repo name. Or you can build and push it manually.

To build it. Use your own username and repo name of your dockerhub.

```
 docker build -t hobbeslucretius/udaconnect-api:latest 
```

To test it. To run it in the detach mode use -d argument.

```
 docker run hobbeslucretius/udaconnect-api:latest 
```

To push it

```
docker push hobbeslucretius/udaconnect-api:latest 
```
