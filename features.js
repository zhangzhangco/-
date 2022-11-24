/* Filter accross all collumns in table */

$(document).ready(function(){
  $("#search").on("input", function() {
    var value = $(this).val().toLowerCase();
    $("#searchTable tr").filter(function() {
      $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
    });
  });
});

/* Clear filtering */

$(document).on('click', '.clear-filter', function(){       

  var docTable = $('#sorttableDocs').DataTable();
  docTable
   .search( '' )
   .columns().search( '' )
   .draw();

  $('#sorttableDocs').DataTable().searchPanes.clearSelections();
  $('#sorttableDocs').DataTable().order([1, 'asc']).draw();

  var groupTable = $('#sorttableGroups').DataTable();
  groupTable
   .search( '' )
   .columns().search( '' )
   .draw();

  $('#sorttableGroups').DataTable().searchPanes.clearSelections();
  $('#sorttableGroups').DataTable().order([0, 'asc']).draw();

  var groupProj = $('#sorttableProjs').DataTable();
  groupProj
   .search( '' )
   .columns().search( '' )
   .draw();

  $('#sorttableProjs').DataTable().searchPanes.clearSelections();
  $('#sorttableProjs').DataTable().order([0, 'asc']).draw();

  var url= document.location.href;
  window.history.pushState({}, "", url.split("?")[0]);

});

/* DataTable options for sort headers and filtering - Groups*/

$(document).ready(function() {

  var searchOptions = $.fn.dataTable.ext.deepLink( ['search.search' ] );

  var defaultOptions = {
    autoWidth: false,
    paging: false,
    responsive: true,
    buttons: [
      {
        extend: 'searchPanes',
        config:{
          cascadePanes: true,
          emptyMessage:"<i><b>None Defined</b></i>",
          dtOpts: {
            select: {
                style: 'multi'
            }
          }, 
          layout: 'columns-4',
          viewTotal: true,
          columns: [1, 7, 3, 4]
        }
      },
      {
        text: '清除所有过滤项',
        action: function ( e, dt, node, config ) {
          var table = $('#sorttableGroups').DataTable();
          table
           .search( '' )
           .columns().search( '' )
           .draw();

          $('#sorttableGroups').DataTable().searchPanes.clearSelections();
          $('#sorttableGroups').DataTable().order([0, 'asc']).draw();

          var url= document.location.href;
          window.history.pushState({}, "", url.split("?")[0]);
        }
      }
    ],
    columnDefs:[
      {
        width: '16.6%',
        targets:[2]
      },
      {
        width: '20%',
        targets:[6]
      },
      {
        visible: true,
        targets:[7],
        searchPanes: {
          header: "Technical Committee"
        }
      },
      {
        width: '16.6%',
        targets:[8]
      }
    ],
    dom: 
      "<'row'<'col d-print-none d-flex align-items-center'B><'col d-flex justify-content-center align-items-center'i><'col d-print-none d-flex justify-content-end align-items-center'f>>" +
      "<'row'<'col-sm-12't>>",
    language: {
      processing: "加载过滤选项", 
      loadingRecords: "载入中...",
      lengthMenu: "显示 _MENU_ 项结果",
      zeroRecords: "没有符合的结果",
      info: "显示第 _START_ 至 _END_ 项结果，共 _TOTAL_ 项",
      infoEmpty: "显示第 0 至 0 项结果，共 0 项",
      infoFiltered: "(从 _MAX_ 项结果中过滤)",
      infoPostFix: "",
      search: "搜索:",
      paginate: {
        first: "第一页",
        previous: "上一页",
        next: "下一页",
        last: "最后一页"
      },
      aria: {
        sortAscending: ": 升序排列",
        sortDescending: ": 降序排列"
      },
      searchPanes: {
        collapse: {0: '过滤选项', _: '过滤选项 (%d)'}
      }
    }
  };

  var dt = $('#sorttableGroups').DataTable( 
    $.extend( defaultOptions, searchOptions )
  );

});

/* DataTable options for sort headers and filtering - Projects*/

