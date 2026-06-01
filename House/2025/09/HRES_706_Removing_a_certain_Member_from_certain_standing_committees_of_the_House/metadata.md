# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/706?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/706
- Title: Removing a certain Member from certain standing committees of the House.
- Congress: 119
- Bill type: HRES
- Bill number: 706
- Origin chamber: House
- Introduced date: 2025-09-15
- Update date: 2025-09-27T08:05:36Z
- Update date including text: 2025-09-27T08:05:36Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-09-15: Introduced in House
- 2025-09-15 - IntroReferral: Referred to the House Committee on Ethics.
- 2025-09-15 - IntroReferral: Submitted in House
- 2025-09-15 - IntroReferral: Submitted in House
- Latest action: 2025-09-15: Submitted in House

## Actions

- 2025-09-15 - IntroReferral: Referred to the House Committee on Ethics.
- 2025-09-15 - IntroReferral: Submitted in House
- 2025-09-15 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-15",
    "latestAction": {
      "actionDate": "2025-09-15",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/706",
    "number": "706",
    "originChamber": "House",
    "policyArea": {
      "name": "Congress"
    },
    "sponsors": [
      {
        "bioguideId": "C001103",
        "district": "1",
        "firstName": "Earl",
        "fullName": "Rep. Carter, Earl L. \"Buddy\" [R-GA-1]",
        "lastName": "Carter",
        "party": "R",
        "state": "GA"
      }
    ],
    "title": "Removing a certain Member from certain standing committees of the House.",
    "type": "HRES",
    "updateDate": "2025-09-27T08:05:36Z",
    "updateDateIncludingText": "2025-09-27T08:05:36Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-15",
      "committees": {
        "item": {
          "name": "Ethics Committee",
          "systemCode": "hsso00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Ethics.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-15",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-09-15",
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
          "date": "2025-09-15T16:02:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ethics Committee",
      "systemCode": "hsso00",
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
      "bioguideId": "C001120",
      "district": "2",
      "firstName": "Dan",
      "fullName": "Rep. Crenshaw, Dan [R-TX-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Crenshaw",
      "party": "R",
      "sponsorshipDate": "2025-09-15",
      "state": "TX"
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
      "sponsorshipDate": "2025-09-15",
      "state": "OK"
    },
    {
      "bioguideId": "M001240",
      "district": "6",
      "firstName": "Addison",
      "fullName": "Rep. McDowell, Addison P. [R-NC-6]",
      "isOriginalCosponsor": "True",
      "lastName": "McDowell",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2025-09-15",
      "state": "NC"
    },
    {
      "bioguideId": "M001212",
      "district": "1",
      "firstName": "Barry",
      "fullName": "Rep. Moore, Barry [R-AL-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-09-15",
      "state": "AL"
    },
    {
      "bioguideId": "V000135",
      "district": "3",
      "firstName": "Derrick",
      "fullName": "Rep. Van Orden, Derrick [R-WI-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Orden",
      "party": "R",
      "sponsorshipDate": "2025-09-15",
      "state": "WI"
    },
    {
      "bioguideId": "S000522",
      "district": "4",
      "firstName": "Christopher",
      "fullName": "Rep. Smith, Christopher H. [R-NJ-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Smith",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2025-09-16",
      "state": "NJ"
    },
    {
      "bioguideId": "A000372",
      "district": "12",
      "firstName": "Rick",
      "fullName": "Rep. Allen, Rick W. [R-GA-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Allen",
      "middleName": "W.",
      "party": "R",
      "sponsorshipDate": "2025-09-26",
      "state": "GA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres706ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 706\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 15, 2025 Mr. Carter of Georgia (for himself, Mr. Crenshaw , Mrs. Bice , Mr. McDowell , Mr. Moore of Alabama , and Mr. Van Orden ) submitted the following resolution; which was referred to the Committee on Ethics\nRESOLUTION\nRemoving a certain Member from certain standing committees of the House.\nThat the following named Members be, and are hereby, removed from the following standing committees of the House of Representatives:\nCommittee on the Budget:\nMs. Omar.\nCommittee on Education and Workforce:\nMs. Omar.",
      "versionDate": "2025-09-15",
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
        "name": "Congress",
        "updateDate": "2025-09-24T16:52:46Z"
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
      "date": "2025-09-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres706ih.xml"
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
      "title": "Removing a certain Member from certain standing committees of the House.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-17T04:48:25Z"
    },
    {
      "title": "Removing a certain Member from certain standing committees of the House.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-16T08:05:39Z"
    }
  ]
}
```
