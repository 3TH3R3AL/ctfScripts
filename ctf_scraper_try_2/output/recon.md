# Recon Report: ea1bbd87be43bc2df877415c773072ee.ctf.hacker101.com


## Notes


##Paths




### /

<details>
<summary>Headers</summary>
```html
Date
Content-Type
Content-Length
Connection
Server
```
</details>
<details>
<summary>Response</summary>
```html

<!doctype html>
<html>
	<head>
		<title>Micro-CMS</title>
	</head>
	<body>
		
		<ul>
<li><a href="page/1">Micro-CMS Changelog</a></li>
<li><a href="page/2">Markdown Test</a></li>
		</ul>
		<a href="page/create">Create a new page</a>
	</body>
</html>

```
</details>
<details>
<summary>Rendered</summary>


<!doctype html>
<html>
	<head>
		<title>Micro-CMS</title>
	</head>
	<body>
		
		<ul>
<li><a href="page/1">Micro-CMS Changelog</a></li>
<li><a href="page/2">Markdown Test</a></li>
		</ul>
		<a href="page/create">Create a new page</a>
	</body>
</html>

</details>

### /page/1

<details>
<summary>Headers</summary>
```html
Date
Content-Type
Content-Length
Connection
Server
```
</details>
<details>
<summary>Response</summary>
```html

<!doctype html>
<html>
	<head>
		<title>Micro-CMS Changelog</title>
	</head>
	<body>
		<a href="../">&lt;-- Go Home</a><br>
		<a href="edit/1">Edit this page</a>
		<h1>Micro-CMS Changelog</h1>
<h2>Version 2</h2>
<p>This version fixed the multitude of security flaws and general functionality bugs that plagued v1.  Additionally, we added user authentication; we're still not sure why we didn't think about that the first time, but hindsight is 20/20.  By default, users need to be an admin to add or edit pages now.</p>
	</body>
</html>

```
</details>
<details>
<summary>Rendered</summary>


<!doctype html>
<html>
	<head>
		<title>Micro-CMS Changelog</title>
	</head>
	<body>
		<a href="../">&lt;-- Go Home</a><br>
		<a href="edit/1">Edit this page</a>
		<h1>Micro-CMS Changelog</h1>
<h2>Version 2</h2>
<p>This version fixed the multitude of security flaws and general functionality bugs that plagued v1.  Additionally, we added user authentication; we're still not sure why we didn't think about that the first time, but hindsight is 20/20.  By default, users need to be an admin to add or edit pages now.</p>
	</body>
</html>

</details>

### /page/2

<details>
<summary>Headers</summary>
```html
Date
Content-Type
Content-Length
Connection
Server
```
</details>
<details>
<summary>Response</summary>
```html

<!doctype html>
<html>
	<head>
		<title>Markdown Test</title>
	</head>
	<body>
		<a href="../">&lt;-- Go Home</a><br>
		<a href="edit/2">Edit this page</a>
		<h1>Markdown Test</h1>
<p>Just testing some markdown functionality.</p>
<p><img alt="adorable kitten" src="https://static1.squarespace.com/static/54e8ba93e4b07c3f655b452e/t/56c2a04520c64707756f4267/1493764650017/" /></p>
<p><button>Some button</button></p>
	</body>
</html>

```
</details>
<details>
<summary>Rendered</summary>


<!doctype html>
<html>
	<head>
		<title>Markdown Test</title>
	</head>
	<body>
		<a href="../">&lt;-- Go Home</a><br>
		<a href="edit/2">Edit this page</a>
		<h1>Markdown Test</h1>
<p>Just testing some markdown functionality.</p>
<p><img alt="adorable kitten" src="https://static1.squarespace.com/static/54e8ba93e4b07c3f655b452e/t/56c2a04520c64707756f4267/1493764650017/" /></p>
<p><button>Some button</button></p>
	</body>
</html>

</details>

### /page/create

<details>
<summary>Headers</summary>
```html
Date
Content-Type
Content-Length
Connection
Server
Location
```
</details>
<details>
<summary>Response</summary>
```html
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<title>Redirecting...</title>
<h1>Redirecting...</h1>
<p>You should be redirected automatically to target URL: <a href="/login">/login</a>.  If not click the link.
```
</details>
<details>
<summary>Rendered</summary>

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<title>Redirecting...</title>
<h1>Redirecting...</h1>
<p>You should be redirected automatically to target URL: <a href="/login">/login</a>.  If not click the link.
</details>

### /login

<details>
<summary>Headers</summary>
```html
Date
Content-Type
Content-Length
Connection
Server
```
</details>
<details>
<summary>Response</summary>
```html

<!doctype html>
<html>
	<head>
		<title>Log in</title>
	</head>
	<body>
		<a href="home">&lt;-- Go Home</a>
		<h1>Log In</h1>
		<form method="POST">
			Username: <input type="text" name="username"><br>
			Password: <input type="password" name="password"><br>
			<input type="submit" value="Log In">
			<div style="color: red"></div>
		</form>
	</body>
</html>

```
</details>
<details>
<summary>Rendered</summary>


<!doctype html>
<html>
	<head>
		<title>Log in</title>
	</head>
	<body>
		<a href="home">&lt;-- Go Home</a>
		<h1>Log In</h1>
		<form method="POST">
			Username: <input type="text" name="username"><br>
			Password: <input type="password" name="password"><br>
			<input type="submit" value="Log In">
			<div style="color: red"></div>
		</form>
	</body>
</html>

</details>


## Flag
