import requests

base_url = "https://localhost:44370/api/Category"

resp = requests.get("https://localhost:44370/swagger/index.html", verify=False)


def get_categories():
    try:
        response = requests.get(f"{base_url}/categories", verify=False)
        response.raise_for_status()
        categories = response.json()
        print("Categoriile disponibile sunt:")
        for category in categories:
            print(f"ID: {category['id']}, Nume: {category['name']}")
    except requests.exceptions.RequestException as e:
        print("Eroare la obținerea categoriilor:", e)


def get_category_details(id):
    try:
        response = requests.get(f"{base_url}/categories/{id}", verify=False)
        if response.status_code == 404:
            print("Categoria", id, "nu există.")
        else:
            response.raise_for_status()

            products_response = requests.get(f"{base_url}/categories/{id}/products", verify=False)
            products_response.raise_for_status()
            products = products_response.json()

            if len(products) > 0:
                print("Produsele din această categorie sunt:")
                for product in products:
                    print(products)
            else:
                print("Această categorie nu are produse.")
    except requests.exceptions.RequestException as e:
        print("Eroare la obținerea detaliilor despre categoria", id + ":", e)


def create_category(category_name):
    data = {"title": category_name}
    url = base_url + "/categories"
    response = requests.post(url, json=data, verify=False)
    if response.status_code == 200:
        print("Request successful!")
        print(response.json())
        get_categories()
    else:
        print("Request failed with status code:", response.status_code)


def delete_category(id):
    try:
        response = requests.delete(f"{base_url}/categories/{id}", verify=False)
        if response.status_code == 404:
            print("Categoria", id, "nu există.")
        else:
            response.raise_for_status()
            print("Categoria", id, "a fost ștearsă cu succes.")
    except requests.exceptions.RequestException as e:
        print("Eroare la ștergerea categoriei", id + ":", e)


def modify_category_title(category_name):
    data = {"title": category_name}
    response = requests.put(base_url + f"{id}", json=data, verify=False)
    if response.status_code == 200:
        print('category renamed successfully')
    else:
        print('Failed to delete category:', response.status_code)


def create_product(id, product_name, pret):
    data = {"title": product_name, "price": str(pret), "categoryId": id}
    response = requests.post(base_url + f"/categories/{id}/products", json=data, verify=False)
    if response.status_code == 200:
        print('Success')
    else:
        print("Request failed with status code:", response.status_code)


def show_category_products(id):
    category = requests.get(base_url + f"/categories/{id}/products", verify=False)
    if category.status_code == 200:
        categories = category.json()
        for category in categories:
            print(category)
    else:
        print("Request failed with status code:", category.status_code)


def process_choice(choice):
    if choice == "1":
        get_categories()
    elif choice == "2":
        id = input("Introduceți ID-ul categoriei: ")
        get_category_details(id)
    elif choice == "3":
        category_name = input("Introduceți numele categoriei: ")
        create_category(category_name)
    elif choice == "4":
        id = input("Introduceți ID-ul categoriei pe care doriți să o ștergeți: ")
        delete_category(id)
    elif choice == "5":
        id = input("Introduceti id-ul pentru categoria dorita: ")
        category_name = input("Introduce noul nume al categoriei:")
    elif choice == "6":
        id = input("Introduceți ID-ul categoriei: ")
        product_name = input("Introduceți numele produsului: ")
        pret = input("pretul:")
        create_product(id, product_name, pret)
    elif choice == "7":
        id = input("Introduceți ID-ul categoriei: ")
        show_category_products(id)
    elif choice == "8":
        print("La revedere!")
        return False
    return True


def menu():
    while True:
        print("|===== Meniu =====|")
        print("1. Afișează categoriile disponibile")
        print("2. Afișează detalii despre o categorie")
        print("3. Adaugă o categorie nouă")
        print("4. Șterge o categorie")
        print("5. Modifică titlul unei categorii")
        print("6. Adaugă produs într-o categorie")
        print("7. Afișează lista de produse dintr-o categorie")
        print("8. Ieșire")

        choice = input("Introduceți opțiunea dorită: ")
        if not process_choice(choice):
            break


menu()