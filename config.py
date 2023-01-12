import json
import os

nbRouteurs = 14;
fileObject = open("config.json", "r")
jsonContent = fileObject.read()
cList = json.loads(jsonContent)
print(cList["AS1"]["routeurs"])

os.remove("config.cfg")
fichier = open("config.cfg", "a")
fichier.write("\n!\nversion 15.2\nservice timestamps debug datetime msec\nservice timestamps log datetime msec\n!\nhostname ")
fichier.write(cList["AS1"]["routeurs"][0])
fichier.write("\n!\nboot-start-marker\nboot-end-marker\n!\n!\n!\nno aaa new-model\nno ip icmp rate-limit unreachable\nip cef\n!\n!\n!\n!\n!\n!\nno ip domain lookup\nipv6 unicast-routing\nipv6 cef\n!\n!\nmultilink bundle-name authenticated\n!\n!\n!\n!\n!\n!\n!\n!\n!\nip tcp synwait-time 5\n!\n!\n!\n!\n!\n!\n!\n!\n!\n")

print("protocole de ",cList["AS1"]["routeurs"][0]," ?")
protocole=input()

nbInterfaces = 0;
for i in range(len(cList["AS1"])):
    connexion = cList["AS1"]["connections"][i].split("-")
    if ((connexion[0]=="R1") or (connexion[1]=="R1")):
        fichier.write("interface ")
        fichier.write(cList["config"]["interfaces"][i])
        fichier.write("\n")
        fichier.write(cList["config"]["conf"][0])
        fichier.write("IPaddress\n")
        if protocole == "RIP":
            fichier.write(cList["config"]["conf"][1])
        elif protocole == "OSPF":
            fichier.write(cList["config"]["conf"][2])
        fichier.write("\n!\n")
        nbInterfaces = nbInterfaces+1
if nbInterfaces<4:
    for i in range(4-nbInterfaces):
        fichier.write("interface ")
        fichier.write(cList["config"]["interfaces"][i+nbInterfaces])
        fichier.write("\n")
        fichier.write(cList["config"]["no conf"])
        fichier.write("\n!\n")

fichier.write("router bgp ")
fichier.write("AS")
fichier.write("\n bgp router-id ")
fichier.write("12.12.12.12")
fichier.write("\n bgp log-neighbor-changes\n no bgp default ipv4-unicast\n")

fichier.write("!\n!\n!\n!\ncontrol-plane\n!\n!\nline con 0\n exec-timeout 0 0\n privilege level 15\n logging synchronous\ stopbits 1\nline aux 0\n exec-timeout 0 0\n privilege level 15\n logging synchronous\n stopbits 1\nline vty 0 4\n login\n!\n!\nend")

fichier.close()

fileObject.close()
