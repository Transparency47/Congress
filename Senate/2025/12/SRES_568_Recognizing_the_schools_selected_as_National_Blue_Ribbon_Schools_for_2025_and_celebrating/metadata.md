# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/568?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-resolution/568
- Title: A resolution recognizing the schools selected as National Blue Ribbon Schools for 2025 and celebrating the history of the Blue Ribbon Schools Program.
- Congress: 119
- Bill type: SRES
- Bill number: 568
- Origin chamber: Senate
- Introduced date: 2025-12-18
- Update date: 2026-01-06T18:58:23Z
- Update date including text: 2026-01-06T18:58:23Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-12-18: Introduced in Senate
- 2025-12-18 - IntroReferral: Introduced in Senate
- 2025-12-18 - IntroReferral: Referred to the Committee on Health, Education, Labor, and Pensions. (text: CR S8924)
- Latest action: 2025-12-18: Introduced in Senate

## Actions

- 2025-12-18 - IntroReferral: Introduced in Senate
- 2025-12-18 - IntroReferral: Referred to the Committee on Health, Education, Labor, and Pensions. (text: CR S8924)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-18",
    "latestAction": {
      "actionDate": "2025-12-18",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-resolution/568",
    "number": "568",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Education"
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
    "title": "A resolution recognizing the schools selected as National Blue Ribbon Schools for 2025 and celebrating the history of the Blue Ribbon Schools Program.",
    "type": "SRES",
    "updateDate": "2026-01-06T18:58:23Z",
    "updateDateIncludingText": "2026-01-06T18:58:23Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-18",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Referred to the Committee on Health, Education, Labor, and Pensions. (text: CR S8924)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-12-18",
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
          "date": "2025-12-18T18:24:27Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Health, Education, Labor, and Pensions Committee",
      "systemCode": "sshr00",
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
      "bioguideId": "D000622",
      "firstName": "Tammy",
      "fullName": "Sen. Duckworth, Tammy [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Duckworth",
      "party": "D",
      "sponsorshipDate": "2025-12-18",
      "state": "IL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres568is.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 568\nIN THE SENATE OF THE UNITED STATES\nDecember 18, 2025 Mr. Durbin (for himself and Ms. Duckworth ) submitted the following resolution; which was referred to the Committee on Health, Education, Labor, and Pensions\nRESOLUTION\nRecognizing the schools selected as National Blue Ribbon Schools for 2025 and celebrating the history of the Blue Ribbon Schools Program.\nThat the Senate\u2014\n**(1)**\nrecognizes and celebrates\u2014\n**(A)**\nthe schools selected to be 2025 National Blue Ribbon Schools before the Blue Ribbon Schools program was discontinued; and\n**(B)**\nthe history of the Blue Ribbon Schools program;\n**(2)**\ncommends the educators, school administrators, and communities of such schools for their hard work that led to this achievement; and\n**(3)**\ncalls upon the Secretary of Education to immediately reinstate the Blue Ribbon Schools program.",
      "versionDate": "2025-12-18",
      "versionType": "IS"
    }
  ]
}
```

## API Data: relatedbills

```json
{
  "relatedBills": [
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-12-18",
        "text": "Referred to the House Committee on Education and Workforce."
      },
      "number": "961",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Recognizing the schools selected as National Blue Ribbon Schools for 2025 and celebrating the history of the Blue Ribbon Schools Program.",
      "type": "HRES"
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
        "name": "Education",
        "updateDate": "2026-01-06T18:58:23Z"
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
      "date": "2025-12-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres568is.xml"
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
      "title": "A resolution recognizing the schools selected as National Blue Ribbon Schools for 2025 and celebrating the history of the Blue Ribbon Schools Program.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-20T05:48:17Z"
    },
    {
      "title": "A resolution recognizing the schools selected as National Blue Ribbon Schools for 2025 and celebrating the history of the Blue Ribbon Schools Program.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-19T11:56:22Z"
    }
  ]
}
```
