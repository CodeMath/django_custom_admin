document.addEventListener("DOMContentLoaded", function () {
    var inputs = document.querySelectorAll('.image-preview-input input[type="file"]');
    inputs.forEach(function(input) {
        input.addEventListener('change', function(event) {
            var file = event.target.files[0];
            var reader = new FileReader();
            reader.onload = function(e) {
                var img = document.querySelector('img[data-preview-for="' + input.name + '"]');
                if (img) {
                    img.src = e.target.result;
                }
            };
            reader.readAsDataURL(file);
        });
    });
});
