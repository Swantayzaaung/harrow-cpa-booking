document.querySelectorAll('.room-btn').forEach(roomBtn => {
    roomBtn.dataset.room
});


$('.room-btn').click(function() {
    // get room number
    let room_id = this.innerHTML;
    // modify modal content
    // date, no people, time slot, room number
    // room number, date, time slot, no people
    let modal = document.querySelector(".modal-body");
    modal.innerHTML = room_id;
});