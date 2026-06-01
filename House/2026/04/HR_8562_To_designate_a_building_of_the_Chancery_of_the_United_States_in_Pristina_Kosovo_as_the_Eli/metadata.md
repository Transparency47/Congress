# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8562?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8562
- Title: To designate a building of the Chancery of the United States in Pristina, Kosovo, as the "Eliot L. Engel Building".
- Congress: 119
- Bill type: HR
- Bill number: 8562
- Origin chamber: House
- Introduced date: 2026-04-28
- Update date: 2026-05-22T18:20:22Z
- Update date including text: 2026-05-22T18:20:22Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-04-28: Introduced in House
- 2026-04-28 - IntroReferral: Introduced in House
- 2026-04-28 - IntroReferral: Introduced in House
- 2026-04-28 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- 2026-05-13 - Committee: Committee Consideration and Mark-up Session Held
- 2026-05-13 - Committee: Ordered to be Reported by the Yeas and Nays: 39 - 7.
- Latest action: 2026-04-28: Introduced in House

## Actions

- 2026-04-28 - IntroReferral: Introduced in House
- 2026-04-28 - IntroReferral: Introduced in House
- 2026-04-28 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- 2026-05-13 - Committee: Committee Consideration and Mark-up Session Held
- 2026-05-13 - Committee: Ordered to be Reported by the Yeas and Nays: 39 - 7.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-28",
    "latestAction": {
      "actionDate": "2026-04-28",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8562",
    "number": "8562",
    "originChamber": "House",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "T000486",
        "district": "15",
        "firstName": "Ritchie",
        "fullName": "Rep. Torres, Ritchie [D-NY-15]",
        "lastName": "Torres",
        "party": "D",
        "state": "NY"
      }
    ],
    "title": "To designate a building of the Chancery of the United States in Pristina, Kosovo, as the \"Eliot L. Engel Building\".",
    "type": "HR",
    "updateDate": "2026-05-22T18:20:22Z",
    "updateDateIncludingText": "2026-05-22T18:20:22Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-05-13",
      "committees": {
        "item": {
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Ordered to be Reported by the Yeas and Nays: 39 - 7.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-05-13",
      "committees": {
        "item": {
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Committee Consideration and Mark-up Session Held",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-28",
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
      "actionCode": "Intro-H",
      "actionDate": "2026-04-28",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-04-28",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
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
        "item": [
          {
            "date": "2026-05-13T15:35:00Z",
            "name": "Markup By"
          },
          {
            "date": "2026-04-28T13:01:05Z",
            "name": "Referred To"
          }
        ]
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
      "bioguideId": "M001157",
      "district": "10",
      "firstName": "Michael",
      "fullName": "Rep. McCaul, Michael T. [R-TX-10]",
      "isOriginalCosponsor": "True",
      "lastName": "McCaul",
      "middleName": "T.",
      "party": "R",
      "sponsorshipDate": "2026-04-28",
      "state": "TX"
    },
    {
      "bioguideId": "M001137",
      "district": "5",
      "firstName": "Gregory",
      "fullName": "Rep. Meeks, Gregory W. [D-NY-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Meeks",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2026-04-28",
      "state": "NY"
    },
    {
      "bioguideId": "M001199",
      "district": "21",
      "firstName": "Brian",
      "fullName": "Rep. Mast, Brian J. [R-FL-21]",
      "isOriginalCosponsor": "True",
      "lastName": "Mast",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2026-04-28",
      "state": "FL"
    },
    {
      "bioguideId": "L000606",
      "district": "16",
      "firstName": "George",
      "fullName": "Rep. Latimer, George [D-NY-16]",
      "isOriginalCosponsor": "False",
      "lastName": "Latimer",
      "party": "D",
      "sponsorshipDate": "2026-04-29",
      "state": "NY"
    },
    {
      "bioguideId": "W000795",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Wilson, Joe [R-SC-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Wilson",
      "party": "R",
      "sponsorshipDate": "2026-04-29",
      "state": "SC"
    },
    {
      "bioguideId": "K000375",
      "district": "9",
      "firstName": "William",
      "fullName": "Rep. Keating, William R. [D-MA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Keating",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2026-05-11",
      "state": "MA"
    },
    {
      "bioguideId": "S000344",
      "district": "32",
      "firstName": "Brad",
      "fullName": "Rep. Sherman, Brad [D-CA-32]",
      "isOriginalCosponsor": "False",
      "lastName": "Sherman",
      "party": "D",
      "sponsorshipDate": "2026-05-12",
      "state": "CA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8562ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8562\nIN THE HOUSE OF REPRESENTATIVES\nApril 28, 2026 Mr. Torres of New York (for himself, Mr. McCaul , Mr. Meeks , and Mr. Mast ) introduced the following bill; which was referred to the Committee on Foreign Affairs\nA BILL\nTo designate a building of the Chancery of the United States in Pristina, Kosovo, as the Eliot L. Engel Building .\n#### 1. Designation\nThe building of the Chancery of the United States located at Arberia, Nr.25 Rr. 4 KORRIKU in Pristina, Kosovo, shall be designated as the Eliot L. Engel Building .\n#### 2. References\nAny reference in a law, map, regulation, document, paper, or other record of the United States to the building referred to in section 1 shall be deemed to be a reference to the Eliot L. Engel Building .",
      "versionDate": "2026-04-28",
      "versionType": "Introduced in House"
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
        "updateDate": "2026-05-08T20:32:49Z"
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
      "date": "2026-04-28",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8562ih.xml"
        }
      ],
      "type": "Introduced in House"
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
      "title": "To designate a building of the Chancery of the United States in Pristina, Kosovo, as the \"Eliot L. Engel Building\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-06T04:18:31Z"
    },
    {
      "title": "To designate a building of the Chancery of the United States in Pristina, Kosovo, as the \"Eliot L. Engel Building\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-29T08:07:13Z"
    }
  ]
}
```
