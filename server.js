const http = require('http');
const fs = require('fs');
const server = http.createServer();
//виклик під час запиту на  серверhttp://localhost:8080/xmld
server.on('request', async (request, response) => {
  const baseURL =  request.protocol + '://' + request.headers.host + '/';
  const reqUrl = new URL(request.url,baseURL);
  console.log(reqUrl);
  switch (reqUrl.pathname) {
    case '/xml':
      const xml = fs.readFileSync('./break.xml');
      response.writeHead(200, {"Content-Type": "application/xml"});
      response.end(xml);
      break
    case '/html':
      const html = fs.readFileSync('./html.html');
      response.writeHead(200, {"Content-Type": "text/html"});
      response.end(html);
      break
    default:
      response.writeHead(404, {"Content-Type": "text/plain"});
      response.end("Not Found, wrong path\n");
      break;
  }
});

server.listen(8080, () => {
  console.log('Started listening on 8080');
});