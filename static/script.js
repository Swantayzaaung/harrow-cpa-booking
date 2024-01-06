document.querySelectorAll('.room-btn').forEach(roomBtn => {
    roomBtn.dataset.room
});

$(document).ready(function() {
    $('.room-btn').click(function() {
        // get room number
        let room_id = this.innerHTML;

        // MODIFY MODAL CONTENT
        // insert room id
        let rid_disp = document.getElementById("room_id");
        rid_disp.setAttribute('value', room_id);
        rid_disp.setAttribute('readonly', true);

        // insert date
        let date_disp = document.getElementById("date"); // get the date from the calendar somehow
        date_disp.setAttribute('value', "14-12-2023");
        date_disp.setAttribute('readonly', true);
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