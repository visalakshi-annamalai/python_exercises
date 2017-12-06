def avoids(str,forbidden):
    for i in forbidden:
        if i in str:
            return False
    else:
        return True
str="rnbw"
forbidden=['a','e','i','o','u']
print avoids(str,forbidden)

