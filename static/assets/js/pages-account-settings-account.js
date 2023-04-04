"use strict";
document.addEventListener("DOMContentLoaded", function (e) {
  {
    let e = document.getElementById("uploadedAvatar");
    const l = document.querySelector(".account-file-input"),
      c = document.querySelector(".account-image-reset");
    if (e) {
      const r = e.src;
      (l.onchange = () => {
        l.files[0] && (e.src = window.URL.createObjectURL(l.files[0]));
      }),
        (c.onclick = () => {
          (l.value = ""), (e.src = r);
        });
    }
  }
}),
  $(function () {
    var e = $(".select2");
    e.length &&
      e.each(function () {
        var e = $(this);
        e.wrap('<div class="position-relative"></div>'),
          e.select2({ dropdownParent: e.parent() });
      });
  });
