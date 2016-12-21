# CMPUT404LAB9_W2016
Django applications demonstrating Django Rest Framework and cross application authentication.
Iguana application will serve the rest API.
Leopard application will query the rest API with:
* No Authentication
* HTTP Basic Authentication
* HTTP Token Authentication

Iguana application also has OAuth and OAuth 2 support.

## Getting Started
1. Check out this repository locally to your machine
2. Create a python virtual environment, install the requirements
3. Navigate to the leopard application, migrate the django application.
4. Navigate to the iguana application, migrate the django application.
5. Within the iguana application, create a superuser.
6. Run the iguana application on the default settings (localhost, 8000).
7. Run the leopard application on a separate port (9000).
8. Use the leopard application to query the iguana application’s user api using the three basic authentication methods.

## LICENSE
The MIT License (MIT)

Copyright (c) 2016 Alexander Wong

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
