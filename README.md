# Python module `mdx_figures`

This is the extension `mdx_figures` for [Python-Markdown]
to make captioned figures out of images that are followed by a description.

In contrast to other extensions with that purpose, this one

  * does not introduce new syntax tokens,
  * does not change the block/inline category of the `![]` element
  * does not repurpose existing image attributes like `alt` or `title`,
  * allows use of Markdown in the caption,
  * is most natural to write, thus fitting the Markdown spirit very well.

Forked from [lehni] who forked from [helderco].
Added a cherry-pick from the fork by [gijsdeheij].

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
[helderco]: https://github.com/helderco/markdown-figures
[lehni]: https://github.com/lehni/markdown-figures
[gijsdeheij]: https://github.com/gijsdeheij/markdown-figures/commit/83318e69543ca3176de4b64ec2a5e2c6a91b73b8
