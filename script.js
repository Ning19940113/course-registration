document.getElementById('subjects').addEventListener('change', function() {
  const selectedSubjects = Array.from(this.selectedOptions).map(option => option.text); // 显示中文
  document.getElementById('subject-list').innerText = selectedSubjects.join(', ');
});

document.getElementById('times').addEventListener('change', function() {
  const selectedTimes = Array.from(this.selectedOptions).map(option => option.text); // 显示中文
  document.getElementById('time-list').innerText = selectedTimes.join(', ');
});

document.getElementById('time-slots').addEventListener('change', function() {
  const selectedTimeSlots = Array.from(this.selectedOptions).map(option => option.text); // 显示中文
  document.getElementById('time-slot-list').innerText = selectedTimeSlots.join(', ');
});
