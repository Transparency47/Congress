# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/540?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-resolution/540
- Title: A resolution recognizing Human Rights Day on December 10, 2025, and commemorating the 77th anniversary of the Universal Declaration of Human Rights and the Celebration of "Human Rights Day".
- Congress: 119
- Bill type: SRES
- Bill number: 540
- Origin chamber: Senate
- Introduced date: 2025-12-10
- Update date: 2025-12-15T18:30:53Z
- Update date including text: 2025-12-15T18:30:53Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-10: Introduced in Senate
- 2025-12-10 - IntroReferral: Introduced in Senate
- 2025-12-10 - IntroReferral: Referred to the Committee on the Judiciary. (text: CR S8627)
- Latest action: 2025-12-10: Introduced in Senate

## Actions

- 2025-12-10 - IntroReferral: Introduced in Senate
- 2025-12-10 - IntroReferral: Referred to the Committee on the Judiciary. (text: CR S8627)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-10",
    "latestAction": {
      "actionDate": "2025-12-10",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-resolution/540",
    "number": "540",
    "originChamber": "Senate",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "C001088",
        "district": "",
        "firstName": "Christopher",
        "fullName": "Sen. Coons, Christopher A. [D-DE]",
        "lastName": "Coons",
        "party": "D",
        "state": "DE"
      }
    ],
    "title": "A resolution recognizing Human Rights Day on December 10, 2025, and commemorating the 77th anniversary of the Universal Declaration of Human Rights and the Celebration of \"Human Rights Day\".",
    "type": "SRES",
    "updateDate": "2025-12-15T18:30:53Z",
    "updateDateIncludingText": "2025-12-15T18:30:53Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-10",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Referred to the Committee on the Judiciary. (text: CR S8627)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-12-10",
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
          "date": "2025-12-10T18:34:43Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Judiciary Committee",
      "systemCode": "ssju00",
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
      "bioguideId": "T000476",
      "firstName": "Thomas",
      "fullName": "Sen. Tillis, Thomas [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Tillis",
      "middleName": "Roland",
      "party": "R",
      "sponsorshipDate": "2025-12-10",
      "state": "NC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres540is.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 540\nIN THE SENATE OF THE UNITED STATES\nDecember 10, 2025 Mr. Coons (for himself and Mr. Tillis ) submitted the following resolution; which was referred to the Committee on the Judiciary\nRESOLUTION\nRecognizing Human Rights Day on December 10, 2025, and commemorating the 77th anniversary of the Universal Declaration of Human Rights and the Celebration of Human Rights Day .\nThat the Senate\u2014\n**(1)**\ndesignates December 10, 2025, as Human Rights Day and recognizes its global significance;\n**(2)**\nrecognizes the 77th anniversary of the Universal Declaration of Human Rights;\n**(3)**\nreaffirms the Universal Declaration of Human Rights;\n**(4)**\nsupports the work of civil society leaders and human rights defenders globally;\n**(5)**\ncondemns the use of political imprisonment as a tool of repression to restrict civil liberties and human rights;\n**(6)**\ncalls upon governments around the world to immediately and unconditionally release political prisoners who are being unjustly detained for advocating for human rights and civil society; and\n**(7)**\nencourages the people of the United States\u2014\n**(A)**\nto observe Human Rights Day ; and\n**(B)**\nto continue their commitment to upholding freedom, democracy, and human rights around the world.",
      "versionDate": "2025-12-10",
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
        "updateDate": "2025-12-15T18:30:53Z"
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
      "date": "2025-12-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres540is.xml"
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
      "title": "A resolution recognizing Human Rights Day on December 10, 2025, and commemorating the 77th anniversary of the Universal Declaration of Human Rights and the Celebration of \"Human Rights Day\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-13T03:18:25Z"
    },
    {
      "title": "A resolution recognizing Human Rights Day on December 10, 2025, and commemorating the 77th anniversary of the Universal Declaration of Human Rights and the Celebration of \"Human Rights Day\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-11T11:56:17Z"
    }
  ]
}
```
