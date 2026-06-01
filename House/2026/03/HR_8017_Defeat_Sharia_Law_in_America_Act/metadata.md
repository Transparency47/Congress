# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8017?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8017
- Title: Defeat Sharia Law in America Act
- Congress: 119
- Bill type: HR
- Bill number: 8017
- Origin chamber: House
- Introduced date: 2026-03-19
- Update date: 2026-04-06T13:23:03Z
- Update date including text: 2026-04-06T13:23:03Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-03-19: Introduced in House
- 2026-03-19 - IntroReferral: Introduced in House
- 2026-03-19 - IntroReferral: Introduced in House
- 2026-03-19 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2026-03-19: Introduced in House

## Actions

- 2026-03-19 - IntroReferral: Introduced in House
- 2026-03-19 - IntroReferral: Introduced in House
- 2026-03-19 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-19",
    "latestAction": {
      "actionDate": "2026-03-19",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8017",
    "number": "8017",
    "originChamber": "House",
    "policyArea": {
      "name": "Civil Rights and Liberties, Minority Issues"
    },
    "sponsors": [
      {
        "bioguideId": "M001212",
        "district": "1",
        "firstName": "Barry",
        "fullName": "Rep. Moore, Barry [R-AL-1]",
        "lastName": "Moore",
        "party": "R",
        "state": "AL"
      }
    ],
    "title": "Defeat Sharia Law in America Act",
    "type": "HR",
    "updateDate": "2026-04-06T13:23:03Z",
    "updateDateIncludingText": "2026-04-06T13:23:03Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-19",
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
      "actionCode": "Intro-H",
      "actionDate": "2026-03-19",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-03-19",
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
        "item": {
          "date": "2026-03-19T13:03:20Z",
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
      "bioguideId": "S001224",
      "district": "3",
      "firstName": "Keith",
      "fullName": "Rep. Self, Keith [R-TX-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Self",
      "party": "R",
      "sponsorshipDate": "2026-03-19",
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
      "sponsorshipDate": "2026-03-19",
      "state": "TX"
    },
    {
      "bioguideId": "B001302",
      "district": "5",
      "firstName": "Andy",
      "fullName": "Rep. Biggs, Andy [R-AZ-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Biggs",
      "party": "R",
      "sponsorshipDate": "2026-03-24",
      "state": "AZ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8017ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8017\nIN THE HOUSE OF REPRESENTATIVES\nMarch 19, 2026 Mr. Moore of Alabama (for himself, Mr. Self , and Mr. Gooden ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo amend the Civil Rights Act of 1964 to improve prohibitions on discrimination by public accommodations.\n#### 1. Short title\nThis Act may be cited as the Defeat Sharia Law in America Act .\n#### 2. Discrimination\nSection 201(a) of the Civil Rights Act of 1964 ( 42 U.S.C. 2000a(a) ) is amended by adding at the end the following: An establishment covered by this section that provides goods, services, facilities, privileges, advantages, or accommodations by implementing Sharia law shall be considered to be discriminating or segregating on the ground of religion under this subsection. .",
      "versionDate": "2026-03-19",
      "versionType": "Introduced in House"
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
        "actionDate": "2026-02-12",
        "text": "Read twice and referred to the Committee on the Judiciary."
      },
      "number": "3887",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Defeat Sharia Law in America Act",
      "type": "S"
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
        "name": "Civil Rights and Liberties, Minority Issues",
        "updateDate": "2026-04-06T13:23:03Z"
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
      "date": "2026-03-19",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8017ih.xml"
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
      "title": "Defeat Sharia Law in America Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-02T12:08:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Defeat Sharia Law in America Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-02T12:08:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Civil Rights Act of 1964 to improve prohibitions on discrimination by public accommodations.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-02T12:03:26Z"
    }
  ]
}
```
