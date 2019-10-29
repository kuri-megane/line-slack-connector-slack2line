import os

from linebot import LineBotApi
from linebot.models import TextSendMessage
from slackbot.bot import listen_to
from slackbot.bot import respond_to

CHANNEL_ACCESS_TOKEN = os.environ["LINE_CHANNEL_ACCESS_TOKEN"]

line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)


# メンションされたメッセージに対して
@respond_to('reply (.*)')
def mention_func(message, _):

    # slack投稿者のユーザ名を取得
    name = message.channel._client.users[message._body['user']]['real_name'] + "さん\n"

    # slackに投稿されたメッセージのパース
    text = message.body['text']
    parse_msg = text.split(' ')

    if len(parse_msg) >= 3:
        _, to, *send_msg = parse_msg

        # lineに送る
        line_bot_api.push_message(
            to=to,
            messages=TextSendMessage(text=name + ' '.join(map(str, send_msg)))
        )

        # メッセージにスタンプをつける
        message.react('+1')


# reply で始まるメッセージに対して
@listen_to(r'^reply\s+\S.*')
def reaction_func(message):

    # slack投稿者のユーザ名を取得
    name = message.channel._client.users[message._body['user']]['real_name'] + "さん\n"

    # slackに投稿されたメッセージのパース
    text = message.body['text']
    parse_msg = text.split(' ')

    if len(parse_msg) >= 3:
        _, to, *send_msg = parse_msg

        # lineに送る
        line_bot_api.push_message(
            to=to,
            messages=TextSendMessage(text=name + ' '.join(map(str, send_msg)))
        )

        # メッセージにスタンプをつける
        message.react('+1')
