def group_by_marks(marks, pass_marks)
    marks.group_by { |k, v| v >= pass_marks ? 'Passed' : 'Failed'}
  # your code here
end

marks = {"Ramesh":23, "Vivek":40, "Harsh":88, "Mohammad":60}
p group_by_marks(marks, 30)
