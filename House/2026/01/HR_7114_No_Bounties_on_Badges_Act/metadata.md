# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7114?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7114
- Title: No Bounties on Badges Act
- Congress: 119
- Bill type: HR
- Bill number: 7114
- Origin chamber: House
- Introduced date: 2026-01-15
- Update date: 2026-02-04T19:15:04Z
- Update date including text: 2026-02-04T19:15:04Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-01-15: Introduced in House
- 2026-01-15 - IntroReferral: Introduced in House
- 2026-01-15 - IntroReferral: Introduced in House
- 2026-01-15 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2026-01-15: Introduced in House

## Actions

- 2026-01-15 - IntroReferral: Introduced in House
- 2026-01-15 - IntroReferral: Introduced in House
- 2026-01-15 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-15",
    "latestAction": {
      "actionDate": "2026-01-15",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7114",
    "number": "7114",
    "originChamber": "House",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "M001236",
        "district": "14",
        "firstName": "Tim",
        "fullName": "Rep. Moore, Tim [R-NC-14]",
        "lastName": "Moore",
        "party": "R",
        "state": "NC"
      }
    ],
    "title": "No Bounties on Badges Act",
    "type": "HR",
    "updateDate": "2026-02-04T19:15:04Z",
    "updateDateIncludingText": "2026-02-04T19:15:04Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-01-15",
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
      "actionDate": "2026-01-15",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-01-15",
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
          "date": "2026-01-15T14:02:45Z",
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
      "bioguideId": "E000235",
      "district": "4",
      "firstName": "Mike",
      "fullName": "Rep. Ezell, Mike [R-MS-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Ezell",
      "party": "R",
      "sponsorshipDate": "2026-01-15",
      "state": "MS"
    },
    {
      "bioguideId": "N000026",
      "district": "22",
      "firstName": "Troy",
      "fullName": "Rep. Nehls, Troy E. [R-TX-22]",
      "isOriginalCosponsor": "True",
      "lastName": "Nehls",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2026-01-15",
      "state": "TX"
    },
    {
      "bioguideId": "B001260",
      "district": "16",
      "firstName": "Vern",
      "fullName": "Rep. Buchanan, Vern [R-FL-16]",
      "isOriginalCosponsor": "True",
      "lastName": "Buchanan",
      "party": "R",
      "sponsorshipDate": "2026-01-15",
      "state": "FL"
    },
    {
      "bioguideId": "C001087",
      "district": "1",
      "firstName": "Eric",
      "fullName": "Rep. Crawford, Eric A. \"Rick\" [R-AR-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Crawford",
      "middleName": "A. \"Rick\"",
      "party": "R",
      "sponsorshipDate": "2026-01-15",
      "state": "AR"
    },
    {
      "bioguideId": "R000609",
      "district": "5",
      "firstName": "John",
      "fullName": "Rep. Rutherford, John H. [R-FL-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Rutherford",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2026-01-15",
      "state": "FL"
    },
    {
      "bioguideId": "D000032",
      "district": "19",
      "firstName": "Byron",
      "fullName": "Rep. Donalds, Byron [R-FL-19]",
      "isOriginalCosponsor": "False",
      "lastName": "Donalds",
      "party": "R",
      "sponsorshipDate": "2026-01-30",
      "state": "FL"
    },
    {
      "bioguideId": "G000558",
      "district": "2",
      "firstName": "Brett",
      "fullName": "Rep. Guthrie, Brett [R-KY-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Guthrie",
      "party": "R",
      "sponsorshipDate": "2026-02-02",
      "state": "KY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7114ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7114\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 15, 2026 Mr. Moore of North Carolina (for himself, Mr. Ezell , Mr. Nehls , Mr. Buchanan , Mr. Crawford , and Mr. Rutherford ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo amend title 18, United States Code, to authorize awards for the arrest or conviction of individuals that deliberately target law enforcement officials with acts of violence or intimidation, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the No Bounties on Badges Act .\n#### 2. Awards authorized\n##### (a) In general\nChapter 204 of title 18, United States Code, is amended\u2014\n**(1)**\nin the chapter heading by striking and espionage and inserting , espionage, and offering of bounties ; and\n**(2)**\nin section 3071, by adding at the end the following:\n(c) With respect to acts of offering a bounty or offering money or other pecuniary compensation for harming or killing of any law enforcement officer of the United States, the Attorney General may reward any individual who furnishes information\u2014 (1) leading to the arrest or conviction, in any country, of any individual or individuals for commission of such an act; (2) leading to the arrest or conviction, in any country, of any individual or individuals for conspiring or attempting to commit such an act; or (3) leading to the prevention or frustration of such an act. .\n##### (b) Clerical amendment\nThe item relating to chapter 204 in the table of chapters for part II of title 18, United States Code, is amended to read as follows:\n204.\nRewards for information concerning terrorist acts, espionage, or offering of bounties\n3071.",
      "versionDate": "2026-01-15",
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
        "actionDate": "2025-12-11",
        "text": "Read twice and referred to the Committee on the Judiciary."
      },
      "number": "3453",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "No Bounties on Badges Act",
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
        "name": "Crime and Law Enforcement",
        "updateDate": "2026-02-04T19:15:04Z"
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
      "date": "2026-01-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7114ih.xml"
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
      "title": "No Bounties on Badges Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-03T11:08:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "No Bounties on Badges Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-03T11:08:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 18, United States Code, to authorize awards for the arrest or conviction of individuals that deliberately target law enforcement officials with acts of violence or intimidation, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-03T11:03:54Z"
    }
  ]
}
```
