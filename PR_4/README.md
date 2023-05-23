 #Înainte de lansarea programului, am descărcat de pe ELSE („UtmShop”).

   Acest cod reprezintă o aplicație de linie de comandă care permite utilizatorului să interacționeze cu o API REST pentru gestionarea categoriilor și produselor. 


      # import requests
   Acest import permite utilizarea funcțiilor și metodelor din modulul requests pentru a efectua cereri HTTP către API.


   Definirea variabilei base_url:

    # base_url = "https://localhost:44370/api/Category"
Această variabilă stochează URL-ul de bază al API-ului cu care se vor face cererile.


    Efectuarea unei cereri GET pentru a obține documentația API-ului:
    # resp = requests.get("https://localhost:44370/swagger/index.html", verify=False)
Această cerere GET este utilizată pentru a obține documentația API-ului prin accesarea paginii Swagger. Parametrul verify=False este setat pentru a dezactiva verificarea certificatului SSL în cazul în care se utilizează un server local neautentificat.


    Definirea funcției get_categories():
 
        #def get_categories():
          # Codul funcției...
Această funcție efectuează o cerere GET către API pentru a obține categoriile disponibile și le afișează în consolă.


     Definirea funcției get_category_details(id):

            #def get_category_details(id):
              # Codul funcției...
Această funcție efectuează o cerere GET către API pentru a obține detalii despre o categorie specificată prin ID și le afișează în consolă.

 
     Definirea funcției create_category(category_name):


           #def create_category(category_name):
             # Codul funcției...
Această funcție efectuează o cerere POST către API pentru a crea o categorie nouă pe baza unui nume specificat de utilizator.


     Definirea funcției delete_category(id):

            #def delete_category(id):
               # Codul funcției...
Această funcție efectuează o cerere DELETE către API pentru a șterge o categorie specificată prin ID.


     Definirea funcției modify_category_title(category_name):

        #def modify_category_title(category_name):
            # Codul funcției...
Această funcție efectuează o cerere PUT către API pentru a modifica titlul unei categorii existente.


   Definirea funcției create_product(id, product_name, pret):

         #def create_product(id, product_name, pret):
            # Codul funcției...
Această funcție efectuează o cerere POST către API pentru a crea un produs nou într-o categorie specificată.


     Definirea funcției show_category_products(id):

         #def show_category_products(id):
              # Codul funcției



