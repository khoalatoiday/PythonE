  # path("",home.get_home),
#     path("admin/books/", product.get_products),
#   path("books", product.get_products_for_users),
#     path("bookForm",product.getAddBookForm),
#     path("add",product.addBook),
#     path("bookForm/<int:id>/",product.getEditBookForm),
#     path("edit/<int:id>/",product.editBook),
#     path("delete/<int:id>/",product.deleteBook),
#     path("login", authen.getLoginForm),
#     path("register", authen.getRegisterForm),
#     path("activeRegister",authen.register),
#     path("activeLogin",authen.loginAction),
#     path("logout",authen.logout_view),
#     path("changePassword",authen.getChangePassWordForm),
#     path("changePasswordAction", authen.change_password),
#     path("userinfo",customer.getCustomerInfo),
#     path("changeUserInfo", customer.changeCustomerInfo), 
#    path("error", home.get_error)

<!--Card image-->
        <div class="view view-cascade overlay text-center">
          <img
            class="card-img-top"
            src="/home/media/{{book.image}}"
            alt=""
            height="200px"
            width="200px"
          />
          <a>
            <div class="mask rgba-white-slight"></div>
          </a>
        </div>

          