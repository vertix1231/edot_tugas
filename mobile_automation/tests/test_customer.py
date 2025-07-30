# import pytest
# from test_data.customer_data import generate_customer_data

# # @pytest.mark.customer
# # class TestCustomer:
# #     def test_create_customer(self, customer_page):
# #         customer_data = customer_page.create_customer()
# #         assert customer_page.is_customer_created()
# #         assert customer_data["name"] in customer_page.get_success_message()
    
# #     def test_create_customer_special_chars(self, customer_page):
# #         customer_data = customer_page.create_customer(
# #             name="Customer $pecial@Name!",
# #             phone="+62-123-4567",
# #             address="Jl. Sudirman No. 123, Jakarta"
# #         )
# #         assert customer_page.is_customer_created()
# #         assert "Customer $pecial@Name!" in customer_page.get_success_message()
    
# #     def test_create_customer_missing_name(self, customer_page):
# #         customer_page.tap(customer_page.CREATE_BUTTON)
# #         customer_page.tap(customer_page.SAVE_BUTTON)
# #         assert "name is required" in customer_page.get_error_message().lower()