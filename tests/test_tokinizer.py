from hello_bot.tokinizer import Token


def test_token():
    token = Token.nikname
    catched = token.catch("@nikmosi")

    assert catched == "nikmosi"