$(document).ready(function() {

  var searchOptions = $.fn.dataTable.ext.deepLink( ['search.search' ] );

  var defaultOptions = {
    autoWidth: false,
    paging: false,
    responsive: false,
    buttons: [
      {
        extend: 'searchPanes',
        config:{
          cascadePanes: true,
          emptyMessage:"<i><b>未定义</b></i>",
          dtOpts: {
            select: {
                style: 'multi'
            }
          }, 
          layout: 'columns-5',
          viewTotal: true,
          columns: [8, 2, 0, 12, 6]
        }
      },
      {
        text: '清除所有过滤项',
        action: function ( e, dt, node, config ) {
          var table = $('#sorttableProjs').DataTable();
          table
           .search( '' )
           .columns().search( '' )
           .draw();

          $('#sorttableProjs').DataTable().searchPanes.clearSelections();
          $('#sorttableProjs').DataTable().order([0, 'asc']).draw();

          var url= document.location.href;
          window.history.pushState({}, "", url.split("?")[0]);
        }
      }
    ],
    dom: 
      "<'row'<'col d-print-none d-flex align-items-center'B><'col d-flex justify-content-center align-items-center'i><'col d-print-none d-flex justify-content-end align-items-center'f>>" +
      "<'row'<'col-sm-12't>>",
      language: {
        processing: "加载过滤选项", 
        loadingRecords: "载入中...",
        lengthMenu: "显示 _MENU_ 项结果",
        zeroRecords: "没有符合的结果",
        info: "显示第 _START_ 至 _END_ 项结果，共 _TOTAL_ 项",
        infoEmpty: "显示第 0 至 0 项结果，共 0 项",
        infoFiltered: "(从 _MAX_ 项结果中过滤)",
        infoPostFix: "",
        search: "搜索:",
        paginate: {
          first: "第一页",
          previous: "上一页",
          next: "下一页",
          last: "最后一页"
        },
        aria: {
          sortAscending: ": 升序排列",
          sortDescending: ": 降序排列"
        },
        searchPanes: {
          collapse: {0: '过滤选项', _: '过滤选项 (%d)'}
        }
      },
    columnDefs:[
      {
        visible: false,
        targets:[4],
        searchPanes: {
          header: "已批准"
        }
      },
      {
        visible: false,
        targets:[6],
        searchPanes: {
          header: "状态"
        }
      },
      {
        visible: false,
        targets:[8],
        searchPanes: {
          header: "归口",
          dtOpts: {
            order: [[ 0, "desc" ]]
            }
        }
      },
      {
        visible: false,
        targets:[12],
        searchPanes: {
          header: "牵头单位",
          dtOpts: {
            order: [[ 0, "desc" ]]
            }
        }
      },
      {
        width: '25%',
        targets: [13]
      },
      {
        width: '16.6%',
        targets: [15]
      }
    ]
  }

  var dt = $('#sorttableProjs').DataTable( 
    $.extend( defaultOptions, searchOptions )
  );

});

/* DataTable options for sort headers and filtering - Documents*/

