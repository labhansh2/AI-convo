import asyncio
from EdgeGPT import Chatbot as m_chatbot, ConversationStyle
from pprint import pprint
import os
from Bard import Chatbot as g_chatbot
from dotenv import load_dotenv
from termcolor import colored
import pathlib

load_dotenv()
bard_token = os.getenv("BARD_KEY")
bing_text = colored('Bing', 'blue')
bard_text = colored('Bard', 'magenta')
init_text = colored('Init', 'green')

load_dotenv()
init = os.getenv("init_msg")
if len(init) == 0:
    init = 'Hi I am Bard. Would you like to discuss interesting topics like cosmos with me?'

log_path = pathlib.Path(__file__).parent/"chat_logs"
with open(log_path/".log_counter.txt", 'r') as get_count:
    data = get_count.read()

next = str(int(data) + 1)
with open(log_path/".log_counter.txt", 'w') as edit_count:
    edit_count.write(next)

log_file = fr"{log_path}/chat_{next}.txt"


def log(bot, bot_resp):

    resp = f"{bot_resp}\n{'-'*100}"

    if bot == 'bing':
        bot_log = f"{bing_text} : {resp}"
        log = f"Bing : {resp}\n"
    elif bot == 'bard':
        bot_log = f"{bard_text} : {resp}"
        log = f"Bard : {resp}\n"
    elif bot == 'init':
        bot_log = f"{init_text} : {resp}"
        log = f"Init : {resp}\n"

    print(bot_log)

    with open(log_file, 'a', encoding='utf-8') as logger:
        logger.write(log)


async def main():

    global init
    global bard_token
    global bing_text
    global bard_text

    bing = await m_chatbot.create(cookie_path='cookies.json')

    bard = g_chatbot(bard_token)

    bard_resp = init
    log('init', init)

    try:
        get_bing = await bing.ask(prompt=bard_resp,
                                  conversation_style=ConversationStyle.creative,
                                  wss_link="wss://sydney.bing.com/sydney/ChatHub")
    except:
        bing_resp = 'Bing Broke'
        log('bing', bing_resp)
        return
    else:
        bing_resp = get_bing['item']['messages'][1]['text']
        log('bing', bing_resp)
        if "Click" in bing_resp and "New topic" in bing_resp:
            print('MAX CAPACITY REACHED FOR BING')
            return

    while True:

        try:

            get_bard = bard.ask(bing_resp)
        except:
            bard_resp = 'Bard Broke'
            log('bard', bard_resp)
            return
        else:
            bard_resp = get_bard['content']
            log('bard', bard_resp)

        try:
            get_bing = await bing.ask(prompt=bard_resp,
                                      conversation_style=ConversationStyle.creative,
                                      wss_link="wss://sydney.bing.com/sydney/ChatHub")
        except:
            bing_resp = 'Bing Broke'
            log('bing', bing_resp)
            return
        else:
            bing_resp = get_bing['item']['messages'][1]['text']
            log('bing', bing_resp)
            if "Click" in bing_resp and "New topic" in bing_resp:
                print('MAX CAPACITY REACHED FOR BING')
                return

    else:
        m_chatbot.close()


if __name__ == "__main__":

    asyncio.run(main())
