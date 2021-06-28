/* add smooh effect for search input */
var img;
window.onload = function () {
  var popup = document.getElementById("searchInput");
  var search = document.getElementById("searchbtn");
  document.onclick = function (e) {
    if (e.target.id !== "searchbtn") {
      if (popup.classList.contains("show") && !popup.contains(e.target)) {
        popup.classList.remove("show");
      }
    } else {
      popup.classList.toggle("show");
    }
  };
};

/* add smooth effect for dropdowns */
$(".dropdown-menu").addClass("invisible");

$(".dropdown").on("show.bs.dropdown", function (e) {
  $(".dropdown-menu").removeClass("invisible");
  $(this).find(".dropdown-menu").first().stop(true, true).slideDown();
});

// ADD SLIDEUP ANIMATION TO DROPDOWN-MENU
$(".dropdown").on("hide.bs.dropdown", function (e) {
  $(this).find(".dropdown-menu").first().stop(true, true).slideUp();
});
$(document).ready(function () {
  $(".crop").hide();
});
/* img  profile photo uploading */

function uploadImg() {
  var $uploadCrop;
  $("#imgInput").click();

  function readFile(input) {
    $(".crop").show();

    if (input.files && input.files[0]) {
      var reader = new FileReader();

      reader.onload = function (e) {
        $(".profileTop").addClass("ready");

        $uploadCrop
          .croppie("bind", {
            url: e.target.result,
          })
          .then(function () {});
      };

      reader.readAsDataURL(input.files[0]);
    } else {
      swal("Sorry - you're browser doesn't support the FileReader API");
    }
  }

  $uploadCrop = $("#img-upload").croppie({
    viewport: {
      width: 100,
      height: 100,
      type: "circle",
    },
    boundary: {
      width: 300,
      height: 200,
    },
    showZoomer: false,
    enableExif: true,
  });

  $("#imgInput").on("change", function () {
    readFile(this);
  });

  $("#choose").on("click", function (ev) {
    $uploadCrop
      .croppie("result", {
        type: "blob",
        size: "viewport",
      })
      .then(function (resp) {
        const date = new Date().getTime() / 1000;
        img = new File([resp], `${date}.jpeg`, { type: "image/jpeg" });
        const url = URL.createObjectURL(resp);

        $("#ppimage").attr("src", url);
        $(".crop").hide();
        $("#img-upload").hide();
      });
  });
}

/* upload word doc */
function uploadDoc(e) {
  $("#docId").click();
  $("#docId").on("change", function (e) {
    $("#fileName").text(this.files[0].name);
  });
}
