var els = document.getElementsByClassName('single_todo_checkbox')

console.log(els)
for (var i = 0; i < els.length; i++) {
  // Here we have the same `onclick`
  els[i].addEventListener('change', function (event) {
    if (event.target.checked) {
      console.log('Checkbox ' + event.target.innerHTML + ' is checked');
      // Perform your action here
    }
    //console log the single element
    console.log(event.target)
    console.log('Element ' + event.target.innerHTML + ' was just clicked')
  })
}