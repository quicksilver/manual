The following AppleScript code should be saved as a standard AppleScript
.scpt file named Convert Units To... in \~/Library/Application
Support/Quicksilver/Actions.

# Usage

Put Quicksilver's first pane into text mode and then type in a value
with units. Select this action in the second pane, then put the third
pane into text mode and type in the units you want to convert the value
into. The result will be returned into Quicksilver's first pane.

## Notes

Temperatures can be converted between the Celsius (ºC), Fahrenheit (ºF),
and Kelvin (K) scales.

When entering temperature units, the degree symbol may be entered as "º"
(press ⌥0), "\*", "deg" or "degrees", or it may be skipped entirely. The
scale can be indicated using either its letter symbol or its full name.
The term "centigrade" can be used as a synonym for Celsius. The script
can handle the symbols ºC and ºF regardless of whether they are composed
using º followed by the appropriate letter, or using the single Unicode
characters ℃ and ℉.

For a list of other available units, open /usr/share/misc/units.lib in
TextEdit.

This script uses the `units` command line tool to get the required
conversion rates, and then calculates the new values based on those
rates.

The numerical value can be a simple number (e.g. 10, -48, 67.528, etc.)
or an arithmetic expression you want to evaluate (e.g. 16^2-56, 2+2,
95/5, etc.). If no numerical value is supplied, the default value of 1
will be used.

## Examples

| First pane (in text mode) | Second pane         | Third pane (in text mode) | Result                   |
|---------------------------|---------------------|---------------------------|--------------------------|
| 3 m/s                     | Convert Units To... | miles/hour                | 6.7108089 miles/hour     |
| 10 kg/m^3/s               | Convert Units To... | lbs/gallon/day            | 7210.4294 lbs/gallon/day |
| -15 ºC                    | Convert Units To... | Fahrenheit                | 5 ºF                     |
| 450 deg F                 | Convert Units To... | K                         | 505.372222 K             |

# Code

``` applescript
using terms from application "Quicksilver"
    on process text thetext with args
        return convertUnits(thetext, args)
    end process text

    on get argument count
        return 2
    end get argument count

    on get direct types
        return {"NSStringPboardType"}
    end get direct types

    on get indirect types
        return {"NSStringPboardType"}
    end get indirect types
end using terms from

on convertUnits(input, targetUnits)
    --replace "º" with "deg" because that is easier to process below
    set input to my findReplace("º", "deg", input)
    set targetUnits to my findReplace("º", "deg", targetUnits)

    --split value from units
    set input to do shell script "echo " & quoted form of input & " | perl -pe 's/\\s(?!$)/\\0/ ; s/(?<=\\d)\\B(?=[a-zA-Z])/\\0/'"
    if input does not contain string id 0 then set input to "1" & string id 0 & input
    set {inputValue, inputUnits} to my delimitText(string id 0, input)

    --Process Unicode symbols for ºC and ºF. This is easier in AppleScript than perl.
    set inputUnits to my findReplace("℃", "degC", inputUnits)
    set targetUnits to my findReplace("℃", "degC", targetUnits)
    set inputUnits to my findReplace("℉", "degF", inputUnits)
    set targetUnits to my findReplace("℉", "degF", targetUnits)

    (* The regular expressions in perlSubstitutions do the following:
    1) Reformat various ways that the user might enter units for temperature.
    2) Allow "h" for the unit "hour". If "h" is being used as the "hecto-" prefix or as part of a longer unit name, it will not be altered.
    3) Allow "L" or "l" for the unit "litre". If "L" or "l" are being used as part of a longer unit name, it will not be altered.
    4) Allow "g" for the unit "gram", and "mg" for the unit "milligram". If "g" is being used as part of a longer unit name, it will not be altered.
    *)
    set perlSubstitutions to {¬
        "s/centigrade/Celsius/g", ¬
        "s/\\b(C|\\*C|ºC|deg C|degrees C|degCelsius|deg Celsius|degrees Celsius|Celsius)\\b/degC/", ¬
        "s/\\b(F|\\*F|ºF|℉|deg F|degrees F|degFahrenheit|deg Fahrenheit|degrees Fahrenheit|Fahrenheit)\\b/degF/", ¬
        "s/\\b(\\*K|ºK|degK|deg K|degrees K|degKelvin|deg Kelvin|degrees Kelvin|Kelvin)\\b/K/", ¬
        "s/\\bh(?![a-zA-Z])/hour/g", ¬
        "s/\\b[Ll](?![a-zA-Z])/litre/g", ¬
        "s/\\bg(?![a-zA-Z])/grams/g", ¬
        "s/\\bmg(?![a-zA-Z])/milligrams/g"}
    set inputUnits to do shell script "echo " & quoted form of inputUnits & " | perl -pe " & quoted form of my concatenateList(" ; ", perlSubstitutions)
    set targetUnits to do shell script "echo " & quoted form of targetUnits & " | perl -pe " & quoted form of my concatenateList(" ; ", perlSubstitutions)

    --Convert the input value
    try
        set conversionRate to (do shell script "units " & quoted form of inputUnits & space & quoted form of targetUnits)
        if conversionRate contains "conformability error" or conversionRate contains "unknown unit" then error conversionRate
        set conversionRate to do shell script "echo " & quoted form of first paragraph of conversionRate & " | perl -pe 's/^\\s*// ; s/^\\(-> x// ; s/^\\*(?!\\s)/\\* / ; s/\\)$//'"

        set convertedValue to inputValue & " * " & item 2 of my delimitText("* ", conversionRate)
        set convertedValue to (run script convertedValue) as text
        set convertedValue to do shell script "echo " & quoted form of convertedValue & " | perl -pe 's/(\\.\\d+)0*$/$1/ ; s/\\.$//'"
    on error errMsg
        return errMsg
    end try

    --Reformat certain target units to proper unit symbols
    set targetUnits to my findReplace("degC", "ºC", targetUnits)
    set targetUnits to my findReplace("degF", "ºF", targetUnits)
    set targetUnits to my findReplace({"milligrams", "milligram"}, "mg", targetUnits)
    set targetUnits to my findReplace({"grams", "gram"}, "g", targetUnits)
    set targetUnits to my findReplace({"litres", "liters", "litre", "liter"}, "l", targetUnits)
    set targetUnits to my findReplace({"hours", "hour"}, "h", targetUnits)

    return convertedValue & space & targetUnits
end convertUnits

on findReplace(findText, replaceText, sourceText)
    set ASTID to AppleScript's text item delimiters
    set AppleScript's text item delimiters to findText
    set sourceText to text items of sourceText
    set AppleScript's text item delimiters to replaceText
    set sourceText to sourceText as text
    set AppleScript's text item delimiters to ASTID
    return sourceText
end findReplace

on delimitText(delims, sourceText)
    set ASTID to AppleScript's text item delimiters
    set AppleScript's text item delimiters to delims
    set sourceText to text items of sourceText
    set AppleScript's text item delimiters to ASTID
    return sourceText
end delimitText

on concatenateList(delim, sourceText)
    set ASTID to AppleScript's text item delimiters
    set AppleScript's text item delimiters to delim
    set sourceText to sourceText as text
    set AppleScript's text item delimiters to ASTID
    return sourceText
end concatenateList
```
