// Basic client-side interactions and lightweight validation
document.addEventListener('DOMContentLoaded', function () {
  const navToggle = document.getElementById('navToggle');
  const mainNav = document.getElementById('mainNav');
  if (navToggle && mainNav) {
    navToggle.addEventListener('click', () => mainNav.classList.toggle('open'))
  }

  // Simple form handlers — replace action with backend endpoints later
  const contactForm = document.getElementById('contactForm');
  if (contactForm) {
    contactForm.addEventListener('submit', e => {
      e.preventDefault();
      alert('Contact form submitted (frontend only). Implement backend POST /contact to store messages.');
      contactForm.reset();
    })
  }

  const loginForm = document.getElementById('loginForm');
  if (loginForm) {
    loginForm.addEventListener('submit', e => {
      // e.preventDefault();
      // alert('Login attempted (frontend only). Hook to backend /login for real auth.');
    })
  }

  // const signupForm = document.getElementById('signupForm');
  // if (signupForm) {
  //   signupForm.addEventListener('submit', e => {
  //     // e.preventDefault();
  //     // alert('Sign up attempted (frontend only). Hook to backend /signup to create users.');
  //     // signupForm.reset();
  //   })
  // }
  const swiper = new Swiper('.js-banking-slider', {
    // Horizontal direction
    direction: 'horizontal',
    loop: true,

    // Auto sliding
    autoplay: {
      delay: 3000,
      disableOnInteraction: false,
    },

    // How many slides to show
    slidesPerView: 1,
    spaceBetween: 29,

    // Responsive breakpoints
    breakpoints: {
      768: {
        slidesPerView: 2,
      },
      1024: {
        slidesPerView: 3,
      }
    },

    // Navigation arrows
    // navigation: {
    //     nextEl: '.swiper-button-next',
    //     prevEl: '.swiper-button-prev',
    // },

    // Pagination dots
    pagination: {
      el: '.swiper-pagination',
      clickable: true,
    },
  });

  const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add("show");
      }
    });
  });

  const elements = document.querySelectorAll(".poster-heading");

  elements.forEach((el) => observer.observe(el));

  setTimeout(function () {
    var msg = document.getElementById("flashMessage");

    if (msg) {
      msg.style.opacity = "0";

      setTimeout(function () {
        msg.remove();
      }, 500);
    }

  }, 3000);

});
