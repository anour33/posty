class Post:
    def __init__(self, id, photo_url, name, body):
        self.id = id
        self.photo_url = photo_url
        self.name = name
        self.body = body

posts = []

class PostStore:
    def get_all(self):
        for post in posts :

            return posts

    def add(self, post):
        self.get_all()
        posts.append(post)

    def get_by_id(self, id):
        self.get_all()
        for post in posts:
           if id == post.id:
                return post
        else:
              return None





post_store = PostStore()
post1=Post(id=1 , photo_url="photo_url" , name="salim",body="body" )
post2=Post(id=2 , photo_url="photo_url" , name="sara",body="body" )
post3=Post(id=3 , photo_url="photo_url" , name="samir",body="body" )

post_store.add(post1)
post_store.add(post2)
post_store.add(post3)

mes_posts = post_store.get_all()
print(mes_posts)
mon_post=post_store.get_by_id(1)
print(mon_post)

