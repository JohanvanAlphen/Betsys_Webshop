__winc_id__ = "d7b474e9b3a54d23bca54879a4f1855b"
__human_name__ = "Betsy Webshop"

from models import *
from setupdb import *
from datetime import datetime
from rich import print
from time import sleep


def search(term: str):
    term = term.lower()
    query = Products.select().where(Products.name.contains(term)
                                    | Products.description.contains(term))
    if query:
        print(
            f":magnifying_glass_tilted_right: Your search term {term} has been matched to:")
        for product in query:
            print(product.name)
    else:
        print(
            f"[bold red]:exclamation_mark: No products found with {term}[/bold red]")


def list_user_products(user_id: int):
    query = Products.select().where(Products.owner == user_id)

    if query:
        user = Users.get_by_id(user_id)
        print(
            f"[bold]:magnifying_glass_tilted_right: Products of {user.name}:[/bold]")
        for product in query:
            print(f"{product.name}: Quantity owned: {product.amount_in_stock}")
    else:
        print(
            f"[bold red]:exclamation_mark: No match found or invalid id was given.[/bold red]")


def list_products_per_tag(tag_id: int):
    query = Products.select().join(ProductTag).join(
        Tags).where(Tags.tag_id == tag_id)

    if query:
        tag = Tags.get_by_id(tag_id)
        print(
            f":magnifying_glass_tilted_right: Tagged products with tag [bold]{tag.name}[/bold]:")
        for product in query:
            print(f"{product.name}")
    else:
        print(
            "[bold red]:exclamation_mark: No products found with this tag or tag does not exist[/bold red]")


def add_product_to_catalog(user_id: int, product_id: int):
    user = Users.get_by_id(user_id)
    product = Products.get_by_id(product_id)

    product.owner = user
    product.save()

    print(f":thumbs_up: Product {product.name} added for {user.name}")


def update_stock(product_id, new_quantity):
    query = Products.get_by_id(product_id)

    old_stock = query.amount_in_stock
    query.amount_in_stock = new_quantity
    query.save()
    print(
        f"[bold]:memo: Old Stock of {query.name}: {old_stock}, new stock: {new_quantity}[/bold]")


def purchase_product(product_id: int, buyer_id: int, quantity: int):
    product = Products.get_by_id(product_id)
    buyer = Users.get_by_id(buyer_id)

    if buyer_id == product.owner:
        print(
            f"[bold red]:cross_mark: You cannot buy products from yourself {buyer.name}.[/bold red]")

    if quantity >= product.amount_in_stock:
        print(
            f"[bold red]:exclamation_mark: Insufficient stock of {product.name}![/bold red] [bold]Current stock is {product.amount_in_stock}.[/bold]")

    else:
        price_per_unit = product.price_per_unit
        purchased_price = round(product.price_per_unit * quantity, 2)

        transaction = Transactions.create(
            buyer=buyer_id,
            purchased_product=product_id,
            purchased_quantity=quantity,
            purchased_price=purchased_price,
            date=datetime.now().date()
        )
        print(
            f"[bold]:thumbs_up: On {transaction.date} {buyer.name} bought {quantity} of {product.name} for total amount of: €{transaction.purchased_price}.[/bold]\n:euro_banknote: Price per unit is €{price_per_unit}")

        new_quantity = product.amount_in_stock - quantity

        update_stock(product_id, new_quantity)


def remove_product(product_id):
    try:
        query = Products.get_by_id(product_id)
        print(f":thumbs_up: Product {query.name} has been removed!")
        query.delete_instance()

    except DoesNotExist:
        print(
            f":exclamation_mark: Product id {product_id} does not exist or has already been removed.")


