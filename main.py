from website import create_app

app = create_app()
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8080)
