from hello_bot.tokinizer import Token


def test_nikname_token():
    token = Token.nikname
    catched = token.catch("@nikmosi")

    assert catched == "nikmosi"

def test_nikname_token_with_two_nikname():
    token = Token.nikname
    catched = token.catch("@nikmosi @jeezer")

    assert catched == "nikmosi"
