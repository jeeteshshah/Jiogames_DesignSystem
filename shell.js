/* JioGames DLS — shell.js
   Injects left sidebar nav + right page TOC.
   Place <script src="/shell.js"> at bottom of <body>.
*/
(function () {
  /* ── Left nav data ── */
  var NAV = [
    {
      group: 'Foundations',
      items: [
        { label: 'Overview',     path: '/'              },
        { label: 'Foundations',  path: '/foundations/'  },
        { label: 'Colours',      path: '/colours/'      },
        { label: 'Typography',   path: '/typography/'   },
        { label: 'Spacing',      path: '/spacing/'      },
        { label: 'Radius',       path: '/radius/'       },
        { label: 'Motion',       path: '/motion/'       },
        { label: 'Elevation',    path: '/elevation/'    },
      ]
    },
    {
      group: 'Core Systems',
      items: [
        { label: 'Buttons',       path: '/buttons/',       badge: 'deep' },
        { label: 'Icons',         path: '/icons/',         badge: 'deep' },
        { label: 'AppBar',        path: '/appbar/'                        },
        { label: 'TV Focus',      path: '/tv-focus/',      badge: 'deep' },
        { label: 'Accessibility', path: '/accessibility/', badge: 'deep' },
        { label: 'Templates',     path: '/templates/'                     },
        { label: 'Governance',    path: '/governance/'                    },
      ]
    },
    {
      group: 'Components',
      items: [
        { label: 'Cards',        path: '/cards/',        badge: 'deep' },
        { label: 'Inputs',       path: '/inputs/'    },
        { label: 'Search',       path: '/search/'    },
        { label: 'Chips',        path: '/chips/'     },
        { label: 'Rails',        path: '/rails/'     },
        { label: 'Genre Tiles',  path: '/genre-tiles/' },
        { label: 'Pass Cards',   path: '/pass-cards/'  },
        { label: 'Page Dots',    path: '/page-dots/'   },
        { label: 'Tab Bar',      path: '/tab-bar/'   },
        { label: 'Navigation',   path: '/navigation/'},
        { label: 'Bottom Sheet', path: '/bottom-sheet/' },
        { label: 'Drawer',       path: '/drawer/'    },
        { label: 'Dialogs',      path: '/dialogs/'   },
        { label: 'Toast',        path: '/toast/'     },
        { label: 'Banners',      path: '/banners/'   },
        { label: 'Lists',        path: '/lists/'     },
        { label: 'Toggle',       path: '/toggle/'    },
        { label: 'Badges',       path: '/badges/'    },
        { label: 'Forms',        path: '/forms/'     },
      ]
    },
    {
      group: 'Feedback',
      items: [
        { label: 'Avatar',        path: '/avatar/',        badge: 'draft' },
        { label: 'Skeleton',      path: '/skeleton/',      badge: 'draft' },
        { label: 'Progress Bar',  path: '/progress-bar/',  badge: 'draft' },
      ]
    },
    {
      group: 'Form Controls',
      items: [
        { label: 'Checkbox',   path: '/checkbox/',  badge: 'draft' },
        { label: 'Radio',      path: '/radio/',     badge: 'draft' },
        { label: 'Label',      path: '/label/',     badge: 'draft' },
        { label: 'Textarea',   path: '/textarea/',  badge: 'draft' },
        { label: 'Slider',     path: '/slider/',    badge: 'draft' },
        { label: 'Select',     path: '/select/',    badge: 'draft' },
        { label: 'Combobox',   path: '/combobox/',  badge: 'draft' },
      ]
    },
    {
      group: 'Navigation',
      items: [
        { label: 'Tabs',            path: '/tabs/',            badge: 'draft' },
        { label: 'Accordion',       path: '/accordion/',       badge: 'draft' },
        { label: 'Collapsible',     path: '/collapsible/',     badge: 'draft' },
        { label: 'Toggle Group',    path: '/toggle-group/',    badge: 'draft' },
        { label: 'Navigation Menu', path: '/navigation-menu/', badge: 'draft' },
      ]
    },
    {
      group: 'Overlays',
      items: [
        { label: 'Tooltip',       path: '/tooltip/',       badge: 'draft' },
        { label: 'Popover',       path: '/popover/',       badge: 'draft' },
        { label: 'Hover Card',    path: '/hover-card/',    badge: 'draft' },
        { label: 'Context Menu',  path: '/context-menu/',  badge: 'draft' },
        { label: 'Dropdown Menu', path: '/dropdown-menu/', badge: 'draft' },
      ]
    },
    {
      group: 'Data & Layout',
      items: [
        { label: 'Data Table',  path: '/data-table/',        badge: 'draft' },
        { label: 'Scroll Area', path: '/scroll-area/',       badge: 'draft' },
        { label: 'Carousel',    path: '/carousel-component/', badge: 'draft' },
        { label: 'Chart',       path: '/chart/',             badge: 'draft' },
        { label: 'Separator',   path: '/separator/',         badge: 'draft' },
        { label: 'Aspect Ratio',path: '/aspect-ratio/',      badge: 'draft' },
      ]
    },
    {
      group: 'Complex',
      items: [
        { label: 'Command',     path: '/command/',    badge: 'draft' },
        { label: 'Calendar',    path: '/calendar/',   badge: 'draft' },
        { label: 'Date Picker', path: '/date-picker/', badge: 'draft' },
        { label: 'Menubar',     path: '/menubar/',    badge: 'draft' },
        { label: 'Resizable',   path: '/resizable/',  badge: 'draft' },
      ]
    }
  ];

  var curPath = window.location.pathname;
  if (curPath.slice(-1) !== '/') curPath += '/';

  // Detect if running from file:// (standalone) vs http://
  var isFile = window.location.protocol === 'file:';

  // Known section names — used to detect depth for file:// mode
  var SECTIONS = ['foundations','colours','typography','spacing','radius','motion','elevation',
    'buttons','icons','appbar','tv-focus','accessibility','templates','governance',
    'cards','inputs','search','chips','rails','genre-tiles','pass-cards','page-dots',
    'tab-bar','navigation','bottom-sheet','drawer','dialogs','toast','banners',
    'lists','toggle','badges','forms',
    'avatar','skeleton','progress-bar',
    'checkbox','radio','label','textarea','slider','select','combobox',
    'tabs','accordion','collapsible','toggle-group','navigation-menu',
    'tooltip','popover','hover-card','context-menu','dropdown-menu',
    'data-table','scroll-area','carousel-component','chart','separator','aspect-ratio',
    'command','calendar','date-picker','menubar','resizable'];

  // Are we inside a subdirectory?
  var pathParts = curPath.replace(/\/index\.html\/?$/, '/').replace(/\/$/, '').split('/');
  var lastName = pathParts[pathParts.length - 1];
  var inSub = SECTIONS.indexOf(lastName) !== -1;
  var base = inSub ? '../' : '';

  // Convert an absolute DLS path like /buttons/ to the correct relative path
  function toHref(absPath) {
    if (!isFile) return absPath; // http:// — absolute paths work fine
    if (absPath === '/') return inSub ? '../index.html' : 'index.html';
    // Strip leading slash, e.g. /buttons/ → buttons/index.html
    var seg = absPath.replace(/^\//, '').replace(/\/$/, '');
    return base + seg + '/index.html';
  }

  function isActive(itemPath) {
    if (itemPath === '/') {
      if (isFile) return !inSub && (curPath.endsWith('/index.html/') || curPath.endsWith('jiogames-design-system//'));
      return curPath === '/';
    }
    var seg = itemPath.replace(/^\//, '').replace(/\/$/, '');
    return lastName === seg;
  }

  /* ── Build left sidebar ── */
  var sideHtml = '<div class="ds-shell-logo">' +
    '<a href="' + toHref('/') + '" class="ds-shell-logo-link">' +
    '<img src="' + base + 'logos/JioGames_ServiceLogo_Horizontal_White.svg" class="ds-shell-logo-img" alt="JioGames DLS">' +
    '</a>' +
    '<span class="ds-shell-logo-ver">v1.0</span>' +
    '</div>' +
    '<div class="ds-shell-search-wrap">' +
    '<input type="search" id="ds-nav-search" class="ds-shell-search" placeholder="Search components & icons…" autocomplete="off">' +
    '</div>' +
    '<div class="ds-shell-nav-wrap" id="ds-nav-wrap">';

  NAV.forEach(function (group) {
    sideHtml += '<div class="ds-shell-group" data-group="' + group.group.toLowerCase() + '"><span class="ds-shell-group-label">' + group.group + '</span>';
    group.items.forEach(function (item) {
      var active = isActive(item.path) ? ' active' : '';
      var badge = '';
      if (item.badge === 'draft') badge = '<span class="ds-shell-link-badge ds-shell-link-badge--draft">Draft</span>';
      sideHtml += '<a href="' + toHref(item.path) + '" class="ds-shell-link' + active + '" data-label="' + item.label.toLowerCase() + '">' + item.label + badge + '</a>';
    });
    sideHtml += '</div>';
  });
  sideHtml += '</div>';

  var shell = document.createElement('aside');
  shell.className = 'ds-shell';
  shell.innerHTML = sideHtml;
  document.body.insertBefore(shell, document.body.firstChild);
  document.body.classList.add('ds-shell-body');

  /* ── Scroll active nav item into view ── */
  var activeLink = shell.querySelector('.ds-shell-link.active');
  if (activeLink) {
    var navWrap = shell.querySelector('#ds-nav-wrap');
    if (navWrap) {
      /* Use requestAnimationFrame so the sidebar has rendered and has height */
      requestAnimationFrame(function () {
        var linkTop = activeLink.offsetTop;
        var navH = navWrap.clientHeight;
        navWrap.scrollTop = Math.max(0, linkTop - navH / 2 + activeLink.clientHeight / 2);
      });
    }
  }

  /* ── Build right TOC ── */
  var main = document.querySelector('main.ds-main, main.ds-content');
  if (main) {
    var headings = main.querySelectorAll('h1.ds-page-title, h1.component-page-title, h2.ds-section-title, h3.ds-subsection-title');
    if (headings.length > 1) {
      var tocEl = document.createElement('nav');
      tocEl.className = 'ds-toc';
      tocEl.setAttribute('aria-label', 'Page contents');

      var tocHtml = '<span class="ds-toc-label">On this page</span>';
      var idx = 0;
      headings.forEach(function (h) {
        if (h.tagName === 'H1') return; // skip page H1
        if (!h.id) {
          h.id = 'toc-' + idx++;
        }
        var isSub = h.tagName === 'H3';
        var cls = 'ds-toc-link' + (isSub ? ' ds-toc-link--sub' : '');
        tocHtml += '<a href="#' + h.id + '" class="' + cls + '">' + h.textContent.trim() + '</a>';
      });

      tocEl.innerHTML = tocHtml;
      document.body.appendChild(tocEl);

      /* scroll-spy */
      var links = tocEl.querySelectorAll('.ds-toc-link');
      var sectionIds = [];
      links.forEach(function (a) {
        var href = a.getAttribute('href');
        if (href && href.startsWith('#')) sectionIds.push(href.slice(1));
      });

      function onScroll() {
        var scrollY = window.scrollY + 100;
        var active = null;
        sectionIds.forEach(function (id) {
          var el = document.getElementById(id);
          if (el && el.getBoundingClientRect().top + window.scrollY <= scrollY) {
            active = id;
          }
        });
        links.forEach(function (a) {
          var href = a.getAttribute('href');
          a.classList.toggle('active', href === '#' + active);
        });
      }

      window.addEventListener('scroll', onScroll, { passive: true });
      onScroll();
    }
  }

  /* ── Sidebar search ── */
  var navSearch = document.getElementById('ds-nav-search');
  var navWrap = document.getElementById('ds-nav-wrap');

  // Icon results panel injected below search input
  var iconPanel = document.createElement('div');
  iconPanel.id = 'ds-icon-results';
  iconPanel.style.cssText = 'display:none;padding:8px 12px 4px;border-bottom:1px solid var(--border-subtle);';
  navWrap.parentNode.insertBefore(iconPanel, navWrap);

  function getIconNames() {
    // Pull from injected sprite symbols (works after sprite-loader runs)
    var syms = document.querySelectorAll('symbol[id^="ic_"]');
    if (syms.length) {
      var names = [];
      syms.forEach(function (s) { names.push(s.id); });
      return names;
    }
    return [];
  }

  function renderIconPanel(q) {
    if (!q) { iconPanel.style.display = 'none'; return; }
    var names = getIconNames();
    var matches = names.filter(function (id) {
      return id.toLowerCase().indexOf(q) !== -1;
    }).slice(0, 8);

    iconPanel.innerHTML = '';

    if (matches.length) {
      var label = document.createElement('div');
      label.style.cssText = 'font-size:10px;font-weight:700;color:var(--text3);letter-spacing:.4px;text-transform:uppercase;margin-bottom:8px;';
      label.textContent = 'Icons';
      iconPanel.appendChild(label);

      var grid = document.createElement('div');
      grid.style.cssText = 'display:grid;grid-template-columns:repeat(4,1fr);gap:4px;margin-bottom:6px;';

      matches.forEach(function (id) {
        var cell = document.createElement('a');
        cell.href = toHref('/icons/') + '?q=' + encodeURIComponent(q) + '#gallery';
        cell.title = id.replace(/^ic_/, '').replace(/_/g, ' ');
        cell.style.cssText = 'display:flex;flex-direction:column;align-items:center;gap:4px;padding:8px 4px;border-radius:var(--r3);background:rgba(255,255,255,.04);border:1px solid var(--border-subtle);cursor:pointer;text-decoration:none;transition:background 120ms,border-color 120ms;';
        cell.innerHTML = '<svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor" style="color:var(--text2);flex-shrink:0"><use href="#' + id + '"></use></svg>' +
          '<span style="font-size:8px;color:var(--text3);text-align:center;word-break:break-all;line-height:1.2;overflow:hidden;max-height:2.6em;">' +
          id.replace(/^ic_/, '').replace(/_/g, ' ') + '</span>';
        cell.addEventListener('mouseenter', function () {
          cell.style.background = 'rgba(0,168,89,.1)';
          cell.style.borderColor = 'rgba(0,168,89,.3)';
        });
        cell.addEventListener('mouseleave', function () {
          cell.style.background = 'rgba(255,255,255,.04)';
          cell.style.borderColor = 'var(--border-subtle)';
        });
        grid.appendChild(cell);
      });
      iconPanel.appendChild(grid);
    }

    // "See all" link
    var seeAll = document.createElement('a');
    seeAll.href = toHref('/icons/') + '?q=' + encodeURIComponent(q) + '#gallery';
    seeAll.style.cssText = 'display:block;font-size:11px;font-weight:600;color:var(--jio);text-decoration:none;padding:4px 0 8px;';
    seeAll.textContent = matches.length ? 'See all results in Icons →' : 'Search "' + q + '" in Icons →';
    iconPanel.appendChild(seeAll);

    iconPanel.style.display = '';
  }

  if (navSearch && navWrap) {
    navSearch.addEventListener('input', function () {
      var q = navSearch.value.trim().toLowerCase();
      var groups = navWrap.querySelectorAll('.ds-shell-group');
      groups.forEach(function (grp) {
        var links = grp.querySelectorAll('.ds-shell-link');
        var anyVisible = false;
        links.forEach(function (a) {
          var label = a.getAttribute('data-label') || '';
          var show = !q || label.indexOf(q) !== -1;
          a.style.display = show ? '' : 'none';
          if (show) anyVisible = true;
        });
        grp.style.display = anyVisible ? '' : 'none';
      });

      renderIconPanel(q);

      if (!q) {
        groups.forEach(function (grp) {
          grp.style.display = '';
          grp.querySelectorAll('.ds-shell-link').forEach(function (a) { a.style.display = ''; });
        });
      }
    });
    navSearch.addEventListener('keydown', function (e) {
      if (e.key === 'Escape') { navSearch.value = ''; navSearch.dispatchEvent(new Event('input')); }
    });
  }

  /* ── Mobile menu toggle ── */
  var toggle = document.createElement('button');
  toggle.className = 'ds-menu-toggle';
  toggle.setAttribute('aria-label', 'Open navigation');
  toggle.innerHTML = '☰';
  document.body.appendChild(toggle);

  var overlay = document.createElement('div');
  overlay.className = 'ds-overlay';
  document.body.appendChild(overlay);

  toggle.addEventListener('click', function () {
    shell.classList.toggle('open');
    overlay.classList.toggle('visible');
  });
  overlay.addEventListener('click', function () {
    shell.classList.remove('open');
    overlay.classList.remove('visible');
  });

  /* ── Keyboard shortcuts: G then letter ── */
  var shortcutPaths = {
    b: '/buttons/', c: '/colours/', t: '/typography/',
    s: '/spacing/', i: '/icons/',   g: '/governance/',
    a: '/accessibility/', v: '/tv-focus/', r: '/radius/',
    m: '/motion/', e: '/elevation/', k: '/cards/',
    f: '/foundations/', p: '/appbar/', n: '/navigation/',
    l: '/lists/', d: '/dialogs/', w: '/search/',
  };
  var gPressed = false;
  document.addEventListener('keydown', function (e) {
    if (e.target.tagName === 'INPUT' || e.target.tagName === 'TEXTAREA') return;
    if (e.key === 'g' && !e.metaKey && !e.ctrlKey) { gPressed = true; return; }
    if (gPressed) {
      gPressed = false;
      var dest = shortcutPaths[e.key.toLowerCase()];
      if (dest) window.location.href = toHref(dest);
    }
  });
})();
