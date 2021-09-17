from models import *
all_posts = {}

# def get_fields(table):
#     ls = []
#     posts = table.select()
#     for i in str(posts).split():
#         g = i.find('"t1"."')
#         if g != -1:
#             if i[-1] == ",":
#                 i = i[:-1]
#             ls.append(i[6:-1])
#     ls.pop(0)
#     return ls
#
# def add_fields(table, *argss):
#     with db:
#         name = table.__name__
#         data = tuple(argss)
#         fields = []
#         for f in get_fields(table):
#             fields.append(str(name) + "." + str(f))#  тут ошибка надо сделать из строки 'Post.name_post' -> Post.name_post
#         name.insert_many(data, fields).execute()


def add_post(post_name, number_of_people):
    # if post_name not in all_posts:
    Post.update(number_of_people_in_the_current_position=3)
    print(all_posts[post_name])
    return all_posts[post_name]


def del_post(ident):
    post = Post.get(Post.id == ident)
    post.delete_instance()


def run():
    with db:
        # add_post("Менеджер", 2)
        del_post(13)
        # print(get_fields(Post))
        print(all_posts)
        posts = Post.select()
        for p in posts:
            print(p.post_name, p.number_of_people_in_the_current_position)
        print(posts)
        # db.drop_tables([Post], safe=True)
        # db.create_tables([Post], safe=True)