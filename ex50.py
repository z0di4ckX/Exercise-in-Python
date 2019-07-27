import webbrowser

urls = (
    '/', 'index'
)

app = webbrowser.application(urls, globals())

class index:
    def GET(self):
        greeting = "Hello word"
        return greeting

if __name__ == "__main__":
    app.run()