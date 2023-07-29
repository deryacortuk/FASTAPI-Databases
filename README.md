
# FastAPI Automatic Docs

FastAPI generates JSON schema definitions for our models and automatically documents 
our routes, including their request body type, path and query parameters, and response 
models. This documentation is of two types:
• Swagger    visit the http://127.0.0.1:8000/docs URL: 
• ReDoc  visit the http://127.0.0.1:8000/redoc URL


# Path parameters
Path parameters are parameters included in an API route to identify resources. These 
parameters serve as an identifier and, sometimes, a bridge to enable further operations in 
a web application.

FastAPI also provides a Path class that distinguishes path parameters from other 
arguments present in the route function. The Path class also helps give route parameters 
more context during the documentation automatically provided by OpenAPI via Swagger
and ReDoc and acts as a validator.
Path(..., kwargs)
The Path class takes a first positional argument set to None or ellipsis (...). 
If the first argument is set to an ellipsis (...), the path parameter becomes 
required. The Path class also contains arguments used for numerical 
validations if a path parameter is a number. Definitions include gt and le
– gt means greater than and le means less than. When used, the route will 
validate the path parameter against these arguments.

# Query parameters
A query parameter is an optional parameter that usually appears after a question mark in 
a URL. It is used to filter requests and return specific data based on the queries supplied.
In a route handler function, an argument that isn’t homonymous with the path parameter 
is a query. You can also define a query by creating an instance of the FastAPI Query()
class in the function argument, such as the following:
async query_route(query: str = Query(None):
 return query.
FastAPI also provides us with a Body() class to provide extra validation. 

# Response Models and Error Handling
Response models serve as templates for returning data from an API route path. They 
are built on Pydantic to properly render a response from requests sent to the server.
Error handling includes the practices and activities involved in handling errors 
from an application. These practices include returning adequate error status codes 
and error messages.

A response header consists of the request's status and additional information to guide the 
delivery of the response body. An example of the information contained in the response 
header is Content-Type, which tells the client the content type returned

The response body, on the other hand, is the data requested from the server by the client. 
The response body is determined from the Content-Type header variable and the most 
commonly used one is application/json. 

Status codes
Status codes are unique short codes issued by a server in response to a client’s request. 
Response status codes are grouped into five categories, each denoting a different response:
• 1XX: Request has been received.
• 2XX: The request was successful.
• 3XX: Request redirected.
• 4XX: There’s an error from the client.
• 5XX: There’s an error from the server.


Error handling
Errors from requests can result from attempting to access non-existent resources, 
protected pages without sufficient permissions, and even server errors. Errors in FastAPI 
are handled by raising an exception using FastAPI’s HTTPException class. 
An HTTP exception is an event that is used to indicate a fault or issue in the 
request flow.

The HTTPException class takes three arguments:
• status_code: The status code to be returned for this disruption
• detail: Accompanying message to be sent to the client
• headers: An optional parameter for responses requiring headers


Templating in 
FastAPI

Templating is the process of displaying the data gotten from the API in various formats. 
Templates act as a frontend component in web applications

Jinja is a templating engine written in Python designed to help the rendering process of 
API responses. In every templating language, there are variables that get replaced with the 
actual values passed to them when the template is rendered, and there are tags that control 
the logic of the template.
The Jinja templating engine makes use of curly brackets { } to distinguish its expressions 
and syntax from regular HTML, text and any other variable in the template file.
The {{ }} syntax is called a variable block. The {% %} syntax houses control structures 
such as if/else, loops, and macros.
The three common syntax blocks used in the Jinja templating language include 
the following:
• {% … %} – This syntax is used for statements such as control structures.
• {{ todo.item }} – This syntax is used to print out the values of the expressions 
passed to it.
• {# This is a great API book! #} – This syntax is used when writing 
comments and is not displayed on the web page.

Filters
Despite the similarity between Python and Jinja’s syntax, modifications such as joining 
strings, setting the first character of a string to uppercase, and so on cannot be done using 
Python’s syntax in Jinja. Therefore, to perform such modifications, we have filters in Jinja.
A filter is separated from the variable by a pipe symbol (|) and may entertain optional 
arguments in parentheses. A filter is defined in this format:
{{ variable | filter_name(*args) }}


If there are no arguments, the definition becomes the following:
{{ variable | filter_name }}
Let’s take a look at some common filters in the following subsections.
The default filter
The default filter variable is used to replace the output of the passed value if it turns out 
to be None:
{{ todo.item | default('This is a default todo item') }}
This is a default todo item
The escape filter
This filter is used to render raw HTML output:
{{ "<title>Todo Application</title>" | escape }}
<title>Todo Application</title>
The conversion filters
These filters include int and float filters used to convert from one data type to another:
{{ 3.142 | int }}
3
{{ 31 | float }}
31.0
The join filter
This filter is used to join elements in a list into a string as in Python:
{{ ['Packt', 'produces', 'great', 'books!'] | join(' ') }}
Packt produces great books!
The length filter
This filter is used to return the length of the object passed. It fulfills the same role as
len() in Python:
Todo count: {{ todos | length }}
Todo count: 4

Using if statements
The usage of if statements in Jinja is similar to their usage in Python. if statements are 
used in the {% %} control blocks. Let’s look at an example:
{% if todo | length < 5 %}
 You don't have much items on your todo list!
{% else %}
 You have a busy day it seems!
{% endif %}
Loops
We can also iterate through variables in Jinja. This could be a list or a general function, 
such as the following, for example:
{% for todo in todos %}
 <b> {{ todo.item }} </b>
{% endfor %}
You can access special variables inside a for loop, such as loop.index, which gives 
the index of the current iteration. The following is a list of the special variables and 
their descriptions:
Macros
A macro in Jinja is a function that return an HTML string. The main use case for 
macros is to avoid the repetition of code and instead use a single function call. For 
example, an input macro is defined to reduce the continuous definition of input tags 
in an HTML form:
{% macro input(name, value='', type='text', size=20 %}
 <div class="form">
 <input type="{{ type }}" name="{{ name }}" 
 value="{{ value|escape }}" size="{{ size }}">
 </div>
{% endmacro %}
Now, to quickly create an input in your form, the macro is called:
{{ input('item') }}
This will return the following:
<div class="form">
 <input type="text" name="item" value="" size="20">
</div>

we need to install the Jinja package and create a new folder, templates, 
in our project directory. This folder will store all our Jinja files, which are HTML files 
mixed with Jinja’s syntax. 
let’s install the Jinja package and create the templates folder:
$ pip install jinja2
Then, add to file 
from fastapi.templating import Jinja2Templates
templates = Jinja2Templates(directory="templates/")


Structuring FastAPI 
Applications

Structuring refers to the arrangement of application components in an organized format, 
which can be modular to improve the readability of the application’s code and content. 
An application with proper structuring enables faster development, faster debugging, 
and an overall increase in productivity.

What Is Depends?
The Depends class is responsible for exercising dependency injection in 
FastAPI applications. The Depends class takes a truth source such as 
a function as an argument and is passed as a function argument in a route, 
mandating that the dependency condition be satisfied before any operation can 
be executed. 

# Authentication methods in FastAPI
There are several authentication methods available in FastAPI. FastAPI supports the 
common authentication methods of basic HTTP authentication, cookies, and bearer 
token authentication. Let’s briefly look at what each method entails:
• Basic HTTP authentication: In this authentication method, the user credentials, 
which is usually a username and password, are sent via an Authorization HTTP 
header. The request in turn returns a WWW-Authenticate header containing 
a Basic value and an optional realm parameter, which indicates the resource the 
the authentication request is made to.
• Cookies: Cookies are employed when data is to be stored on the client side, such as 
in web browsers. FastAPI applications can also employ cookies to store user data, 
which can be retrieved by the server for authentication purposes.
• Bearer token authentication: This method of authentication involves the use of 
security tokens called bearer tokens. These tokens are sent alongside the Bearer
keyword in an Authorization header request. The most used token is JWT, 
which is usually a dictionary comprising the user ID and the token’s expiry time.

# Dependency injection
Dependency injection is a pattern where an object – 
In FastAPI, a dependency can be defined as either a function or a class. The dependency 
created gives us access to its underlying values or methods, eliminating the need to create 
these objects in the functions inheriting them. Dependency injection helps in reducing 
code repetition in some cases, such as in enforcing authentication and authorization. a function – receives an 
instance variable needed for the further execution of the function. 
In FastAPI, dependencies are injected by declaring them in the path operation function 
arguments. 

# What Is a JWT and Why Is It Signed?
A JWT is an encoded string usually containing a dictionary housing a payload, 
a signature, and its algorithm. JWTs are signed using a unique key known only 
to the server and client to avoid the encoded string being tampered with by an 
external body.

# CORS
Cross-Origin Resource Sharing (CORS) serves as a rule that prevents unregistered clients 
access to a resource.
When our web API is consumed by a frontend application, the browser will not allow 
cross-origin HTTP requests. This means that resources can only be accessed from the 
exact origin as the API or origins permitted by the API.
FastAPI provides a CORS middleware, CORSMiddleware, that allows us to register 
domains which can access our API. The middleware takes an array of origins which will 
be permitted to access the resources on the server. 

# What is a middleware?
A middleware is a function that acts as an intermediary between an 
operation. In web APIs, a middleware serves as an mediator in 
a request-response operation.


