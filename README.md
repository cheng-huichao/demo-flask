# demo-flask deployment

  flask + uwsgi + nginx

  ## flask run.py file

  ## uwsgi config
  
```
  [uwsgi] 
  ; socket or http 
  socket = 127.0.0.1:9095 
  ;local project path: /Users/chenghuichao/Dev/demo_flask/ 
  ;production path: /usr/http/demo_flask/ 
  chdir = /usr/http/demo_flask/ 
  ; run.py is the application entry file, app is the instance in the run.py file. 
  module = run:app 
  processes = 4 
  master = true 
  threads = 2 
  daemonize = uwsgi.log 
  ;restart uwsgi:     uwsgi --reload uwsgi.pid 
  ;stop uwsgi:        uwsgi --stop uwsgi.pid 
  pidfile = uwsgi.pid 
  virtualenv = %(chdir)venv 
```

  ## nginx.conf
  
  ```
  server {
    listen       80;
    listen      [::]:80;
    server_name  demo-flask.com;

    charset UTF-8;
    access_log  /var/log/nginx/host.access.log  main;
    error_log   /var/log/nginx/errors.log;

    client_max_body_size 75M;

    location / {
        uwsgi_pass      127.0.0.1:9095;
        include         /etc/nginx/uwsgi_params;
    }

    location /static/ {
        alias           /usr/http/demo-flask/static/;
        access_log      off;
        autoindex       on;
    }

    location /media/ {
        alias           /usr/http/demo-flask/media/;
        access_log      off;
        autoindex       on;
    }

    #error_page  404              /404.html;

    # redirect server error pages to the static page /50x.html
    #
    error_page   500 502 503 504  /50x.html;
    location = /50x.html {
        root   /usr/share/nginx/html;
    }
}


  ```
  
 ## if using supervisor conf
 
 ```
 [program:demo-flask-site]
command=uwsgi --ini /usr/http/demo_flask/uwsgi.ini
directory=/usr/http/demo_flask/
startsecs=0
stopwaitsecs=0
autostart=true
autorestart=true
 ```
 
 
 
  
