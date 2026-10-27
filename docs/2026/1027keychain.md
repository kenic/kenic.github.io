# 秘密鍵のパスフレーズをキーチェーンに保存する

SSHの秘密鍵のパスフレーズを毎回打っているんですが、だるい ^^;
Macだったらキーチェーンに保存すればいいらしい。手順は下記の通り。

まず下記を1回実行 (id_rsaは秘密鍵のファイルに置き換える)

```
ssh-add --apple-use-keychain ~/.ssh/id_rsa
```

パスフレーズを聞かれるので入力。
次に、~/.ssh/config に以下にこんな感じのを追加。

```
Host *
    AddKeysToAgent yes
    UseKeychain yes

Host github.com
    User git
    IdentityFile ~/.ssh/id_rsa
```

以上です ^^;