document.querySelectorAll('.room-btn').forEach(roomBtn => {
    roomBtn.dataset.room
});

$(document).ready(function() {
    $('.room-btn').click(function() {
        // get room number
        let room_id = this.innerHTML;
        console.log(this, room_id);
        // modify modal content
        // room number, date, time slot, no people
        let rid_disp = document.getElementById("room_id");
        console.log(rid_disp)
        // rid_disp.value = room_id;
        rid_disp.setAttribute('value', room_id);
        rid_disp.setAttribute('readonly', true);
        // rid_disp.setAttribute('value', room_id);

        let date_disp = document.getElementById("date"); // get the date from the calendar somehow
        // date_disp.value = "14th December 2023";
        date_disp.setAttribute('value', "14th Decemeber 2023");
        date_disp.setAttribute('readonly', true);
        // date_disp.setAttribute('value', "14th December 2023");
        // let timeslot_disp = document.getElementById("timeslot");

        // rid_disp.innerHTML = room_id
    });

    // $('.date-selector').click(function() {
    //     // added by mat taylor (can delete when needed)
    //     // remove the 'current-date' class to the div that it was previously on
    //     let calender_days_disp = document.querySelector('/'.calendar-days);
    //     console.log(calender_days_disp.children.length);
        
    //     for (let i=0; i<31; i++); {
    //         let day_disp = calender_days_disp.children[i]
    //         console.log(day_disp);
    //         day_disp.classList.remove('current-date');
    //     }
    //     // add the 'current-date' class to 'this'
    //     this.classList.add('current-date');
    // });

});