tab_text = "Ejemplo Restuarante"
url = "https://www.wikipedia.org"
asset = "assets/img.png"
desc = "Esto es una descripcion"

__HEAD__ = f"""
<head>
  <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <!-- This is Edge's Fund. -->
    <base href="">
    <meta charset="utf-8" />
    <title>{tab_text}</title>
    <meta http-equiv="Accept-CH" content="Sec-CH-UA-Platform-Version, Sec-CH-UA-Model" /><link rel="icon" type="image/x-icon" href="assets/default-favicon.ico"/>
    <link rel="canonical" href="{url}"/>
    <meta property="og:site_name" content="{tab_text}"/>
    <meta property="og:title" content="{tab_text}"/>
    <meta property="og:url" content="{url}"/>
    <meta property="og:type" content="website"/>
<meta property="og:description" content="{desc}"/>
    <meta property="og:image" content="{asset}"/>
    <meta property="og:image:width" content="90"/>
    <meta property="og:image:height" content="50"/>
    <meta itemprop="name" content="{tab_text}"/>
    <meta itemprop="url" content="{url}"/>
    <meta itemprop="description" content="{desc}"/>
    <meta itemprop="thumbnailUrl" content="{asset}"/>
    <link rel="image_src" href="{asset}"/>
    <meta itemprop="image" content="{asset}"/>
    <meta name="twitter:title" content="{tab_text}"/>
    <meta name="twitter:image" content="{asset}"/>
    <meta name="twitter:url" content="{url}"/>
    <meta name="twitter:card" content="summary"/>
    <meta name="twitter:description" content="{desc}"/>
    <meta name="description" content="{desc}" />

</head>
"""

if __name__ == "__main__":
    fp = "coo.html"
    with open(fp, "w+") as fp:
        fp.write(__HEAD__)
