from helpers import (
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

def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
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
        elif choice == "7":
            list_categories()
        elif choice == "8":
            find_category_by_name()
        elif choice == "9":
            find_category_by_id()
        elif choice == "10":
            list_posts()
        elif choice == "11":
            find_post_by_title()
        elif choice == "12":
            find_post_by_id()
        elif choice == "13":
            add_new_post()
        elif choice == "14":
            edit_post()
        elif choice == "15":
            delete_post()
        elif choice == "16":
            list_posts_by_user()
        elif choice == "17":
            list_posts_by_category()
        elif choice == "18":
            list_category_by_user()
        elif choice == "19":
            list_users_by_category()
        else:
            print("Invalid choice")
        

def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. List all users")
    print("2. Find user by name")
    print("3. Find user by id")
    print("4: Add new user")
    print("5: Edit existing user")
    print("6: Delete exisitng user")
    print("7. List all categories")
    print("8. Find category by name")
    print("9. Find category by id")
    print("10. List all posts")
    print("11. Find post by name")
    print("12. Find post by id")
    print("13: Add new post")
    print("14: Edit existing post")
    print("15: Delete exisitng post")
    print("16. List posts by user")
    print("17. List posts by category")
    print("18. List category contributions by user")
    print("19: List user's contributors by category")


if __name__ == "__main__":
    main()