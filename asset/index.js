        /*navbar menu*/
        function openNav() {
            document.getElementById("mySidenav").style.width = "250px";
            document.getElementById("main").style.marginLeft = "250px";
          }

          function closeNav() {
            document.getElementById("mySidenav").style.width = "0";
            document.getElementById("main").style.marginLeft= "0";
          }

      
      /*slideshow*/

          let slideIndex = 1;
          showSlides(slideIndex);
          
          function plusSlides(n) {
            showSlides(slideIndex += n);
          }
          
          function currentSlide(n) {
            showSlides(slideIndex = n);
          }
          
          function showSlides(n) {
            let i;
            let slides = document.getElementsByClassName("mySlides");
            let dots = document.getElementsByClassName("dot");
            if (n > slides.length) {slideIndex = 1}    
            if (n < 1) {slideIndex = slides.length}
              for (i = 0; i < slides.length; i++) {
                slides[i].style.display = "none";  
              }
              for (i = 0; i < dots.length; i++) {
                dots[i].className = dots[i].className.replace(" active", "");
              }
            slides[slideIndex-1].style.display = "block";  
            dots[slideIndex-1].className += " active";
          }

          /*column2's category buttons*/
        filterSelection("all")
        function filterSelection(c) {
          var x, i;
          x = document.getElementsByClassName("column2");
          if (c == "all") c = "";
            for (i = 0; i < x.length; i++) {
                w3RemoveClass(x[i], "show");
                if (x[i].className.indexOf(c) > -1) w3AddClass(x[i], "show");
            }
        }
    
        function w3AddClass(element, name) {
          var i, arr1, arr2;
          arr1 = element.className.split(" ");
          arr2 = name.split(" ");
          for (i = 0; i < arr2.length; i++) {
              if (arr1.indexOf(arr2[i]) == -1) {element.className += " " + arr2[i];}
          }
        }
    
        function w3RemoveClass(element, name) {
          var i, arr1, arr2;
          arr1 = element.className.split(" ");
          arr2 = name.split(" ");
          for (i = 0; i < arr2.length; i++) {
              while (arr1.indexOf(arr2[i]) > -1) {
              arr1.splice(arr1.indexOf(arr2[i]), 1);     
              }
          }
        element.className = arr1.join(" ");
        }
    
        // Add active class to the current button (highlight it)
        var btnContainer = document.getElementById("myBtnContainer");
        var btns = btnContainer.getElementsByClassName("btn");
        for (var i = 0; i < btns.length; i++) {
          btns[i].addEventListener("click", function(){
              var current = document.getElementsByClassName("active");
              current[0].className = current[0].className.replace(" active", "");
              this.className += " active";
          });
        }

        //Scroll back to top        
          (function($) { "use strict";
          $(document).ready(function(){"use strict";
      
                  var progressPath = document.querySelector('.progress-wrap path');
                  var pathLength = progressPath.getTotalLength();
                  progressPath.style.transition = progressPath.style.WebkitTransition = 'none';
                  progressPath.style.strokeDasharray = pathLength + ' ' + pathLength;
                  progressPath.style.strokeDashoffset = pathLength;
                  progressPath.getBoundingClientRect();
                  progressPath.style.transition = progressPath.style.WebkitTransition = 'stroke-dashoffset 10ms linear';
                  var updateProgress = function () {
                      var scroll = $(window).scrollTop();
                      var height = $(document).height() - $(window).height();
                      var progress = pathLength - (scroll * pathLength / height);
                      progressPath.style.strokeDashoffset = progress;
                  }
                  updateProgress();
                  $(window).scroll(updateProgress);
                  var offset = 50;
                  var duration = 550;
                  jQuery(window).on('scroll', function() {
                      if (jQuery(this).scrollTop() > offset) {
                          jQuery('.progress-wrap').addClass('active-progress');
                      } else {
                          jQuery('.progress-wrap').removeClass('active-progress');
                      }
                  });
                  jQuery('.progress-wrap').on('click', function(event) {
                      event.preventDefault();
                      jQuery('html, body').animate({scrollTop: 0}, duration);
                      return false;
                  })
      
      
              });
      
          })(jQuery);
