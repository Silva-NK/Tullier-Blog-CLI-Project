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
    try:
        id_ = int(input("Enter the category's ID: "))
    except:
        print("Invalid ID. Please enter an integer number.\n")
        return
    
    from lib.db.connection import Session
    from lib.db.models import Category

    session = Session()
    category = session.query(Category).filter_by(id=id_).first()
    if not category:
        print("\nNo category with that ID found.\n")
        return
    
    new_name = input("Enter category's new name: ").strip()
    if not new_name:
        print("Name cannot be an empty string.\n")
        return
    
    try:
        category.update_name(session, new_name)
        print(f"\nSuccess! Category updated to: <ID: {category.id} | Name: {category.name}>\n")

    except Exception as exc:
        session.rollback()
        print(f"\nError occurred while updating category: {exc}\n")

    finally:
        session.close()


def delete_category():
    try:
        id_ = int(input("Enter the category's ID: "))
    except:
        print("Invalid ID. Please enter an integer number.\n")
        return
    
    from lib.db.connection import Session
    from lib.db.models import Category

    session = Session()
    category = Category.find_by_id(id_)
    if not category:
        print("\nNo category with that ID found.\n")
        return
    
    confirm = input("Are you sure you want to delete this category? (yes/no): ").strip().lower()
    if confirm != 'yes':
        print("Category Deletion cancelled.\n")
        return
    
    try:
        category.delete(session)
        print(f"\nSuccess! Category deleted: <ID: {category.id} | Name: {category.name}>\n")
    
    except Exception as exc:
        session.rollback()
        print(f"\nError occurred while deleting category: {exc}\n")
    
    finally:
        session.close()


# Post Helper Functions

def list_posts():
    posts = Post.get_all()
    if posts:
        print("\n=== All Posts ===\n")
        for post in posts:
            print(f"Post ID: {post.id}\nTitle: {post.title}\nCategory ID: {post.category_id}\nUser ID: {post.user_id}\nContent: {post.content}\n{'-'*40}")
    else:
        print("\nNo posts found.")
    print("\n")


def find_post_by_title():
    title = input("Enter post's full or partial title: ")
    posts = Post.find_by_title(title)
    if posts:
        print("\n=== Partial or Fully Matching Categories ===\n")
        for post in posts:
            print(f"Post ID: {post.id}\nTitle: {post.title}\nCategory ID: {post.category_id}\nUser ID: {post.user_id}\nContent: {post.content}\n{'-'*40}")
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
        print(f"Post ID: {post.id}\nTitle: {post.title}\nCategory ID: {post.category_id}\nUser ID: {post.user_id}\nContent: {post.content}\n{'-'*40}")
    else:
        print("\nNo post with matching ID found.")
    print("\n")


def add_new_post():
    from lib.db.connection import Session
    from lib.db.models import Post

    title = input("Enter the post's title: ").strip()
    if not title:
        print("\nTitle cannot be an empty string\n")
        return
        
    content = input("Enter the post's content: ").strip()
    if not content:
        print("\nContent cannot be an empty string\n")
        return
        
    user_id_input = input("Enter post's user's ID: ")
    if not user_id_input:
        print("\nUser ID cannot be empty.\n")
        return
    try:
        user_id = int(user_id_input)
    except ValueError:
        print("\nUser ID must be an integer.\n")
        return
        
    category_id_input = input("Enter post's category's ID: ")
    if not category_id_input:
        print("\nCategory ID cannot be empty.\n")
        return
    try:
        category_id = int(category_id_input)
    except ValueError:
        print("\nCategory ID must be an integer.\n")
        return
        
    session = Session()
    try:
        post = Post.create(session, title, content, user_id, category_id)
        print(f"\nSuccess! New post added:\nPost ID: {post.id}\nTitle: {post.title}\nCategory ID: {post.category_id}\nUser ID: {post.user_id}\nContent: {post.content}\n{'-'*40}")
    except Exception as exc:
        session.rollback()
        print(f"\nError occurred while adding post: {exc}\n")
    finally:
        session.close()
        

def edit_post():
    from lib.db.connection import Session
    from lib.db.models import Post

    try:
        id_ = int(input("Enter the post's ID: "))
    except ValueError:
        print("Invalid ID. Please enter an integer.\n")
        return
    
    session = Session()
    try:
        post = session.query(Post).filter_by(id=id_).first()
        if not post:
            print("\nNo Post found with that ID.\n")
            return
        
        new_title = input("Enter post's new title: ").strip()
        if not new_title:
            print("\nTitle cannot be an empty string.\n")
            return

        new_content = input("Enter post's new content: ").strip()
        if not new_content:
            print("\nContent cannot be an empty string.\n")
            return

        new_user_id = input("Enter post's new user's ID: ").strip()
        if new_user_id:
            try:
                new_user_id = int(new_user_id)
            except ValueError:
                print("Invalid User ID. It must be an integer.\n")
                return
        else:
            new_user_id = None

        new_category_id = input("Enter post's new category's ID: ").strip()
        if new_category_id:
            try:
                new_category_id = int(new_category_id)
            except ValueError:
                print("Invalid Category ID. It must be an integer.\n")
                return
        else:
            new_category_id = None

        post.update_post(session, new_title, new_content, new_user_id, new_category_id)
        print(f"\nSuccess! Post edited:\nPost ID: {post.id}\nTitle: {post.title}\nCategory ID: {post.category_id}\nUser ID: {post.user_id}\nContent: {post.content}\n{'-'*40}")
    
    except Exception as exc:
        session.rollback()
        print(f"\nError occurred while editing post: {exc}\n")
    
    finally:
        session.close()


