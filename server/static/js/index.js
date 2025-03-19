let key_reports = false;
const button_reports = document.getElementById("reports");
const arrow = document.getElementById("arrow");
const list_reports = document.getElementById("view-reports");

function show_report() {
    if (!key_reports) {
        button_reports.style.backgroundColor = "#EAAC25";
        list_reports.classList.add("list-reports-visible");
        arrow.classList.add("rotate");
        key_reports = true;

        button_reports.addEventListener('mouseenter', function (e) {
            e.target.style.backgroundColor = '#3078FF';
        });

        button_reports.addEventListener('mouseleave', function (e) {
            e.target.style.backgroundColor = '#EAAC25';
        });
    } else {
        button_reports.style.backgroundColor = "#3078FF";
        list_reports.classList.remove("list-reports-visible");
        arrow.classList.remove("rotate");
        key_reports = false;

        button_reports.addEventListener('mouseenter', function (e) {
            e.target.style.backgroundColor = '#EAAC25';
        });

        button_reports.addEventListener('mouseleave', function (e) {
            e.target.style.backgroundColor = '#3078FF';
        });
    }
}

document.addEventListener('DOMContentLoaded', function () {
    const tables = [document.getElementById('table1'), document.getElementById('table')];
    const contextMenu = document.getElementById('contextMenu');

    // Функция для снятия выделения со всех строк
    function clearSelection() {
        tables.forEach(table => {
            if (table) {
                const rows = table.querySelectorAll('tr');
                rows.forEach(row => {
                    row.classList.remove('selected'); // Удаляем класс выделения
                });
            }
        });
    }

    // Обработчик события для обеих таблиц
    tables.forEach(table => {
        if (table) { // Проверяем, существует ли таблица
            // Обработчик клика левой кнопкой мыши для выделения строки
            table.addEventListener('click', function (event) {
                if (event.target.tagName === 'TD') {
                    const row = event.target.parentNode;
                    clearSelection(); // Снимаем выделение со всех строк
                    row.classList.add('selected'); // Добавляем класс выделения
                }
            });

            // Обработчик события для правого клика
            table.addEventListener('contextmenu', function (event) {
                event.preventDefault(); // Отменяем стандартное контекстное меню

                // Проверяем, является ли кликнутый элемент ячейкой (td)
                if (event.target.tagName === 'TD') {
                    // Выделяем строку
                    const row = event.target.parentNode;
                    clearSelection(); // Снимаем выделение со всех строк
                    row.classList.add('selected'); // Добавляем класс выделения

                    // Позиционируем контекстное меню
                    contextMenu.style.display = 'block';
                    contextMenu.style.left = event.pageX + 'px';
                    contextMenu.style.top = event.pageY + 'px';

                    // Сохраняем ссылку на строку для дальнейших действий
                    contextMenu.dataset.row = row.rowIndex;
                    contextMenu.dataset.tableId = table.id; // Сохраняем ID таблицы
                }
            });
        }
    });

    // Обработчик клика вне таблиц для снятия выделения
    document.addEventListener('click', function (event) {
        const isClickInsideTable = tables.some(table => table && table.contains(event.target));
        const isClickInsideContextMenu = contextMenu.contains(event.target);

        if (!isClickInsideTable && !isClickInsideContextMenu) {
            clearSelection(); // Убираем выделение со всех строк
            contextMenu.style.display = 'none'; // Скрываем контекстное меню
        }
    });

    // Обработчик клика по элементам контекстного меню
    document.getElementById('editRow').addEventListener('click', function (event) {
        event.preventDefault(); // Отменяем переход по ссылке
        const rowIndex = contextMenu.dataset.row;
        const tableId = contextMenu.dataset.tableId;
        alert('Редактировать строку: ' + rowIndex + ' в таблице ' + tableId); // Здесь можно добавить логику редактирования
        contextMenu.style.display = 'none'; // Скрываем меню
    });

    document.getElementById('deleteRow').addEventListener('click', function (event) {
        event.preventDefault(); // Отменяем переход по ссылке
        const rowIndex = contextMenu.dataset.row;
        const tableId = contextMenu.dataset.tableId;
        const table = document.getElementById(tableId); // Получаем таблицу по ID
        const row = table.rows[rowIndex]; // Находим строку по индексу
        if (row) {
            row.parentNode.removeChild(row); // Удаляем строку
            alert('Строка ' + rowIndex + ' удалена из таблицы ' + tableId + '.'); // Подтверждение удаления
        }
        contextMenu.style.display = 'none'; // Скрываем меню
    });
});

