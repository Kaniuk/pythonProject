import pytest
from modules.common.database import Database


@pytest.mark.database
def test_database_connection():
    db = Database()
    db.test_connection()


@pytest.mark.database
def test_check_all_users():
    db = Database()
    users = db.get_all_users()

    print(users)


@pytest.mark.database
def test_check_user():
    db = Database()
    user = db.get_user_address_by_name("Sergii")

    assert user[0][0] == "Maydan Nezalezhnosti 1"
    assert user[0][1] == "Kyiv"
    assert user[0][2] == "3127"
    assert user[0][3] == "Ukraine"


@pytest.mark.database
def test_add_user():
    db = Database()
    db.insert_user("Anrriy", "Maydan Nezalezhnosti 2", "Lviv", 5555, "Ukraine")
    user = db.get_user_address_by_name("Anrriy")

    assert user[0][0] == "Maydan Nezalezhnosti 2"
    assert user[0][1] == "Lviv"
    assert user[0][2] == "5555"
    assert user[0][3] == "Ukraine"


@pytest.mark.database
def test_add_user_without_data():
    db = Database()
    with pytest.raises(ValueError, match="Name field cannot be empty"):
        db.insert_user("", "Maydan Nezalezhnosti 2", "Lviv", 5555, "Ukraine")

    with pytest.raises(ValueError, match="Address field cannot be empty"):
        db.insert_user("Anrriy", "", "Lviv", 5555, "Ukraine")

    with pytest.raises(ValueError, match="City field cannot be empty"):
        db.insert_user("Anrriy", "Maydan Nezalezhnosti 2", "", 5555, "Ukraine")

    with pytest.raises(ValueError, match="Postal code field cannot be empty"):
        db.insert_user("Anrriy", "Maydan Nezalezhnosti 2", "Lviv", "", "Ukraine")

    with pytest.raises(ValueError, match="Country field cannot be empty"):
        db.insert_user("Anrriy", "Maydan Nezalezhnosti 2", "Lviv", 5555, "")


@pytest.mark.database
def test_product_qnt_update():
    db = Database()
    db.update_product_qnt_by_id(1, 25)
    water_qnt = db.select_product_qnt_by_id(1)

    assert water_qnt[0][0] == 25


@pytest.mark.database
def test_product_qnt_updatet_without_data():
    db = Database()
    with pytest.raises(ValueError, match="Id field must be integer"):
        db.update_product_qnt_by_id("", 26)
    with pytest.raises(ValueError, match="Quantity field must be integer"):
        db.update_product_qnt_by_id(1, "")


@pytest.mark.database
def test_product_insert():
    db = Database()
    db.insert_product(4, "печиво", "солодке", 30)
    water_qnt = db.select_product_qnt_by_id(4)

    assert water_qnt[0][0] == 30


@pytest.mark.database
def test_invalid_name_and_description_lenght():
    db = Database()
    db.insert_product(5, "A" * 25, "solodke", 35)
    product = db.select_product_by_id(5)
    print(f" Продукт: {product}")

    assert len(product[0][1]) >= 3 and len(product[0][1]) <= 25
    assert len(product[0][2]) >= 3 and len(product[0][1]) <= 25


@pytest.mark.database
def test_add_product_with_invalid_description_type():
    db = Database()
    # It is possible to enter integer to name field
    # with pytest.raises(TypeError):
    #     db.insert_product(5, 12345, "солодке", 20)

    with pytest.raises(TypeError):
        db.insert_product(6, "печиво", 67890, 20)

    with pytest.raises(TypeError):
        db.insert_product(7, 12345, 67890, 20)


@pytest.mark.database
def test_add_product_with_invalid_product_id_or_qnt():
    db = Database()

    with pytest.raises(TypeError):
        db.insert_product("", "печиво", "солодке", 30)

    with pytest.raises(TypeError):
        db.insert_product(4, "печиво", "солодке", "pouy")


@pytest.mark.database
def test_product_delete():
    db = Database()
    db.insert_product(99, "testovi", "dani", 999)
    db.delete_product_by_id(99)
    qnt = db.select_product_qnt_by_id(99)

    assert len(qnt) == 0


@pytest.mark.database
def test_detailed_orders():
    db = Database()
    orders = db.get_detailed_orders()
    print("Zamowlenia", orders)

    assert len(orders) == 1

    assert orders[0][0] == 1
    assert orders[0][1] == "Sergii"
    assert orders[0][2] == "солодка вода"
    assert orders[0][3] == "з цукром"
