Title: neovimのcolorscheme選び
Category: 開発環境
Tags: neovim

neovimでいい感じcolorscheme(テーマ)を選び、deinで導入する一連の流れについて説明します。

# vim color schemesで好きなテーマを選ぶ

[Trending vim color schemes | vimcolorschemes](https://vimcolorschemes.com/)

上のサイトでは、よく使われているテーマを調べることができます。

自分が好きなテーマを選んでください。

# deinに追加

`dein.toml`に以下の内容を追記します。

```toml
[[plugins]]
repo = 'テーマのURL'
```

その後、

```vimscript
colorscheme gruvbox(自分の選んだテーマの名前)
```

と、`dein.toml`を読み込んだあとに呼び出すようにvimrcに追記しましょう。

