// Faz a mensagem sumir depois de 3 segundos (se ela existir)
document.addEventListener('DOMContentLoaded', function() {
    const mensagens = document.querySelectorAll('.flash-msg');

    mensagens.forEach(function(msg) {
      setTimeout(function() {
        msg.style.transition = 'opacity 0.5s ease';
        msg.style.opacity = '0';

        setTimeout(function() {
          msg.remove();
        }, 500);
      }, 3000);
    });
  });