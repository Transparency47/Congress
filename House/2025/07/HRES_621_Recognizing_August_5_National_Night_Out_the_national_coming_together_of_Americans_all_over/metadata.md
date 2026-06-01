# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/621?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/621
- Title: Recognizing August 5, National Night Out, the national coming together of Americans all over the Nation to unite and promote public safety.
- Congress: 119
- Bill type: HRES
- Bill number: 621
- Origin chamber: House
- Introduced date: 2025-07-29
- Update date: 2025-09-09T14:06:55Z
- Update date including text: 2025-09-09T14:06:55Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-07-29: Introduced in House
- 2025-07-29 - IntroReferral: Referred to the House Committee on the Judiciary.
- 2025-07-29 - IntroReferral: Submitted in House
- 2025-07-29 - IntroReferral: Submitted in House
- Latest action: 2025-07-29: Submitted in House

## Actions

- 2025-07-29 - IntroReferral: Referred to the House Committee on the Judiciary.
- 2025-07-29 - IntroReferral: Submitted in House
- 2025-07-29 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-29",
    "latestAction": {
      "actionDate": "2025-07-29",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/621",
    "number": "621",
    "originChamber": "House",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "T000474",
        "district": "35",
        "firstName": "Norma",
        "fullName": "Rep. Torres, Norma J. [D-CA-35]",
        "lastName": "Torres",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Recognizing August 5, National Night Out, the national coming together of Americans all over the Nation to unite and promote public safety.",
    "type": "HRES",
    "updateDate": "2025-09-09T14:06:55Z",
    "updateDateIncludingText": "2025-09-09T14:06:55Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-29",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-29",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-07-29",
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
          "date": "2025-07-29T21:06:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
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
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-07-29",
      "state": "PA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres621ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 621\nIN THE HOUSE OF REPRESENTATIVES\nJuly 29, 2025 Mrs. Torres of California (for herself and Mr. Fitzpatrick ) submitted the following resolution; which was referred to the Committee on the Judiciary\nRESOLUTION\nRecognizing August 5, National Night Out, the national coming together of Americans all over the Nation to unite and promote public safety.\nThat the House of Representatives\u2014\n**(1)**\nencourages law enforcement departments to use National Night Out to improve relationships with the communities they serve;\n**(2)**\nencourages public safety departments to inform communities\u2014\n**(A)**\nhow to most effectively contact their 911 responders and emergency service providers; and\n**(B)**\nhow they carry out their duties; and\n**(3)**\nrecognizes the impact that has been made for over 40 years in communities all over the United States of America by National Night Out in creating a more united country by fostering relationships between residents, neighbors, and local law enforcement, and promoting public safety awareness.",
      "versionDate": "2025-07-29",
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
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-09-09T14:06:55Z"
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
      "date": "2025-07-29",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres621ih.xml"
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
      "title": "Recognizing August 5, National Night Out, the national coming together of Americans all over the Nation to unite and promote public safety.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-30T13:03:25Z"
    },
    {
      "title": "Recognizing August 5, National Night Out, the national coming together of Americans all over the Nation to unite and promote public safety.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-30T12:51:51Z"
    }
  ]
}
```
