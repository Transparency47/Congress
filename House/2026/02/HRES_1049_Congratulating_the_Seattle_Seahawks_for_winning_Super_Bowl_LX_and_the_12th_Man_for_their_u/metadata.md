# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/1049?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/1049
- Title: Congratulating the Seattle Seahawks for winning Super Bowl LX and the 12th Man for their unwavering support.
- Congress: 119
- Bill type: HRES
- Bill number: 1049
- Origin chamber: House
- Introduced date: 2026-02-10
- Update date: 2026-02-13T17:57:52Z
- Update date including text: 2026-02-13T17:57:52Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-02-10: Introduced in House
- 2026-02-10 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- 2026-02-10 - IntroReferral: Submitted in House
- 2026-02-10 - IntroReferral: Submitted in House
- Latest action: 2026-02-10: Submitted in House

## Actions

- 2026-02-10 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- 2026-02-10 - IntroReferral: Submitted in House
- 2026-02-10 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-10",
    "latestAction": {
      "actionDate": "2026-02-10",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/1049",
    "number": "1049",
    "originChamber": "House",
    "policyArea": {
      "name": "Sports and Recreation"
    },
    "sponsors": [
      {
        "bioguideId": "D000617",
        "district": "1",
        "firstName": "Suzan",
        "fullName": "Rep. DelBene, Suzan K. [D-WA-1]",
        "lastName": "DelBene",
        "party": "D",
        "state": "WA"
      }
    ],
    "title": "Congratulating the Seattle Seahawks for winning Super Bowl LX and the 12th Man for their unwavering support.",
    "type": "HRES",
    "updateDate": "2026-02-13T17:57:52Z",
    "updateDateIncludingText": "2026-02-13T17:57:52Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-02-10",
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
      "actionDate": "2026-02-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2026-02-10",
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
          "date": "2026-02-10T15:02:25Z",
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
      "bioguideId": "J000298",
      "district": "7",
      "firstName": "Pramila",
      "fullName": "Rep. Jayapal, Pramila [D-WA-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Jayapal",
      "party": "D",
      "sponsorshipDate": "2026-02-10",
      "state": "WA"
    },
    {
      "bioguideId": "L000560",
      "district": "2",
      "firstName": "Rick",
      "fullName": "Rep. Larsen, Rick [D-WA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Larsen",
      "party": "D",
      "sponsorshipDate": "2026-02-10",
      "state": "WA"
    },
    {
      "bioguideId": "G000600",
      "district": "3",
      "firstName": "Marie",
      "fullName": "Rep. Perez, Marie Gluesenkamp [D-WA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Perez",
      "middleName": "Gluesenkamp",
      "party": "D",
      "sponsorshipDate": "2026-02-10",
      "state": "WA"
    },
    {
      "bioguideId": "N000189",
      "district": "4",
      "firstName": "Dan",
      "fullName": "Rep. Newhouse, Dan [R-WA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Newhouse",
      "party": "R",
      "sponsorshipDate": "2026-02-10",
      "state": "WA"
    },
    {
      "bioguideId": "R000621",
      "district": "6",
      "firstName": "Emily",
      "fullName": "Rep. Randall, Emily [D-WA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Randall",
      "party": "D",
      "sponsorshipDate": "2026-02-10",
      "state": "WA"
    },
    {
      "bioguideId": "S001216",
      "district": "8",
      "firstName": "Kim",
      "fullName": "Rep. Schrier, Kim [D-WA-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Schrier",
      "party": "D",
      "sponsorshipDate": "2026-02-10",
      "state": "WA"
    },
    {
      "bioguideId": "S000510",
      "district": "9",
      "firstName": "Adam",
      "fullName": "Rep. Smith, Adam [D-WA-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2026-02-10",
      "state": "WA"
    },
    {
      "bioguideId": "S001159",
      "district": "10",
      "firstName": "Marilyn",
      "fullName": "Rep. Strickland, Marilyn [D-WA-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Strickland",
      "party": "D",
      "sponsorshipDate": "2026-02-10",
      "state": "WA"
    },
    {
      "bioguideId": "B001322",
      "district": "5",
      "firstName": "Michael",
      "fullName": "Rep. Baumgartner, Michael [R-WA-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Baumgartner",
      "party": "R",
      "sponsorshipDate": "2026-02-10",
      "state": "WA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1049ih.xml",
      "text": "IV\n119th CONGRESS\n2d Session\nH. RES. 1049\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 10, 2026 Ms. DelBene (for herself, Ms. Jayapal , Mr. Larsen of Washington , Ms. Perez , Mr. Newhouse , Ms. Randall , Ms. Schrier , Mr. Smith of Washington , Ms. Strickland , and Mr. Baumgartner ) submitted the following resolution; which was referred to the Committee on Oversight and Government Reform\nRESOLUTION\nCongratulating the Seattle Seahawks for winning Super Bowl LX and the 12th Man for their unwavering support.\nThat the House of Representatives\u2014\n**(1)**\nCongratulates\u2014\n**(A)**\nthe Seattle Seahawks for their triumphant victory in Super Bowl LX and acknowledges the exceptional performances of players, coaches, and support staff;\n**(B)**\nSeahawks Chair Jody Allen;\n**(C)**\nSeahawks President Chuck Arnold;\n**(D)**\nSeahawks President of Football Operations/General Manager John Schneider; and\n**(E)**\nSeahawks Head Coach Mike Macdonald;\n**(2)**\nRecognizes Kenneth Walker III for his MVP performance and historic impact on the game;\n**(3)**\nCommends Jason Myers for his record-breaking five field goals and outstanding scoring achievement;\n**(4)**\nSalutes the Seahawks' defense for its dominance, resilience, and pivotal role in securing the championship;\n**(5)**\nCelebrates the Seahawks 12th Man, for being the most loyal and loudest sports fans in the world; and\n**(6)**\nRequests that the Clerk of the House transmit an enrolled copy of this resolution to\u2014\n**(A)**\nSeahawks Chair Jody Allen;\n**(B)**\nSeahawks President Chuck Arnoldi;\n**(C)**\nSeahawks President of Football Operations/General Manager John Schneider; and\n**(D)**\nSeahawks Head Coach Mike Macdonald.",
      "versionDate": "2026-02-10",
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
        "name": "Sports and Recreation",
        "updateDate": "2026-02-13T17:57:52Z"
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
      "date": "2026-02-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1049ih.xml"
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
      "title": "Congratulating the Seattle Seahawks for winning Super Bowl LX and the 12th Man for their unwavering support.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-12T04:33:45Z"
    },
    {
      "title": "Congratulating the Seattle Seahawks for winning Super Bowl LX and the 12th Man for their unwavering support.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-11T09:06:25Z"
    }
  ]
}
```
