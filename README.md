## 概要
* fluentdのテスト
* APIサーバ(python, flask) -> ログサーバ(fluentd, python) -> Mongo, S3

## fluentd.conf
<match fluent.test.**>
    @type file
    path /Users/onpajapan27/test/fluentd_test/log_server/log
</match>

<source>
  @type forward
</source>


## TODO
* 現状はログサーバが受け取ってlogファイルに保存してるだけなので、pythonで扱いたい
