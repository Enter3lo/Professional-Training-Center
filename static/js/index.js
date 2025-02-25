let key_reports = false;
const button_reports = document.getElementById("reports");
const arrow = document.getElementById("arrow");
const list_reports = document.getElementById("view-reports");

function show_report() {
    if (!key_reports) {
        button_reports.style.backgroundColor = "#EAAC25";
        list_reports.classList.add("list-reports-visible");
        arrow.classList.add("rotate");
        key_reports = true;

        button_reports.addEventListener('mouseenter', function (e) {
            e.target.style.backgroundColor = '#3078FF';
        });

        button_reports.addEventListener('mouseleave', function (e) {
            e.target.style.backgroundColor = '#EAAC25';
        });
    } else {
        button_reports.style.backgroundColor = "#3078FF";
        list_reports.classList.remove("list-reports-visible");
        arrow.classList.remove("rotate");
        key_reports = false;

        button_reports.addEventListener('mouseenter', function (e) {
            e.target.style.backgroundColor = '#EAAC25';
        });

        button_reports.addEventListener('mouseleave', function (e) {
            e.target.style.backgroundColor = '#3078FF';
        });
    }
}
