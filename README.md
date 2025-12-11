# Agile Project

## Assignment I - Python Programs with Git Workflow

This repository contains three enhanced Python programs demonstrating Git workflow with branching and commits.

### Programs Included

#### 1. **Calculator Program** (`calculator.py`)
A full-featured calculator with a menu-driven interface.

**Features:**
- ✅ Addition operation
- ✅ Subtraction operation
- ✅ **Multiplication operation** (ENHANCED)
- ✅ **Division operation with zero-check** (ENHANCED)
- ✅ **Interactive menu system** (ENHANCED)
- Input validation for numeric values
- Error handling for division by zero

**How to Run:**
```bash
python calculator.py
```

---

#### 2. **Student Grade Checker** (`grade_checker.py`)
A comprehensive grade management system for students.

**Features:**
- ✅ Check individual student grades
- ✅ Batch check multiple students
- ✅ **A+ grade support (95+)** (ENHANCED)
- Grading scale: A+ (95+), A (90-94), B (80-89), C (70-79), D (60-69), F (0-59)
- Grade descriptions for each level
- Detailed grade reports

**How to Run:**
```bash
python grade_checker.py
```

**Grade Scale:**
- A+ (95-100): Excellent - Outstanding performance
- A (90-94): Excellent - Very Good performance
- B (80-89): Good - Above average performance
- C (70-79): Average - Satisfactory performance
- D (60-69): Below Average - Passing performance
- F (0-59): Fail - Needs improvement

---

#### 3. **Temperature Converter** (`temperature_converter.py`)
A complete temperature conversion tool supporting multiple scales.

**Features:**
- ✅ Celsius ↔ Fahrenheit conversion
- ✅ **Celsius ↔ Kelvin conversion** (ENHANCED)
- ✅ **Fahrenheit ↔ Kelvin conversion** (ENHANCED)
- ✅ Interactive menu for easy navigation
- View conversion formulas
- Precise temperature calculations with 2 decimal places

**How to Run:**
```bash
python temperature_converter.py
```

**Supported Conversions:**
- Celsius to Fahrenheit: °F = (°C × 9/5) + 32
- Fahrenheit to Celsius: °C = (°F - 32) × 5/9
- Celsius to Kelvin: K = °C + 273.15
- Kelvin to Celsius: °C = K - 273.15
- Fahrenheit to Kelvin: K = (°F - 32) × 5/9 + 273.15
- Kelvin to Fahrenheit: °F = (K - 273.15) × 9/5 + 32

---

## Git Workflow Summary

### Commits Made:
```
18f89a9 - Add three Python programs: Calculator, Grade Checker, and Temperature Converter
```

### Branches:
- **main**: Contains the initial version with all enhanced programs
- **feature/enhanced-programs**: Development branch for future enhancements

### Repository Information:
- **Owner**: santhoshh005
- **Repository**: Agile
- **Remote**: https://github.com/santhoshh005/Agile

### Git Commands Used:
```bash
# Create a new branch
git branch feature/enhanced-programs

# Switch to the new branch
git switch feature/enhanced-programs

# Alternative: Checkout command
git checkout feature/enhanced-programs

# Push changes to GitHub
git push -u origin feature/enhanced-programs
```

---

## Testing the Programs

Each program includes input validation and error handling. To test them:

1. **Calculator**: Test all four operations and edge cases (division by zero)
2. **Grade Checker**: Test grade calculations and the new A+ grade (95+)
3. **Temperature Converter**: Test all conversion combinations and verify calculations

---

## File Structure:
```
Agile/
├── calculator.py
├── grade_checker.py
├── temperature_converter.py
└── README.md
```