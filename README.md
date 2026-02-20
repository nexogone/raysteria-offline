<p align="center">
  <img src="/assets/logo-dark.svg#gh-light-mode-only" alt="Raysteria Logo Dark" width="60%" height="auto" />
  <img src="/assets/logo-light.svg#gh-dark-mode-only" alt="Raysteria Logo Light" width="60%" height="auto" />
</p>

<p align="center">
A server re-implementation for a certain mobile gacha game. 
</p>

> [!CAUTION]
> Project on early development stage, don't use in production!

## Quick Start
### Android (via Termux):
```
pkg install git python rust binutils uv libuv -y
git clone https://github.com/nexogone/raysteria-offline.git

cd raysteria-offline
uv run uvicorn raysteria:create_app --host localhost --port 5001 --factory
```

### Android (via Termux) - Alternative method:
```
pkg install git python -y
pip install litestar==2.21.0 jinja2==3.1.6 uvicorn==0.41.0

cd ~/storage/shared
git clone https://github.com/nexogone/raysteria-offline.git

cd ~/storage/shared/raysteria-offline
uvicorn raysteria:create_app --host localhost --port 5001 --factory
```
