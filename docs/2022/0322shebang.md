# Lispのshebang

Lispの実行の仕方がわからん。REPLであそんでいるので...
調べたけどすぐ忘れちゃうから書いておく。

(1) プロンプトでこうする

```(load "foo.lisp")```

(2) シェルから実行する

```sbcl --script foo.lisp```

(3) shebangを使う

```#!/usr/local/bin/sbcl --script
(code....)```

なるほどね。

参考文献<br />
[https://marui.hatenablog.com/entry/20090401/1238629439](https://marui.hatenablog.com/entry/20090401/1238629439)
