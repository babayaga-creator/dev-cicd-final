#!/bin/sh

kubectl create namespace final

kubectl create secret generic mysql-secret --from-literal=mysql-root-password=kube1234 --from-literal=mysql-user=username --from-literal=mysql-password=password --from-literal=mysql-database=example -n final
kubectl create secret docker-registry regcred --docker-server=ghcr.io --docker-username=babayaga-creator --docker-password=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  --docker-email=arif.cihangir@gmail.com -n final


kubectl apply -f manifests/mysql/configmap.yml -n final
kubectl apply -f manifests/mysql/mysql-service.yml -n final
kubectl apply -f manifests/mysql/mysql.yml -n final
kubectl apply -f manifests/flask/flask-service.yml -n final
kubectl apply -f manifests/flask/flask.yml -n final
