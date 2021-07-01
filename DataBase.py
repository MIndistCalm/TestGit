from models import *

def get_fields(table):
    ls = []
    posts = table.select()
    for i in str(posts).split():
        g = i.find('"t1"."')
        if g != -1:
            if i[-1] == ",":
                i = i[:-1]
            ls.append(i[6:-1])
    ls.pop(0)
    return ls

def add_fields(table, *argss):
    with db:
        name = table.__name__
        data = tuple(argss)
        fields = []
        for f in get_fields(table):
            fields.append(str(name) + "." + str(f))# тут ошибка надо сделать из строки 'Post.name_post' -> Post.name_post
        name.insert_many(data, fields).execute()



def run(*args):
    with db:
        add_fields(Post, "Менеджер", 1)
        posts = Post.select()
        for p in posts:
            print(p.post_name, p.number_of_people_in_the_current_position)
        print(posts)

        print(get_fields(Post))
