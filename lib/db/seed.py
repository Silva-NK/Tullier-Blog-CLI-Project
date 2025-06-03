from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from lib.db.connection import Engine, Session 
from lib.db.models import Base, User, Category, Post


session = Session()

# Drop all existing table first
Base.metadata.drop_all(Engine)

#Recreate all the tables as defined in models.py
Base.metadata.create_all(Engine)

categories = [
    "Psychologic Well-Being & Self-Awareness",
    "Trauma Healing & Recovery",
    "Faith & Mental Health",
    "Women's Empowerment & Healing",
    "Culture, Tradition & Choice",
    "Life Stories & Testimonials",
    "Youth Leadership & Mentorship",
    "Relationships & Emotional Well-Being"
]

for cat_name in categories:
    session.add(Category(name=cat_name))

session.commit()
print("Seeded permanent categories.")


user1 = User(name="June Smith")
user2 = User(name="James Smith")
user3 = User(name="Jane Doe")
user4 = User(name="John Doe")
user5 = User(name="Marcus Ficsher")
user6 = User(name="Rick Trout")
user7 = User(name="Hannah Kamen")

session.add_all([user1, user2, user3, user4, user5, user6, user7])
session.commit()
print("Seeded editable example users.")

cat1 = session.query(Category).filter_by(name="Psychologic Well-Being & Self-Awareness").first()
cat2 = session.query(Category).filter_by(name="Trauma Healing & Recovery").first()
cat3 = session.query(Category).filter_by(name="Faith & Mental Health").first()
cat4 = session.query(Category).filter_by(name="Women's Empowerment & Healing").first()
cat5 = session.query(Category).filter_by(name="Culture, Tradition & Choice").first()
cat6 = session.query(Category).filter_by(name="Life Stories & Testimonials").first()
cat7 = session.query(Category).filter_by(name="Youth Leadership & Mentorship").first()
cat8 = session.query(Category).filter_by(name="Relationships & Emotional Well-Being").first()

post1 = Post(
    title="Understanding Our Minds",
    content="Trauma leaves deep scars. But through compassion and support, healing is possible for anyone.",
    user_id=user3.id, category_id=cat1.id
)

post2 = Post(
    title="Healing from the Past",
    content="Self-awareness is the first step toward growth. We must understand our patterns and beliefs to change them.",
    user_id=user4.id, category_id=cat2.id
)

post3 = Post(
    title="Finding Faith in Dark Times",
    content="Faith can be a beacon when mental health feels shaky. Balancing spirituality and self-care is key.",
    user_id=user1.id, category_id=cat3.id
)

post4 = Post(
    title="Empowering Women Everywhere",
    content="Self-awareness is the first step toward growth. We must understand our patterns and beliefs to change them.",
    user_id=user5.id, category_id=cat4.id
)

post5 = Post(
    title="Tradition Meets Choice",
    content="Our culture shapes our lives, but we must also honour our personal choices.",
    user_id=user2.id, category_id=cat5.id
)

post6 = Post(
    title="A Story Worth Sharing",
    content="My life story is one of ups and downs, but I share it with the hope that others find strength too.",
    user_id=user7.id, category_id=cat6.id
)

post7 = Post(
    title="Youth Leadership Matters",
    content="Young people have the power to lead. Let's invest in their vision for a better world.",
    user_id=user6.id, category_id=cat7.id
)

post8 = Post(
    title="Love and Well-Being",
    content="Relationships are about trust and respect. Healthy connections can boost emotional well-being.",
    user_id=user4.id, category_id=cat8.id
)

session.add_all([post1, post2, post3, post4, post5, post6, post7, post8])
session.commit()
print("Seeded editable example posts.")