const date_start = document.getElementById('date_start');
const date_finish = document.getElementById('date_finish');
const count_hundred = document.getElementById('count_hundred');
const count_month = document.getElementById('count_month');

function calculateDates() {
    const startDate = new Date(date_start.value);
    const finishDate = new Date(date_finish.value);

    if (!isNaN(startDate) && !isNaN(finishDate) && startDate < finishDate) {
        // Рассчитываем разницу в миллисекундах
        const totalDays = Math.ceil((finishDate - startDate) / (1000 * 60 * 60 * 24));

        // Рассчитываем количество рабочих дней (исключая выходные)
        let workingDays = 0;
        for (let d = 0; d <= totalDays; d++) {
            const currentDay = new Date(startDate);
            currentDay.setDate(startDate.getDate() + d);
            // Проверяем, является ли день рабочим (с понедельника по пятницу)
            if (currentDay.getDay() !== 0 && currentDay.getDay() !== 6) {
                workingDays++;
            }
        }

        // Заполняем поля
        count_hundred.value = workingDays * 8; // Предполагаем 8 часов в день
        count_month.value = Math.floor(totalDays / 30); // Примерное количество месяцев
    } else {
        count_hundred.value = '';
        count_month.value = '';
    }
}

date_start.addEventListener('change', calculateDates);
date_finish.addEventListener('change', calculateDates);

const priceInput = document.getElementById('price');

priceInput.addEventListener('input', function (event) {
    // Удаляем все символы, кроме цифр и запятой
    let value = priceInput.value.replace(/[^0-9,]/g, '');

    // Если запятая присутствует, ограничиваем до 2 цифр после запятой
    if (value.indexOf(',') !== -1) {
        const parts = value.split(',');
        value = parts[0] + ',' + parts[1].substring(0, 2);
    }

    // Добавляем "р" в конце
    if (value) {
        priceInput.value = value;
    } else {
        priceInput.value = '';
    }
});

// Обработка фокуса для удаления "р" при редактировании
priceInput.addEventListener('focus', function () {
    if (priceInput.value) {
        priceInput.value = priceInput.value.replace(/р$/, '');
    }
});

// Обработка потери фокуса для добавления "р" обратно
priceInput.addEventListener('blur', function () {
    if (priceInput.value) {
        // Если введено целое число, добавляем ",00"
        if (!priceInput.value.includes(',')) {
            priceInput.value += ',00';
        }
        priceInput.value = priceInput.value.replace(/р$/, '') + 'р';
    }
});

function validateForm() {
    const requiredFields = document.querySelectorAll('.required');
    let valid = true;

    // Сброс ошибок
    const errorMessages = document.querySelectorAll('.error-message');
    const inputs = document.querySelectorAll('.required');

    errorMessages.forEach(msg => msg.remove());
    inputs.forEach(input => input.classList.remove('error'));

    requiredFields.forEach(field => {
        if (!field.value.trim()) {
            valid = false;
            showError(field, 'Заполните поле');
        }
    });

    return valid; // Если все поля валидны, форма будет отправлена
}

function showError(input, message) {
    input.classList.add('error'); // Добавляем класс для изменения стиля границы
    const errorSpan = document.createElement('span');
    errorSpan.className = 'error-message';
    errorSpan.textContent = message;
    input.parentNode.appendChild(errorSpan);
}