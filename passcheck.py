import requests
import hashlib
import sys

def request_data_api(head_char):
    url = 'https://api.pwnedpasswords.com/range/' + head_char
    res = requests.get(url)
    return res

def read_num_hacked(hashs,hash_to_check):
    hashs = (line.split(':') for line in hashs.text.splitlines())
    for h, counts in hashs:
        if (h == hash_to_check):
            return counts
    return 0
        

def pwned_api_check(password):
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper() # converting the password to sha1 
    head_char = sha1password[:5] #this will help finding my password without providing full to Api
    tail_char = sha1password[5:] #this will help matching my password in lists 
    response = request_data_api(head_char)
    return read_num_hacked(response,tail_char)

def main(args):
    for password in args:
        count = pwned_api_check(password)
        if (int(count) > 1 and int(count) <= 10):
            print(f'your {password} was hacked {count} times, you should consider changing your password')
        elif int(count) > 10:
            print(f'your {password} was hacked {count} times, chage your password now!!')
        else:
            print(f'Your {password} is secured and safe')


if __name__ == "__main__":
    main(sys.argv[1:])