def main():

    print("If database exists it will be deleted first to make a clean start!")
    print("")
    sleep(1.00)

    if os.path.exists("betsys_webshop.db") == True:
        delete_database()

    print("Creating database, wait a moment...")
    sleep(2.00)

    create_test_data()
    print("")
    sleep(2.00)

    # Search function:
    print(
        "Starting Search function with term [italic blue]broek[/italic blue], wait a moment...")
    sleep(2.00)
    search("broek")
    print("")
    sleep(2.00)

    # List User Products function:
    print(
        "Starting List User Products function with [italic blue]user_id: 1[/italic blue] which is [bold]Bas Sillen[/bold], wait a moment...")
    sleep(2.00)
    list_user_products(1)
    print("")
    sleep(2.00)

    # List Products Per Tag function:
    print(
        "Starting List Products Per Tag function with [italic blue]tag_id: 2[/italic blue] which is [bold]katoen[/bold], wait a moment...")
    sleep(2.00)
    list_products_per_tag(2)
    print("")
    sleep(2.00)

    # Add Product To Catalog function:
    print(
        "Starting Add Product To Catalog function with [italic blue]user_id: 2[/italic blue] which is [bold]Ben Boute[/bold] and [italic blue]product id: 3[/italic blue] which is [bold]Chino[/bold], wait a moment...")
    sleep(2.00)
    add_product_to_catalog(2, 3)
    print("")
    sleep(2.00)

    # Update Stock function:
    print(
        "Starting the Update Stock function with [italic blue]product_id: 5[/italic blue] which is [bold]Tshirt[/bold] and adjust the [italic blue]stock[/italic blue] to [bold]25[/bold], wait a moment...")
    sleep(2.00)
    update_stock(5, 25)
    print("")
    sleep(2.00)

    # Purchase Product function:
    print(
        "Starting Purchase Product function with [italic blue]product_id: 4[/italic blue] which is [bold]Vest[/bold], \n[italic blue]buyer_id: 5[/italic blue] which is [bold]Wil Bierman[/bold],\nand [italic blue]quantity[/italic blue] of [bold]2[/bold], wait a moment...")
    sleep(2.00)
    purchase_product(4, 5, 2)
    print("")
    sleep(2.00)

    # Remove Product function:
    print(
        "Starting Remove Product function with [italic blue]product_id: 2[/italic blue] which is [bold]hoodie[/bold], wait a moment...")
    sleep(2.00)
    remove_product(2)
    print("")
    sleep(2.00)

    print(f":zany_face: And Now For Something Completely Different...")
    print("")
    sleep(2.00)
    print("Invalid fields:")
    print("")
    sleep(2.00)

    # Invalid Search:
    print(
        "Invalid Search with term [italic blue]jas[/italic blue], wait a moment...")
    sleep(2.00)
    search("jas")
    print("")
    sleep(2.00)

    # Invalid List User Products:
    print(
        "Invalid List User Products with [italic blue]user_id: 8[/italic blue], wait a moment...")
    sleep(2.00)
    list_user_products(8)
    print("")
    sleep(2.00)

    # Invalid List Products Per Tag:
    print(
        "Invalid List Products Per Tag with [italic blue]tag_id: 9[/italic blue], wait a moment...")
    sleep(2.00)
    list_products_per_tag(9)
    print("")
    sleep(2.00)

    # Insufficient stock:
    print("Insufficient stock for [italic blue]product_id: 1[/italic blue] which is [bold]spijkerbroek[/bold], \n[italic blue]buyer_id: 3[/italic blue] which is [bold]Bennie Koekoek[/bold],\nand [italic blue]quantity[/italic blue] of [bold]8[/bold], wait a moment... ")
    sleep(2.00)
    purchase_product(1, 3, 8)
    print("")
    sleep(2.00)

    # Invalid id for Remove Product:
    print(
        "Invalid id for Remove Product: [italic blue]product_id: 7[/italic blue], wait a moment...")
    sleep(2.00)
    remove_product(7)
    print("")
    sleep(2.00)
    print(
        f":anxious_face_with_sweat: [bold green]Thank you for your attention and patience![/bold green]")


if __name__ == '__main__':
    main()
