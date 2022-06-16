var date_range = null;

var date_now = moment().format('DD-MM-YYYY')

function generate_report() {
    var parameters = {
        'action': 'search_report',
        'start_date': '2022-06-02',
        'end_date': '2022-06-16',
    }

    if (date_range !== null) {
        parameters['start_date'] = date_range.startDate.format('YYYY-MM-DD')
        parameters['end_date'] = date_range.endDate.format('YYYY-MM-DD')
    }

    $('#data').DataTable({
        responsive: true,
        autoWidth: false,
        destroy: true,
        deferRender: true,
        ajax: {
            url: window.location.pathname,
            type: 'POST',
            data: parameters,
            dataSrc: ""
        },
        initComplete: function (settings, json) {
        }
    });
}


$(function () {
    $('input[name="date_range"]').daterangepicker({
        locale: {
            format: 'DD-MM-YYYY',
            applyLabel: 'Aplicar',
            cancelLabel: 'Cancelar',
        }
    }).on('apply.daterangepicker', function (ev, picker) {
        date_range = picker;
        generate_report();
    }).on('cancel.daterangepicker', function (ev, picker) {
        $(this).data('daterangepicker').setStartDate(date_now);
        $(this).data('daterangepicker').setEndDate(date_now);
        date_range = picker
        generate_report();
    });

});




