import requests

question = input('Enter your question for the magic 8 ball: ')

try:
    # this url doesn't work. program will crash without exception handling
    magic_8_ball_url = f'https://8ball.delegator.com/magic/JSON/{question}'

    # working url
    # magic_8_ball_url = f'https://magic-8-ball-mctc.uc.r.appspot.com/magic/JSON/{question}'

    response = requests.get(magic_8_ball_url).json()    # make api request and get json response
    print(response)

    answer = response['magic']['answer']    # access answer from json response
    print(f'The magic 8 ball says... {answer}')

except Exception as e:
    print(e)    # print information about the error
    print('Sorry, can\'t contact the magic 8 ball right now.')
