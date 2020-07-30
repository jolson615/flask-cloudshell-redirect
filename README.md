# Google Cloud Shell Proxy Testing

This miniature Flask app includes four links which show the differences we've encountered between the Cloud Shell .dev and .com environments.

## Quick setup

To run in Cloud Shell:
```
pip3 install flask
pip3 install python-dotenv
```

Then:
```
flask run
```

## Four Tests

We tested four different versions of a redirect trying to trigger the regex in a .dev environment. Only the third one worked, which entailed hardcoding the host and port, so that method of course means the redirect works in the .dev test environment but fails in deployment. 

* Test 1 uses `redirect("/success")`
* Test 2 uses `redirect(url_for("success"))`
* Test 4 forcefully adds the host, but omits the port: `redirect(f"http://0.0.0.0{url_for('success')}")`
* Test 3 forcefully adds the host and port into the redirect location: `redirect(f"http://0.0.0.0:5000{url_for('success')}")`

## Debugging route

Since Test 2 is the recommended method, we've added a "/location" route, which uses the same redirect as Test 2, but returns just the location header string instead of the 302 response itself. It demonstrates that the response header includes a relative filepath. 

If you print out the entire body of the 302 response generated, you'll see this:

```
[b'<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">\n<title>Redirecting...</title>\n<h1>Redirec
ting...</h1>\n<p>You should be redirected automatically to target URL: <a href="/success">/success</a>
.  If not click the link.']
```