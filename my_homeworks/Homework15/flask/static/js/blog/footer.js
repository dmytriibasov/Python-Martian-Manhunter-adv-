$(document).ready(function () {
    $.ajax({
        method: "GET",
        url: "/footer-links",
        success: function (data) {
            if (data.success) {
                for (let el of data.items) {
                    let footerLinkHtml = "<li class=\"nav-item\">\n" +
                        "                    <a class=\"nav-link active\" aria-current=\"page\" href=\""+ el.link +"\">" + el.name + "</a>\n" +
                        "                </li>"
                    $("#footerLinksList").append(footerLinkHtml);
                }
            }
        }
    });
});