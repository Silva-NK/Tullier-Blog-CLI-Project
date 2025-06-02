from lib.db.models import User, Category, Post

def exit_program():
    print("Goodbye!")
    exit()
    
    
def list_users():
    users = User.get_all()
    if users:
        print("\n=== All Users ===")
        for user in users:
            print(f"<ID: {user.id} | Name: {user.name}>")
    else:
        print("\nNo users found.")


def find_user_by_name():
    print(2)


def find_user_by_id():
    print(3)


def add_new_user():
    print(4)


def edit_user():
    print(5)


def delete_user():
    print(6)


def list_categories():
    categories = Category.get_all()
    if categories:
        print("\n=== All Categories ===")
        for category in categories:
            print(f"<ID: {category.id} | Name: {category.name}>")
    else:
        print("\nNo categories found.")


def find_category_by_name():
    print(8)


def find_category_by_id():
    print(9)


def list_posts():
    posts = Post.get_all()
    if posts:
        print("\n=== All Posts ===")
        for post in posts:
            print(f"<ID: {post.id} | Category_id: {post.category_id} | By User_id: {post.user_id} | Title: {post.title}>")
    else:
        print("\nNo posts found.")


def find_post_by_title():
    print(11)


def find_post_by_id():
    print(12)


def add_new_post():
    print(13)


def edit_post():
    print(14)


def delete_post():
    print(15)


def list_posts_by_user():
    print(16)


def list_posts_by_category():
    print(17)


def list_category_by_user():
    print(18)

    
def list_users_by_category():
    print(19)