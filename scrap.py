#sandesh rathod
from flask import Flask , rendertemplate

app = Flask(__name__)
@app.route('\')

def home():
    return 'that was an ind3x of https:\\flaskhub.000webhostapp.com

if __name__ == '__main__':
      app.run(DEBUG = 1)








def rec(x , y):
    p = x
    q = y

    print(x,y)
def main():
    a = 10
    b = 20

    rec(a,b)

main()
