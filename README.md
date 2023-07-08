# Writing a CRUD application for Django with different paradigm approaches.

This project contains reference examples for writing Django View with functional and OOP paradigms.

## API Endpoints

- GET, POST ```http://127.0.0.1:8000/apis/{version_number}/{plural-model-name}/```
- GET, PUT, DELETE ```http://127.0.0.1:8000/apis/{version_number}/{plural-model-name}/{lookup}/```

Example:
- GET, POST ```http://127.0.0.1:8000/apis/1.0/persons/```
- GET, PUT, DELETE ```http://127.0.0.1:8000/apis/1.0/persons/{lookup}/```

## URL Patterns
```
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("coreapp.urls")),
    path("f1/", include("f1.urls")),
    path("f2/", include("f2.urls")),
    path("f3/", include("f3.urls")),
    path("c1/", include("c1.urls")),
    path("c2/", include("c2.urls")),
    path("c3/", include("c3.urls")),
    path("apis/1.0/", include("apis1.urls")),
    path("apis/2.0/", include("apis2.urls")),
    path("apis/3.0/", include("apis3.urls")),
]
```
## Who need this project?

Anyone who want to learn different paradigm approach about writing view in Django.

### Dependencies

* The program runs on Django Web Framework so any web server which run Django is enough.
* A little passion. 

### Installing

* Install Django 
* Or just run ```$ pip install -r requirements.txt```

### Executing program

* This is a web application you just need web browser to use program.
* A large screen tablet will make things a lot easier.
```
code blocks for commands
```

## Help

If you have any question don't hesitate to ask.
```
command to run if program contains helper info
```

## Authors

Contributors names and contact info

ex. OHA TEAM  
ex. [@OHA]([https://twitter.com/dompizzie](https://github.com/oha-organization))

## Version History

* 0.2
    * This is beta version for now
    * See [commit change]() or See [release history]()
* 0.1
    * Initial Release

## License

This project is licensed under the [GNU] GNU General Public License - see the LICENSE.md file for details

## Acknowledgments

Inspiration, code snippets, etc.
* [awesome-readme](https://github.com/matiassingers/awesome-readme)
* [PurpleBooth](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2)
* [dbader](https://github.com/dbader/readme-template)
* [zenorocha](https://gist.github.com/zenorocha/4526327)
* [fvcproductions](https://gist.github.com/fvcproductions/1bfc2d4aecb01a834b46)