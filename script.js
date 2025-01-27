// 监听科目选择变化，并显示已选择的科目
document.getElementById("subjects").addEventListener("change", function() {
    var selectedSubjects = Array.from(this.selectedOptions).map(option => option.value);
    document.getElementById("selected-subjects").innerText = "已选择科目: " + selectedSubjects.join(", ");
});

// 监听时间段选择变化，并显示已选择的时间段
document.getElementById("time").addEventListener("change", function() {
    var selectedTime = Array.from(this.selectedOptions).map(option => option.value);
    document.getElementById("selected-time").innerText = "已选择时间: " + selectedTime.join(", ");
});
