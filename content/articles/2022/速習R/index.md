Title: Rを速習したときのメモ
Category: プログラミング
Tags: R


[たのしいR言語入門 - Qiita](https://qiita.com/ninomiyt/items/06fdb1d9052b9b6d8d45)

```r
x <- 10 # 代入

c(1, 2, 3) # ベクトル

list(1, "a", 3.14) # リスト
person <- list(名字="山田", 名前="太郎", 性別="男")
person$名字

身長 <- c(160, 170, 180)
体重 <- c(50, 60, 70)
X = data.frame(身長, 体重)
X$身長

X$BMI <- round(X$体重 / (X$身長 / 100) ^ 2)

# 正規分布の乱数を100万個作る
x <- rnorm(1000000)
# ヒストグラムを描く
hist(x)

```

[R言語を初めて学んだのでまとめてみた - Qiita](https://qiita.com/piro87084806/items/d75d9bb9a6db4e4d8b9a)

```r
■テストの点数をx、回数をyとした際の、ブートストラップ法で平均値を求める関数の作成例
avg_function <- function(x, y) {
  # 平均値を格納するために、空のベクトルaverageを作成
  average <- c()
  # y回繰り返す処理を作成
  for(i in 1:y) {
    # test_scoreから復元抽出で7つのデータをサンプリングし、sample_scoreというベクトルに格納する
    sample_score <- sample(x, size = length(x), replace = TRUE)
    # meanを使って平均値を計算し、mというベクトルに格納する
    m <- mean(sample_score)
    # 計算結果をaverageに格納
    average <- c(average, m)
  }
  return(average)
}

# 作成した関数に直接の値で処理する場合
avg_function(x=c(70, 80, 40, 55, 95, 33, 63), y=1000)

# テストの点数が入ったベクトルtest_scoreを作成
test_score <- c(70, 80, 40, 55, 95, 33, 63)
# 作成した関数にベクトルの値を用いて処理する場合
avg_function(x=test_score, y=1000)
```

[Pythonプログラマが30分でわかるR - Qiita](https://qiita.com/zettsu-t/items/4e52a877f92c5c05caf8)

```r
is.na(0)
is.na(NA)
is.infinite(0)
is.infinite(Inf)
is.infinite(-Inf)
is.nan(NaN)
-Inf < 0
is.null(0)
is.null(NULL)
2 + NA # NA
2 > NA # NA
```

NA: 欠損値

NAN: 値ではない

```r
score_vec <- c(15, 26, 37, 48)
name_vec <- c("foo", "bar", "poi")
score_vec #  ##[1] 15 26 37 48
score_vec[1] # ##[1] 15
score_vec[c(1, 4)] # ## [1] 15, 48

c(c(1, 2, 3), c(4, 5)) # ベクトルの結合
```

```r
NROW(c(10, 20, 30)) # 要素数
seq_len(3) # range(1,4)
seq_len(NROW(c(10, 20, 30))) # c(1, 2, 3)
```

```r
a_lst <- list(name = "foo", score = 80, year = 2019)
a_lst$score
a_lst[["score"]]
a_lst[[2]]
```
