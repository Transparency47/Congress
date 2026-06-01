# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2387?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2387
- Title: LEAD Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 2387
- Origin chamber: Senate
- Introduced date: 2025-07-23
- Update date: 2025-12-05T22:56:33Z
- Update date including text: 2025-12-05T22:56:33Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-07-23: Introduced in Senate
- 2025-07-23 - IntroReferral: Introduced in Senate
- 2025-07-23 - IntroReferral: Read twice and referred to the Committee on Foreign Relations.
- Latest action: 2025-07-23: Introduced in Senate

## Actions

- 2025-07-23 - IntroReferral: Introduced in Senate
- 2025-07-23 - IntroReferral: Read twice and referred to the Committee on Foreign Relations.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-23",
    "latestAction": {
      "actionDate": "2025-07-23",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2387",
    "number": "2387",
    "originChamber": "Senate",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "C001095",
        "district": "",
        "firstName": "Tom",
        "fullName": "Sen. Cotton, Tom [R-AR]",
        "lastName": "Cotton",
        "party": "R",
        "state": "AR"
      }
    ],
    "title": "LEAD Act of 2025",
    "type": "S",
    "updateDate": "2025-12-05T22:56:33Z",
    "updateDateIncludingText": "2025-12-05T22:56:33Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-23",
      "committees": {
        "item": {
          "name": "Foreign Relations Committee",
          "systemCode": "ssfr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Foreign Relations.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-07-23",
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
          "date": "2025-07-23T14:25:11Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Foreign Relations Committee",
      "systemCode": "ssfr00",
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
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "True",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "DE"
    },
    {
      "bioguideId": "C001056",
      "firstName": "John",
      "fullName": "Sen. Cornyn, John [R-TX]",
      "isOriginalCosponsor": "True",
      "lastName": "Cornyn",
      "party": "R",
      "sponsorshipDate": "2025-07-23",
      "state": "TX"
    },
    {
      "bioguideId": "B001305",
      "firstName": "Ted",
      "fullName": "Sen. Budd, Ted [R-NC]",
      "isOriginalCosponsor": "False",
      "lastName": "Budd",
      "party": "R",
      "sponsorshipDate": "2025-07-30",
      "state": "NC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2387is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2387\nIN THE SENATE OF THE UNITED STATES\nJuly 23, 2025 Mr. Cotton (for himself, Mr. Coons , and Mr. Cornyn ) introduced the following bill; which was read twice and referred to the Committee on Foreign Relations\nA BILL\nTo amend the Arms Export Control Act to address arms export controls for certain unmanned aircraft systems and items, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Leading Exports of Aerial Drones Act of 2025 or the LEAD Act of 2025 .\n#### 2. Arms export controls for covered unmanned aircraft systems and items\n##### (a) Arms Export Control Act\n**(1) Section 38**\nSection 38 of the Arms Export Control Act ( 22 U.S.C. 2778 ) is amended by adding at the end the following:\n(m) Covered unmanned aircraft systems and items (1) In general For purposes of transfers of defense articles and defense services under this Act, covered unmanned aircraft systems and items\u2014 (A) shall be treated as manned aircraft systems items; and (B) shall not be considered launch vehicles, missile technology, or missile equipment subject to controls or export restrictions for purposes of adherence by the United States to the Missile Technology Control Regime. (2) Definition of covered unmanned aircraft systems and items In this subsection, the term covered unmanned aircraft systems and items means unmanned aircraft systems and related items that\u2014 (A) are controlled under the International Traffic in Arms Regulations and enumerated in the Missile Technology Control Regime Annex; and (B) are designed to be reusable. .\n**(2) Chapter 7**\nChapter 7 of such Act ( 22 U.S.C. 2797 et seq. ) is amended by inserting after section 73B the following:\n73C. Statement of policy on covered unmanned aircraft systems and items It is the policy of the United States to treat covered unmanned aircraft systems and items (as defined in section 38(m)(2)(B)) as manned aircraft systems and items for purposes of implementing the Missile Technology Control Regime. .\n##### (b) International Traffic in Arms Regulations\n**(1) United States Munitions List**\nNot later than 180 days after the date of the enactment of this Act, the President shall amend section 121.1 of title 22, Code of Federal Regulations, to provide that covered unmanned aircraft systems and items\u2014\n**(A)**\nare subject to the same export control provisions as manned aircraft systems and items and that, for purposes of part 121 of such title, shall be reviewed under the same criteria and guidelines as manned aircraft systems and items; and\n**(B)**\nare distinct from launch vehicles, missile technology, and missile equipment and are subject to separate export control provisions and that, for purposes of part 121 of such title, shall be reviewed under criteria specific to their technological and operational characteristics.\n**(2) Missile Technology Control Regime**\nNot later than 180 days after the date of the enactment of this Act, the President shall amend section 120.23 of title 22, Code of Federal Regulations, to provide that, for purposes of implementing the Missile Technology Control Regime, the United States shall treat covered unmanned aircraft systems and items\u2014\n**(A)**\nseparately from missile technology, including for purposes of co-production and co-development agreements with allies and partners; and\n**(B)**\nas manned aircraft systems and items that shall not be subject to controls, missile technology reviews, or export restrictions for purposes of adherence by the United States to the Missile Technology Control Regime.\n**(3) Definitions**\nIn this section:\n**(A) Covered unmanned aircraft systems and items**\nThe term covered unmanned aircraft systems and items has the meaning given that term in subsection (m)(2) of section 38 of the Arms Export Control Act ( 22 U.S.C. 2778 ), as added by subsection (a).\n**(B) Missile; Missile Technology Control Regime**\nThe terms missile and Missile Technology Control Regime have the meanings given those terms in section 74(a) of the Arms Export Control Act ( 22 U.S.C. 2797c(a) ).",
      "versionDate": "2025-07-23",
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
        "actionDate": "2025-07-23",
        "text": "Referred to the House Committee on Foreign Affairs."
      },
      "number": "4753",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "LEAD Act of 2025",
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
        "name": "International Affairs",
        "updateDate": "2025-08-01T18:29:00Z"
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
      "date": "2025-07-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2387is.xml"
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
      "title": "LEAD Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-01T03:53:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "LEAD Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-01T03:53:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Leading Exports of Aerial Drones Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-01T03:53:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Arms Export Control Act to address arms export controls for certain unmanned aircraft systems and items, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-01T03:48:25Z"
    }
  ]
}
```
