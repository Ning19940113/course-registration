document.addEventListener('DOMContentLoaded', function() {
  const subjects = document.getElementById('subjects');
  const timeslot = document.getElementById('timeslot');
  const otherTime = document.getElementById('other_time');
  const remarks = document.getElementById('remarks');
  
  // 确保提交按钮只能在必填项填满后才可点击
  document.querySelector('form').addEventListener('submit', function(event) {
    const name = document.getElementById('name').value;
    const grade = document.getElementById('grade').value;
    const subjectSelected = subjects.selectedOptions.length > 0;
    const timeslotSelected = timeslot.value !== "";
    const weekdaySelected = document.getElementById('weekday').selectedOptions.length > 0;

    if (!name || !grade || !subjectSelected || !timeslotSelected || !weekdaySelected) {
      alert("所有必填项必须填写！");
      event.preventDefault();
    }
  });
});
