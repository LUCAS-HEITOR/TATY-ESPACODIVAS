// ========== MENU MOBILE ==========
const mobileMenuToggle = document.getElementById('mobileMenuToggle');
const navMenu = document.getElementById('navMenu');

if (mobileMenuToggle) {
    mobileMenuToggle.addEventListener('click', () => {
        navMenu.classList.toggle('active');
        mobileMenuToggle.classList.toggle('active');
    });

    // Fechar menu ao clicar em um link
    const navLinks = document.querySelectorAll('.nav-menu a');
    navLinks.forEach(link => {
        link.addEventListener('click', () => {
            navMenu.classList.remove('active');
            mobileMenuToggle.classList.remove('active');
        });
    });
}

// ========== NAVBAR SCROLL ==========
window.addEventListener('scroll', () => {
    const navbar = document.querySelector('.navbar');
    if (window.scrollY > 50) {
        navbar.style.boxShadow = '0 4px 20px rgba(0, 0, 0, 0.1)';
    } else {
        navbar.style.boxShadow = '0 4px 6px rgba(0, 0, 0, 0.1)';
    }
});

// ========== FECHAR ALERTAS ==========
const closeAlertButtons = document.querySelectorAll('.close-alert');
closeAlertButtons.forEach(button => {
    button.addEventListener('click', () => {
        const alert = button.parentElement;
        alert.style.opacity = '0';
        alert.style.transform = 'translateX(100px)';
        setTimeout(() => {
            alert.remove();
        }, 300);
    });
});

// Auto-fechar alertas após 5 segundos
const alerts = document.querySelectorAll('.alert');
alerts.forEach(alert => {
    setTimeout(() => {
        const closeButton = alert.querySelector('.close-alert');
        if (closeButton) {
            closeButton.click();
        }
    }, 5000);
});

// ========== ANIMAÇÃO AOS SIMPLES ==========
const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('aos-animate');
            observer.unobserve(entry.target);
        }
    });
}, observerOptions);

document.querySelectorAll('[data-aos]').forEach(el => {
    observer.observe(el);
});

// ========== SMOOTH SCROLL ==========
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});

// ========== VALIDAÇÃO DE DATA (RESERVA) ==========
const dataInput = document.getElementById('data_desejada');
if (dataInput) {
    // Definir data mínima como amanhã
    const tomorrow = new Date();
    tomorrow.setDate(tomorrow.getDate() + 1);
    const minDate = tomorrow.toISOString().split('T')[0];
    dataInput.setAttribute('min', minDate);
    
    // Desabilitar domingos
    dataInput.addEventListener('input', function() {
        const selectedDate = new Date(this.value + 'T00:00:00');
        if (selectedDate.getDay() === 0) { // 0 = Domingo
            alert('Desculpe, não abrimos aos domingos. Por favor, escolha outro dia.');
            this.value = '';
        }
    });
}

// ========== FORMATAÇÃO DE TELEFONE ==========
const telefoneInputs = document.querySelectorAll('input[type="tel"]');
telefoneInputs.forEach(input => {
    input.addEventListener('input', function(e) {
        let value = e.target.value.replace(/\D/g, '');
        
        if (value.length <= 11) {
            if (value.length <= 10) {
                value = value.replace(/^(\d{2})(\d)/g, '($1) $2');
                value = value.replace(/(\d)(\d{4})$/, '$1-$2');
            } else {
                value = value.replace(/^(\d{2})(\d)/g, '($1) $2');
                value = value.replace(/(\d)(\d{4})$/, '$1-$2');
            }
        }
        
        e.target.value = value;
    });
});

// ========== LOADING NO SUBMIT ==========
const forms = document.querySelectorAll('form');
forms.forEach(form => {
    form.addEventListener('submit', function(e) {
        const submitBtn = this.querySelector('button[type="submit"]');
        if (submitBtn) {
            submitBtn.disabled = true;
            submitBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Enviando...';
        }
    });
});

// ========== PREVIEW DE SERVIÇO SELECIONADO ==========
const servicoSelect = document.getElementById('servico');
if (servicoSelect) {
    servicoSelect.addEventListener('change', function() {
        const selectedOption = this.options[this.selectedIndex];
        if (selectedOption.value) {
            // Adicionar efeito visual de seleção
            this.style.borderColor = '#e91e63';
            this.style.boxShadow = '0 0 0 3px rgba(233, 30, 99, 0.1)';
        }
    });
}

// ========== ANIMAÇÃO DE ENTRADA ==========
window.addEventListener('load', () => {
    document.body.style.opacity = '0';
    document.body.style.transition = 'opacity 0.3s ease';
    
    requestAnimationFrame(() => {
        document.body.style.opacity = '1';
    });
});

// ========== PARALLAX SUAVE NO HERO ==========
const hero = document.querySelector('.hero');
if (hero) {
    window.addEventListener('scroll', () => {
        const scrolled = window.pageYOffset;
        const parallaxSpeed = 0.5;
        
        if (scrolled < window.innerHeight) {
            hero.style.transform = `translateY(${scrolled * parallaxSpeed}px)`;
        }
    });
}

// ========== COUNTER ANIMATION ==========
function animateCounter(element) {
    const target = parseInt(element.getAttribute('data-target'));
    const duration = 2000; // 2 segundos
    const increment = target / (duration / 16); // 60 FPS
    let current = 0;
    
    const updateCounter = () => {
        current += increment;
        if (current < target) {
            element.textContent = Math.floor(current);
            requestAnimationFrame(updateCounter);
        } else {
            element.textContent = target;
        }
    };
    
    updateCounter();
}

// Observar elementos com contador
const counters = document.querySelectorAll('[data-target]');
const counterObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            animateCounter(entry.target);
            counterObserver.unobserve(entry.target);
        }
    });
}, { threshold: 0.5 });

counters.forEach(counter => {
    counterObserver.observe(counter);
});

console.log('🌸 Taty Espaço Divas - Website carregado com sucesso!');
