"""
slack側のbotの設定
"""
import os

# トークンを指定
API_TOKEN = os.environ["SLACK_API_TOKEN"]

# このbot宛の標準の応答メッセージ
DEFAULT_REPLY = "このbotにはメッセージを送ることはできません"

# プラグインスクリプトのリスト
PLUGINS = ['plugins']
