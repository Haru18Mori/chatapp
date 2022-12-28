作業ツリー　樹形図みたいなフォルダの塊のこと
リポジトリ　作業ツリーの一番上のフォルダのこと
コミット　ファイルとかを変更したときにそれをリポジトリに記録すること
コミットメッセージ　〜〜が更新されたよ〜と

 - テストコードのメモ
２個のお返事　２００とか３０２とか番号
（ただのGET処理→１個のお返事、かPOST処理→２個のお返事なのか）
TestsWithAuthMixinで自分から便利機能を作ってあげる
ログインしないと入れないところを明確に分ける必要があるため。
POSTの時はデータとURL、二つのステータスコード、レスポンスがTRUEか
GETの時はURLとちゃんとアクセスできているかの２００番、HTML(テンプレート）があっているかどうか
clsってなんだにゃ？？？
→→→classの略で、主体みたいな感じ。引数で、何かが入ってくる。関数みたいな感じ


 - ロギング

まずpython３でシェルを開く
```python
→import logging
logging.basicConfig(level=logging.INFO)
logging.info("info-level log")
logging.warning("warning-level log")
```

 - 時間を表示
```python
import logging
logging.basicConfig(format="%(asctime)s %(levelname)s:%(message)s")
```

format="%(asctime)s : %(message)s"とか
 - ファイルで使う

settings.pyに

```python
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "simple": {
            "format": "%(levelname)s: %(message)s",
        }
    },
    "handlers": {
        "stream": {
            "level": "INFO",
            "class": "logging.StreamHandler",
            "formatter": "simple",
        },
    },
    "loggers": {
        "main": {
            "handlers": ["stream"],
            "level": "INFO",
            "propagate": True,
        },
    },
}
```

views.pyに
```python
import logging

logger = logging.getLogger(__name__)

@login_required
def talk_room(request, user_id):
    # ...
    if request.method == "GET":
        form = TalkForm()
    elif request.method == "POST":
        # ...
        if form.is_valid():
            # ...
            logger.info("A message has been sent: %s to %s", request.user.username, friend.username)  # 追加
            return redirect("talk_room", user_id)
    # ...
```

