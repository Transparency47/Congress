# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/520?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/520
- Title: Recognizing the life, achievements, and public service of former First Lady Barbara Pierce Bush on the occasion of her 100th birthday.
- Congress: 119
- Bill type: HRES
- Bill number: 520
- Origin chamber: House
- Introduced date: 2025-06-17
- Update date: 2025-12-05T22:51:24Z
- Update date including text: 2025-12-05T22:51:24Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-06-17: Introduced in House
- 2025-06-17 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- 2025-06-17 - IntroReferral: Submitted in House
- 2025-06-17 - IntroReferral: Submitted in House
- Latest action: 2025-06-17: Submitted in House

## Actions

- 2025-06-17 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- 2025-06-17 - IntroReferral: Submitted in House
- 2025-06-17 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-17",
    "latestAction": {
      "actionDate": "2025-06-17",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/520",
    "number": "520",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "P000048",
        "district": "11",
        "firstName": "August",
        "fullName": "Rep. Pfluger, August [R-TX-11]",
        "lastName": "Pfluger",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "Recognizing the life, achievements, and public service of former First Lady Barbara Pierce Bush on the occasion of her 100th birthday.",
    "type": "HRES",
    "updateDate": "2025-12-05T22:51:24Z",
    "updateDateIncludingText": "2025-12-05T22:51:24Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-17",
      "committees": {
        "item": {
          "name": "Oversight and Government Reform Committee",
          "systemCode": "hsgo00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Oversight and Government Reform.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-17",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-06-17",
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
          "date": "2025-06-17T15:03:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Oversight and Government Reform Committee",
      "systemCode": "hsgo00",
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
      "bioguideId": "A000375",
      "district": "19",
      "firstName": "Jodey",
      "fullName": "Rep. Arrington, Jodey C. [R-TX-19]",
      "isOriginalCosponsor": "True",
      "lastName": "Arrington",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2025-06-17",
      "state": "TX"
    },
    {
      "bioguideId": "E000071",
      "district": "6",
      "firstName": "Jake",
      "fullName": "Rep. Ellzey, Jake [R-TX-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Ellzey",
      "party": "R",
      "sponsorshipDate": "2025-06-17",
      "state": "TX"
    },
    {
      "bioguideId": "G000589",
      "district": "5",
      "firstName": "Lance",
      "fullName": "Rep. Gooden, Lance [R-TX-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Gooden",
      "party": "R",
      "sponsorshipDate": "2025-06-17",
      "state": "TX"
    },
    {
      "bioguideId": "B001291",
      "district": "36",
      "firstName": "Brian",
      "fullName": "Rep. Babin, Brian [R-TX-36]",
      "isOriginalCosponsor": "True",
      "lastName": "Babin",
      "party": "R",
      "sponsorshipDate": "2025-06-17",
      "state": "TX"
    },
    {
      "bioguideId": "W000816",
      "district": "25",
      "firstName": "Roger",
      "fullName": "Rep. Williams, Roger [R-TX-25]",
      "isOriginalCosponsor": "True",
      "lastName": "Williams",
      "party": "R",
      "sponsorshipDate": "2025-06-17",
      "state": "TX"
    },
    {
      "bioguideId": "G000601",
      "district": "12",
      "firstName": "Craig",
      "fullName": "Rep. Goldman, Craig A. [R-TX-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Goldman",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-06-17",
      "state": "TX"
    },
    {
      "bioguideId": "W000814",
      "district": "14",
      "firstName": "Randy",
      "fullName": "Rep. Weber, Randy K. Sr. [R-TX-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Weber",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-06-17",
      "state": "TX"
    },
    {
      "bioguideId": "J000304",
      "district": "13",
      "firstName": "Ronny",
      "fullName": "Rep. Jackson, Ronny [R-TX-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Jackson",
      "party": "R",
      "sponsorshipDate": "2025-06-17",
      "state": "TX"
    },
    {
      "bioguideId": "B001298",
      "district": "2",
      "firstName": "Don",
      "fullName": "Rep. Bacon, Don [R-NE-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Bacon",
      "party": "R",
      "sponsorshipDate": "2025-06-17",
      "state": "NE"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2025-06-20",
      "state": "NY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres520ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 520\nIN THE HOUSE OF REPRESENTATIVES\nJune 17, 2025 Mr. Pfluger (for himself, Mr. Arrington , Mr. Ellzey , Mr. Gooden , Mr. Babin , Mr. Williams of Texas , Mr. Goldman of Texas , Mr. Weber of Texas , Mr. Jackson of Texas , and Mr. Bacon ) submitted the following resolution; which was referred to the Committee on Oversight and Government Reform\nRESOLUTION\nRecognizing the life, achievements, and public service of former First Lady Barbara Pierce Bush on the occasion of her 100th birthday.\nThat the House of Representatives\u2014\n**(1)**\nhonors the life, achievements, and distinguished public service of Barbara Pierce Bush (referred to in this resolution as Barbara Bush );\n**(2)**\nrecognizes Barbara Bush on the occasion of her 100th birthday and expresses thanks and commendations to her and her family;\n**(3)**\nacknowledges the positive impact that Barbara Bush contributed to the United States through her tireless dedication to promoting literacy and uplifting her fellow citizens; and\n**(4)**\ncelebrates the legacy of Barbara Bush as a model citizen and public servant of the United States.",
      "versionDate": "2025-06-17",
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
        "actionDate": "2025-06-06",
        "text": "Referred to the House Committee on Oversight and Government Reform."
      },
      "number": "36",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Recognizing the life, achievements, and public service of former First Lady Barbara Pierce Bush on the occasion of her 100th birthday.",
      "type": "HCONRES"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-06-17",
        "text": "Submitted in the Senate, considered, and agreed to without amendment and with a preamble by Unanimous Consent. (consideration: CR S3442; text: CR S3441-3442)"
      },
      "number": "286",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "A resolution recognizing the life, achievements, and public service of former First Lady Barbara Pierce Bush on the occasion of her 100th birthday.",
      "type": "SRES"
    }
  ]
}
```

## API Data: subjects

```json
{
  "subjects": [
    {
      "legislativeSubjects": {
        "item": [
          {
            "name": "Commemorative events and holidays",
            "updateDate": "2025-07-22T19:39:02Z"
          },
          {
            "name": "Congressional tributes",
            "updateDate": "2025-07-22T19:39:02Z"
          },
          {
            "name": "Presidents and presidential powers, Vice Presidents",
            "updateDate": "2025-07-22T19:39:02Z"
          },
          {
            "name": "U.S. history",
            "updateDate": "2025-07-22T19:39:02Z"
          }
        ]
      },
      "policyArea": {
        "name": "Government Operations and Politics",
        "updateDate": "2025-07-22T12:15:25Z"
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
      "date": "2025-06-17",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres520ih.xml"
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
      "title": "Recognizing the life, achievements, and public service of former First Lady Barbara Pierce Bush on the occasion of her 100th birthday.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-18T08:18:20Z"
    },
    {
      "title": "Recognizing the life, achievements, and public service of former First Lady Barbara Pierce Bush on the occasion of her 100th birthday.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-18T08:05:35Z"
    }
  ]
}
```
