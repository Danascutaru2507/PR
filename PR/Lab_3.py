import socket


domain_name = input("Introduceti numele de domeniu: ")

try:
    ip_addresses = socket.gethostbyname_ex(domain_name)[2]
    print("Adresele IP asociate domeniului {} sunt:".format(domain_name))
    for ip in ip_addresses:
        print(ip)
except socket.gaierror:
    print("Nu am putut obtine adresele IP pentru domeniul {}".format(domain_name))

ip_address = input("Introduceti adresa IP: ")

try:
    domain_name = socket.gethostbyaddr(ip_address)[0]
    print("Numele de domeniu asociat cu adresa IP {} este: {}".format(ip_address, domain_name))
except socket.herror:
    print("Nu am putut obtine numele de domeniu pentru adresa IP {}".format(ip_address))

import socket

current_dns = socket.gethostbyname_ex(socket.gethostname())[2][0]

print("Serverul DNS curent este: {}".format(current_dns))


dns_server = input("Introduceți adresa serverului DNS sau lăsați gol pentru a utiliza serverul presetat de sistem: ")
if dns_server:
    socket.setdefaulttimeout(2)
    try:
        socket.gethostbyname_ex(dns_server)
        print("Serverul DNS a fost schimbat cu succes la adresa: {}".format(dns_server))
    except socket.gaierror:
        print("Nu am putut utiliza serverul DNS indicat")
else:
    dns_server = None
    print("Se va utiliza serverul presetat de sistem.")
