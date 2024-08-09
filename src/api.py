import routers

app = dict()


app.update({"/connections": routers.ConnectionRouter})
