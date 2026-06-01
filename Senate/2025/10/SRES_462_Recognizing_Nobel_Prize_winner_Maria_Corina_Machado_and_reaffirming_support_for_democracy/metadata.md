# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/462?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-resolution/462
- Title: A resolution recognizing Nobel Prize winner Maria Corina Machado and reaffirming support for democracy in Venezuela.
- Congress: 119
- Bill type: SRES
- Bill number: 462
- Origin chamber: Senate
- Introduced date: 2025-10-22
- Update date: 2025-11-24T20:32:48Z
- Update date including text: 2025-11-24T20:32:48Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-10-22: Introduced in Senate
- 2025-10-22 - IntroReferral: Introduced in Senate
- 2025-10-22 - IntroReferral: Referred to the Committee on Foreign Relations. (text: CR S7700)
- Latest action: 2025-10-22: Introduced in Senate

## Actions

- 2025-10-22 - IntroReferral: Introduced in Senate
- 2025-10-22 - IntroReferral: Referred to the Committee on Foreign Relations. (text: CR S7700)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-10-22",
    "latestAction": {
      "actionDate": "2025-10-22",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-resolution/462",
    "number": "462",
    "originChamber": "Senate",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "D000563",
        "district": "",
        "firstName": "Richard",
        "fullName": "Sen. Durbin, Richard J. [D-IL]",
        "lastName": "Durbin",
        "party": "D",
        "state": "IL"
      }
    ],
    "title": "A resolution recognizing Nobel Prize winner Maria Corina Machado and reaffirming support for democracy in Venezuela.",
    "type": "SRES",
    "updateDate": "2025-11-24T20:32:48Z",
    "updateDateIncludingText": "2025-11-24T20:32:48Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-10-22",
      "committees": {
        "item": {
          "name": "Foreign Relations Committee",
          "systemCode": "ssfr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Referred to the Committee on Foreign Relations. (text: CR S7700)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-10-22",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in Senate",
      "type": "IntroReferral"
    }
  ]
}
```

## API Data: committees

```json
{
  "committees": [
    {
      "activities": {
        "item": {
          "date": "2025-10-22T21:54:47Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Foreign Relations Committee",
      "systemCode": "ssfr00",
      "type": "Standing"
    }
  ]
}
```

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "S001217",
      "firstName": "Rick",
      "fullName": "Sen. Scott, Rick [R-FL]",
      "isOriginalCosponsor": "True",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-10-22",
      "state": "FL"
    },
    {
      "bioguideId": "S001181",
      "firstName": "Jeanne",
      "fullName": "Sen. Shaheen, Jeanne [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Shaheen",
      "party": "D",
      "sponsorshipDate": "2025-10-22",
      "state": "NH"
    },
    {
      "bioguideId": "C001098",
      "firstName": "Ted",
      "fullName": "Sen. Cruz, Ted [R-TX]",
      "isOriginalCosponsor": "True",
      "lastName": "Cruz",
      "party": "R",
      "sponsorshipDate": "2025-10-22",
      "state": "TX"
    },
    {
      "bioguideId": "G000574",
      "firstName": "Ruben",
      "fullName": "Sen. Gallego, Ruben [D-AZ]",
      "isOriginalCosponsor": "True",
      "lastName": "Gallego",
      "party": "D",
      "sponsorshipDate": "2025-10-22",
      "state": "AZ"
    },
    {
      "bioguideId": "B001267",
      "firstName": "Michael",
      "fullName": "Sen. Bennet, Michael F. [D-CO]",
      "isOriginalCosponsor": "True",
      "lastName": "Bennet",
      "party": "D",
      "sponsorshipDate": "2025-10-22",
      "state": "CO"
    }
  ]
}
```

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres462is.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 462\nIN THE SENATE OF THE UNITED STATES\nOctober 22 (legislative day, October 21), 2025 Mr. Durbin (for himself, Mr. Scott of Florida , Mrs. Shaheen , Mr. Cruz , Mr. Gallego , and Mr. Bennet ) submitted the following resolution; which was referred to the Committee on Foreign Relations\nRESOLUTION\nRecognizing Nobel Prize winner Mar\u00eda Corina Machado and reaffirming support for democracy in Venezuela.\nThat the Senate\u2014\n**(1)**\ncommends Mar\u00eda Corina Machado for her peaceful and determined effort to see a free and democratic Venezuela;\n**(2)**\ncongratulates Mar\u00eda Corina Machado for winning the Nobel Peace Prize;\n**(3)**\ndemands the Maduro regime ensure her safety and release her colleagues and other political prisoners from detention;\n**(4)**\nrecognizes the legitimate results of the July 2024 Venezuelan election won by Edmundo Gonz\u00e1lez and expects the Maduro regime to also recognize those results without any further delay; and\n**(5)**\nsupports the aspirations of the Venezuelan people to reverse the country\u2019s tragic decline by freely and democratically choosing their leaders.",
      "versionDate": "2025-10-22",
      "versionType": "IS"
    }
  ]
}
```

## API Data: subjects

```json
{
  "subjects": [
    {
      "legislativeSubjects": "",
      "policyArea": {
        "name": "International Affairs",
        "updateDate": "2025-11-20T17:21:32Z"
      }
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-10-22",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres462is.xml"
        }
      ],
      "type": "IS"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A resolution recognizing Nobel Prize winner Maria Corina Machado and reaffirming support for democracy in Venezuela.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-24T02:03:15Z"
    },
    {
      "title": "A resolution recognizing Nobel Prize winner Maria Corina Machado and reaffirming support for democracy in Venezuela.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-23T10:56:19Z"
    }
  ]
}
```
