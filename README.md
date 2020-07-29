# Python module `mdx_figures`

This is the extension `mdx_figures` for [Python-Markdown]
to make captioned figures out of images that are followed by a description.

In contrast to other extensions with that purpose, this one

  * does not introduce new syntax tokens,
  * does not change the block/inline category of the image,
  * does not repurpose existing image attributes like `alt` or `title`,
  * allows use of Markdown in the caption,
  * is most natural to write, thus fitting the Markdown spirit very well.

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

For `mkdocs` add this to your `mkdocs.yml` file:

```yaml
markdown_extensions:
    - mdx_figures
```

[Python-Markdown]: https://pypi.org/project/Markdown/

