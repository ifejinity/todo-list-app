const createTaskButton = document.querySelector('#create_task_button');
const createTaskForm = document.querySelector('#create_task_form');
const updateTaskButton = document.querySelector('#update_task_button');
const updateTaskForm = document.querySelector('#update_task_form');

/**submit create task form */
createTaskButton.addEventListener('click', () => {
   createTaskForm.submit();
})

/**update task */
updateTaskButton.addEventListener('click', () => {
    updateTaskForm.submit();
 })