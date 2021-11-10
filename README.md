# Algeo02-20017

Kelompok 46 Kompres Air Hangat

- 13520017 Diky Restu Maulana
- 13520024 Hilya Fadhilah Imania
- 13520148 Fikri Ihsan Fadhiilah


## Library

Client
  - Vue 3
  - Vite
  - Naive UI
  - Axios

Server
  - Flask
  - flask_cors

Algoritma
  - numpy


## Run

Requirements

- Node.js 16
- yarn 1.22
- Python 3.9
- pipenv 2021.11

### Install

``` bash

# install client
cd src/client
yarn

# install server
cd ..
pipenv install

```

### Client

``` bash

cd ./src/client

# development: serve client dengan hot reload
yarn dev

# build untuk integrasi dengan server
yarn build

```

### Server

``` bash

cd ./src
pipenv run flask run

```

Note:
  1. Jika belum menjalankan `yarn build` maka client tidak dapat diakses melalui server.
  2. Jika kode client mengalami perubahan, jalankan `yarn build` kembali untuk memperbarui.
