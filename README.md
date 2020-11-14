# liftr

A project that aims to provide an intuitive syntax to generate spreadsheets for lifting programs.

## how to use

Liftr uses .yaml files to generate a csv file containing your lifting program.

## how to write a program

Every yaml file will need config section, this is used to see which units you would like to use.
```yaml
config:
  units: lbs
```
This tells Liftr you are using lbs. You can write whatever you want for the units, it is purely aesthetic. If this isn't given, it will default to lbs.

The next section is the maxes section. This is only required if you plan on using percentages in your program. If you aren't, you can skip this step.
```yaml
maxes:
  Bench Press: 275
  Squat: 275
```
This allows you to use percentages when you put in Bench Press or Squat as the name of the exercise. If you try to use a percentage with a lift not listed here, you will encounter an error.

The last section is the program section. This specifies the exercises you want in the spreadsheet. It is separated by week, then day, then exercise. This section has to be begun with the keyword program.
```
program:
  Week 1:
    Day 1:
      Squat:
        sets: 6
        reps: 6
        weight: 70%
      Close-Grip Bench Press:
        sets: 5
        reps: 10
        weight: 185
```
Week 1 and Day 1 can be named to whatever organizational system you prefer, but internally it is weeks with days, and exercises in each day.
If you are specifying a static weight, just put the number. If you are using a percentage, make sure you put a % sign after the percentage you wish to use.

All of this put together will look like:
```yaml
config:
  units: lbs
maxes:
  Bench Press: 275
  Squat: 275
program:
  Week 1:
    Day 1:
      Squat:
        sets: 6
        reps: 6
        weight: 70%
      Close-Grip Bench Press:
        sets: 5
        reps: 10
        weight: 185
 ```
