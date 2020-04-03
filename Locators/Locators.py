class Locators():

    search_list = "s-results-list-atf"

    # Homepage Objects

    accLoginButton_id            = "nav-link-accountList"
    searchBar_id                 = "twotabsearchtextbox"
    searchButton_xpath           = "/html/body/div[1]/header/div/div[1]/div[3]/div/form/div[2]/div/input"
    listButton_xpath             = "/html/body/div[2]/header/div/div[1]/div[2]/div/a[2]/span[2]"
    wishList_xpath               = "/html/body/div[2]/header/div/div[1]/div[4]/div[2]/div[2]/div/div[1]/div[3]/div/a[2]/span"


    # LoginPage Objects

    emailTextbox_id              = "ap_email"
    continueButton_id            = "continue"
    passwordTextbox_id           = "ap_password"
    signInButton_id              = "signInSubmit"

    # Search Result Page Objects

    resultPage2_xpath            = "/html/body/div[1]/div[1]/div[1]/div[2]/div/span[8]/div/div/span/div/div/ul/li[3]/a"
    product_xpath                = "/html/body/div[1]/div[1]/div[1]/div[2]/div/span[4]/div[1]/div[3]/div/span/div/div/div[2]/div[2]/div/div[1]/div/div/div[1]/h2/a/span"
    page2button_xpath            = "/html/body/div[1]/div[1]/div[1]/div[2]/div/span[8]/div/div/span/div/div/ul/li[3]/a"
    noResultCheck_xpath          = "/html/body/div[1]/div[1]/div[1]/div[2]/div/span[3]/div/span/div/div/div[1]/span[1]"
    ## no result for "item"


    # ProductDetailPage Objects

    addToList_Button_id          = "add-to-wishlist-button-submit"
    closeButton_xpath            = "button.a-button-close:nth-child(2) > i:nth-child(1)"
    productTitle_id              = "productTitle"


    # WishListPage Objects

    #privateWishList_xpath        = "//*[@id='wl-list-title-2JFM8NJHBTVJA']"
    privateWishList_xpath        = "/html/body/div[1]/div[1]/div[2]/div/div[1]/div/div/div/div[1]/div/nav/ul/li[1]/span/div/div/a/div[1]"
    productOptionsButton_xpath   = "/html/body/div[1]/div[1]/div[2]/div/div[1]/div/div/div/div[2]/div[7]/div[3]/div/div[3]/ul/li[1]/span/div[3]/div/div[1]/span/div"
    deleteButton_xpath           = "/html/body/div[5]/div/div[1]/div/div[1]/ul/span[3]/li/span"

    ## Wishlist Delete İtems.

    product_title_id             = "productTitle"
    wishlist_product_xpath       = "/html/body/div[1]/div[1]/div[2]/div/div[1]/div/div/div/div[2]/div[7]/div[3]/div/div[3]/ul/li[1]/span/div[3]/div/a"
    wishlist_allprod             = "g-items-grid"
    wishlist_control             = "/html/body/div[1]/div[1]/div[2]/div/div[1]/div/div/div/div[2]/div[7]/div[4]/span/span"
    shopping_list                = "Shopping List"