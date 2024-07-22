(self.webpackChunk_N_E=self.webpackChunk_N_E||[]).push([[508],{7498:function(e,t){"use strict";var r,n;Object.defineProperty(t,"__esModule",{value:!0}),function(e,t){for(var r in t)Object.defineProperty(e,r,{enumerable:!0,get:t[r]})}(t,{PrefetchKind:function(){return r},ACTION_REFRESH:function(){return o},ACTION_NAVIGATE:function(){return l},ACTION_RESTORE:function(){return u},ACTION_SERVER_PATCH:function(){return f},ACTION_PREFETCH:function(){return a},ACTION_FAST_REFRESH:function(){return i},ACTION_SERVER_ACTION:function(){return c}});let o="refresh",l="navigate",u="restore",f="server-patch",a="prefetch",i="fast-refresh",c="server-action";(n=r||(r={})).AUTO="auto",n.FULL="full",n.TEMPORARY="temporary",("function"==typeof t.default||"object"==typeof t.default&&null!==t.default)&&void 0===t.default.__esModule&&(Object.defineProperty(t.default,"__esModule",{value:!0}),Object.assign(t.default,t),e.exports=t.default)},30:function(e,t,r){"use strict";function getDomainLocale(e,t,r,n){return!1}Object.defineProperty(t,"__esModule",{value:!0}),Object.defineProperty(t,"getDomainLocale",{enumerable:!0,get:function(){return getDomainLocale}}),r(2866),("function"==typeof t.default||"object"==typeof t.default&&null!==t.default)&&void 0===t.default.__esModule&&(Object.defineProperty(t.default,"__esModule",{value:!0}),Object.assign(t.default,t),e.exports=t.default)},5170:function(e,t,r){"use strict";Object.defineProperty(t,"__esModule",{value:!0}),Object.defineProperty(t,"default",{enumerable:!0,get:function(){return g}});let n=r(8754),o=n._(r(7294)),l=r(4450),u=r(2227),f=r(4364),a=r(109),i=r(3607),c=r(1823),s=r(9031),d=r(920),p=r(30),v=r(7192),b=r(7498),h=new Set;function prefetch(e,t,r,n,o,l){if(!l&&!(0,u.isLocalURL)(t))return;if(!n.bypassPrefetchedCheck){let o=void 0!==n.locale?n.locale:"locale"in e?e.locale:void 0,l=t+"%"+r+"%"+o;if(h.has(l))return;h.add(l)}let f=l?e.prefetch(t,o):e.prefetch(t,r,n);Promise.resolve(f).catch(e=>{})}function isModifiedEvent(e){let t=e.currentTarget,r=t.getAttribute("target");return r&&"_self"!==r||e.metaKey||e.ctrlKey||e.shiftKey||e.altKey||e.nativeEvent&&2===e.nativeEvent.which}function linkClicked(e,t,r,n,l,f,a,i,c,s){let{nodeName:d}=e.currentTarget,p="A"===d.toUpperCase();if(p&&(isModifiedEvent(e)||!c&&!(0,u.isLocalURL)(r)))return;e.preventDefault();let navigate=()=>{let e=null==a||a;"beforePopState"in t?t[l?"replace":"push"](r,n,{shallow:f,locale:i,scroll:e}):t[l?"replace":"push"](n||r,{forceOptimisticNavigation:!s,scroll:e})};c?o.default.startTransition(navigate):navigate()}function formatStringOrUrl(e){return"string"==typeof e?e:(0,f.formatUrl)(e)}let y=o.default.forwardRef(function(e,t){let r,n;let{href:u,as:f,children:h,prefetch:y=null,passHref:g,replace:_,shallow:m,scroll:O,locale:C,onClick:E,onMouseEnter:T,onTouchStart:P,legacyBehavior:j=!1,...M}=e;r=h,j&&("string"==typeof r||"number"==typeof r)&&(r=o.default.createElement("a",null,r));let k=o.default.useContext(c.RouterContext),R=o.default.useContext(s.AppRouterContext),x=null!=k?k:R,A=!k,I=!1!==y,L=null===y?b.PrefetchKind.AUTO:b.PrefetchKind.FULL,{href:N,as:S}=o.default.useMemo(()=>{if(!k){let e=formatStringOrUrl(u);return{href:e,as:f?formatStringOrUrl(f):e}}let[e,t]=(0,l.resolveHref)(k,u,!0);return{href:e,as:f?(0,l.resolveHref)(k,f):t||e}},[k,u,f]),U=o.default.useRef(N),w=o.default.useRef(S);j&&(n=o.default.Children.only(r));let D=j?n&&"object"==typeof n&&n.ref:t,[K,F,H]=(0,d.useIntersection)({rootMargin:"200px"}),V=o.default.useCallback(e=>{(w.current!==S||U.current!==N)&&(H(),w.current=S,U.current=N),K(e),D&&("function"==typeof D?D(e):"object"==typeof D&&(D.current=e))},[S,D,N,H,K]);o.default.useEffect(()=>{x&&F&&I&&prefetch(x,N,S,{locale:C},{kind:L},A)},[S,N,F,C,I,null==k?void 0:k.locale,x,A,L]);let q={ref:V,onClick(e){j||"function"!=typeof E||E(e),j&&n.props&&"function"==typeof n.props.onClick&&n.props.onClick(e),x&&!e.defaultPrevented&&linkClicked(e,x,N,S,_,m,O,C,A,I)},onMouseEnter(e){j||"function"!=typeof T||T(e),j&&n.props&&"function"==typeof n.props.onMouseEnter&&n.props.onMouseEnter(e),x&&(I||!A)&&prefetch(x,N,S,{locale:C,priority:!0,bypassPrefetchedCheck:!0},{kind:L},A)},onTouchStart(e){j||"function"!=typeof P||P(e),j&&n.props&&"function"==typeof n.props.onTouchStart&&n.props.onTouchStart(e),x&&(I||!A)&&prefetch(x,N,S,{locale:C,priority:!0,bypassPrefetchedCheck:!0},{kind:L},A)}};if((0,a.isAbsoluteUrl)(S))q.href=S;else if(!j||g||"a"===n.type&&!("href"in n.props)){let e=void 0!==C?C:null==k?void 0:k.locale,t=(null==k?void 0:k.isLocaleDomain)&&(0,p.getDomainLocale)(S,e,null==k?void 0:k.locales,null==k?void 0:k.domainLocales);q.href=t||(0,v.addBasePath)((0,i.addLocale)(S,e,null==k?void 0:k.defaultLocale))}return j?o.default.cloneElement(n,q):o.default.createElement("a",{...M,...q},r)}),g=y;("function"==typeof t.default||"object"==typeof t.default&&null!==t.default)&&void 0===t.default.__esModule&&(Object.defineProperty(t.default,"__esModule",{value:!0}),Object.assign(t.default,t),e.exports=t.default)},920:function(e,t,r){"use strict";Object.defineProperty(t,"__esModule",{value:!0}),Object.defineProperty(t,"useIntersection",{enumerable:!0,get:function(){return useIntersection}});let n=r(7294),o=r(3436),l="function"==typeof IntersectionObserver,u=new Map,f=[];function createObserver(e){let t;let r={root:e.root||null,margin:e.rootMargin||""},n=f.find(e=>e.root===r.root&&e.margin===r.margin);if(n&&(t=u.get(n)))return t;let o=new Map,l=new IntersectionObserver(e=>{e.forEach(e=>{let t=o.get(e.target),r=e.isIntersecting||e.intersectionRatio>0;t&&r&&t(r)})},e);return t={id:r,observer:l,elements:o},f.push(r),u.set(r,t),t}function observe(e,t,r){let{id:n,observer:o,elements:l}=createObserver(r);return l.set(e,t),o.observe(e),function(){if(l.delete(e),o.unobserve(e),0===l.size){o.disconnect(),u.delete(n);let e=f.findIndex(e=>e.root===n.root&&e.margin===n.margin);e>-1&&f.splice(e,1)}}}function useIntersection(e){let{rootRef:t,rootMargin:r,disabled:u}=e,f=u||!l,[a,i]=(0,n.useState)(!1),c=(0,n.useRef)(null),s=(0,n.useCallback)(e=>{c.current=e},[]);(0,n.useEffect)(()=>{if(l){if(f||a)return;let e=c.current;if(e&&e.tagName){let n=observe(e,e=>e&&i(e),{root:null==t?void 0:t.current,rootMargin:r});return n}}else if(!a){let e=(0,o.requestIdleCallback)(()=>i(!0));return()=>(0,o.cancelIdleCallback)(e)}},[f,r,t,a,c.current]);let d=(0,n.useCallback)(()=>{i(!1)},[]);return[s,a,d]}("function"==typeof t.default||"object"==typeof t.default&&null!==t.default)&&void 0===t.default.__esModule&&(Object.defineProperty(t.default,"__esModule",{value:!0}),Object.assign(t.default,t),e.exports=t.default)},9008:function(e,t,r){e.exports=r(9201)},1664:function(e,t,r){e.exports=r(5170)},9564:function(e,t,r){"use strict";r.d(t,{x:function(){return i}});var n=r(5059),o=r(1628),l=r(3179),u=r(296),f=r(5432);function compact(e){let t=Object.assign({},e);for(let e in t)void 0===t[e]&&delete t[e];return t}var a=r(5893),i=(0,n.G)(function(e,t){let r=(0,o.mq)("Text",e),{className:n,align:i,decoration:c,casing:s,...d}=(0,l.Lr)(e),p=compact({textAlign:e.align,textDecoration:e.decoration,textTransform:e.casing});return(0,a.jsx)(u.m.p,{ref:t,className:(0,f.cx)("chakra-text",e.className),...p,...d,__css:r})});i.displayName="Text"}}]);