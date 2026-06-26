/* JioGames DLS — sprite-loader.js
   Injects sprite.svg inline so <use href="#ic_name"> works in file:// and server mode.
   Loads from window.__JIO_SPRITE__ (set by sprite-data.js) when available,
   falls back to XHR for server context.
*/
(function () {
  var loaderScript = (function () {
    var scripts = document.querySelectorAll('script[src*="sprite-loader"]');
    return scripts.length ? scripts[scripts.length - 1] : null;
  })();

  var base = loaderScript ? loaderScript.getAttribute('src').replace('sprite-loader.js', '') : '../';
  var spritePath = base + 'sprite.svg';
  var dataPath = base + 'sprite-data.js';

  function inject(svgText) {
    var div = document.createElement('div');
    div.style.cssText = 'position:absolute;width:0;height:0;overflow:hidden;';
    div.setAttribute('aria-hidden', 'true');
    div.innerHTML = svgText;
    document.body.insertBefore(div, document.body.firstChild);
    document.querySelectorAll('use[href*="sprite.svg#"]').forEach(function (u) {
      var id = u.getAttribute('href').split('#')[1];
      u.setAttribute('href', '#' + id);
    });
  }

  function tryXHR(async) {
    try {
      var xhr = new XMLHttpRequest();
      xhr.open('GET', spritePath, async);
      if (async) {
        xhr.onload = function () { if (xhr.responseText) inject(xhr.responseText); };
        xhr.send();
      } else {
        xhr.send();
        if (xhr.status === 200 && xhr.responseText) inject(xhr.responseText);
      }
    } catch (e) {
      if (!async) tryXHR(true);
    }
  }

  // 1. Already loaded by sprite-data.js (file:// safe)
  if (window.__JIO_SPRITE__) {
    inject(window.__JIO_SPRITE__);
    return;
  }

  // 2. On a server — XHR works fine
  if (window.location.protocol !== 'file:') {
    tryXHR(false);
    return;
  }

  // 3. file:// without sprite-data.js — inject script tag to load it, then inject
  var s = document.createElement('script');
  s.src = dataPath;
  s.onload = function () {
    if (window.__JIO_SPRITE__) inject(window.__JIO_SPRITE__);
  };
  document.head.appendChild(s);
})();
