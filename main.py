from termcolor import colored

from locker import Locker


def get_user_input():
    print(" ")
    print(colored("\n[+] Loker management system", "red",
                  attrs=['bold']))
    print(colored("[+] init[jumlah loker]: untuk membuat jumlah loker", 'blue', attrs=['bold']))
    print(colored("[+] status: untuk menampilkan status dari masing-masing nomer loker", 'blue', attrs=['bold']))
    print(
        colored("[+] input[tipe identitas][nomer identitas]: untuk memasukan kartu identitas", 'blue', attrs=['bold']))
    print(colored("[+] leave[nomer loker]: untuk mengosongkan loker", 'blue', attrs=['bold']))
    print(colored("[+] find[nomer identitas]: menampilkan nomer loker berdasarkan nomer identitas", 'blue',
                  attrs=['bold']))
    print(colored("[+] search[tipe identitas]: akan menampilkan nomer identitas sesuai tipe identitas yang dicari",
                  'blue', attrs=['bold']))
    print(colored("[+] exit: untuk mengakhiri program", 'blue', attrs=['bold']))


def main():
    while True:
        try:
            get_user_input()
            text = input('(loker)')
        except not text:
            break
        if not text:
            continue
        locker = Locker(text)
        locker.run()


if __name__ == '__main__':
    main()
