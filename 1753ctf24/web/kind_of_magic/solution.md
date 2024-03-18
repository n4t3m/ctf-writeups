We are given a website where we can upload an image and the size of it is reduced. We are also given the source code.

Looking at the function that handles user input:

```rs
#[post("/resize?<x>&<y>", data="<image>")]
fn resize(image: ImageData, x: Option<u16>, y: Option<u16>) -> Result<Vec<u8>, BadRequest<String>> {
    let max_size = 1024;
    let default_size = 32;
    let size_x = min(x.unwrap_or(default_size), max_size);
    let size_y = min(y.unwrap_or(default_size), max_size);
    let wand = MagickWand::new();
    let _ = wand.read_image_blob(&image.data);
    wand.resize_image(size_x.into(), size_y.into(), bindings::FilterType_LanczosFilter);
    match wand.write_image_blob("PNG") {
        Ok(vec) => Ok(vec),
        Err(_) => Err(BadRequest("couldn't convert provided image".into())) // might be our problem, but blame the user anyway
    }
}
```

We can see that `MagickWand` is used to resize the image.

Looking at the `Dockerfile` included in the source file, we see the following line:


```
RUN pacman --noconfirm -Syu && \
    pacman --noconfirm -S libpng libraqm liblqr libxext fontconfig lcms2 libltdl pkg-config clang rust && \
    curl https://archive.archlinux.org/packages/i/imagemagick/imagemagick-7.1.0.49-1-x86_64.pkg.tar.zst > imagemagick-7.1.0.49.tar.zst && \
    pacman --noconfirm -U imagemagick-7.1.0.49.tar.zst && \
    rm imagemagick-7.1.0.49.tar.zst
```

A quick google search shows that this version of imagemagick is vulnerable to `CVE-2022-44268`. It also indicates the flag is located at `/flag` on the server.

I found a [public exploit](https://github.com/kljunowsky/CVE-2022-44268), ran it against the server, and recieved the flag.'

Flag: `1753c{there_is_magic_in_the_air_its_called_CVE_2022_44268}`