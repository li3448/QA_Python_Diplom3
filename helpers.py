def create_order(index_page):
    index_page.add_ingredient_to_order_by_index(1)
    index_page.add_ingredient_to_order_by_index(4)
    index_page.click_button_place_order()
    index_page.click_cross_button_in_popup_window()
