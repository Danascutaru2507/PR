     Acest cod este un exemplu simplu de utilizare a modulului socket din Python pentru a obține informații despre adresele IP și numele de domeniu asociate unui domeniu sau unei adrese IP și pentru a modifica serverul DNS folosit de sistem. 

     1. Pentru început, este importat modulul socket, care oferă funcționalități de rețea în Python.
           

     2. Ulterior, Utilizatorul este întâmpinat cu un mesaj și solicitat să introducă un nume de domeniu.  Într-un bloc try-except, se încearcă obținerea adreselor IP asociate domeniului introdus. Funcția socket.gethostbyname_ex() este utilizată pentru a obține informații despre domeniu. Lista de adrese IP este stocată în variabila ip_addresses.
    
    
    3. Dacă nu se întâmpină erori, se afișează adresele IP asociate domeniului. În cazul în care apare o excepție socket.gaierror, se afișează un mesaj de eroare.  Utilizatorul este solicitat să introducă o adresă IP.  Într-un alt bloc try-except, se încearcă obținerea numelui de domeniu asociat adresei IP introduse. Funcția socket.gethostbyaddr() este utilizată pentru a obține informații despre adresa IP. Numele de domeniu este stocat în variabila domain_name.


    4. Dacă nu se întâmpină erori, se afișează numele de domeniu asociat adresei IP. În cazul în care apare o excepție socket.herror, se afișează un mesaj de eroare. Se importă din nou modulul socket pentru a utiliza alte funcții. Este obținută adresa IP a serverului DNS curent utilizând socket.gethostbyname_ex() și socket.gethostname(). Adresa IP este stocată în variabila current_dns.
   
   
    5. Se afișează adresa IP a serverului DNS curent.  Utilizatorul este solicitat să introducă o adresă IP pentru un server DNS sau să lase câmpul gol pentru a utiliza serverul presetat de sistem.  Dacă a fost introdusă o adresă IP, se încearcă schimbarea serverului DNS utilizând funcția socket.gethostbyname_ex() pentru a verifica validitatea adresei IP introduse. Dacă nu apar erori, se afișează un mesaj de confirmare pentru schimbarea serverului DNS.  În cazul în care apare o excepție socket.gaierror, se afișează un mesaj de eroare.  Dacă utilizatorul a lăsat câmpul gol, se atribuie variabilei dns_server valoarea None și se afișează un mesaj indicând că serverul presetat de sistem va fi utilizat.