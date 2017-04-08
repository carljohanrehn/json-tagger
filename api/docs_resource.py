import falcon
from falcon.util.uri import parse_host
from string import Template

doc_template = Template(open("api/views/index.html", "r").read())

class DocsResource(object):
    def on_get(self, request, response):
        response.content_type = "text/html"
        response.body = doc_template.substitute(
            site="%s://%s" % (request.protocol, request.headers["HOST"])
        )