$(function () {
  $.get('https://swapi-api.alx-tools.com/api/people/5/?format=json', function (data, Status) {
    if (Status === 'success') {
      $('#character').text(data.name);
    }
  });
});
