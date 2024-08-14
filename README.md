# EXAMPLE OF A NEW PROJECT ARCHITECTURE

## Architecture key points

### Layers

#### We define 4 separated layers:

1. Routers (Controllers) - responsible for validating client payload (if it's provided) and calling corresponding services.
2. Services - responsible for performing business logic, calling Repos for data management.
3. Repos - responsible for interacting with Data Sources, making queries to DB / API services.
4. Models - responsible to keep the data.


#### We define the way layers are going to interact:

- Interaction between layers strictly goes from top to bottom.
- Only neighbor layers can interact.
- Layers cannot interact with themselves (Services fall under the exception due to having reused logic).

<i>Right:</i><br/>
- <b>Routers</b> can call <b>Services</b>
- <b>Services</b> can call <b>Repos</b>
- <b>Repos</b> can call <b>Models</b>
- <b>Services</b> can call <b>Services</b>

<i>Wrong:</i><br/>
- <b>Repos</b> cannot call <b>Services</b>
- <b>Services</b> cannot call <b>Models</b>
- <b>Repos</b> cannot call <b>Repos</b>

![alt text](./docs/arc.png)

### Treat Ecommerce Platforms as Data Sources.

We perform the same types of operations (CRUD) by interacting with Ecommerce Platforms
as we do with our DataBase. So, lets provide Repos for them as well.

### Use Classes instead of functions
- func-based routers -> classed-based routers
- (?) func-based services -> class-based services
- crud operations -> repos

### Dependency Injection & Dependency Inversion

- Provide called code as a dependency instead of using it in place.

- Use interfaces for the dependencies instead of specific implementations. 

- Use specific implementation as a default value for the dependency
if only one implementation is actually going to be used.

### Define public API:

- use `_<name>` to not expose methods/funcs outside class/module.
- each module should have `__all__` at the top of itself exposing only what can be used out of it.
- each package should have `__all__` in its `__init__.py` exposing only what can be used out of it.
- use relative imports for the modules implemented within the same package.
- use absolute imports for the modules implemented outside current package.

## As the result we have:

### Separation into layers
  - Provides us with an easier way to walk through the project.

### Provided Repos for Ecommerce Platforms
  - Simplify further integrations with new platforms, by extending code and not modifying the existing one.

### Using classes than functions:
  - For routers, it becomes easier to follow REST.
  - For repos, it enables us to inherit base repos omitting code duplicating.
  - (?) For services, it makes us easier to provide type annotations for routers' dependencies. 

### Dependency Injection & Dependency Inversion 
  - Provides us with loose-coupled code parts, enabling to easily replace layers with smth different in the future
      (e.g.: move from FASTApi -> Falcon, from SQLAlchemy -> raw SQL queries, or smth else).
  - Provides us with an easier way to interact with different Ecommerce platforms by treating them as one universal thing. 
  - Provides us with an easier way to cover project with tests, since code in each layer can be tested separately provided with mocked dependencies.

### Defined public API:
  - Improves readability:
    - Shortens import statements
    - Explicitly displays what can be used outside
    - Improves IDE suggesting usage, as not listed in `__all__` units will not be
          suggested by IDE to import in.

  - Prevents cycled imports
    - Even though using `*` is a bad practice and should be avoided,
        we additionally omit internal units from importing as they are not listed in `__all__`
