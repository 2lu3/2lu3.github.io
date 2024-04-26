Title: Cloudflareの100MB upload size limit突破のためGit LFS→Git+DVC+Minioに移行した
Category: 研究
Tags: docker, cloudflare, minio, dvc, git, server
Summary: 研究データを自宅サーバーに保管し、バイナリファイルはGit LFSを使用して管理していた。しかし、Cloudflareを導入することでGit LFSでも100MB以上のファイルをアップロードすることができなくなった。そのため、チャンクアップロードに対応したMinioとバイナリファイルバージョン管理ができるDVCを使うことで100MB以上のファイルをアップロードできるようになった。



この記事は[Zenn](https://zenn.dev/2lu3)と[個人ブログ](https://2lu3.github.io/)の両方で公開しています。

# 前提条件

* 研究データを自宅サーバーで管理している
  * 研究データはテキストファイルに加えて10GBを超えるようなバイナリファイルも扱っている
* 以前は、バイナリファイルをGit LFSを用いてバージョン管理していた
* ネットワーク構成変更により、Cloudflare Tunnelを使って外部のネットワークから自宅サーバーにアクセスできるようにした
  * 以前は、DDNS+ルーターのDMZ機能を用いて外部からアクセスできた
* Cloudflare Tunnelでは100MB以上のファイルをアップロードすることができない
  * そのため、10GBを超えるバイナリファイルをGit LFSで管理することができなくなった
  * Git LFSにはチャンクアップロードの機能は実装されていないらしい

# 解決方法

Git LFSの代わりにに、Git + DVC + Minioを使用することで回避した。

## DVCとMinioとは

[Data Version Control](https://dvc.ai/)は機械学習分野のレポジトリ向けにバイナリファイルのバージョン管理をするツールです。機械学習レポジトリでは、同じコードでパラメーターを変えて学習することでパラメーターごとに異なったモデルの重みなどの出力ファイルが出てきます。機械学習向けに便利な機能がありますが、今回私は使わないので説明しません。気になる方は[機械学習プロジェクトのデータバージョン管理ツール『DVC』の「Get Started」のサブノート #機械学習 - Qiita](https://qiita.com/meow_noisy/items/a644547930e6f2dea12d)がわかりやすかったのでそちらを参照してください。

MinioはAWS S3互換 OSS オブジェクトストレージサーバーです。DVCはバイナリファイルのアップロード先を色々設定できるのですが、Minioも指定できます。Git LFSと異なり1つの大きなファイルを分割してアップロードするチャンクアップロードに対応しているので、先述のCloudflare Tunnelの100MB制限を突破することができます。

## 自宅サーバー側での作業

### Cloudflare TunnelでMinio用のサブドメインを設定する

`http://minio:9000`(API用)と`http://minio:9001`(Webページ用)のそれぞれにサブドメインを割り当てました。

### MinioをDocker Containerとしてたてる

タグ名は最後にZがついてるものを選びました。また、Cloudflare TunnelもDockerのコンテナを使っているので、そのコンテナと同じNetworkにいる必要があります。

```yaml
minio:
    image: quay.io/minio/minio:タグ名
    restart: always
    volumes:
      - type: volume
        source: minio_data
        target: /data
    environment:
      MINIO_ROOT_USER: ${MINIO_ROOT_USER}
      MINIO_ROOT_PASSWORD: ${MINIO_ROOT_PASSWORD}
    command: server /data --console-address ":9001"
```

### MinioのBuketを作成する

クライアント側での作業で使うので、作成したBuketの名前は覚えておきましょう。

## クライアント側での作業

### dvcの初期設定

```bash
pipx install dvc[s3]

cd gitで管理しているレポジトリのpath
dvc init

dvc remote add -d minio s3://Bucketの名前
dvc remote modify minio endpointurl Cloudflare Tunnelで指定したドメイン
```

### 使い方

```bash
dvc add ファイル名
dvc push
dvc pull
```

あたりが使えれば良さそう

