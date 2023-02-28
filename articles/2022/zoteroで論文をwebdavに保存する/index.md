Title: zoteroで論文をwebdavに保存する
Category: 開発環境
Tags: ubuntu, vps, zotero, 論文管理
Summary: OSSの論文管理ソフトzoteroとwebdavを組み合わせることで論文を(実質)無制限にアップロードできるようになる方法を説明します。

# 環境

## サーバー側

* Ubuntu22.04
* インストール済みのソフト
  * docker

## 手元側

* Ubuntu22.04
  * WindowsでもMacでも同じ方法でできるはず
* zotero
  * [公式サイト](https://www.zotero.org/)からインストールすべし

# サーバー側の作業

Dockerのインストールはできているものとします。

サーバーのipアドレスが、`serverip.com`であると仮定して話を進めます。

まず、ドメインを契約しているサービスで、`webdav.serverip.com`のレコードを作成してください。

`serverip.com/webdav/`をwebdavに割り当てる方法もありますが、あまり好きではないのでサブドメインを設定しています。



その後、以下のように`docker-compose.yml`を作成してください。

```yaml
version: '3'
services:
  https-portal:
    image: steveltn/https-portal:1
    ports:
      - 80:80
      - 443:443
    environment:
      DOMAINS: >-
        webdav.server_ip.com -> http://webdav:80,
      STAGE: 'production'
      DEBUG: true
      CLIENT_MAX_BODY_SIZE: 0
    volumes:
      - type: volume
        source: https-portal-data
        target: /var/lib/https-portal
    depends_on:
      - webdav
    restart: always
  webdav:
    image: bytemark/webdav
    restart: always
    environment:
      AUTH_TYPE: Basic
      USERNAME: ${WEBDAV_USER_NAME}
      PASSWORD: ${WEBDAV_PASSWORD}
    volumes:
      - type: bind
        source: ./webdav/data/
        target: /var/lib/dav

volumes:
  https-portal-data:
```



`https-portal`は、certbotによるssl口唇を自動でやってくれるdockerイメージです。言い換えると、https化を自動でしてくれます。

`DOMAINS`で指定しているのは、`webdav.server_ip.com`に来たリクエストをすべて`http://webdav:80`に転送するということです。



`webdav`は、webdavサーバーの構築を簡単にできるdockerイメージです。

Basic認証をかけています。dotenvなどを使うか(おすすめ)、`.bashrc`を使うかして、2つの環境変数をexportしておいてください。



あとは、

```bash
mkdir webdav/data
docker compose up -d
```

とすれば、https化するリバースプロキシと、webdavを建てることができます。

80番と443番のポート開放を忘れないようにしてください。

# 手元側の作業

まず、(Ubuntuなら)ファイルを使ってwebdavにアクセスできることを確認します。私の場合、

1. 他の場所
2. `davs://webdav.serverip.com`と入力
3. 接続
4. ユーザー名とパスワード入力

でできました。

詳しいやり方は、「OS名 webdav 接続」と調べてください。



zoteroをインストールしたあと、「編集」→「設定」→「同期」と移動して、「ファイルの同期」のチェックを入れます

そして、

URL: `https://webdav.serverip.com`

ユーザー名: 先ほど設定したユーザー名(`${WEBDAV_USER_NAME}`の中身)

パスワード: 先ほど設定したパスワード(`${WEBDAV_PASSWORD}`の中身)

を入力し、「サーバーを検証する」と押します

そうすると、pdfファイルが自動でwebdavに保存されます。



あとは、[Zoteroの環境設定](https://qiita.com/Yarakashi_Kikohshi/items/39dfbf3059aaf0690761#-zotero-%E3%81%AE%E7%92%B0%E5%A2%83%E8%A8%AD%E5%AE%9A)にしたがって設定をしました。ただし、リンク先の記事ではwebdavではなくdropboxを使っているので注意が必要です。



ipadでやるなら、[私の研究おすすめツール（文献管理編） ](https://note.com/takeshi_teshima/n/nd28a6e3dfb05)がおすすめです。
