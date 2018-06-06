$(document).ready(function () {

  var bindDrpValues = function (control, valueList, setting) {

      for (var i = 0; i < valueList.length; i++) {

          var option = $("<option>");
          option.attr("value", valueList[i][setting.Id]);
          option.html(valueList[i][setting.DisplayName]);
          $(control).append(option);
      }
  };

  var bindControlValue = function (control, valueList, setting,data) {

      var controlType = $(control).prop('tagName');
      var oldVal = control.outerHTML;
      switch (controlType) {
          case "SELECT":
              bindDrpValues(control, valueList, setting);
              break;;
          case "INPUT":
              break;
          default:
      }

      
  };

  var addRow = function (data) {
    
      var drpTypeOfPharma = $(data).find('#drpTypeOfPharma')[0];
      var txtDosage = $(data).find('#txtDosage')[0];
      var control = $(data);

      bindControlValue(drpTypeOfPharma,
          [{ "drgTypeId": 1, "drgName": "XYX" }, { "drgTypeId": 2, "drgName": "XYX1" }],
      {
          Id: 'drgTypeId',
          DisplayName: 'drgName'
      },data);

     
      
      $("#tblGrid").append(data);
      
  };

  var addNewRow = function () {
    debugger;
    addRow("<tr>\r\n    <td>\r\n        <select id=\"drpTypeOfPharma\"></select>\r\n    </td>\r\n    <td>\r\n        <input type=\"text\" id=\"txtDosage\"/>\r\n    </td>\r\n</tr>");
    
    
    
    // $.ajax({
     //    url: 'url',
     //     success: addRow,
     //     error: function (data) {
     //             debugger;
     //          alert("Fail" + data);
     //          }
     //       });
  };

  var addEvent = function () {
      $("#btnAdd").click(addNewRow);
  };
  addEvent();
})