export default function cleanSet(set, startString) {
  if (!startString || typeof startString !== 'string'){
    return '';
  }
  const parts = [];
  for (const value of set) {
    if (typeof value === 'string' && value.startsWith(startString)){
      const restOfString = value.slice(startString.length);
      parts.push(restOfString);
    }
  }
  return parts.join('-');
}
