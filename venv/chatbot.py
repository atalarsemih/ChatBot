from cleverbotfree import Cleverbot


@Cleverbot.connect
def chat(bot,user_prompt,bot_prompt):
    while True:
        user_input = input(user_prompt)
        if user_input == "quit":
            break
    reply = bot.single_exchange(user_input)
    print(bot_prompt, reply)
    bot_reply_eng
    speak(bot_reply_eng)


    chat("Me","Jarvis")