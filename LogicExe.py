# check if magician AND expert: "you are a masster magician"
#Check if magician but not expert: " at least you're getting there"
# if you're not a magician: "you need magic powers"

is_magician =False
is_expert = True 

if is_magician & is_expert:
    print('You are a master magician')
elif is_magician and not is_expert:
    print('at least you\'re getting there')
# else:
#     print('You need magic powers')
elif not is_magician:
    print('You need magic powers')
