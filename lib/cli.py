from lib.helpers import (
    exit_program,
    list_users,
    find_user_by_name,
    find_user_by_id,
    add_new_user,
    edit_user,
    delete_user,
    list_categories,
    find_category_by_name,
    find_category_by_id,
    add_new_category,
    edit_category,
    delete_category,
    list_posts,
    find_post_by_title,
    find_post_by_id,
    add_new_post,
    edit_post,
    delete_post,
    list_posts_by_user,
    list_posts_by_category,
    list_category_by_user,
    list_users_by_category
)

def c(text, color_code):
    return f"\033[{color_code}m{text}\033[0m"

def main_menu():
    while True:
        print("\n" + "*"*50)
        print(c("📝  Welcome to the Tullier Blog Manager CLI!  📝", "36"))  # Cyan
        print("*"*50 + "\n")
        print(c("Main Menu:", "33"))
        print(c("1. User Management", "32"))
        print(c("2. Category Management", "32"))
        print(c("3. Post Management", "32"))
        print(c("4. Relational Queries", "32"))  # Added new submenu
        print(c("0. Exit\n", "32"))

        choice = input(c("Key in option: ", "36"))
        if choice == "0":
            exit_program()
        elif choice == "1":
            user_management()
        elif choice == "2":
            category_management()
        elif choice == "3":
            post_management()
        elif choice == "4":
            relational_queries()  # New submenu
        else:
            print(c("Invalid choice", "31"))

def user_management():
    while True:
        print("\n" + c("🔹 User Management Options:", "33"))
        print(c("1. List all users", "32"))
        print(c("2. Find user by name", "32"))
        print(c("3. Find user by id", "32"))
        print(c("4. Add new user", "32"))
        print(c("5. Edit existing user", "32"))
        print(c("6. Delete existing user", "32"))
        print(c("0. Back to Main Menu\n", "32"))
        print(c("*. Exit Program\n", "32"))

        choice = input(c("Key in option: ", "36"))
        if choice == "0":
            break
        elif choice == "*":
            exit_program()
        elif choice == "1":
            list_users()
        elif choice == "2":
            find_user_by_name()
        elif choice == "3":
            find_user_by_id()
        elif choice == "4":
            add_new_user()
        elif choice == "5":
            edit_user()
        elif choice == "6":
            delete_user()
        else:
            print(c("Invalid choice", "31"))


def category_management():
    while True:
        print("\n" + c("🔹 Category Management Options:", "33"))
        print(c("1. List all categories", "32"))
        print(c("2. Find category by name", "32"))
        print(c("3. Find category by id", "32"))
        print(c("4. Add new category", "32"))
        print(c("5. Edit existing category", "32"))
        print(c("6. Delete existing category", "32"))
        print(c("0. Back to Main Menu\n", "32"))
        print(c("*. Exit Program\n", "32"))

        choice = input(c("Key in option: ", "36"))
        if choice == "0":
            break
        elif choice == "*":
            exit_program()
        elif choice == "1":
            list_categories()
        elif choice == "2":
            find_category_by_name()
        elif choice == "3":
            find_category_by_id()
        elif choice == "4":
            add_new_category()
        elif choice == "5":
            edit_category()
        elif choice == "6":
            delete_category()
        else:
            print(c("Invalid choice", "31"))

def post_management():
    while True:
        print("\n" + c("🔹 Post Management Options:", "33"))
        print(c("1. List all posts", "32"))
        print(c("2. Find post by title", "32"))
        print(c("3. Find post by id", "32"))
        print(c("4. Add new post", "32"))
        print(c("5. Edit existing post", "32"))
        print(c("6. Delete existing post", "32"))
        print(c("0. Back to Main Menu\n", "32"))
        print(c("*. Exit Program\n", "32"))

        choice = input(c("Key in option: ", "36"))
        if choice == "0":
            break
        elif choice == "*":
            exit_program()
        elif choice == "1":
            list_posts()
        elif choice == "2":
            find_post_by_title()
        elif choice == "3":
            find_post_by_id()
        elif choice == "4":
            add_new_post()
        elif choice == "5":
            edit_post()
        elif choice == "6":
            delete_post()
        else:
            print(c("Invalid choice", "31"))

def relational_queries():
    while True:
        print("\n" + c("🔹 Relational Queries:", "33"))
        print(c("1. List posts by user", "32"))
        print(c("2. List posts by category", "32"))
        print(c("3. List category contributions by user", "32"))
        print(c("4. List user's contributors by category", "32"))
        print(c("*. Exit Program\n", "32"))

        choice = input(c("Key in option: ", "36"))
        if choice == "0":
            break
        elif choice == "*":
            exit_program()
        elif choice == "1":
            list_posts_by_user()
        elif choice == "2":
            list_posts_by_category()
        elif choice == "3":
            list_category_by_user()
        elif choice == "4":
            list_users_by_category()
        else:
            print(c("Invalid choice", "31"))

if __name__ == "__main__":
    main_menu()
