from selenium.webdriver.common.by import By


class IndexPageLocators:
    BUTTON_PLACE_ORDER = By.XPATH, "//button[text()='Оформить заказ']"

    LIST_OF_INGREDIENTS = By.XPATH, "//a[contains(@class, 'BurgerIngredient_ingredient')]"
    LIST_COUNTERS_OF_INGREDIENTS = By.XPATH, "//*[contains(@class, 'counter_counter__num')]"
    SECTION_CONSTRUCTOR_BASKET = By.XPATH, "//section[contains(@class, 'BurgerConstructor_basket')]"

    BUTTON_CROSS_IN_POPUP_WINDOW = By.XPATH, "//*[contains(@class, 'Modal_modal_opened')]//button"
    MODAL_POPUP_WINDOW = By.XPATH, "//*[contains(@class, 'Modal_modal_opened')]"

    ORDER_NUMBER_IN_POPUP_WINDOW = By.XPATH, "//h2[contains(@class,'title_shadow')]"

    TEXT_NAME_INGREDIENT_IN_DETAILS_WINDOW = By.XPATH, "//*[contains(@class, 'Modal_modal_opened')]/div/div/p"
    TEXT_ORDER_START_TO_PREPARE = By.XPATH, "//*[contains(@class, 'Modal_modal__text')]/p[1]"
