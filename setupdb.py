from models import *
from rich import print
import os


# Hele database verwijderen / Delete complete database:
def delete_database():
    cwd = os.getcwd()
    database_path = os.path.join(cwd, "betsys_webshop.db")
    if os.path.exists(database_path):
        os.remove(database_path)


# Aanmaken van database / Create database:
def create_test_data():
    db.connect()
    cwd = os.getcwd()
    print(
        f":thumbs_up: Betsy's webshop database is created in folder [bold yellow]{cwd}[/bold yellow]")

    db.create_tables(
        [
            Users,
            Products,
            Tags,
            ProductTag,
            Transactions
        ]
    )
    # User 1
    bassillen = Users.create(
        name="Bas Sillen",
        address="De Jonkvrouw Geilstraat 14",
        zip_code="1234 AA",
        city="Raar",
        billing_information="VISA 1234567890"
    )
    # User 2
    benbouten = Users.create(
        name="Ben Boute",
        address="De Crackstraat 3 bis",
        zip_code="2345 BB",
        city="Rectum",
        billing_information="MasterCard 9876543210"
    )
    # User 3
    benniekoekoek = Users.create(
        name="Bennie Koekoek",
        address="Achter den Engelschen Pispot 5",
        zip_code="3456 CC",
        city="Sexbierum",
        billing_information="Paypal"
    )
    # User 4
    heidyheij = Users.create(
        name="Heidy Heij",
        address="Pisbulten 11",
        zip_code="4567 DD",
        city="Hongerige Wolf",
        billing_information="Ideal RABO"
    )
    # User 5
    wilbierman = Users.create(
        name="Wil Bierman",
        address="Sesamstraat 525",
        zip_code="5678 EE",
        city="Waspik",
        billing_information="Overschrijving Bitcoin"
    )

    # Products
    spijkerbroek = Products.create(
        owner=bassillen,
        name="Spijkerbroek",
        description="Broek gemaakt van spijkerstof, model: Baggy",
        price_per_unit=129.00,
        amount_in_stock=5,
    )
    hoodie = Products.create(
        owner=benbouten,
        name="Hoodie",
        description="Trui met capuchon, zakken aan voorzijde",
        price_per_unit=74.95,
        amount_in_stock=3,
    )
    chino = Products.create(
        owner=benniekoekoek,
        name="Chino",
        description="Een chino broek is een broek die zowel casual als zakelijk gedragen kan worden",
        price_per_unit=99.95,
        amount_in_stock=14,
    )
    vest = Products.create(
        owner=heidyheij,
        name="Vest",
        description="Heren vesten zijn perfecte en comfortabele kledingitems. Je draagt ze over een shirt om jezelf warm te worden. Maar andersom trek je een vest net zo snel weer uit. Handig voor ieder seizoen dus!",
        price_per_unit=74.95,
        amount_in_stock=3,
    )
    tshirt = Products.create(
        owner=wilbierman,
        name="Tshirt",
        description="Je hebt nooit genoeg T-shirts in je kledingkast. Je kunt T-shirts eindeloos combineren én ze zijn verkrijgbaar in veel verschillende printjes!",
        price_per_unit=29.95,
        amount_in_stock=28,
    )

    # Tags
    jeans = Tags.create(
        name="jeans"
    )
    katoen = Tags.create(
        name="katoen"
    )
    broek = Tags.create(
        name="broek"
    )
    sweater = Tags.create(
        name="sweater"
    )
    zakelijk = Tags.create(
        name="zakelijk"
    )
    wol = Tags.create(
        name="wol"
    )
    casual = Tags.create(
        name="casual"
    )
    prints = Tags.create(
        name="prints"
    )

    # ProductTags spijkerbroek:
    ProductTag.create(
        product=spijkerbroek,
        tag=jeans
    )
    ProductTag.create(
        product=spijkerbroek,
        tag=katoen
    )
    ProductTag.create(
        product=spijkerbroek,
        tag=broek
    )

    # Product tags hoodie:
    ProductTag.create(
        product=hoodie,
        tag=katoen
    )
    ProductTag.create(
        product=hoodie,
        tag=sweater
    )

    # Product tags chino:
    ProductTag.create(
        product=chino,
        tag=broek
    )
    ProductTag.create(
        product=chino,
        tag=zakelijk
    )

    # Product tags vest
    ProductTag.create(
        product=vest,
        tag=katoen
    )
    ProductTag.create(
        product=vest,
        tag=zakelijk
    )
    ProductTag.create(
        product=vest,
        tag=wol
    )

    # Product tags tshirt:
    ProductTag.create(
        product=tshirt,
        tag=katoen
    )
    ProductTag.create(
        product=tshirt,
        tag=casual
    )
    ProductTag.create(
        product=tshirt,
        tag=prints
    )
