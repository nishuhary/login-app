from website import create_app
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
