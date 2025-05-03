const createTaskButton = document.querySelector('#create_task_button');
const createTaskForm = document.querySelector('#create_task_form');

/**submit create task form */
createTaskButton.addEventListener('click', () => {
   createTaskForm.submit();
})

/**update task */
const updateTask = (id) => {
    const updateTaskForm = document.querySelector(`#update_task_form_${id}`);
    updateTaskForm.submit();
}