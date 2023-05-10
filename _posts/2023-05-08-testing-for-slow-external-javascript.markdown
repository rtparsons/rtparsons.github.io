---
layout: post
title:  "Testing for slow external Javascript files"
date:   2023-05-08 20:00:00 +0000
categories: javascript web
---

I recently came across an issue where a web page would "hang". The page was loaded and everything visible, but all javascript functionality such as click handlers were un-responsive. That was until the page had finished loading a minute later and it all came back to life.

Identifying the culprit was easy, simply open up chrome developer tools, go to the network tab and look for the resource still loading. The culprit was an external Javascript call that was timing out. But in the short time it took me to fire up my development environment, the file was loading fine again.

### Replicating...

Chrome developer tools has a "throttle" feature which emulates slow internet connection, but this affects all web requests and I needed something more targeted. After a quick search I came across a Chrome plugin called [URL Throttler](https://chrome.google.com/webstore/detail/url-throttler/kpkeghonflnkockcnaegmphgdldfnden).

<img src="/assets/images/url-throttler.png" alt="URL Throttler screen grab" style="max-height:300px">

URL Throttler allows you to specify a set of url patterns with a delay, and then all requests to matching URL's will be delayed by that amount. Using this I could emulate not only a delay to the know affected resources, but check all of my sites other external dependencies too.

### The bug...

```javascript
window.addEventListener("load", (event) => {
    document.getElementById('myButton').addEventListener('click', (event) => {
        // click logic...
    });
});
```

The event handlers for all of the items on the page were bound from the Javascript, and all of these handlers weren't being setup until the window load event was fired. The [load event](https://developer.mozilla.org/en-US/docs/Web/API/Window/load_event) isn't fired until the page and all of its resources have finished loading.

Fixing in this case was simple, as the function call didn't depend on any of the external resources, it could be moved out of the window load event. Phew.