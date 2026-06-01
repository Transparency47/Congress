# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/612?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/612
- Title: Celebrating 250 years of Army Medicine.
- Congress: 119
- Bill type: HRES
- Bill number: 612
- Origin chamber: House
- Introduced date: 2025-07-25
- Update date: 2025-09-19T17:41:36Z
- Update date including text: 2025-09-19T17:41:36Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-07-25: Introduced in House
- 2025-07-25 - IntroReferral: Referred to the House Committee on Armed Services.
- 2025-07-25 - IntroReferral: Submitted in House
- 2025-07-25 - IntroReferral: Submitted in House
- Latest action: 2025-07-25: Submitted in House

## Actions

- 2025-07-25 - IntroReferral: Referred to the House Committee on Armed Services.
- 2025-07-25 - IntroReferral: Submitted in House
- 2025-07-25 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-25",
    "latestAction": {
      "actionDate": "2025-07-25",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/612",
    "number": "612",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "M001199",
        "district": "21",
        "firstName": "Brian",
        "fullName": "Rep. Mast, Brian J. [R-FL-21]",
        "lastName": "Mast",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "Celebrating 250 years of Army Medicine.",
    "type": "HRES",
    "updateDate": "2025-09-19T17:41:36Z",
    "updateDateIncludingText": "2025-09-19T17:41:36Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-25",
      "committees": {
        "item": {
          "name": "Armed Services Committee",
          "systemCode": "hsas00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Armed Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-25",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-07-25",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
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
          "date": "2025-07-25T15:01:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Armed Services Committee",
      "systemCode": "hsas00",
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
      "bioguideId": "C001051",
      "district": "31",
      "firstName": "John",
      "fullName": "Rep. Carter, John R. [R-TX-31]",
      "isOriginalCosponsor": "True",
      "lastName": "Carter",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-07-25",
      "state": "TX"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres612ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 612\nIN THE HOUSE OF REPRESENTATIVES\nJuly 25, 2025 Mr. Mast (for himself and Mr. Carter of Texas ) submitted the following resolution; which was referred to the Committee on Armed Services\nRESOLUTION\nCelebrating 250 years of Army Medicine.\nThat the House of Representatives\u2014\n**(1)**\ngathers to commemorate the 250th anniversary of the Army Medical Department, a beacon of unwavering dedication, innovation, and selfless service to the brave men and women of the United States Army;\n**(2)**\nexpresses its profound gratitude to the Army Medical Department for their\u2014\n**(A)**\nunwavering commitment to the health and well-being of United States soldiers, past and present;\n**(B)**\nlegacy of service, sacrifice, and innovation which continues to inspire; and\n**(C)**\ndedication that ensures that the United States Army remains the most ready and capable fighting force in the world; and\n**(3)**\nremembers and honors the countless lives saved and forever changed by the compassionate care of Army Medicine.",
      "versionDate": "2025-07-25",
      "versionType": "IH"
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
        "updateDate": "2025-09-19T17:41:36Z"
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
      "date": "2025-07-25",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres612ih.xml"
        }
      ],
      "type": "IH"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Celebrating 250 years of Army Medicine.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-26T08:18:30Z"
    },
    {
      "title": "Celebrating 250 years of Army Medicine.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-26T08:05:35Z"
    }
  ]
}
```
