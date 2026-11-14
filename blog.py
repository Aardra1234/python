blog_views = [150, 800, 2500, 600, 1200, 450, 3000]
total = 0
count = 0
for x in blog_views:
    if x > 1000:
        print("Trending") 
        count+=1
    elif 500 <= x <= 1000:
        print("Average")
    elif x < 500: 
        print("Low Traffic")
    total+=x
print("the total number of views: ",total)
print("how many posts were Trending: ",count)