# r2cloud-public
Unofficial web client for display data from R2Server API (public)

## Setup using docker
* create own setting file (`setting.py`), example you can found in `setting-exmaple.py`
* run docker container with command 

```sh
docker run -d \
  --name=r2cloud-public \
  --mount type=bind,source="$(pwd)/setting.py",target="/r2cloud_public/setting.py" \
  -p 5000:5000 \
  lukasplevac/r2cloud-public
```

### Advence docker

#### Build own image
```sh
docker build . -t lukasplevac/r2cloud-public
```
or
```sh
make build
```

####  volumes
* `/r2cloud_public/setting.py:ro          `- setting file
* `/r2cloud_public/static/a:rw            `- dir with downloaded a
* `/r2cloud_public/static/data:rw         `- dir with downloaded binary files (decoded binary)
* `/r2cloud_public/static/spects:rw       `- dir with downloaded spectrograms

#### ports
* `5000` - http ui website

## Setup without docker
* install `python3` and `python3-pip` - `apt install python3 python3-pip`
* from `pip3` install `r2cloud`, `Flask` and `requests` - `pip3 install Flask && pip3 install r2cloud && pip3 install requests`
* create own setting file (`setting.py`), example you can found in `setting-exmaple.py`
* run app using `env FLASK_APP=root.py flask run` in `src` dir
