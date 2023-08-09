/*
  Divide & Conquer Exercise
  Unit 19 of Springboard SWE Bootcamp
   
  Solution by José Delpino
*/

describe("#findRotationCount", function () {
  it("returns the number of rotations", function () {
    expect(findRotationCount([15, 18, 2, 3, 6, 12])).toBe(2);
    expect(findRotationCount([7, 9, 11, 12, 5])).toBe(4);
    expect(findRotationCount([7, 9, 11, 12, 15])).toBe(0);
  });
});
