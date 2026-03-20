# TCP-HTTP-IP-connections-using-python

A comprehensive collection of Python scripts demonstrating TCP/IP socket programming, HTTP communication, and web scraping techniques.

## Overview

This project includes various implementations of network communication using Python's socket library, HTTP requests, and web scraping with BeautifulSoup.

## File Structure

### Basic Socket Programming

#### `server.py`
Basic TCP server implementation that listens on localhost:1234 and sends a welcome message to each connected client.
- Listens for up to 5 concurrent clients
- Sends "Welcome to the server" message upon connection

#### `client.py`
Basic TCP client that connects to the server on localhost:1234 and receives the welcome message.
- Connects to server and displays the received message

### Echo Communication (Versions 1-3)

#### `echoserver.py` & `echoclient.py`
Simple echo server-client pair on port 1235.
- Client sends "hello!" message
- Server receives and echoes back the exact message

#### `echoserverv2.py` & `echoclientv2.py`
Enhanced echo implementation with message header handling for large messages (port 1236).
- Supports messages larger than buffer size (15 bytes)
- Uses 10-byte header to specify message length
- Handles fragmented message reception

#### `echoserverv3.py` & `echoclientv3.py`
Interactive echo implementation with exit command (port 1236).
- Interactive client prompts user for input
- Server continues until "exit" command is received
- Multi-message support within single connection
- Message header and fragmentation handling

### HTTP Communication via Raw Sockets

#### `get.py`
HTTP GET request implementation using raw TCP sockets (not using requests library).
- Connects to example.com on port 80
- Sends raw HTTP GET request
- Retrieves and displays response headers and content
- Includes tasks for enhancement (retrieve full content, test 404 responses, HTTP/2)

#### `post.py`
HTTP POST request implementation using raw TCP sockets.
- Sends POST request to example.com with Content-Length header
- Demonstrates proper HTTP POST formatting
- Includes notes on Content-Length header requirements

### HTTP Requests Library

#### `request.py`
Simple HTTP GET request using the requests library.
- Fetches content from https://uom.lk
- Displays status code, URL, and response text
- Can be modified to test other URLs (httpbin.org, Google, etc.)

### Web Scraping

#### `scrape.py`
BeautifulSoup HTML parsing basics.
- Demonstrates BeautifulSoup navigation of HTML structure
- Shows methods: finding titles, accessing attributes, finding all elements
- Uses example HTML about "The Dormouse's story"
- Educational example of parsing HTML trees

#### `scrape2.py`
Google search scraping implementation.
- Scrapes Google search results for "Sri Lanka"
- Extracts headings and links from search results
- Includes note about retrieving paginated results using GET parameters

### API Requests

#### `main2.py`
Vehicle API client implementation.
- Makes GET request to vehicleapi.com/vehicles
- Displays HTTP status code and JSON response
- Demonstrates API integration

## Dependencies

Install required packages using:
```bash
pip install -r requirements.txt
```

### requirements.txt Contents:
- `requests` - HTTP library for making web requests
- `beautifulsoup4` - HTML/XML parsing and web scraping library

## Usage Examples

### Running Echo Server-Client:
```bash
# Terminal 1 - Start server
python echoserver.py

# Terminal 2 - Run client
python client.py
```

### Enhanced Echo with Large Messages:
```bash
# Terminal 1
python echoserverv2.py

# Terminal 2
python echoclientv2.py
```

### Interactive Echo (v3):
```bash
# Terminal 1
python echoserverv3.py

# Terminal 2
python echoclientv3.py
# Then type messages and press Enter, type "exit" to quit
```

### HTTP Client Examples:
```bash
python get.py   # GET request via raw socket
python post.py  # POST request via raw socket
python request.py  # GET request using requests library
```

### Web Scraping:
```bash
python scrape.py   # BeautifulSoup parsing demo
python scrape2.py  # Google search scraping
```

## Key Concepts Demonstrated

1. **Socket Programming** - Low-level TCP/IP communication
2. **Server-Client Architecture** - Bidirectional communication patterns
3. **Message Fragmentation** - Handling messages larger than buffer size
4. **HTTP Protocol** - Raw HTTP request/response formatting
5. **Web Scraping** - HTML parsing and data extraction
6. **API Integration** - Making requests to web APIs
7. **Error Handling** - HTTP status codes and response codes

## Notes

- Most local server examples use localhost (127.0.0.1) for testing
- Buffer sizes vary: typically 1024 bytes for HTTP, 15 bytes for echo v2/v3
- HTTP examples connect to real websites which may require internet access
- Some scripts include commented-out tasks and enhancement suggestions