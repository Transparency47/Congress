# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3243?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3243
- Title: Ending Forced Arbitration of Race Discrimination Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 3243
- Origin chamber: Senate
- Introduced date: 2025-11-20
- Update date: 2026-01-10T06:45:09Z
- Update date including text: 2026-01-10T06:45:09Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-11-20: Introduced in Senate
- 2025-11-20 - IntroReferral: Introduced in Senate
- 2025-11-20 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2025-11-20: Introduced in Senate

## Actions

- 2025-11-20 - IntroReferral: Introduced in Senate
- 2025-11-20 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-20",
    "latestAction": {
      "actionDate": "2025-11-20",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3243",
    "number": "3243",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Law"
    },
    "sponsors": [
      {
        "bioguideId": "B001288",
        "district": "",
        "firstName": "Cory",
        "fullName": "Sen. Booker, Cory A. [D-NJ]",
        "lastName": "Booker",
        "party": "D",
        "state": "NJ"
      }
    ],
    "title": "Ending Forced Arbitration of Race Discrimination Act of 2025",
    "type": "S",
    "updateDate": "2026-01-10T06:45:09Z",
    "updateDateIncludingText": "2026-01-10T06:45:09Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-11-20",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-11-20",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in Senate",
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
          "date": "2025-11-20T18:05:11Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Judiciary Committee",
      "systemCode": "ssju00",
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
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "CT"
    },
    {
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "True",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "DE"
    },
    {
      "bioguideId": "D000563",
      "firstName": "Richard",
      "fullName": "Sen. Durbin, Richard J. [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Durbin",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "IL"
    },
    {
      "bioguideId": "G000555",
      "firstName": "Kirsten",
      "fullName": "Sen. Gillibrand, Kirsten E. [D-NY]",
      "isOriginalCosponsor": "True",
      "lastName": "Gillibrand",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "NY"
    },
    {
      "bioguideId": "H001042",
      "firstName": "Mazie",
      "fullName": "Sen. Hirono, Mazie K. [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Hirono",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "HI"
    },
    {
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "CA"
    },
    {
      "bioguideId": "V000128",
      "firstName": "Chris",
      "fullName": "Sen. Van Hollen, Chris [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Hollen",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "MD"
    },
    {
      "bioguideId": "W000817",
      "firstName": "Elizabeth",
      "fullName": "Sen. Warren, Elizabeth [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warren",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "MA"
    },
    {
      "bioguideId": "W000802",
      "firstName": "Sheldon",
      "fullName": "Sen. Whitehouse, Sheldon [D-RI]",
      "isOriginalCosponsor": "True",
      "lastName": "Whitehouse",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "RI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3243is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3243\nIN THE SENATE OF THE UNITED STATES\nNovember 20, 2025 Mr. Booker (for himself, Mr. Blumenthal , Mr. Coons , Mr. Durbin , Mrs. Gillibrand , Ms. Hirono , Mr. Padilla , Mr. Van Hollen , Ms. Warren , and Mr. Whitehouse ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo amend title 9, United States Code, with respect to arbitration of disputes involving race discrimination.\n#### 1. Short title\nThis Act may be cited as the Ending Forced Arbitration of Race Discrimination Act of 2025 .\n#### 2. Predispute arbitration of disputes involving race discrimination\n##### (a) In general\nTitle 9, United States Code, is amended by adding at the end the following:\n5 Arbitration of disputes involving race discrimination Sec. 501. Definitions. 502. No validity or enforceability. 501. Definitions In this chapter: (1) Predispute arbitration agreement; predispute joint-action waiver The terms predispute arbitration agreement and predispute joint-action waiver have the meanings given the terms in section 401. (2) Race discrimination dispute The term race discrimination dispute means a dispute relating to conduct that is alleged to constitute discrimination (including harassment), or retaliation, on the basis of race, color, or national origin under applicable Federal, Tribal, State, or local law. 502. No validity or enforceability (a) In general Notwithstanding any other provision of this title, at the election of the person alleging conduct constituting a race discrimination dispute, or the named representative of a class or in a collective action alleging such conduct, no predispute arbitration agreement or predispute joint-action waiver shall be valid or enforceable with respect to a case which is filed under Federal, Tribal, State, or local law and relates to the race discrimination dispute. (b) Determination of applicability An issue as to whether this chapter applies with respect to a dispute shall be determined under Federal law. The applicability of this chapter to an agreement to arbitrate and the validity and enforceability of an agreement to which this chapter applies shall be determined by a court, rather than an arbitrator, irrespective of whether the party resisting arbitration challenges the arbitration agreement specifically or in conjunction with other terms of the contract containing such agreement, and irrespective of whether the agreement purports to delegate such determinations to an arbitrator. .\n##### (b) Technical and conforming amendments\n**(1) In general**\nTitle 9, United States Code is amended\u2014\n**(A)**\nin section 2, by inserting or 5 before the period at the end;\n**(B)**\nin section 208, in the second sentence, by inserting or 5 before the period at the end; and\n**(C)**\nin section 307, in the second sentence, by inserting or 5 before the period at the end.\n**(2) Table of chapters**\nThe table of chapters for title 9, United States Code, is amended by adding at the end the following:\n5. Arbitration of disputes involving race discrimination 501. .\n#### 3. Applicability\nThis Act, and the amendments made by this Act, shall apply with respect to any dispute or claim that arises or accrues on or after the date of enactment of this Act.",
      "versionDate": "2025-11-20",
      "versionType": "Introduced in Senate"
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
        "actionDate": "2025-11-20",
        "text": "Referred to the House Committee on the Judiciary."
      },
      "number": "6172",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Ending Forced Arbitration of Race Discrimination Act of 2025",
      "type": "HR"
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
        "name": "Law",
        "updateDate": "2026-01-05T15:05:17Z"
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
      "date": "2025-11-20",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3243is.xml"
        }
      ],
      "type": "Introduced in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Ending Forced Arbitration of Race Discrimination Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-19T05:28:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Ending Forced Arbitration of Race Discrimination Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-19T05:28:14Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title 9, United States Code, with respect to arbitration of disputes involving race discrimination.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-19T05:28:13Z"
    }
  ]
}
```
