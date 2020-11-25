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

    def update(self, id, fields):
        post =self.get_by_id(id)
        post.name = fields['name']
        post.photo_url = fields['photo_url']
        post.body = fields['body']

        return post


    def delete(self, id):
        post=self.get_by_id(id)
        posts.remove(post)
        return post










post_store = PostStore()
post1=Post(id=1 , photo_url="photo_url" , name="SALIM",body="hello you all" )
post2=Post(id=2 , photo_url="photo_url" , name="SARA",body="hey you" )
post3=Post(id=3 , photo_url="photo_url" , name="SAMIR",body="hola" )

post_store.add(post1)
post_store.add(post2)
post_store.add(post3)

mes_posts = post_store.get_all()
print(mes_posts)

mon_post=post_store.get_by_id(3)
print(mon_post.id , mon_post.name ,":" ,  mon_post.body)


updated_fields = {'name' :'wissem', 'photo_url': 'photo_url2' , 'body':"i'm an other person"}
newPost=post_store.update(3, updated_fields)
print(newPost.id , newPost.name , ":" , newPost.body)

to_remove=post_store.delete(2)
print(posts)
print("deleet post id=",to_remove.id ,'\n', to_remove.name , "who said <<", to_remove.body , ">>")

