document.getElementById("booking-form").addEventListener("submit", function(event) {
    event.preventDefault();
    const name = document.getElementById("name").value;
    const date = document.getElementById("date").value;
    const time = document.getElementById("time").value;
    const people = document.getElementById("people").value;

    alert(`Booking confirmed!\nName: ${name}\nDate: ${date}\nTime: ${time}\nPeople: ${people}`);
});
