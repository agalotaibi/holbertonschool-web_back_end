export default function getListStudentIds(list) {
    if (!Array.isArray(list)) {
        return [];
    }

    const ids = list.map((item) => item.id);
    return ids;

}
