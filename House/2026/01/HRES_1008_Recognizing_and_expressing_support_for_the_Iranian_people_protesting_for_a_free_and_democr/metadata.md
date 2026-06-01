# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/1008?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/1008
- Title: Recognizing and expressing support for the Iranian people protesting for a free and democratic Iran.
- Congress: 119
- Bill type: HRES
- Bill number: 1008
- Origin chamber: House
- Introduced date: 2026-01-16
- Update date: 2026-01-21T06:57:35Z
- Update date including text: 2026-01-21T06:57:35Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-01-16: Introduced in House
- 2026-01-16 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- 2026-01-16 - IntroReferral: Submitted in House
- 2026-01-16 - IntroReferral: Submitted in House
- Latest action: 2026-01-16: Submitted in House

## Actions

- 2026-01-16 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- 2026-01-16 - IntroReferral: Submitted in House
- 2026-01-16 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-16",
    "latestAction": {
      "actionDate": "2026-01-16",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/1008",
    "number": "1008",
    "originChamber": "House",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "A000381",
        "district": "3",
        "firstName": "Yassamin",
        "fullName": "Rep. Ansari, Yassamin [D-AZ-3]",
        "lastName": "Ansari",
        "party": "D",
        "state": "AZ"
      }
    ],
    "title": "Recognizing and expressing support for the Iranian people protesting for a free and democratic Iran.",
    "type": "HRES",
    "updateDate": "2026-01-21T06:57:35Z",
    "updateDateIncludingText": "2026-01-21T06:57:35Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-01-16",
      "committees": {
        "item": {
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Foreign Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-01-16",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2026-01-16",
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
          "date": "2026-01-16T20:00:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Foreign Affairs Committee",
      "systemCode": "hsfa00",
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
      "bioguideId": "F000450",
      "district": "5",
      "firstName": "Virginia",
      "fullName": "Rep. Foxx, Virginia [R-NC-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Foxx",
      "party": "R",
      "sponsorshipDate": "2026-01-16",
      "state": "NC"
    },
    {
      "bioguideId": "H001047",
      "district": "4",
      "firstName": "James",
      "fullName": "Rep. Himes, James A. [D-CT-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Himes",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2026-01-16",
      "state": "CT"
    },
    {
      "bioguideId": "B000740",
      "district": "5",
      "firstName": "Stephanie",
      "fullName": "Rep. Bice, Stephanie I. [R-OK-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Bice",
      "middleName": "I.",
      "party": "R",
      "sponsorshipDate": "2026-01-16",
      "state": "OK"
    },
    {
      "bioguideId": "S001190",
      "district": "10",
      "firstName": "Bradley",
      "fullName": "Rep. Schneider, Bradley Scott [D-IL-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Schneider",
      "middleName": "Scott",
      "party": "D",
      "sponsorshipDate": "2026-01-16",
      "state": "IL"
    },
    {
      "bioguideId": "C001126",
      "district": "15",
      "firstName": "Mike",
      "fullName": "Rep. Carey, Mike [R-OH-15]",
      "isOriginalCosponsor": "True",
      "lastName": "Carey",
      "party": "R",
      "sponsorshipDate": "2026-01-16",
      "state": "OH"
    },
    {
      "bioguideId": "S001201",
      "district": "3",
      "firstName": "Thomas",
      "fullName": "Rep. Suozzi, Thomas R. [D-NY-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Suozzi",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2026-01-16",
      "state": "NY"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2026-01-16",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1008ih.xml",
      "text": "IV\n119th CONGRESS\n2d Session\nH. RES. 1008\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 16, 2026 Ms. Ansari (for herself, Ms. Foxx , Mr. Himes , Mrs. Bice , Mr. Schneider , Mr. Carey , Mr. Suozzi , and Mr. Fitzpatrick ) submitted the following resolution; which was referred to the Committee on Foreign Affairs\nRESOLUTION\nRecognizing and expressing support for the Iranian people protesting for a free and democratic Iran.\nThat the House of Representatives\u2014\n**(1)**\ncommends the bravery and resolve of the Iranian people in their fight for a free and democratic Iran;\n**(2)**\nstrongly condemns the brutality of the Islamic Republic, which uses violent military force to suppress civilian protesters;\n**(3)**\ndemands that the Iranian regime cease its threats, intimidation, and violence against peaceful protesters, release all political prisoners, and allow unhindered medical assistance to demonstrators wounded by the regime\u2019s violent repression;\n**(4)**\nrecognizes the right of the Iranian people to freely determine, through free and fair elections, the nature of their political regime;\n**(5)**\nurges immediate expansion of unrestricted internet access and civilian lines of communication across Iran; and\n**(6)**\nimplores the Government of the United States to work in coordination with its allies to consider and implement concrete measures to deter further lethal violence against protesters.",
      "versionDate": "2026-01-16",
      "versionType": "IH"
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
        "actionDate": "2026-01-13",
        "text": "Referred to the House Committee on Foreign Affairs."
      },
      "number": "993",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Recognizing and expressing support for the Iranian people protesting for a free and democratic Iran.",
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
        "name": "International Affairs",
        "updateDate": "2026-01-20T16:36:37Z"
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
      "date": "2026-01-16",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1008ih.xml"
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
      "title": "Recognizing and expressing support for the Iranian people protesting for a free and democratic Iran.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-17T09:18:23Z"
    },
    {
      "title": "Recognizing and expressing support for the Iranian people protesting for a free and democratic Iran.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-17T09:06:04Z"
    }
  ]
}
```
