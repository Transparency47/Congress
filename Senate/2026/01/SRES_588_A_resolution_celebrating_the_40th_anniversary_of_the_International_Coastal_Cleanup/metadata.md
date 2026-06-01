# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/588?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-resolution/588
- Title: A resolution celebrating the 40th anniversary of the International Coastal Cleanup.
- Congress: 119
- Bill type: SRES
- Bill number: 588
- Origin chamber: Senate
- Introduced date: 2026-01-27
- Update date: 2026-02-03T17:57:15Z
- Update date including text: 2026-02-03T17:57:15Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-01-27: Introduced in Senate
- 2026-01-27 - IntroReferral: Introduced in Senate
- 2026-01-27 - IntroReferral: Referred to the Committee on Commerce, Science, and Transportation. (text: CR S294)
- Latest action: 2026-01-27: Introduced in Senate

## Actions

- 2026-01-27 - IntroReferral: Introduced in Senate
- 2026-01-27 - IntroReferral: Referred to the Committee on Commerce, Science, and Transportation. (text: CR S294)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-27",
    "latestAction": {
      "actionDate": "2026-01-27",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-resolution/588",
    "number": "588",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Public Lands and Natural Resources"
    },
    "sponsors": [
      {
        "bioguideId": "V000128",
        "district": "",
        "firstName": "Chris",
        "fullName": "Sen. Van Hollen, Chris [D-MD]",
        "lastName": "Van Hollen",
        "party": "D",
        "state": "MD"
      }
    ],
    "title": "A resolution celebrating the 40th anniversary of the International Coastal Cleanup.",
    "type": "SRES",
    "updateDate": "2026-02-03T17:57:15Z",
    "updateDateIncludingText": "2026-02-03T17:57:15Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-01-27",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Referred to the Committee on Commerce, Science, and Transportation. (text: CR S294)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-01-27",
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
          "date": "2026-01-27T22:43:33Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Commerce, Science, and Transportation Committee",
      "systemCode": "sscm00",
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
      "bioguideId": "A000382",
      "firstName": "Angela",
      "fullName": "Sen. Alsobrooks, Angela D. [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Alsobrooks",
      "party": "D",
      "sponsorshipDate": "2026-01-27",
      "state": "MD"
    },
    {
      "bioguideId": "B001303",
      "firstName": "Lisa",
      "fullName": "Sen. Blunt Rochester, Lisa [D-DE]",
      "isOriginalCosponsor": "True",
      "lastName": "Blunt Rochester",
      "party": "D",
      "sponsorshipDate": "2026-01-27",
      "state": "DE"
    },
    {
      "bioguideId": "H001046",
      "firstName": "Martin",
      "fullName": "Sen. Heinrich, Martin [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Heinrich",
      "party": "D",
      "sponsorshipDate": "2026-01-27",
      "state": "NM"
    },
    {
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2026-01-27",
      "state": "OR"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/sres/BILLS-119sres588is.xml",
      "text": "III\n119th CONGRESS\n2d Session\nS. RES. 588\nIN THE SENATE OF THE UNITED STATES\nJanuary 27, 2026 Mr. Van Hollen (for himself, Ms. Alsobrooks , Ms. Blunt Rochester , Mr. Heinrich , and Mr. Merkley ) submitted the following resolution; which was referred to the Committee on Commerce, Science, and Transportation\nRESOLUTION\nCelebrating the 40th anniversary of the International Coastal Cleanup.\nThat the Senate\u2014\n**(1)**\ncelebrates 2025 as the 40th anniversary of the International Coastal Cleanup;\n**(2)**\nsupports the goals and ambitions of the International Coastal Cleanup;\n**(3)**\nencourages the people of the United States to participate in International Coastal Cleanup activities; and\n**(4)**\nhighlights the importance of reducing plastic pollution and addressing the problem at its source by producing less plastics.",
      "versionDate": "2026-01-27",
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
        "name": "Public Lands and Natural Resources",
        "updateDate": "2026-02-03T17:57:15Z"
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
      "date": "2026-01-27",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/sres/BILLS-119sres588is.xml"
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
      "title": "A resolution celebrating the 40th anniversary of the International Coastal Cleanup.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-30T04:03:25Z"
    },
    {
      "title": "A resolution celebrating the 40th anniversary of the International Coastal Cleanup.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-28T11:56:19Z"
    }
  ]
}
```
