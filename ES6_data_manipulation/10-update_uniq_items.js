export default function updateUniqueItems(value) {
  if (!(value instanceof Map)) {
    throw new Error('Cannot process');
  }

  value.forEach((quantity, name) => {
    if (quantity === 1) {
      value.set(name, 100);
    }
  });

  return value;
}
