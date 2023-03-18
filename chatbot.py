import random

responses = {
  "你好": ["你好", "你好呀", "您好"],
  "您是谁": ["我是一个聊天机器人", "我是ChatGPT"],
  "你会做什么": ["我会回答你的问题", "我会聊天"],
}

def generate_response(user_input):
    if user_input in responses:
        return random.choice(responses[user_input])
    else:
        return "我不知道你在说什么"


if __name__ == '__main__':


    while True:
        message = input("请输入您的问题：")
        response = generate_response(message)
        print("机器人：" + response)

