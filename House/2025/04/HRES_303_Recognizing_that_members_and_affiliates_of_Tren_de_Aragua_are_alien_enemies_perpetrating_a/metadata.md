# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/303?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hres/303
- Title: Recognizing that members and affiliates of Tren de Aragua are alien enemies perpetrating an invasion of the United States and affirming that the President is exercising his constitutional authority to repel that invasion.
- Congress: 119
- Bill type: HRES
- Bill number: 303
- Origin chamber: House
- Introduced date: 2025-04-08
- Update date: 2025-04-09T14:28:33Z
- Update date including text: 2025-04-09T14:28:33Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-04-08: Introduced in House
- 2025-04-08 - IntroReferral: Referred to the House Committee on the Judiciary.
- 2025-04-08 - IntroReferral: Submitted in House
- 2025-04-08 - IntroReferral: Submitted in House
- Latest action: 2025-04-08: Submitted in House

## Actions

- 2025-04-08 - IntroReferral: Referred to the House Committee on the Judiciary.
- 2025-04-08 - IntroReferral: Submitted in House
- 2025-04-08 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-08",
    "latestAction": {
      "actionDate": "2025-04-08",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hres/303",
    "number": "303",
    "originChamber": "House",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "B001302",
        "district": "5",
        "firstName": "Andy",
        "fullName": "Rep. Biggs, Andy [R-AZ-5]",
        "lastName": "Biggs",
        "party": "R",
        "state": "AZ"
      }
    ],
    "title": "Recognizing that members and affiliates of Tren de Aragua are alien enemies perpetrating an invasion of the United States and affirming that the President is exercising his constitutional authority to repel that invasion.",
    "type": "HRES",
    "updateDate": "2025-04-09T14:28:33Z",
    "updateDateIncludingText": "2025-04-09T14:28:33Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-08",
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
      "actionDate": "2025-04-08",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-04-08",
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
          "date": "2025-04-08T14:03:15Z",
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
      "bioguideId": "R000614",
      "district": "21",
      "firstName": "Chip",
      "fullName": "Rep. Roy, Chip [R-TX-21]",
      "isOriginalCosponsor": "True",
      "lastName": "Roy",
      "party": "R",
      "sponsorshipDate": "2025-04-08",
      "state": "TX"
    },
    {
      "bioguideId": "H001077",
      "district": "3",
      "firstName": "Clay",
      "fullName": "Rep. Higgins, Clay [R-LA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Higgins",
      "party": "R",
      "sponsorshipDate": "2025-04-08",
      "state": "LA"
    },
    {
      "bioguideId": "O000175",
      "district": "5",
      "firstName": "Andrew",
      "fullName": "Rep. Ogles, Andrew [R-TN-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Ogles",
      "party": "R",
      "sponsorshipDate": "2025-04-08",
      "state": "TN"
    },
    {
      "bioguideId": "M001211",
      "district": "15",
      "firstName": "Mary",
      "fullName": "Rep. Miller, Mary E. [R-IL-15]",
      "isOriginalCosponsor": "True",
      "lastName": "Miller",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-04-08",
      "state": "IL"
    },
    {
      "bioguideId": "M001212",
      "district": "1",
      "firstName": "Barry",
      "fullName": "Rep. Moore, Barry [R-AL-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-04-08",
      "state": "AL"
    },
    {
      "bioguideId": "C001132",
      "district": "2",
      "firstName": "Elijah",
      "fullName": "Rep. Crane, Elijah [R-AZ-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Crane",
      "party": "R",
      "sponsorshipDate": "2025-04-08",
      "state": "AZ"
    },
    {
      "bioguideId": "T000165",
      "district": "7",
      "firstName": "Thomas",
      "fullName": "Rep. Tiffany, Thomas P. [R-WI-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Tiffany",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2025-04-08",
      "state": "WI"
    },
    {
      "bioguideId": "H001052",
      "district": "1",
      "firstName": "Andy",
      "fullName": "Rep. Harris, Andy [R-MD-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Harris",
      "party": "R",
      "sponsorshipDate": "2025-04-08",
      "state": "MD"
    },
    {
      "bioguideId": "B001317",
      "district": "2",
      "firstName": "Josh",
      "fullName": "Rep. Brecheen, Josh [R-OK-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Brecheen",
      "party": "R",
      "sponsorshipDate": "2025-04-08",
      "state": "OK"
    },
    {
      "bioguideId": "G000603",
      "district": "26",
      "firstName": "Brandon",
      "fullName": "Rep. Gill, Brandon [R-TX-26]",
      "isOriginalCosponsor": "True",
      "lastName": "Gill",
      "party": "R",
      "sponsorshipDate": "2025-04-08",
      "state": "TX"
    },
    {
      "bioguideId": "B001325",
      "district": "3",
      "firstName": "Sheri",
      "fullName": "Rep. Biggs, Sheri [R-SC-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Biggs",
      "party": "R",
      "sponsorshipDate": "2025-04-08",
      "state": "SC"
    },
    {
      "bioguideId": "C001115",
      "district": "27",
      "firstName": "Michael",
      "fullName": "Rep. Cloud, Michael [R-TX-27]",
      "isOriginalCosponsor": "True",
      "lastName": "Cloud",
      "party": "R",
      "sponsorshipDate": "2025-04-08",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres303ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 303\nIN THE HOUSE OF REPRESENTATIVES\nApril 8, 2025 Mr. Biggs of Arizona (for himself, Mr. Roy , Mr. Higgins of Louisiana , Mr. Ogles , Mrs. Miller of Illinois , Mr. Moore of Alabama , Mr. Crane , Mr. Tiffany , Mr. Harris of Maryland , Mr. Brecheen , Mr. Gill of Texas , Mrs. Biggs of South Carolina , and Mr. Cloud ) submitted the following resolution; which was referred to the Committee on the Judiciary\nRESOLUTION\nRecognizing that members and affiliates of Tren de Aragua are alien enemies perpetrating an invasion of the United States and affirming that the President is exercising his constitutional authority to repel that invasion.\nThat the House of Representatives\u2014\n**(1)**\nrecognizes that Tren de Aragua is a terrorist organization perpetrating an invasion of the United States directly and at the direction of a foreign government;\n**(2)**\nrecognizes that members and affiliates of Tren de Aragua are alien enemies; and\n**(3)**\nrecognizes and affirms that the President is exercising his Constitutional and legal authority to repel an invasion of alien enemies by apprehending, restraining, securing, and removing members and affiliates of Tren de Aragua from the United States of America.",
      "versionDate": "2025-04-08",
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
        "name": "Immigration",
        "updateDate": "2025-04-09T14:28:33Z"
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
      "date": "2025-04-08",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres303ih.xml"
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
      "title": "Recognizing that members and affiliates of Tren de Aragua are alien enemies perpetrating an invasion of the United States and affirming that the President is exercising his constitutional authority to repel that invasion.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-09T08:18:14Z"
    },
    {
      "title": "Recognizing that members and affiliates of Tren de Aragua are alien enemies perpetrating an invasion of the United States and affirming that the President is exercising his constitutional authority to repel that invasion.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-09T08:06:58Z"
    }
  ]
}
```
