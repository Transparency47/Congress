# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3374?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3374
- Title: SAFE Chips Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 3374
- Origin chamber: Senate
- Introduced date: 2025-12-04
- Update date: 2026-01-07T16:23:15Z
- Update date including text: 2026-01-07T16:23:15Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-04: Introduced in Senate
- 2025-12-04 - IntroReferral: Introduced in Senate
- 2025-12-04 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.
- Latest action: 2025-12-04: Introduced in Senate

## Actions

- 2025-12-04 - IntroReferral: Introduced in Senate
- 2025-12-04 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-04",
    "latestAction": {
      "actionDate": "2025-12-04",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3374",
    "number": "3374",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Foreign Trade and International Finance"
    },
    "sponsors": [
      {
        "bioguideId": "R000618",
        "district": "",
        "firstName": "Pete",
        "fullName": "Sen. Ricketts, Pete [R-NE]",
        "lastName": "Ricketts",
        "party": "R",
        "state": "NE"
      }
    ],
    "title": "SAFE Chips Act of 2025",
    "type": "S",
    "updateDate": "2026-01-07T16:23:15Z",
    "updateDateIncludingText": "2026-01-07T16:23:15Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-04",
      "committees": {
        "item": {
          "name": "Banking, Housing, and Urban Affairs Committee",
          "systemCode": "ssbk00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-12-04",
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
          "date": "2025-12-04T20:13:26Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Banking, Housing, and Urban Affairs Committee",
      "systemCode": "ssbk00",
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
      "sponsorshipDate": "2025-12-04",
      "state": "DE"
    },
    {
      "bioguideId": "C001095",
      "firstName": "Tom",
      "fullName": "Sen. Cotton, Tom [R-AR]",
      "isOriginalCosponsor": "True",
      "lastName": "Cotton",
      "party": "R",
      "sponsorshipDate": "2025-12-04",
      "state": "AR"
    },
    {
      "bioguideId": "S001181",
      "firstName": "Jeanne",
      "fullName": "Sen. Shaheen, Jeanne [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Shaheen",
      "party": "D",
      "sponsorshipDate": "2025-12-04",
      "state": "NH"
    },
    {
      "bioguideId": "M001243",
      "firstName": "David",
      "fullName": "Sen. McCormick, David [R-PA]",
      "isOriginalCosponsor": "True",
      "lastName": "McCormick",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2025-12-04",
      "state": "PA"
    },
    {
      "bioguideId": "K000394",
      "firstName": "Andy",
      "fullName": "Sen. Kim, Andy [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Kim",
      "party": "D",
      "sponsorshipDate": "2025-12-04",
      "state": "NJ"
    },
    {
      "bioguideId": "B001299",
      "firstName": "Jim",
      "fullName": "Sen. Banks, Jim [R-IN]",
      "isOriginalCosponsor": "False",
      "lastName": "Banks",
      "party": "R",
      "sponsorshipDate": "2025-12-11",
      "state": "IN"
    },
    {
      "bioguideId": "W000817",
      "firstName": "Elizabeth",
      "fullName": "Sen. Warren, Elizabeth [D-MA]",
      "isOriginalCosponsor": "False",
      "lastName": "Warren",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-12-11",
      "state": "MA"
    },
    {
      "bioguideId": "S001198",
      "firstName": "Dan",
      "fullName": "Sen. Sullivan, Dan [R-AK]",
      "isOriginalCosponsor": "False",
      "lastName": "Sullivan",
      "party": "R",
      "sponsorshipDate": "2025-12-16",
      "state": "AK"
    },
    {
      "bioguideId": "K000384",
      "firstName": "Timothy",
      "fullName": "Sen. Kaine, Tim [D-VA]",
      "isOriginalCosponsor": "False",
      "lastName": "Kaine",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-12-16",
      "state": "VA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3374is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3374\nIN THE SENATE OF THE UNITED STATES\nDecember 4, 2025 Mr. Ricketts (for himself, Mr. Coons , Mr. Cotton , Mrs. Shaheen , Mr. McCormick , and Mr. Kim ) introduced the following bill; which was read twice and referred to the Committee on Banking, Housing, and Urban Affairs\nA BILL\nTo amend the Export Control Reform Act of 2018 to prohibit the issuance of licenses for the export, reexport, or in-country transfer of advanced integrated circuits to or in foreign adversaries.\n#### 1. Short title\nThis Act may be cited as the Secure and Feasible Exports of Chips Act of 2025 or the SAFE Chips Act of 2025 .\n#### 2. Control of exports of advanced integrated circuits\nPart I of Export Control Reform Act of 2018 ( 50 U.S.C. 4811 et seq. ) is amended by inserting after section 1758 the following:\n1758A. Control of exports of advanced integrated circuits (a) License requirement On and after the date of the enactment of this section, the Secretary shall\u2014 (1) require a license for the export, reexport, or in-country transfer of an advanced integrated circuit\u2014 (A) to or in a foreign adversary country; or (B) to an entity located in any country if the entity, or the ultimate parent company of the entity, has its headquarters in a foreign adversary country; and (2) deny any application for such a license. (b) Exclusion Subsection (a) shall not apply to an advanced integrated circuit or product containing such a circuit that is not designed or marketed for data centers. (c) Definitions In this section: (1) Advanced integrated circuit (A) In general Subject to subparagraphs (B) and (C), the term advanced integrated circuit means\u2014 (i) an integrated circuit, computer, or other product\u2014 (I) classified under Export Control Classification Number 3A090 or 4A090 or a related Export Control Classification Number; or (II) that is functionally equivalent or substantially similar to a circuit, computer, or product described in subclause (I); or (ii) an integrated circuit that has one or more digital processing units with\u2014 (I) a total processing performance of 4,800 or more; (II) a total processing performance of 2,400 or more and a performance density of 1.6 or more; (III) a total processing performance of 1,600 or more and a performance density of 3.2 or more; (IV) a total DRAM bandwidth of 4,100 gigabytes per second or more; (V) an interconnect bandwidth of 1,100 gigabytes per second or more; or (VI) a combination of DRAM bandwidth and interconnect bandwidth of 5,000 gigabytes per second or more. (B) Authority to update technical parameters Beginning 30 months after the date of the enactment of this section, subject to subparagraph (C), and after approval by a majority vote of the End-User Review Committee, the Secretary may modify the technical parameters for the definition of advanced integrated circuit for purposes of this section through a notice in the Federal Register. (C) Briefing required Not later than 30 days before any modification to the definition of advanced integrated circuit under subparagraph (B) is published in the Federal Register, the Secretary shall provide a briefing to the Committee on Banking, Housing, and Urban Affairs of the Senate and the Committee on Foreign Affairs of the House of Representatives that includes\u2014 (i) a description of the planned modification; (ii) the date that the planned modification is expected to be published in the Federal Register; (iii) a detailed justification for why the planned modification is in the national interest of the United States; (iv) an assessment of how the planned modification and resulting sales to the People's Republic of China would\u2014 (I) affect the capabilities of leading Chinese artificial intelligence firms; and (II) alter the military, cyber, or other offensive capabilities of the People's Republic of China; and (v) an analysis of how and to what extent the United States will continue to maintain an advantage in computing relative to the People's Republic of China. (2) Foreign adversary country The term foreign adversary country \u2014 (A) means a country specified in section 4872(f)(2) of title 10, United States Code; and (B) includes the Macau Special Administrative Region and the Hong Kong Special Administrative Region of the People's Republic of China. (3) Performance density; total processing performance The terms performance density and total processing performance have the meanings given those terms in, and are calculated as provided for under, Export Control Classification Number 3A090 in the Commerce Control List set forth in Supplement No. 1 to part 774 of the Export Administration Regulations (as in effect on the day before the date of the enactment of this section). .",
      "versionDate": "2025-12-04",
      "versionType": "Introduced in Senate"
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
        "name": "Foreign Trade and International Finance",
        "updateDate": "2026-01-07T16:23:15Z"
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
      "date": "2025-12-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3374is.xml"
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
      "title": "SAFE Chips Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-31T03:38:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "SAFE Chips Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-31T03:38:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Secure and Feasible Exports of Chips Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-31T03:38:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Export Control Reform Act of 2018 to prohibit the issuance of licenses for the export, reexport, or in-country transfer of advanced integrated circuits to or in foreign adversaries.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-31T03:33:16Z"
    }
  ]
}
```
