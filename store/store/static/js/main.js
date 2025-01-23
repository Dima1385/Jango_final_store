document.querySelector('.form-container').addEventListener('submit', async (e) => {
    e.preventDefault();

    const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;
    const formData = new FormData(e.target);

    const response = await fetch('/contact/', {
        method: 'POST',
        headers: {
            'X-CSRFToken': csrfToken,
        },
        body: formData,
    });

    const data = await response.json();
    alert(data.message);
});
