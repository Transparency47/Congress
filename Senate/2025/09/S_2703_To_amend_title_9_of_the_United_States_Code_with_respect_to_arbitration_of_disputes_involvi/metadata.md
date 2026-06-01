# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2703?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2703
- Title: Protecting Older Americans Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 2703
- Origin chamber: Senate
- Introduced date: 2025-09-03
- Update date: 2026-03-05T12:03:20Z
- Update date including text: 2026-03-05T12:03:20Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-09-03: Introduced in Senate
- 2025-09-03 - IntroReferral: Introduced in Senate
- 2025-09-03 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2025-09-03: Introduced in Senate

## Actions

- 2025-09-03 - IntroReferral: Introduced in Senate
- 2025-09-03 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-03",
    "latestAction": {
      "actionDate": "2025-09-03",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2703",
    "number": "2703",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Law"
    },
    "sponsors": [
      {
        "bioguideId": "G000555",
        "district": "",
        "firstName": "Kirsten",
        "fullName": "Sen. Gillibrand, Kirsten E. [D-NY]",
        "lastName": "Gillibrand",
        "party": "D",
        "state": "NY"
      }
    ],
    "title": "Protecting Older Americans Act of 2025",
    "type": "S",
    "updateDate": "2026-03-05T12:03:20Z",
    "updateDateIncludingText": "2026-03-05T12:03:20Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-09-03",
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
      "actionDate": "2025-09-03",
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
        "item": [
          {
            "date": "2025-09-03T22:25:59Z",
            "name": "Referred To"
          },
          {
            "date": "2025-09-03T22:25:59Z",
            "name": "Referred To"
          }
        ]
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
      "bioguideId": "G000359",
      "firstName": "Lindsey",
      "fullName": "Sen. Graham, Lindsey [R-SC]",
      "isOriginalCosponsor": "True",
      "lastName": "Graham",
      "party": "R",
      "sponsorshipDate": "2025-09-03",
      "state": "SC"
    },
    {
      "bioguideId": "D000563",
      "firstName": "Richard",
      "fullName": "Sen. Durbin, Richard J. [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Durbin",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-09-03",
      "state": "IL"
    },
    {
      "bioguideId": "G000386",
      "firstName": "Chuck",
      "fullName": "Sen. Grassley, Chuck [R-IA]",
      "isOriginalCosponsor": "True",
      "lastName": "Grassley",
      "party": "R",
      "sponsorshipDate": "2025-09-03",
      "state": "IA"
    },
    {
      "bioguideId": "H001089",
      "firstName": "Josh",
      "fullName": "Sen. Hawley, Josh [R-MO]",
      "isOriginalCosponsor": "False",
      "lastName": "Hawley",
      "party": "R",
      "sponsorshipDate": "2026-03-03",
      "state": "MO"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "False",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2026-03-04",
      "state": "NJ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2703is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2703\nIN THE SENATE OF THE UNITED STATES\nSeptember 3, 2025 Mrs. Gillibrand (for herself, Mr. Graham , Mr. Durbin , and Mr. Grassley ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo amend title 9 of the United States Code with respect to arbitration of disputes involving age discrimination.\n#### 1. Short title\nThis Act may be cited as the Protecting Older Americans Act of 2025 .\n#### 2. Predispute arbitration of disputes involving age discrimination\n##### (a) In general\nTitle 9 of the United States Code is amended by adding at the end the following:\n5 Arbitration of disputes involving age discrimination Sec. 501. Definitions. 502. No validity or enforceability. 501. Definitions In this chapter: (1) Age discrimination dispute The term age discrimination dispute means a dispute relating to conduct that is alleged to constitute age discrimination against a person who is not less than 40 years of age in any form, including disparate treatment, disparate impact, harassment, and retaliation, that is prohibited under applicable Federal, Tribal, or State law (including local law). (2) Predispute arbitration agreement; predispute joint-action waiver The terms predispute arbitration agreement and predispute joint-action waiver have the meanings given the terms in section 401. 502. No validity or enforceability (a) In general Notwithstanding any other provision of this title, at the election of the person alleging conduct constituting an age discrimination dispute, or the named representative of a class or in a collective action alleging such conduct, no predispute arbitration agreement or predispute joint-action waiver shall be valid or enforceable with respect to a case which is filed under Federal, Tribal, or State law and relates to the age discrimination dispute. (b) Determination of applicability An issue as to whether this chapter applies with respect to a dispute shall be determined under Federal law. The applicability of this chapter to an agreement to arbitrate and the validity and enforceability of an agreement to which this chapter applies shall be determined by a court, rather than an arbitrator, irrespective of whether the party resisting arbitration challenges the arbitration agreement specifically or in conjunction with other terms of the contract containing such agreement, and irrespective of whether the agreement purports to delegate such determinations to an arbitrator. .\n##### (b) Technical and conforming amendments\n**(1) In general**\nTitle 9 of the United States Code is amended\u2014\n**(A)**\nin section 2, by inserting or 5 before the period at the end;\n**(B)**\nin section 208, in the second sentence, by inserting or 5 before the period at the end; and\n**(C)**\nin section 307, in the second sentence, by inserting or 5 before the period at the end.\n**(2) Table of chapters**\nThe table of chapters for title 9, United States Code, is amended by adding at the end the following:\n5. Arbitration of disputes involving age discrimination 501. .\n#### 3. Applicability\nThis Act, and the amendments made by this Act, shall apply with respect to any dispute or claim that arises or accrues on or after the date of enactment of this Act.",
      "versionDate": "2025-09-03",
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
        "actionDate": "2025-09-03",
        "text": "Referred to the House Committee on the Judiciary."
      },
      "number": "5115",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Protecting Older Americans Act of 2025",
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
        "updateDate": "2025-09-23T14:36:47Z"
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
      "date": "2025-09-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2703is.xml"
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
      "title": "Protecting Older Americans Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-05T12:03:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Protecting Older Americans Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-09T04:23:31Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title 9 of the United States Code with respect to arbitration of disputes involving age discrimination.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-09T04:18:27Z"
    }
  ]
}
```
