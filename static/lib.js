var makeEditable = function() {
  var getAll = function(q, ctx) {
    return [].slice.call((ctx||document).querySelectorAll(q));
  };
  var lists = getAll('[data-list]'),
      textNodes = getAll('[data-text]'),
      images = getAll('[data-src]');
  textNodes.forEach(function(txt) {
    txt.contentEditable = true;
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
	link.innerText = 'Edit Me';
      });
      makeRemovable(li);
      list.insertBefore(li, addLi);
    });
    addLi.appendChild(btn);
    list.appendChild(addLi);
  });
};

