from lib.db.models import User, Category, Post

def exit_program():
    print("Goodbye!")
    exit()


# User Helper Functions
    
def list_users():
    users = User.get_all()
    if users:
        print("\n=== All Users ===\n")
        for user in users:
            print(f"<ID: {user.id} | Name: {user.name}>")
    else:
        print("\nNo users found.")
    print("\n")


def find_user_by_name():
    name = input("Enter user's full or partial name: ")
    users = User.find_by_name(name)
    if users:
        print("\n=== Partial or Fully Matching Users ===\n")
        for user in users:
            print(f"<ID: {user.id} | Name: {user.name}>")
    else:
        print("\nNo users found matching that full or partial name.")
    print("\n")


def find_user_by_id():
    try:
        id_ = int(input("Enter the user's ID: "))
    except:
        print("Invalid ID. Please enter a integer number.\n")
        return
    
    user = User.find_by_id(id_)
    if user:
        print("\nSuccess! User found.\n")
        print(f"<ID: {user.id} | Name: {user.name}>")
    else:
        print("\nNo user with matching ID found.")
    print("\n")


def add_new_user():
    name = input("Enter the new user's name: ").strip()
    if not name:
        print("Name cannot be an empty string.\n")
        return
    
    if not all(char.isalpha() or char.isspace() for char in name):
        print("Name must contain only letters and spaces.\n")
        return
    
    from lib.db.connection import Session
    from lib.db.models import User

    session = Session()
    try:
        user = User.create(session, name)
        print(f"\nSuccess! New user added: <ID: {user.id} | Name: {user.name}>\n")
    except Exception as exc:
        session.rollback()
        print(f"\nError occurred while adding user: {exc}\n")
    finally:
        session.close()


def edit_user():
    from lib.db.connection import Session
    from lib.db.models import User

    try:
        id_ = int(input("Enter the user's ID: "))
    except ValueError:
        print("Invalid ID. Please enter an integer number.\n")
        return
    
    session = Session()
    try:
        user = session.query(User).filter_by(id=id_).first()
        if not user:
            print("\nNo user with matching ID found.\n")
            return
        
        new_name = input("Enter user's new name: ").strip()
        if not new_name:
            print("Name cannot be an empty string.\n")
            return
        
        if not all(char.isalpha() or char.isspace() for char in new_name):
            print("Name must contain only letters and spaces.\n")
            return
        
        user.update_name(session, new_name)
        print(f"\nSuccess! User edited: <ID: {user.id} | New Name: {user.name}>\n")

    except Exception as exc:
        session.rollback()
        print(f"\nError occurred while editing user: {exc}\n")

    finally:
        session.close()


def delete_user():
    from lib.db.connection import Session
    from lib.db.models import User

    try:
        id_ = int(input("Enter the user's ID: "))
    except ValueError:
        print("Invalid ID. Please enter an integer number.\n")
        return
    
    session = Session()
    try:
        user = User.find_by_id(id_)
        if not user:
            print("\nNo user with matching ID found.\n")
            return
        
        confirm = input("Are you sure you want to delete this user? (yes/no): ").strip().lower()
        if confirm != 'yes':
            print("User Deletion cancelled.\n")
            return
        
        user.delete(session)
        print(f"\nSuccess! User deleted: <ID: {user.id} | Name: {user.name}>\n")

    except Exception as exc:
        session.rollback()
        print(f"\nError occurred while deleting user: {exc}\n")

    finally:
        session.close()


# Category Helper Functions

def list_categories():
    categories = Category.get_all()
    if categories:
        print("\n=== All Categories ===\n")
        for category in categories:
            print(f"<ID: {category.id} | Name: {category.name}>")
    else:
        print("\nNo categories found.")
    print("\n")


def find_category_by_name():
    name = input("Enter category's full or partial name: ")
    categories = Category.find_by_name(name)
    if categories:
        print("\n=== Partial or Fully Matching Categories ===\n")
        for category in categories:
            print(f"<ID: {category.id} | Name: {category.name}>")
    else:
        print("\nNo categories found matching that full or partial name.")
    print("\n")


def find_category_by_id():
    try:
        id_ = int(input("Enter the category's ID: "))
    except:
        print("Invalid ID. Please enter a integer number.\n")
        return
    
    category = Category.find_by_id(id_)
    if category:
        print("\nSuccess! Category found.\n")
        print(f"<ID: {category.id} | Name: {category.name}>")
    else:
        print("\nNo category with matching ID found.")
    print("\n")
    

def add_new_category():
    name = input("Enter the new category's name: ").strip()
    if not name:
        print("Name cannot be an empty string.\n")
        return
    
    from lib.db.connection import Session
    from lib.db.models import Category

    session = Session()
    try:
        category = Category.create(session, name)
        print(f"\nSuccess! New category added added: <ID: {category.id} | Name: {category.name}>\n")
    except Exception as exc:
        session.rollback()
        print(f"\nError occurred while adding category: {exc}\n")
    finally:
        session.close()


def edit_category():
    print(7)


def delete_category():
    print(10)


# Post Helper Functions

def list_posts():
    posts = Post.get_all()
    if posts:
        print("\n=== All Posts ===\n")
        for post in posts:
            print(f"<ID: {post.id} | Category_id: {post.category_id} | By User_id: {post.user_id} | Title: {post.title}>")
    else:
        print("\nNo posts found.")
    print("\n")


def find_post_by_title():
    title = input("Enter post's full or partial title: ")
    posts = Post.find_by_title(title)
    if posts:
        print("\n=== Partial or Fully Matching Categories ===\n")
        for post in posts:
            print(f"<ID: {post.id} | Category_id: {post.category_id} | By User_id: {post.user_id} | Title: {post.title}>")
    else:
        print("\nNo posts found matching that full or partial title.")
    print("\n")


def find_post_by_id():
    try:
        id_ = int(input("Enter the post's ID: "))
    except:
        print("Invalid ID. Please enter a integer number.\n")
        return
    
    post = Post.find_by_id(id_)
    if post:
        print("\nSuccess! Post found.\n")
        print(f"<ID: {post.id} | Category_id: {post.category_id} | By User_id: {post.user_id} | Title: {post.title}>")
        print(f"< {post.content} >")
    else:
        print("\nNo post with matching ID found.")
    print("\n")


def add_new_post():
    name = input("Enter the new user's name: ").strip()
    if not name:
        print("Name cannot be an empty string.\n")
        return
    
    if not all(char.isalpha() or char.isspace() for char in name):
        print("Name must contain only letters and spaces.\n")
        return
    
    from lib.db.connection import Session
    from lib.db.models import Post

    session = Session()
    try:
        user = User.create(session, name)
        print(f"\nSuccess! New user added: <ID: {user.id} | Name: {user.name}>\n")
    except Exception as exc:
        session.rollback()
        print(f"\nError occurred while adding user: {exc}\n")
    finally:
        session.close()


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