const input = document.getElementById('input');
const list = document.getElementById('list');
const form = document.getElementById('form');

form.addEventListener('submit', (e) => {
    e.preventDefault();
    const text = input.value.trim();
    if (text === '') return;


    if (text.includes('_')) {
        alert('Invalid input');
        return;
    }

    const task = document.createElement('li');
    task.textContent = text;

    task.addEventListener('click', () => {
        task.classList.toggle('done');
    });


    const deleteBtn = document.createElement('button');
    deleteBtn.textContent = "X";
    deleteBtn.classList.add("delete");
    deleteBtn.addEventListener('click', (e) => {
        task.remove();
    });

    task.appendChild(deleteBtn);
    list.appendChild(task);
    input.value = '';
});