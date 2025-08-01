 const filterLinks = document.querySelectorAll('.filter a');
  const projectCards = document.querySelectorAll('.card2');

  filterLinks.forEach(link => {
    link.addEventListener('click', function(e) {
      e.preventDefault();

      const filterValue = this.getAttribute('data-filter');

      projectCards.forEach(card => {
        const type = card.getAttribute('data-type');

        if (filterValue === 'all' || type === filterValue) {
          card.style.display = 'block';
        } else {
          card.style.display = 'none';
        }
      });
    });
  });