#!/bin/sh

docker run \
    --name mysql \
    --network my-network \
    -p 3306:3306 \
    -d \
    --rm \
    -e MYSQL_RANDOM_ROOT_PASSWORD=yes \
    -e MYSQL_DATABASE=example \
    -e MYSQL_USER=username \
    -e MYSQL_PASSWORD=password \
    -v "$(pwd)"/sql:/docker-entrypoint-initdb.d \
    mysql:8


kubectl create secret generic mysql-secret --from-literal=mysql-root-password=kube1234 --from-literal=mysql-user=username --from-literal=mysql-password=password --from-literal=mysql-database=example
kubectl create configmap db --from-literal=mysql-database: database

kubectl create secret docker-registry regcred --docker-server=ghcr.io --docker-username=babayaga-creator --docker-password=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  --docker-email=arif.cihangir@gmail.com
