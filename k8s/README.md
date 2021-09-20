# Kubernetes

- Manually creating the deployment and service:
```
PS C:\Users\aabou> kubectl create deployment my-app --image=aabounegm/devops_app_python
deployment.apps/my-app created
PS C:\Users\aabou> kubectl get deployments
NAME     READY   UP-TO-DATE   AVAILABLE   AGE
my-app   1/1     1            1           106s
PS C:\Users\aabou> kubectl get pods
NAME                     READY   STATUS    RESTARTS   AGE
my-app-965b4d766-sjqxj   1/1     Running   0          2m5s
PS C:\Users\aabou> kubectl expose deployment my-app --type=LoadBalancer --port=5000
service/my-app exposed
```

- Output of `kubectl get pods,svc` after manually creating a deployment and a service:
```
PS C:\Users\aabou> kubectl get pods,svc
NAME                         READY   STATUS    RESTARTS   AGE
pod/my-app-965b4d766-sjqxj   1/1     Running   0          3m15s

NAME                 TYPE           CLUSTER-IP       EXTERNAL-IP   PORT(S)          AGE
service/kubernetes   ClusterIP      10.96.0.1        <none>        443/TCP          21m
service/my-app       LoadBalancer   10.111.158.147   <pending>     5000:31133/TCP   29s
```

- After using configuration files and creating 3 replicas:
```
PS C:\Users\aabou> kubectl get pods,svc
NAME                              READY   STATUS    RESTARTS   AGE
pod/app-python-59fdf85d9b-fxc7r   1/1     Running   0          17s
pod/app-python-59fdf85d9b-rlplm   1/1     Running   0          14s
pod/app-python-59fdf85d9b-xqsxt   1/1     Running   0          21s

NAME                 TYPE           CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
service/app-python   LoadBalancer   10.104.19.136   <pending>     5000:31959/TCP   95s
service/kubernetes   ClusterIP      10.96.0.1       <none>        443/TCP          31m
```
