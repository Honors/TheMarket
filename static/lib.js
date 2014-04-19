var update = function(patch) {
  var xhr = new XMLHttpRequest();
  xhr.open('POST', '/update', true);
  xhr.onload = function () {};
  xhr.send(JSON.stringify(patch));
};
var getAll = function(q, ctx) {
  return [].slice.call((ctx||document).querySelectorAll(q));
};
var setPath = function(obj, path, value) {
  if( path.length == 1 ) {
    obj[path[0]] = value;
  } else {
    obj[path[0]] = obj[path[0]] || (typeof path[1] == 'number' ? [] : {});
    setPath(obj[path[0]], path.slice(1), value);
  }
};
var cleanArrays = function(obj) {
  if( typeof obj == 'object' ) {
    if( obj instanceof Array ) {
      return obj.filter(function(x) {
        return typeof x != 'undefined';
      }).map(cleanArrays);
    } else {
      var b = {};
      for( var k in obj ) {
        b[k] = cleanArrays(obj[k]);
      }
      return b;
    }
  } else {
    return obj;
  }
};
var serialize = function() {
  var lists = getAll('[data-list]'),
      textNodes = getAll('[data-text]'),
      images = getAll('[data-src]');
  var obj = {};
  textNodes.forEach(function(txt) {
    var path = txt.dataset.text,
        comps = path.match(/\[[^\]]+\]/g).map(function(x) {
	  return x.substr(1, x.length - 2);
	}).map(function(x) {
	  return x.match(/^[0-9]+$/) ? parseInt(x, 10) : x;
	});
    setPath(obj, comps, txt.innerHTML);
  });
  obj = cleanArrays(obj);
  return obj;
};
var makeEditable = function() {
  var lists = getAll('[data-list]'),
      textNodes = getAll('[data-text]'),
      images = getAll('[data-src]');
  var toolbar = document.createElement('div');
  toolbar.style.position = 'fixed';
  toolbar.style.bottom = 0;
  toolbar.style.left = 0;
  toolbar.style.width = '100%';
  toolbar.style.height = '50px';
  toolbar.style.background = '#333';
  var saveBtn = document.createElement('button');
  saveBtn.innerText = 'Save';
  saveBtn.addEventListener('click', function(evt) {
    evt.preventDefault();
    update(serialize());
  });
  var doneBtn = document.createElement('button');
  doneBtn.innerText = 'Exit';
  doneBtn.addEventListener('click', function(evt) {
    evt.preventDefault();
    location.href = location.href;
  });
  toolbar.appendChild(saveBtn);
  toolbar.appendChild(doneBtn);
  document.body.appendChild(toolbar);

  textNodes.forEach(function(txt) {
    txt.contentEditable = true;
    txt.className += " editable";
  });
  images.forEach(function(image) {
    var upload = document.createElement('button');
    upload.addEventListener('click', function(evt) {
      evt.preventDefault();
      li.parentNode.removeChild(li);
    });
    upload.innerText = 'Change Image';
    upload.checked = true;
    upload.style.position = 'absolute';
    upload.style.top = 0;
    upload.style.left = 0;
    image.parentNode.insertBefore(upload, image);
  });
  var makeRemovable = function(li) {
      li.style.position = 'relative';
      var rm = document.createElement('button');
      rm.addEventListener('click', function(evt) {
	evt.preventDefault();
	li.parentNode.removeChild(li);
      });
      rm.innerText = 'X';
      rm.checked = true;
      rm.style.position = 'absolute';
      rm.style.top = 0;
      rm.style.right = 0;
      li.appendChild(rm);
  };
  lists.forEach(function(list) {
    var baseLi = list.children[0].cloneNode(true);

    getAll('li', list).forEach(makeRemovable);

    var addLi = document.createElement('li');
    var btn = document.createElement('button');
    btn.innerText = 'Add Element';
    btn.addEventListener('click', function(evt) {
      evt.preventDefault(); 
      var li = baseLi.cloneNode(true);
      getAll('[data-text]', li).forEach(function(link) {
	link.innerText = '';
      });
      makeRemovable(li);
      list.insertBefore(li, addLi);
    });
    addLi.appendChild(btn);
    list.appendChild(addLi);
  });
};
document.getElementById('edit').addEventListener('click', function(evt) {
  evt.preventDefault();
  makeEditable();
});

