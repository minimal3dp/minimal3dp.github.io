(function(){
  // places a Popular Posts widget into any div with id=popular-posts-js
  var container = document.getElementById('popular-posts-js');
  if(!container) return;
  fetch('/data/popular.json')
    .then(function(r){ if(!r.ok) throw new Error('failed fetching popular json'); return r.json()})
    .then(function(json){
      // json can be an array (legacy) or an object with keys (global, blog, tools)
      var section = container.dataset.section || 'global';
      var list = Array.isArray(json) ? json : (json[section] || json.global || []);
      var ul = document.createElement('ul');
      ul.className = 'popular-posts__list';
      list.slice(0,5).forEach(function(p){
        var li = document.createElement('li');
        li.className = 'popular-posts__item';
        var a = document.createElement('a');
        a.href = p.url;
        a.textContent = p.title;
        li.appendChild(a);
        if(p.views){
          var span = document.createElement('span');
          span.className = 'muted';
          span.textContent = ' — ' + p.views + ' views';
          li.appendChild(span);
        }
        ul.appendChild(li);
      });
      // optional title
      var title = document.createElement('h3'); title.className = 'widget-title'; title.textContent = 'Popular This Week';
      container.appendChild(title);
      container.appendChild(ul);
    }).catch(function(err){ console.info('no popular.json available', err) });
})();