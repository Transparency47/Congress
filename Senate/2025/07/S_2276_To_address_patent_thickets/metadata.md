# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2276?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2276
- Title: ETHIC Act
- Congress: 119
- Bill type: S
- Bill number: 2276
- Origin chamber: Senate
- Introduced date: 2025-07-15
- Update date: 2025-12-05T22:08:07Z
- Update date including text: 2025-12-05T22:08:07Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-07-15: Introduced in Senate
- 2025-07-15 - IntroReferral: Introduced in Senate
- 2025-07-15 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2025-07-15: Introduced in Senate

## Actions

- 2025-07-15 - IntroReferral: Introduced in Senate
- 2025-07-15 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-15",
    "latestAction": {
      "actionDate": "2025-07-15",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2276",
    "number": "2276",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Commerce"
    },
    "sponsors": [
      {
        "bioguideId": "W000800",
        "district": "",
        "firstName": "Peter",
        "fullName": "Sen. Welch, Peter [D-VT]",
        "lastName": "Welch",
        "party": "D",
        "state": "VT"
      }
    ],
    "title": "ETHIC Act",
    "type": "S",
    "updateDate": "2025-12-05T22:08:07Z",
    "updateDateIncludingText": "2025-12-05T22:08:07Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-15",
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
      "actionDate": "2025-07-15",
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
          "date": "2025-07-15T16:17:23Z",
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
      "bioguideId": "H001089",
      "firstName": "Josh",
      "fullName": "Sen. Hawley, Josh [R-MO]",
      "isOriginalCosponsor": "True",
      "lastName": "Hawley",
      "party": "R",
      "sponsorshipDate": "2025-07-15",
      "state": "MO"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2025-07-15",
      "state": "MN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2276is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2276\nIN THE SENATE OF THE UNITED STATES\nJuly 15, 2025 Mr. Welch (for himself, Mr. Hawley , and Ms. Klobuchar ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo address patent thickets.\n#### 1. Short title\nThis Act may be cited as the Eliminating Thickets to Increase Competition Act or the ETHIC Act .\n#### 2. Addressing patent thickets\n##### (a) Limit on number of patents per patent group that may be asserted in action for infringement\nSection 271(e) of title 35, United States Code, is amended by adding at the end the following:\n(7) (A) A person who brings an action for infringement of a patent under this section against a party described in subparagraph (B) may assert in the action not more than one patent per Patent Group. (B) A party described in this subparagraph is\u2014 (i) a person who\u2014 (I) submits an application for approval of a drug under subsection (b)(2) or (j) of section 505 of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 355 ), or is a holder of such an approved application; or (II) submits an application for licensure of a biological product under section 351(k) of the Public Health Service Act ( 42 U.S.C. 262(k) ), or is a holder of such a licensure; or (ii) a person making, using, selling, offering for sale, introducing or delivering into interstate commerce, or importing\u2014 (I) a drug approved pursuant to an application under subsection (b)(2) or (j) of section 505 of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 355 ); or (II) a biological product licensed under section 351(k) of the Public Health Service Act ( 42 U.S.C. 262(k) ). (C) A person who brings an action described in subparagraph (A) asserting a patent against a party may not bring any additional actions described in that subparagraph asserting a patent in the same Patent Group against that party. (D) (i) For purposes of this paragraph, the term Patent Group means 2 or more commonly owned patents or applications that\u2014 (I) are identified on 1 or more disclaimers under section 253 to obviate obviousness-type double patenting of another commonly owned patent; or (II) are subject to 1 or more disclaimers under section 253 to obviate obviousness-type double patenting of another commonly owned patent. (ii) For purposes of clause (i)(I)\u2014 (I) each patent or application that identifies the same patent or application on a disclaimer under section 253 is part of the same Patent Group; and (II) each patent or application that is identified on a disclaimer under section 253 is part of the same Patent Group as the patent or application subject to the disclaimer. .\n##### (b) Applicability\nThe amendment made by subsection (a) shall apply with respect to an application submitted under subsection (b)(2) or (j) of section 505 of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 355 ) or section 351(k) of the Public Health Service Act ( 42 U.S.C. 262(k) ) on or after the date of enactment of this Act.",
      "versionDate": "2025-07-15",
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
        "actionDate": "2025-05-08",
        "text": "Referred to the House Committee on the Judiciary."
      },
      "number": "3269",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "ETHIC Act",
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
        "name": "Commerce",
        "updateDate": "2025-08-01T15:00:22Z"
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
      "date": "2025-07-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2276is.xml"
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
      "title": "ETHIC Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-24T01:53:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "ETHIC Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-24T01:53:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Eliminating Thickets to Increase Competition Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-24T01:53:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to address patent thickets.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-24T01:48:20Z"
    }
  ]
}
```
