markdown-captions
=================

Extension for [Python-Markdown][] to parse images with captions inside a figure element.

## A simple example

    ![](http://lorempixel.com/350/150/)
    :   Lorem ipsum dolor sit amet, consectetur adipiscing elit.
        Praesent at consequat magna, faucibus ornare eros. Nam et
        mattis urna. Cras sodales, massa id gravida

Output:

```html
<figure>
    <img alt="" src="http://lorempixel.com/350/150/" />
    <figcaption>
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.
        Praesent at consequat magna, faucibus ornare eros. Nam et
        mattis urna. Cras sodales, massa id gravida</p>
    </figcaption>
</figure>
```

## How to Install

Clone and run

```shell
sudo python setup.py install
```

For mkdocs add this to your mkdocs.yml file:

```yaml
markdown_extensions:
    - mdx_figures
```