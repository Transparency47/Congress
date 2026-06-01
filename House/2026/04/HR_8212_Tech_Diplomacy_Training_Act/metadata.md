# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8212?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8212
- Title: Tech Diplomacy Training Act
- Congress: 119
- Bill type: HR
- Bill number: 8212
- Origin chamber: House
- Introduced date: 2026-04-09
- Update date: 2026-04-28T08:06:01Z
- Update date including text: 2026-04-28T08:06:01Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-04-09: Introduced in House
- 2026-04-09 - IntroReferral: Introduced in House
- 2026-04-09 - IntroReferral: Introduced in House
- 2026-04-09 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- Latest action: 2026-04-09: Introduced in House

## Actions

- 2026-04-09 - IntroReferral: Introduced in House
- 2026-04-09 - IntroReferral: Introduced in House
- 2026-04-09 - IntroReferral: Referred to the House Committee on Foreign Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-09",
    "latestAction": {
      "actionDate": "2026-04-09",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8212",
    "number": "8212",
    "originChamber": "House",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "B001307",
        "district": "4",
        "firstName": "James",
        "fullName": "Rep. Baird, James R. [R-IN-4]",
        "lastName": "Baird",
        "party": "R",
        "state": "IN"
      }
    ],
    "title": "Tech Diplomacy Training Act",
    "type": "HR",
    "updateDate": "2026-04-28T08:06:01Z",
    "updateDateIncludingText": "2026-04-28T08:06:01Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-09",
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
      "actionDate": "2026-04-09",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-04-09",
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
          "date": "2026-04-09T15:33:20Z",
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
      "bioguideId": "H001058",
      "district": "4",
      "firstName": "Bill",
      "fullName": "Rep. Huizenga, Bill [R-MI-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Huizenga",
      "party": "R",
      "sponsorshipDate": "2026-04-20",
      "state": "MI"
    },
    {
      "bioguideId": "S001229",
      "district": "6",
      "firstName": "Jefferson",
      "fullName": "Rep. Shreve, Jefferson [R-IN-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Shreve",
      "party": "R",
      "sponsorshipDate": "2026-04-27",
      "state": "IN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8212ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8212\nIN THE HOUSE OF REPRESENTATIVES\nApril 9, 2026 Mr. Baird introduced the following bill; which was referred to the Committee on Foreign Affairs\nA BILL\nTo require Foreign Service officers to complete certain science, technology, engineering, and mathematics training, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Tech Diplomacy Training Act .\n#### 2. Requirement to complete certain science, technology, engineering, and mathematics training\nSection 708 of the Foreign Service Act of 1980 ( 22 U.S.C. 4028 ) is amended by adding at the end the following new subsection:\n(f) STEM Training (1) In general The Secretary of State, acting through the Director of the George P. Shultz National Foreign Affairs Training Center, shall establish and conduct training on\u2014 (A) matters related to science, technology, engineering, and mathematics, including\u2014 (i) artificial intelligence; (ii) next generation communications; (iii) technological advancements made in different geographic regions; (iv) how such topics affect diplomacy; and (v) any other training with respect to such matters that such secretary determines critical to the Foreign Service; (B) how the United States may utilize emerging science, technology, engineering, and mathematics matters as a tool of diplomacy; and (C) how United States adversaries and national security threats, as identified in the National Security Strategy most recently published by the President on the date on which such training is conducted, utilize technology\u2014 (i) to undermine United States diplomacy; and (ii) when engaging in diplomacy. (2) Condensed training The Secretary of State, acting through the Director of the George P. Shultz National Foreign Affairs Training Center, shall establish a condensed training curriculum on the matters described in paragraph (1). (3) Required training (A) In general The training described under paragraph (1) shall be included in the A\u2013100 course attended by each Foreign Service officer. (B) Existing officers With respect to an officer serving in the Foreign Service on the date of the enactment of the Tech Diplomacy Training Act and who has completed the A\u2013100 course\u2014 (i) the training described under paragraph (1) shall be completed not later than 18 months after such date of enactment; or (ii) the training described under paragraph (2) shall be completed not later than 270 days after such date of enactment. (4) Relation to existing training The training required by this subsection shall be in addition to and conducted separate from each other training required to be completed by a Foreign Service officer. .",
      "versionDate": "2026-04-09",
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
        "updateDate": "2026-04-15T01:11:18Z"
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
      "date": "2026-04-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8212ih.xml"
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
      "title": "Tech Diplomacy Training Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-10T08:23:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Tech Diplomacy Training Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-10T08:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require Foreign Service officers to complete certain science, technology, engineering, and mathematics training, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-10T08:18:23Z"
    }
  ]
}
```
