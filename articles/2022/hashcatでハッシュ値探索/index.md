Title: hashcatでハッシュ値探索
Category: ツール
Tags: ubuntu, WSL
Status: draft


```shell
# 数字のみ

hashcat.exe -m 10700 -a 3 -w 4 hash.txt --increment -1 ?d  '?1?1?1?1?1?1?1?1?1' --session test

# 小文字のみ

hashcat.exe -m 10700 -a 3 -w 4 hash.txt --increment -1 ?l  '?1?1?1?1?1?1?1?1?1' --session test

# 数字＋小文字

hashcat.exe -m 10700 -a 3 -w 4 hash.txt --increment -1 ?d?l  '?1?1?1?1?1?1?1?1?1' --session test

# 数字＋大文字小文字

hashcat.exe -m 10700 -a 3 -w 4 hash.txt --increment -1 ?u?d?l  '?1?1?1?1?1?1?1?1?1' --session test

# （数字＋大文字小文字）＋（数字＋小文字）

hashcat.exe -m 10700 -a 3 -w 4 hash.txt --increment -1 ?d?l -2 ?u?l?d  '?2?1?1?1?1?1?1?1?1' --session test
```
