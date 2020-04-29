#import created app from src
from src import app,db
#init database
db.create_all()
#run application
app.run()

