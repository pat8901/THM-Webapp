from website import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True) # will automaticallly rerun server after a change is made. Turn off when code goes into production