$(document).ready(function() {

  var searchOptions = $.fn.dataTable.ext.deepLink( ['search.search' ] );

  var defaultOptions = {
    paging: false,
    processing: true,
    responsive: true,
    order: [[4, 'des']],   
    buttons: [
        {
        extend: 'searchPanes',
        config:{
          cascadePanes: true,
          emptyMessage:"<i><b>未定义</b></i>",
          dtOpts: {
            select: {
                style: 'multi'
            }
          }, 
          layout: 'columns-6',
          viewTotal: true,
          columns: [2, 4, 6, 7, 8, 10]//5, 6, 7, 9]
        }
      },
      {
        text: '清除所有过滤项',
        action: function ( e, dt, node, config ) {
          var table = $('#sorttableDocs').DataTable();
          table
           .search( '' )
           .columns().search( '' )
           .draw();

          $('#sorttableDocs').DataTable().searchPanes.clearSelections();
          $('#sorttableDocs').DataTable().order([4, 'des']).draw();

          var url= document.location.href;
          window.history.pushState({}, "", url.split("?")[0]);
        }
      }
    ],
    dom: 
      "<'row'<'col d-print-none d-flex align-items-center'B><'col d-flex justify-content-center align-items-center'i><'col d-print-none d-flex justify-content-end align-items-center'f>>" +
      "<'row'<'col-sm-12't>>",
      language: {
        processing: "加载过滤选项", 
        loadingRecords: "载入中...",
        lengthMenu: "显示 _MENU_ 项结果",
        zeroRecords: "没有符合的结果",
        info: "显示第 _START_ 至 _END_ 项结果，共 _TOTAL_ 项",
        infoEmpty: "显示第 0 至 0 项结果，共 0 项",
        infoFiltered: "(从 _MAX_ 项结果中过滤)",
        infoPostFix: "",
        search: "搜索:",
        paginate: {
          first: "第一页",
          previous: "上一页",
          next: "下一页",
          last: "最后一页"
        },
        aria: {
          sortAscending: ": 升序排列",
          sortDescending: ": 降序排列"
        },
        searchPanes: {
          collapse: {0: '过滤选项', _: '过滤选项 (%d)'}
        }
      },
    columnDefs:[
      {
        visible: false,
        width: '5%',
        targets:[4],
        searchPanes: {
          header: "归口",
          dtOpts: {
            order: [[ 0, "desc" ]]
            }
        }
      },
      {
        width: '5%',
        targets:[1],
      },      
      {
        searchPanes: {
          header: "发布",
          dtOpts: {
            order: [[ 1, "desc" ]]
            }
        },
        width: '5%',
        targets:[2],
      },
      {
        width: '5%',
        targets:[3],
      },            
      {
        width: '5%',
        targets:[5],
      },
      {
        searchPanes: {
          orthogonal: 'sp',
          dtOpts: {
            order: [[ 1, "desc" ]]
          },
        },
        render: function (data, type, row) {
          if (type === 'sp') {
            var keywords = [];
            $( $(data), "i" ).each(function( index ) {
              var val = $( this ).text();
              val = val.trim();
              if (val.length > 0) {
                keywords.push(val);
              }
            });
            return keywords;
            }
          return data;
        },
        targets:[7]
      },
      {
        searchPanes: {
          dtOpts: {
            order: [[ 1, "desc" ]]
          },
          options:[
            {
              label: '现行',
              value: function(rowData, rowIdx){
                return rowData[8].includes('[ 现行 ]');
              }
            },
            {
              label: '已修改',
              value: function(rowData, rowIdx){
                return rowData[8].includes('[ 已修改 ]');
              }
            },
            {
              label: '草案',
              value: function(rowData, rowIdx){
                return rowData[8].includes('[ 草案 ]');
              }
            },
            {
              label: '送审稿',
              value: function(rowData, rowIdx){
                return rowData[8].includes('[ 送审稿 ]');
              }
            },
            {
              label: '已重申',
              value: function(rowData, rowIdx){
                return rowData[8].includes('[ 已重申 ]');
              }
            },
            {
              label: '稳定',
              value: function(rowData, rowIdx){
                return rowData[8].includes('[ 稳定 ]');
              }
            },
            {
              label: '被代替',
              value: function(rowData, rowIdx){
                return rowData[8].includes('[ 被代替 ]');
              }
            },
            {
              label: '未知',
              value: function(rowData, rowIdx){
                return rowData[8].includes('[ 未知 ]');
              }
            },
            {
              label: '废止',
              value: function(rowData, rowIdx){
                return rowData[8].includes('[ 废止 ]');
              }
            }
          ]
        },
        targets: [8]
      },
      {
        width: '10%',
        targets: [8]
      },           
      {
        visible: false,
        searchPanes: {
          header: "当前工作",
          orthogonal: 'sp'
        },
        render: function (data, type, row) {
          if (type === 'sp') {
            var currentWork = [];
            $( $(data), "i" ).each(function( index ) {
              var val2 = $( this ).text();

              val2 = val2.trim();
              if (val2.length > 0) {
                currentWork.push(val2);
              }
            });
            return currentWork;
            }
          return data;
        },
        targets:[10]
      }
    ]
  }

  var dt = $('#sorttableDocs').DataTable( 
    $.extend( defaultOptions, searchOptions )
  );

});

/* "Back To Top" button functionality */

$(document).ready(function() {
$(window).scroll(function() {
if ($(this).scrollTop() > 20) {
$('#toTopBtn').fadeIn();
} else {
$('#toTopBtn').fadeOut();
}
});

$('#toTopBtn').click(function() {
$("html, body").animate({
scrollTop: 0
}, 1000);
return false;
});
});