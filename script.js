document.getElementById('subjects').addEventListener('change', function() {
  const selectedSubjects = Array.from(this.selectedOptions).map(option => option.value);
  document.getElementById('subject-list').innerText = selectedSubjects.join(', ');
});

document.getElementById('times').addEventListener('change', function() {
  const selectedTimes = Array.from(this.selectedOptions).map(option => option.value);
  document.getElementById('time-list').innerText = selectedTimes.join(', ');
});
