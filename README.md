
### run pip local
```
python3 -m venv myvenv
source myvenv/bin/activate
pip install -r requirements.txt
```

### run pip ubuntu
https://www.digitalocean.com/community/tutorials/how-to-install-the-django-web-framework-on-ubuntu-18-04
```
python3.6 -m venv my_env
source my_env/bin/activate
pip install -r requirements.txt 
```
### run api
```
python producer.py
python consumer.py
```


### ubuntu run pip
```
https://www.digitalocean.com/community/tutorials/how-to-install-the-django-web-framework-on-ubuntu-18-04
```

sshfs ubuntu@ec2-54-91-224-152.compute-1.amazonaws.com:/home/ubuntu/code ~/kafka_research/producer -o IdentityFile=~/kindom/demo.pem -o allow_other



##### kill port 
```
sudo lsof -i -P -n | grep LISTEN
kill -9 id
```








