Title: 外部から自宅PCにアクセス
Category: 開発環境
Tags: ssh, ubuntu
Summary: 外出中のみVPS経由で自宅PCにアクセスするための方法について説明します

# はじめに

本記事に書いてある手順を実行することは大きなセキュリティリスクになりえます。
セキュリティに関する記事を読み漁りながら安全な方法を見つけたつもりですが、私が知らないセキュリティホールがあるかもしれません。
そのため、この記事を読んだ結果起こったいかなることも責任を負いかねます。つまり、自己責任でお願いします。

# 環境

## 自宅PC

Ubuntu 22.04

## VPS

Ubuntu 22.04

# 事前準備

自宅PCに開けるポート：`HOME_PORT`
VPSに開けるポート：`VPS_PORT`
VPSのIPアドレス：`VPS_IP`

とします。

例えば、`HOME_PORT` = 54321のようになります。

このうち、`HOME_PORT`と`VPS_PORT`はシステムポート以外(=1024~65535)で好きな番号を設定してください。

そして、自宅PCで、`~/.remotessh`を作成して、以下のように書き込んでください。

```
SSH_VPS_PORT=VPS_PORT
SSH_HOME_PORT=HOME_PORT
SSH_VPS_NAME=VPS_IP
```

# VPS側での作業

VPSにsshできる前提で話を進めます。
もし、oepnssh serverがない場合は、自宅PCと同様の作業を行ってください。ただし、`HOME_PORT`の代わりに、`VPS_PORT`を使う必要があります。

## 公開鍵暗号の作成

```bash
ssh-keygen -t ed25519 -C "vps"
```

と実行し、`~/.ssh/id_ed25519.pub`の内容をコピーしてください。

## configファイルの作成

`~/.ssh/config`ファイルを作成し、以下のように設定してください。

```
Host 好きな名前
    HostName localhost
    User 自宅PCのユーザー名
    Port VPS_PORT
    ForwardX11 yes # x11 forwardingできるようになる
    ServerAliveInterval 60 # ずっと放置してても繋がり続ける
    IdentityFile ~/.ssh/id_ed25519
```

# 自宅PCでの作業

## oepnssh serverを建てる

```bash
sudo apt install openssh-server
```

```bash
sudo vi /etc/ssh/sshd_config
```

として、

```
# 変更前
# PORT 22

# 変更後
Port HOME_PORT
```

のように編集してください。

その後、下のコマンドを実行してopenssh serverを再起動してください。

```bash
sudo systemctl restart sshd
```


## `HOME_PORT` を開ける

```bash
sudo apt install -y ufw

sudo ufw enable
sudo ufw allow HOME_PORT
```

上のように実行することで、HOME_PORTへのアクセスを許可するように設定します。

TODO: VPSのIPアドレスからのみ許可する

## VPSの公開鍵を登録する

先ほどコピーした `~/.ssh/id_ed25519.pub`の内容を、`~/.ssh/authorized_keys`の中に貼り付け、保存してください。


# 実際に接続する

```bash
ssh -NR VPS_PORT:localhost:HOME_PORT VPS_IP
```

上のコマンドを使うことで、[リモートフォワード](https://qiita.com/mechamogera/items/b1bb9130273deb9426f5)をつなげます。
その結果、VPSのVPS_PORTにアクセスすると、自宅PCのHOME_PORTにアクセスできます。
何も出力されないはずですが、そのまま置いておいてください。


では、

1. 自宅PC→VPSにssh
2. VPS→自宅PCにssh

して、VPSから自宅PCにsshできることを確かめましょう。


```bash
# VPSにsshする
ssh VPS_IP

# ここはVPSの中にいる状態です
ssh 上で書いた好きな名前
```

うまく行っていれば、上の2行のコマンドを実行するだけで自宅PCにsshできます。

# リモートフォワードをserviceとして登録する

`~/.config/systemd/user/remotessh.service`というファイルを作成し、下の内容を書き込んでください。

```
[Unit]
Description="外部からssh"

[Service]
EnvironmentFile=/home/ユーザー名/.remotessh
ExecStart=ssh -NR ${SSH_VPS_PORT}:localhost:${SSH_HOME_PORT} ${SSH_VPS_NAME}
ExecStop=/bin/kill ${MAINPID}

[Install]
WantedBy=defalt.target
```

これにより、`systemctl --user start remotessh.service`と実行すればVPSから自宅PCにアクセスできるようになり、`systemctl --user stop remotessh.service`と実行すればアクセスできないようになります。

# 参考記事

[ubuntu自宅サーバにsshで外部からアクセス - 勇往邁進](https://frute.hatenablog.com/entry/2018/11/19/003056)
