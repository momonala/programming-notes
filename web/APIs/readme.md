# Flask 

## APIs 

APIs are a way for a closed or source application (think Linux/Windows OS, or Gmail) to interact with another application. As a developer, you can build your own applications that interact with other applications, using their APIs, leveraging what they have already built for you. 

#### Web APIs

Web APIs allow one application to interact with many over the internet. For Web APIs, developers typically only interact with the Application layer in the [OSI model/protocol](https://en.wikipedia.org/wiki/OSI_model).

The most popular application level protocol is the HTTP protocol, or hypertext transfer protocol.  HTTP functions via a series of requests and responses between clients and servers. Other protocols include FTP, IMAP, POP and SSH. 

#### REST 

The Web Service Protocol is one that sits on top of the application  layer. It determines the formats in which APIs are recieved and sent. SOAP, or Simple Object Access Protocol, is one of the most popular. It uses XML to transfer data. SOAP was developed by Microsoft in 1998 and must use XML as the data format. It works with HTTP and other application layer protocols. 

REST, or Representational State Transfer is the up and coming replacement to SOAP. It functions as a set of guidelines for transmitting data. It uses HTTP verbs like GET, POST, PUT and DELETE to transfer data. It can use any type of message formatting (XML or JSON). REST is easier to implement that SOAP. 

#### Message Formatting 

When you have data to transfer, you have to format it. XML and JSON are the two most common types of formatting. XML is similar to HTML and is readable to humans and computers. XML was developed in 1997. 

JSON was developed in 2001 and developed after Javascript. It is more popular nowadays, especially for RESTful APIs. 

#### REST Constraints 

[link](https://www.youtube.com/watch?time_continue=136&v=IvHMM0huDZk)

There are 3 main constraints in REST: 

1. Data is trasmitted via a client/server setup. Clients sends requests, and servers repond with data. Servers can also function as clients, to send more requests downstream. 

2. REST is stateless. This means that a server never remembers data from a client, and each request is sent independently. The state of the client is not retained. This may seem silly, but this [helps applications become scalable](https://ruben.verborgh.org/blog/2012/08/24/rest-wheres-my-state/). If you are shopping for things on Amazon, in a RESTful setup, Amazon servers cannot remember the shopping cart of a user, and they might use tokens to achieve this "memory" instead. 

3. REST requests are explictly stated as cacheable or not cacheable. 

4. RESTful APIs must have the same interface for all devices accessing it. 

5. Layered Systems are ok. A client can interact with one server, and not need to know what other severs that first one interacts with. 

6. Code on Demand (optional) - code can be sent from the server to be executed on demand by the client. 

### HTTP 

#### Pull Protocol 

HTTP is characterized as a pull protocol. This means that actions consist of HTTP requests and responses, which are just text that can be interpreted as messages, images etc. 

#### HTTP Request 

An HTTP request consists of a header and optional body. The first line of the header is the HTTP verb, URI, and HTTP Version number. An example would be `GET /home.html HTTP/1.1`. The rest of the header consists of name-value pairs of data. The body consists of any additional data to be sent. 

#### HTTP Response 

The HTTP Response is similar to the Request. It consists of the header and optional body, and the header consists of the HTTP Version number, status code, andd reason phrase. This might look like "404 NOT FOUND". The Body contains the data that the client requested. 

#### HTTP Tools 

Curl and Postman are two tools for dissecting HTTP messages. Curl is command line based while Postman is GUI. Best is using httplib2 in Python for automation purposes. You will also need the json library to parse your results.  