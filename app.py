import microservice

if __name__ == '__main__':
    microservice.app.run(debug=True, host='0.0.0.0')

app = microservice.app
