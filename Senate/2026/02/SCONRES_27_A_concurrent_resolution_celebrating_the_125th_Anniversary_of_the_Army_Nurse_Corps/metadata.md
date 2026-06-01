# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sconres/27?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-concurrent-resolution/27
- Title: A concurrent resolution celebrating the 125th Anniversary of the Army Nurse Corps.
- Congress: 119
- Bill type: SCONRES
- Bill number: 27
- Origin chamber: Senate
- Introduced date: 2026-02-12
- Update date: 2026-02-17T18:17:40Z
- Update date including text: 2026-02-17T18:17:40Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-02-12: Introduced in Senate
- 2026-02-12 - IntroReferral: Referred to the Committee on Armed Services.
- 2026-02-12 - IntroReferral: Submitted in Senate
- Latest action: 2026-02-12: Submitted in Senate

## Actions

- 2026-02-12 - IntroReferral: Referred to the Committee on Armed Services.
- 2026-02-12 - IntroReferral: Submitted in Senate

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-12",
    "latestAction": {
      "actionDate": "2026-02-12",
      "text": "Submitted in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-concurrent-resolution/27",
    "number": "27",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "W000437",
        "district": "",
        "firstName": "Roger",
        "fullName": "Sen. Wicker, Roger F. [R-MS]",
        "lastName": "Wicker",
        "party": "R",
        "state": "MS"
      }
    ],
    "title": "A concurrent resolution celebrating the 125th Anniversary of the Army Nurse Corps.",
    "type": "SCONRES",
    "updateDate": "2026-02-17T18:17:40Z",
    "updateDateIncludingText": "2026-02-17T18:17:40Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-02-12",
      "committees": {
        "item": {
          "name": "Armed Services Committee",
          "systemCode": "ssas00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Referred to the Committee on Armed Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10025",
      "actionDate": "2026-02-12",
      "committees": {
        "item": {
          "name": "Armed Services Committee",
          "systemCode": "ssas00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in Senate",
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
          "date": "2026-02-12T18:37:01Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Armed Services Committee",
      "systemCode": "ssas00",
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
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2026-02-12",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/sconres/BILLS-119sconres27is.xml",
      "text": "III\n119th CONGRESS\n2d Session\nS. CON. RES. 27\nIN THE SENATE OF THE UNITED STATES\nFebruary 12, 2026 Mr. Wicker (for himself and Mr. Merkley ) submitted the following concurrent resolution; which was referred to the Committee on Armed Services\nCONCURRENT RESOLUTION\nCelebrating the 125th Anniversary of the Army Nurse Corps.\nThat Congress\u2014\n**(1)**\npays tribute to the Army Nurse Corps;\n**(2)**\nrecognizes their 125th anniversary on the 2nd day of February 2026;\n**(3)**\nexpresses profound gratitude for their unwavering commitment to the health care and well-being of our soldiers;\n**(4)**\ncommends the unwavering steadfast dedication, skill, and sacrifice of Army nurses throughout history and their continuous vital contributions to the health and well-being of our service members; and\n**(5)**\nexpresses profound gratitude to all past and present members of the Army Nurse Corps for their selfless service to the Nation.",
      "versionDate": "2026-02-12",
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
        "name": "Armed Forces and National Security",
        "updateDate": "2026-02-17T18:17:40Z"
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
      "date": "2026-02-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/sconres/BILLS-119sconres27is.xml"
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
      "title": "A concurrent resolution celebrating the 125th Anniversary of the Army Nurse Corps.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-14T04:33:25Z"
    },
    {
      "title": "A concurrent resolution celebrating the 125th Anniversary of the Army Nurse Corps.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-13T11:56:25Z"
    }
  ]
}
```
