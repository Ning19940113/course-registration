document.getElementById('registration-form').addEventListener('submit', function(e) {
    e.preventDefault(); // 阻止表单默认提交

    // 获取已选择的科目
    let selectedSubjects = [];
    document.querySelectorAll('input[name="subject"]:checked').forEach(function(subject) {
        selectedSubjects.push(subject.value);
    });

    // 获取已选择的上课时间
    let selectedClassTime = [];
    document.querySelectorAll('input[name="class_time"]:checked').forEach(function(time) {
        selectedClassTime.push(time.value);
    });

    // 获取已选择的时间段
    let selectedTimeSlot = [];
    document.querySelectorAll('input[name="time_slot"]:checked').forEach(function(slot) {
        selectedTimeSlot.push(slot.value);
    });

    // 显示已选择内容
    document.getElementById('selected-subject').textContent = '已选择科目: ' + selectedSubjects.join(', ');
    document.getElementById('selected-class-time').textContent = '已选择意向上课时间: ' + selectedClassTime.join(', ');
    document.getElementById('selected-time-slot').textContent = '已选择时间段: ' + selectedTimeSlot.join(', ');

    // 显示总结
    document.getElementById('selection-summary').style.display = 'block';
});
