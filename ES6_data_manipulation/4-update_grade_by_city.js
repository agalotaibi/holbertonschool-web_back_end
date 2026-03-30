export default function updateStudentGradeByCity(students, city, newGrades) {
  return students
    .filter((student) => student.location === city)
    .map((student) => {
      const gradeEntry = newGrades.filter((gradeObj) => gradeObj.studentId === student.id);

      const finalGrade = gradeEntry.length > 0 ? gradeEntry[0].grade : 'N/A';

      return {
        ...student,
        grade: finalGrade,
      };
    });
}