def delete_post():
    from lib.db.connection import Session
    from lib.db.models import Post

    try:
        id_ = int(input("Enter the post's ID: "))
    except ValueError:
        print("Invalid ID. Please enter an integer number.\n")
        return
    
    session = Session()
    try:
        post = Post.find_by_id(id_)
        if not post:
            print("\nNo post with matching ID found.\n")
            return
        
        confirm = input("Are you sure you want to delete this post? (yes/no): ").strip().lower()
        if confirm != 'yes':
            print("Post Deletion cancelled.\n")
            return
    
        post.delete(session)
        print(f"\nSuccess! Post deleted:\nPost ID: {post.id}\nTitle: {post.title}\nCategory ID: {post.category_id}\nUser ID: {post.user_id}\nContent: {post.content}\n{'-'*40}")
    
    except Exception as exc:
        session.rollback()
        print(f"\nError occurred while deleting post: {exc}\n")
    
    finally:
        session.close()


# Relationship based functions.

def list_posts_by_user():
    from lib.db.connection import Session
    from lib.db.models import User

    try:
        id_ = int(input("Enter user's ID: "))
    except:
        print("Invalid ID. Please enter an integer number.\n")
        return
    
    session = Session()
    try:
        user = session.query(User).filter_by(id=id_).first()
        if not user:
            print("\nNo user with matching ID found.\n")
            return
        
        posts = user.posts

        if not posts:
            print(f"User 'ID: {user.id} | Name: {user.name}' has no posts.")
            return
        
        user_posts = []

        for post in posts:
            user_posts.append((post.id, post.title, post.content, post.category.name))

        print(f"\nPosts by User '{user.name}' (ID: {user.id}):\n")
        for pid, title, content, category in user_posts:
            print(f"Post ID: {pid}\nTitle: {title}\nCategory: {category}\nContent: {content}\n{'-'*40}")

    finally:
        session.close()


def list_posts_by_category():
    from lib.db.connection import Session
    from lib.db.models import Category


    try:
        id_ = int(input("Enter category's ID: "))
    except:
        print("Invalid ID. Please enter an integer number.\n")
        return
    
    session = Session()
    try:
        category = session.query(Category).filter_by(id=id_).first()
        if not category:
            print("\nNo category with matching ID found.\n")
            return
        
        posts = category.posts

        if not posts:
            print(f"Category 'ID: {category.id} | Name: {category.name}' has no posts.\n{'-'*40}\n")
            return
        
        category_posts = []

        for post in posts:
            category_posts.append((post.id, post.title, post.content, post.category.name))

        print(f"\nPosts by Category '{category.name}' (ID: {category.id}):\n")
        for pid, title, content, category in category_posts:
            print(f"Post ID: {pid}\nTitle: {title}\nCategory: {category}\nContent: {content}\n{'-'*40}")

    finally:
        session.close()


def list_category_by_user():
    from lib.db.connection import Session
    from lib.db.models import User, Category

    try:
        id_ = int(input("Enter user's ID: "))
    except ValueError:
        print("Invalid ID. Please enter an integer number.\n")
        return
    
    session = Session()
    try:
        user = session.query(User).filter_by(id=id_).first()
        if not user:
            print("\nNo user with matching ID found.\n")
            return
        
        posts = user.posts
        if not posts:
            print(f"User '{user.name}' (ID: {user.id}) has not contributed to any category.\n{'-'*40}\n")
            return
        
        category_counts = {}
        for post in posts:
            category = post.category
            if category.id not in category_counts:
                category_counts[category.id] = {
                    'name': category.name,
                    'count': 1
                }
            else:
                category_counts[category.id]['count'] += 1

        print(f"\nUser '{user.name}' (ID: {user.id}) contributions by category:\n{'='*50}")
        for cat_id, data in category_counts.items():
            print(f"Category: <ID: {cat_id} | Name: {data['name']} | Posts: {data['count']}>")
        print()

    finally:
        session.close()
            
    
def list_users_by_category():
    from lib.db.connection import Session
    from lib.db.models import User, Category, Post

    try:
        id_ = int(input("Enter category's ID: "))
    except ValueError:
        print("Invalid ID. Please enter an integer number.\n")
        return
    
    session = Session()
    try:
        category = session.query(Category).filter_by(id=id_).first()
        if not category:
            print("\nNo category with matching ID found.\n")
            return
        
        posts = category.posts
        if not posts:
            print(f"\nCategory '{category.name}' (ID: {category.id}) has no contributors yet.\n{'-'*40}\n")
            return
        
        user_counts = {}
        for post in posts:
            user = post.user
            if user.id not in user_counts:
                user_counts[user.id] = {
                    'name': user.name,
                    'count': 1
                }
            else:
                user_counts[user.id]['count'] += 1
        
        print(f"\nCategory '{category.name}' (ID: {category.id}) contributors:\n{'='*50}")
        for user_id, data in user_counts.items():
            print(f"User: <ID: {user_id} | Name: {data['name']} | Posts: {data['count']}>")
        print()

    finally:
        session.close()