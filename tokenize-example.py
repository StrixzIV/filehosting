import re
import os
import pythainlp

info_log = lambda log_message: print(f'\u001b[45;1m ** \u001b[0m {log_message}')
error_log = lambda log_message: print(f'\u001b[41;1m !! \u001b[0m {log_message}')
incoming_log = lambda log_message: print(f'\u001b[42;1m -> \u001b[0m {log_message}')
outgoing_log = lambda log_message: print(f'\u001b[41;1m <- \u001b[0m {log_message}')
clear_log = lambda: os.system('cls' if os.name == 'nt' else 'clear')

clear_log()
info_log("Tokenization example")

while True:
    
    try:
        inp = input('\u001b[47;1m #> \u001b[0m ').strip()
        
        message = inp.lower()
        tokenized_text = pythainlp.word_tokenize(re.sub(r'[\^!#$%&\n\'\"()*+,-./:;<=>?@[\]^_`{|}~]', '', message), keep_whitespace = False)
        
        incoming_log(f'In: {inp}')
        outgoing_log(f'Out: {tokenized_text}')
        
    except (KeyboardInterrupt, EOFError):
        print()
        info_log('Exiting tokeinzation example...')
        exit()
    