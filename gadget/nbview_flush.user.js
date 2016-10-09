// ==UserScript==
// @name        Refresh NBViewer Button
// @namespace   Peijun Zhu
// @description Add a button to navigation bar to flush the cache of nbviewer
// @include     http://nbviewer.jupyter.org/github/*
// @version     2.1
// @grant       none
// ==/UserScript==
function flush() {
  var url = document.location.href;
  while (url.substr( - 1) === '/' || url.substr( - 1) === '#') {
    //Strip # or / in the end
    url = url.substr(0, url.length - 1);
  }
  var tail = '?flush=true';
  if (!url.endsWith(tail)) {
    document.location.href = url + tail;
  } 
  else {
    document.location.reload();
  }
}
function add_flush_button() {
  var lu = document.getElementsByClassName('nav navbar-nav navbar-right') [0];
  var li = document.createElement('li');
  var a = document.createElement('a');
  li.appendChild(a);
  lu.appendChild(li);
  a.href = '#';
  a.onclick = flush;
  a.innerHTML = 'Flush';
}
add_flush_button();
