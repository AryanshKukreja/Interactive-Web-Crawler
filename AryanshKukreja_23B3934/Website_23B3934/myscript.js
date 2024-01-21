document.addEventListener('DOMContentLoaded', function () {
    document.getElementById('hobbyForm').addEventListener('submit', function (event) {
        event.preventDefault();

        var selectedHobby = document.getElementById('hobbySelector').value;

        document.getElementById('keyboardSection').classList.add('hidden');
        document.getElementById('cinemaSection').classList.add('hidden');
        document.getElementById('tableTennisSection').classList.add('hidden');

        document.getElementById(selectedHobby + 'Section').classList.remove('hidden');
    });
});
