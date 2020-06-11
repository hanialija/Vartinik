function fshiKonfirmoCard(id) {

    var pyetja = confirm("A jeni te sigurte qe do ti fshini te dhenat per produktin?");
    if (pyetja == true) {
        $.ajax({
            method: "POST",
            url: "/katalog/fshi/" + id + "/"
        }).done(function (msg) {
            if (msg == true) {
                $("#" + id).remove();

            }
            
        });
    }
    // window.location.replace("/admin/nxenesit/nxenesi/" + id + "/delete/");
    else
        return;
}
