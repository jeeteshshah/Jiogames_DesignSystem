/* JioGames DLS — shell.js
   Injects left sidebar nav + right page TOC.
   Place <script src="/shell.js"> at bottom of <body>.
*/
(function () {
  if (window.self !== window.top) return; // Skip injection when running inside iframe shell

  /* ── Left nav data ── */
  /* status: 'stable' = no badge  |  'beta' = amber badge  |  'draft' = grey badge */
  var NAV = [
    {
      group: 'Getting Started',
      items: [
        { label: 'Getting Started', path: '/getting-started/', status: 'beta' },
        { label: 'Tooling',         path: '/tooling/',         status: 'beta' },
        { label: 'Token Reference', path: '/token-reference/', status: 'beta' },
      ]
    },
    {
      group: 'Foundations',
      items: [
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
        { label: 'Buttons',       path: '/buttons/'                                },
        { label: 'Icons',         path: '/icons/'                                  },
        { label: 'Navigation + AppBar', path: '/navigation/',      status: 'beta'  },
        { label: 'TV Focus',      path: '/tv-focus/',      status: 'beta'          },
        { label: 'Accessibility', path: '/accessibility/'                          },
        { label: 'Templates',     path: '/templates/',     status: 'beta'          },
        { label: 'Governance',    path: '/governance/'                             },
      ]
    },
    {
      group: 'Components',
      items: [
        { label: 'Cards',        path: '/cards/'                          },
        { label: 'Inputs',       path: '/inputs/',       status: 'beta'   },
        { label: 'Search',       path: '/search/',       status: 'beta'   },
        { label: 'Chips',        path: '/chips/',        status: 'beta'   },
        { label: 'Rails',        path: '/rails/',        status: 'beta'   },
        { label: 'Genre Tiles',  path: '/genre-tiles/',  status: 'beta'   },
        { label: 'Pass Cards',   path: '/pass-cards/',   status: 'beta'   },
        { label: 'Page Dots',    path: '/page-dots/',    status: 'beta'   },
        { label: 'Tab Bar',      path: '/tab-bar/',      status: 'beta'   },
        { label: 'Navigation',   path: '/navigation/',   status: 'beta'   },
        { label: 'Bottom Sheet', path: '/bottom-sheet/', status: 'beta'   },
        { label: 'Drawer',       path: '/drawer/',       status: 'draft'  },
        { label: 'Dialogs',      path: '/dialogs/',      status: 'beta'   },
        { label: 'Toast',        path: '/toast/',        status: 'beta'   },
        { label: 'Banners',      path: '/banners/',      status: 'beta'   },
        { label: 'Lists',        path: '/lists/',        status: 'beta'   },
        { label: 'Toggle',       path: '/toggle/',       status: 'beta'   },
        { label: 'Badges',       path: '/badges/',       status: 'beta'   },
        { label: 'Forms',        path: '/forms/',        status: 'beta'   },
        { label: 'Avatar',       path: '/avatar/',       status: 'beta'   },
        { label: 'Skeleton',     path: '/skeleton/',     status: 'beta'   },
        { label: 'Progress Bar', path: '/progress-bar/', status: 'beta'   },
      ]
    },
    {
      group: 'Form Controls',
      items: [
        { label: 'Checkbox',   path: '/checkbox/',  status: 'draft' },
        { label: 'Radio',      path: '/radio/',     status: 'draft' },
        { label: 'Label',      path: '/label/',     status: 'draft' },
        { label: 'Textarea',   path: '/textarea/',  status: 'draft' },
        { label: 'Slider',     path: '/slider/',    status: 'draft' },
        { label: 'Select',     path: '/select/',    status: 'draft' },
        { label: 'Combobox',   path: '/combobox/',  status: 'draft' },
      ]
    },
    {
      group: 'Navigation',
      items: [
        { label: 'Tabs',            path: '/tabs/',            status: 'draft' },
        { label: 'Accordion',       path: '/accordion/',       status: 'draft' },
        { label: 'Collapsible',     path: '/collapsible/',     status: 'draft' },
        { label: 'Toggle Group',    path: '/toggle-group/',    status: 'draft' },
        { label: 'Navigation Menu', path: '/navigation-menu/', status: 'draft' },
      ]
    },
    {
      group: 'Overlays',
      items: [
        { label: 'Tooltip',       path: '/tooltip/',       status: 'draft' },
        { label: 'Popover',       path: '/popover/',       status: 'draft' },
        { label: 'Hover Card',    path: '/hover-card/',    status: 'draft' },
        { label: 'Context Menu',  path: '/context-menu/',  status: 'draft' },
        { label: 'Dropdown Menu', path: '/dropdown-menu/', status: 'draft' },
        { label: 'Command',       path: '/command/',       status: 'draft' },
      ]
    },
    {
      group: 'Data & Layout',
      items: [
        { label: 'Data Table',  path: '/data-table/',         status: 'draft' },
        { label: 'Scroll Area', path: '/scroll-area/',        status: 'draft' },
        { label: 'Carousel',    path: '/carousel-component/', status: 'draft' },
        { label: 'Chart',       path: '/chart/',              status: 'draft' },
        { label: 'Separator',   path: '/separator/',          status: 'draft' },
        { label: 'Aspect Ratio',path: '/aspect-ratio/',       status: 'draft' },
        { label: 'Resizable',   path: '/resizable/',          status: 'draft' },
      ]
    },
    {
      group: 'Patterns',
      items: [
        { label: 'All Patterns',         path: '/patterns/',                    status: 'beta' },
        { label: 'Payment & Checkout',   path: '/patterns/checkout/',           status: 'beta' },
        { label: 'Onboarding',           path: '/patterns/onboarding/',         status: 'beta' },
        { label: 'Game Launch',          path: '/patterns/game-launch/',        status: 'beta' },
        { label: 'Empty Search',         path: '/patterns/empty-search/',       status: 'beta' },
        { label: 'Pull to Refresh',      path: '/patterns/pull-to-refresh/',    status: 'beta' },
        { label: 'Infinite Scroll',      path: '/patterns/load-more/',          status: 'beta' },
        { label: 'Notification Center',  path: '/patterns/notification-center/', status: 'beta' },
        { label: 'Share & Invite',       path: '/patterns/share/',              status: 'beta' },
      ]
    },
    {
      group: 'Complex',
      items: [
        { label: 'Calendar',    path: '/calendar/',    status: 'draft' },
        { label: 'Date Picker', path: '/date-picker/', status: 'draft' },
        { label: 'Menubar',     path: '/menubar/',     status: 'draft' },
      ]
    }
  ];

  var curPath = window.location.pathname;
  if (curPath.slice(-1) !== '/') curPath += '/';

  // Detect if running from file:// (standalone) vs http://
  var isFile = window.location.protocol === 'file:';

  // Known section names — used to detect depth for file:// mode
  var SECTIONS = ['overview',
    'foundations','colours','typography','spacing','radius','motion','elevation',
    'buttons','icons','appbar','tv-focus','accessibility','templates','governance',
    'cards','inputs','search','chips','rails','genre-tiles','pass-cards','page-dots',
    'tab-bar','navigation','bottom-sheet','drawer','dialogs','toast','banners',
    'lists','toggle','badges','forms','avatar','skeleton','progress-bar',
    'checkbox','radio','label','textarea','slider','select','combobox',
    'tabs','accordion','collapsible','toggle-group','navigation-menu',
    'tooltip','popover','hover-card','context-menu','dropdown-menu','command',
    'data-table','scroll-area','carousel-component','chart','separator','aspect-ratio','resizable',
    'calendar','date-picker','menubar',
    'getting-started','tooling','token-reference',
    'patterns','checkout','onboarding','game-launch','empty-search',
    'pull-to-refresh','load-more','notification-center','share'];

  // Are we inside a subdirectory?
  var pathParts = curPath.replace(/\/index\.html\/?$/, '/').replace(/\/$/, '').split('/');
  var lastName = pathParts[pathParts.length - 1];
  var parentName = pathParts[pathParts.length - 2] || '';
  var inSub = SECTIONS.indexOf(lastName) !== -1;
  // Deep sub = patterns/checkout/ etc — parent segment is also a known section
  var inDeepSub = inSub && SECTIONS.indexOf(parentName) !== -1;
  var base = inDeepSub ? '../../' : (inSub ? '../' : '');

  // Convert an absolute DLS path like /buttons/ to a relative path.
  // Always use relative paths so the site works at any base URL (localhost, GitHub Pages, etc.)
  function toHref(absPath) {
    if (absPath === '/') return inDeepSub ? (isFile ? '../../index.html' : '../../') : inSub ? (isFile ? '../index.html' : '../') : (isFile ? 'index.html' : './');
    var seg = absPath.replace(/^\//, '').replace(/\/$/, '');
    return base + seg + (isFile ? '/index.html' : '/');
  }

  function isActive(itemPath) {
    if (itemPath === '/') {
      if (isFile) return !inSub && (curPath.endsWith('/index.html/') || curPath.endsWith('jiogames-design-system//'));
      // On HTTP, home = not inside any known section
      return !inSub;
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

  var overviewActive = isActive('/') ? ' active' : '';
  sideHtml += '<a href="' + toHref('/') + '" class="ds-shell-link' + overviewActive + '" data-label="overview">Overview</a>';

  NAV.forEach(function (group) {
    sideHtml += '<div class="ds-shell-group" data-group="' + group.group.toLowerCase() + '"><span class="ds-shell-group-label">' + group.group + '</span>';
    group.items.forEach(function (item) {
      var active = isActive(item.path) ? ' active' : '';
      var badge = '';
      if (item.status === 'beta')  badge = '<span class="ds-shell-link-badge ds-shell-link-badge--beta">Beta</span>';
      if (item.status === 'draft') badge = '<span class="ds-shell-link-badge ds-shell-link-badge--draft">Draft</span>';
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

  /* ── Search index ── */
  var SEARCH_INDEX = [
    {label:'Buttons',path:'/buttons/',desc:'Primary, secondary, ghost, destructive, ultimate, TV variants. Size scale xs–TV.'},
    {label:'Cards',path:'/cards/',desc:'Landscape, portrait, square game cards. Overlay, skeleton, active states.'},
    {label:'Inputs',path:'/inputs/',desc:'Text input, password, search. Filled, error, disabled states.'},
    {label:'Search',path:'/search/',desc:'Search input with suggestions, recent, empty state.'},
    {label:'Chips',path:'/chips/',desc:'Default, selected, filter, removable chip variants.'},
    {label:'Rails',path:'/rails/',desc:'Horizontal scroll rail for game cards. Gap, padding, scroll snap.'},
    {label:'Genre Tiles',path:'/genre-tiles/',desc:'Game genre selection tiles. Selected state, image background.'},
    {label:'Pass Cards',path:'/pass-cards/',desc:'JioGames Pass Mobile and Ultimate subscription cards.'},
    {label:'Page Dots',path:'/page-dots/',desc:'Carousel pagination dots. Active, inactive, TV variants.'},
    {label:'Tab Bar',path:'/tab-bar/',desc:'Bottom navigation tab bar. Active, inactive, badge states.'},
    {label:'Navigation',path:'/navigation/',desc:'App bar, navigation bar, breadcrumbs, back button patterns.'},
    {label:'Bottom Sheet',path:'/bottom-sheet/',desc:'Slide-up sheet with handle, snap points, dismiss gesture.'},
    {label:'Drawer',path:'/drawer/',desc:'Side drawer overlay navigation panel.'},
    {label:'Dialogs',path:'/dialogs/',desc:'Alert, confirm, error dialogs. Focus trap, accessible.'},
    {label:'Toast',path:'/toast/',desc:'Non-blocking notification. Success, error, info variants.'},
    {label:'Banners',path:'/banners/',desc:'Inline status banners. Success, warning, error, info, dismissible.'},
    {label:'Lists',path:'/lists/',desc:'Vertical list items. Leading icon, trailing action, dividers.'},
    {label:'Toggle',path:'/toggle/',desc:'On/off toggle switch. Checked, disabled, loading states.'},
    {label:'Badges',path:'/badges/',desc:'Count badge, status dot, label badge. Pass, popular, new variants.'},
    {label:'Forms',path:'/forms/',desc:'Form layout, field groups, validation, submit patterns.'},
    {label:'Avatar',path:'/avatar/',desc:'User avatar. Image, initials fallback, size variants.'},
    {label:'Skeleton',path:'/skeleton/',desc:'Loading placeholder. Shimmer animation, reduced-motion safe.'},
    {label:'Progress Bar',path:'/progress-bar/',desc:'Linear progress. Determinate, indeterminate, game loading.'},
    {label:'Colours',path:'/colours/',desc:'Brand green, gold, amber, surfaces, text, borders. WCAG contrast.'},
    {label:'Typography',path:'/typography/',desc:'JioType type scale. Display, heading, body, caption roles.'},
    {label:'Spacing',path:'/spacing/',desc:'8px base scale. --space-* tokens, gutters, rails, card gaps.'},
    {label:'Radius',path:'/radius/',desc:'--r1 (8px) to --r9 (28px) plus --pill. Component radius map.'},
    {label:'Motion',path:'/motion/',desc:'Spring, ease-screen, ease-out curves. Duration tokens. TV motion.'},
    {label:'Elevation',path:'/elevation/',desc:'Surface layers, glass overlays, glow shadows.'},
    {label:'Icons',path:'/icons/',desc:'1,646 icons. JioGames icon library, SVG sprite, search.'},
    {label:'TV Focus',path:'/tv-focus/',desc:'D-pad navigation, focus ring, spatial focus management for TV.'},
    {label:'Accessibility',path:'/accessibility/',desc:'WCAG AA, focus management, screen reader, reduced-motion, forced-colors.'},
    {label:'Governance',path:'/governance/',desc:'RFC process, semver, deprecation policy, contribution workflow.'},
    {label:'Getting Started',path:'/getting-started/',desc:'Installation, token model, first component, pre-ship checklist, font loading.'},
    {label:'Tooling',path:'/tooling/',desc:'validate.sh, build.py, version.sh, ci.sh, pre-commit hook, will-change.'},
    {label:'Token Reference',path:'/token-reference/',desc:'All 444 design tokens. Searchable. Colour, spacing, motion, component tokens.'},
    {label:'Patterns',path:'/patterns/',desc:'Multi-component UX flows: checkout, onboarding, game launch, empty search, pull-to-refresh, infinite scroll, notifications, share.'},
    {label:'Pull to Refresh',path:'/patterns/pull-to-refresh/',desc:'Mobile overscroll refresh. Trigger distance, indicator, states, jitter guard, reduced-motion.'},
    {label:'Infinite Scroll & Load More',path:'/patterns/load-more/',desc:'Infinite scroll vs pagination vs Load More. Game listing, search results, focus recovery, TV guidance.'},
    {label:'Notification Center',path:'/patterns/notification-center/',desc:'Persistent notifications. Read/unread, grouping, deep links, empty state, badges, accessibility.'},
    {label:'Share & Invite',path:'/patterns/share/',desc:'Native share, copy link, invite friend, referral code. Platform differences, success/failure feedback.'},
    {label:'Navigation + AppBar',path:'/navigation/',desc:'App bar, nav bar, back navigation, scroll behavior, transparent bar, sticky, mobile/web/TV.'},
  ];

  /* ── Sidebar search ── */
  var navSearch = document.getElementById('ds-nav-search');
  var navWrap = document.getElementById('ds-nav-wrap');

  // Component search results panel (above icon panel)
  var compPanel = document.createElement('div');
  compPanel.id = 'ds-comp-results';
  compPanel.style.cssText = 'display:none;padding:4px 0;border-bottom:1px solid var(--border-subtle);max-height:260px;overflow-y:auto;';
  navWrap.parentNode.insertBefore(compPanel, navWrap);

  function renderCompPanel(q) {
    if (!q || q.length < 2) { compPanel.style.display = 'none'; return; }
    var matches = SEARCH_INDEX.filter(function(item){
      return item.label.toLowerCase().indexOf(q) !== -1 || item.desc.toLowerCase().indexOf(q) !== -1;
    }).slice(0, 6);
    if (!matches.length) { compPanel.style.display = 'none'; return; }
    var html = '<div style="font-size:10px;font-weight:700;color:var(--text3);letter-spacing:.4px;text-transform:uppercase;padding:8px 12px 4px;">Pages</div>';
    matches.forEach(function(item){
      html += '<a href="' + toHref(item.path) + '" style="display:block;padding:7px 12px;text-decoration:none;border-radius:0;transition:background 100ms;" ' +
        'onmouseenter="this.style.background=\'rgba(255,255,255,.05)\'" onmouseleave="this.style.background=\'\'">' +
        '<div style="font-size:12px;font-weight:700;color:var(--text);margin-bottom:2px">' + item.label + '</div>' +
        '<div style="font-size:11px;color:var(--text3);line-height:1.4;white-space:nowrap;overflow:hidden;text-overflow:ellipsis">' + item.desc + '</div>' +
        '</a>';
    });
    compPanel.innerHTML = html;
    compPanel.style.display = '';
  }

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

  // No-results placeholder
  var noResults = document.createElement('div');
  noResults.id = 'ds-no-results';
  noResults.style.cssText = 'display:none;padding:12px 16px;font-size:12px;color:var(--text3);';
  noResults.innerHTML = 'No results. Try <a href="' + toHref('/token-reference/') + '" style="color:var(--jio);text-decoration:none">Token Reference</a> for tokens or <a href="' + toHref('/icons/') + '" style="color:var(--jio);text-decoration:none">Icons</a>.';
  navWrap.parentNode.insertBefore(noResults, navWrap);

  if (navSearch && navWrap) {
    navSearch.placeholder = 'Search… (or press /)';
    navSearch.addEventListener('input', function () {
      var raw = navSearch.value.trim();
      var q = raw.toLowerCase();
      var groups = navWrap.querySelectorAll('.ds-shell-group');
      var overviewLink = navWrap.parentNode.querySelector('.ds-shell-nav-wrap > .ds-shell-link');
      var navAnyVisible = false;

      // token query (--xxx) → redirect to token-reference with pre-fill
      if (q.startsWith('--') || q.startsWith('var(--')) {
        var tokenQ = q.replace(/^var\(/, '').replace(/\)$/, '').replace(/^--/, '');
        compPanel.innerHTML = '<div style="font-size:10px;font-weight:700;color:var(--text3);letter-spacing:.4px;text-transform:uppercase;padding:8px 12px 4px;">Token</div>' +
          '<a href="' + toHref('/token-reference/') + '?q=' + encodeURIComponent(tokenQ) + '" style="display:block;padding:7px 12px;text-decoration:none;font-size:12px;font-weight:700;color:var(--jio)">' +
          'Search "' + raw + '" in Token Reference →</a>';
        compPanel.style.display = '';
        groups.forEach(function(g){ g.style.display='none'; });
        if(overviewLink) overviewLink.style.display='none';
        iconPanel.style.display='none';
        noResults.style.display='none';
        return;
      }

      // CSS class query (.xxx)
      if (q.startsWith('.')) {
        var classQ = q.slice(1);
        var classMatches = SEARCH_INDEX.filter(function(item){
          return item.label.toLowerCase().indexOf(classQ) !== -1 || item.desc.toLowerCase().indexOf(classQ) !== -1;
        }).slice(0,4);
        if(classMatches.length){
          var html2 = '<div style="font-size:10px;font-weight:700;color:var(--text3);letter-spacing:.4px;text-transform:uppercase;padding:8px 12px 4px;">CSS class</div>';
          classMatches.forEach(function(item){
            html2 += '<a href="' + toHref(item.path) + '" style="display:block;padding:7px 12px;text-decoration:none;" onmouseenter="this.style.background=\'rgba(255,255,255,.05)\'" onmouseleave="this.style.background=\'\'">' +
              '<div style="font-size:12px;font-weight:700;color:var(--text)">' + item.label + '</div>' +
              '<div style="font-size:11px;color:var(--text3)">' + item.desc.substring(0,80) + '…</div></a>';
          });
          compPanel.innerHTML = html2;
          compPanel.style.display = '';
        } else { compPanel.style.display='none'; }
        groups.forEach(function(g){ g.style.display='none'; });
        if(overviewLink) overviewLink.style.display='none';
        iconPanel.style.display='none';
        noResults.style.display = classMatches.length ? 'none' : '';
        return;
      }

      // normal search
      if (overviewLink) {
        var ovShow = !q || 'overview'.indexOf(q) !== -1;
        overviewLink.style.display = ovShow ? '' : 'none';
        if (ovShow) navAnyVisible = true;
      }
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
        if (anyVisible) navAnyVisible = true;
      });

      renderIconPanel(q);
      renderCompPanel(q);

      var compVisible = compPanel.style.display !== 'none';
      var iconVisible = iconPanel.style.display !== 'none';
      noResults.style.display = (q && !navAnyVisible && !compVisible && !iconVisible) ? '' : 'none';

      if (!q) {
        groups.forEach(function (grp) {
          grp.style.display = '';
          grp.querySelectorAll('.ds-shell-link').forEach(function (a) { a.style.display = ''; });
        });
        if (overviewLink) overviewLink.style.display = '';
        compPanel.style.display = 'none';
        noResults.style.display = 'none';
      }
    });
    navSearch.addEventListener('keydown', function (e) {
      if (e.key === 'Escape') { navSearch.value = ''; navSearch.dispatchEvent(new Event('input')); navSearch.blur(); }
    });
  }

  // Global keyboard shortcut: "/" focuses search
  document.addEventListener('keydown', function(e) {
    if (e.key === '/' && e.target.tagName !== 'INPUT' && e.target.tagName !== 'TEXTAREA') {
      e.preventDefault();
      if (navSearch) { navSearch.focus(); navSearch.select(); }
    }
  });

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
  /* ── Force download for spec.md links (blob trick) ── */
  document.addEventListener('click', function (e) {
    var a = e.target.closest && e.target.closest('a.spec-download');
    if (!a) return;
    e.preventDefault();
    var url = a.getAttribute('href');
    var name = a.getAttribute('download') || 'spec.md';
    fetch(url, { cache: 'no-store' })
      .then(function (r) { return r.blob(); })
      .then(function (blob) {
        var b = new Blob([blob], { type: 'text/markdown;charset=utf-8' });
        var u = URL.createObjectURL(b);
        var tmp = document.createElement('a');
        tmp.href = u; tmp.download = name;
        document.body.appendChild(tmp); tmp.click();
        document.body.removeChild(tmp);
        setTimeout(function () { URL.revokeObjectURL(u); }, 1000);
      })
      .catch(function () { window.location.href = url; });
  });

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
