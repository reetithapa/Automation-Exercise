from driver_setup import setup_driver
from login_page import login
from inventory_page import list_product, open_each_product_and_add_to_cart
from cart_page import go_to_cart, get_cart_products
from bug_report import BugReport
from test_context import TestContext

def test_saucedemo_end_to_end():
    driver = setup_driver()
    report = BugReport()
    context = TestContext()
    context.test_case_id = "TC_E2E_001"

    try:
        login(driver, context)

        inventory_products = list_product(driver, context)
        added_products = open_each_product_and_add_to_cart(driver, context)

        go_to_cart(driver, context)
        cart_products = get_cart_products(driver, context)

        context.expected = "All added products should be visible in cart"

        if set(added_products) == set(cart_products):
            context.actual = "Cart products match added products"
            report.add_result(driver, context)
        else:
            context.actual = "Cart products mismatch"
            report.add_result(driver, context, "cart_bug.png")

    except Exception as e:
        context.actual = str(e)
        report.add_result(driver, context, "exception.png")

    finally:
        report.save()
        driver.quit()
        print("Test executed & bug report generated")

if __name__ == "__main__":
    test_saucedemo_end_to_end()
