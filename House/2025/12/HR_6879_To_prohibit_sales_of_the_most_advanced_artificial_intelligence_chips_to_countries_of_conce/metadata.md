# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6879?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6879
- Title: RESTRICT Act
- Congress: 119
- Bill type: HR
- Bill number: 6879
- Origin chamber: House
- Introduced date: 2025-12-18
- Update date: 2026-04-30T08:06:32Z
- Update date including text: 2026-04-30T08:06:32Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-18: Introduced in House
- 2025-12-18 - IntroReferral: Introduced in House
- 2025-12-18 - IntroReferral: Introduced in House
- 2025-12-18 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- Latest action: 2025-12-18: Introduced in House

## Actions

- 2025-12-18 - IntroReferral: Introduced in House
- 2025-12-18 - IntroReferral: Introduced in House
- 2025-12-18 - IntroReferral: Referred to the House Committee on Foreign Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-18",
    "latestAction": {
      "actionDate": "2025-12-18",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6879",
    "number": "6879",
    "originChamber": "House",
    "policyArea": {
      "name": "Foreign Trade and International Finance"
    },
    "sponsors": [
      {
        "bioguideId": "M001137",
        "district": "5",
        "firstName": "Gregory",
        "fullName": "Rep. Meeks, Gregory W. [D-NY-5]",
        "lastName": "Meeks",
        "party": "D",
        "state": "NY"
      }
    ],
    "title": "RESTRICT Act",
    "type": "HR",
    "updateDate": "2026-04-30T08:06:32Z",
    "updateDateIncludingText": "2026-04-30T08:06:32Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-18",
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
      "actionDate": "2025-12-18",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-18",
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
          "date": "2025-12-18T14:03:30Z",
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
      "bioguideId": "K000400",
      "district": "37",
      "firstName": "Sydney",
      "fullName": "Rep. Kamlager-Dove, Sydney [D-CA-37]",
      "isOriginalCosponsor": "True",
      "lastName": "Kamlager-Dove",
      "party": "D",
      "sponsorshipDate": "2025-12-18",
      "state": "CA"
    },
    {
      "bioguideId": "C001091",
      "district": "20",
      "firstName": "Joaquin",
      "fullName": "Rep. Castro, Joaquin [D-TX-20]",
      "isOriginalCosponsor": "True",
      "lastName": "Castro",
      "party": "D",
      "sponsorshipDate": "2025-12-18",
      "state": "TX"
    },
    {
      "bioguideId": "T000468",
      "district": "1",
      "firstName": "Dina",
      "fullName": "Rep. Titus, Dina [D-NV-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Titus",
      "party": "D",
      "sponsorshipDate": "2025-12-18",
      "state": "NV"
    },
    {
      "bioguideId": "S001211",
      "district": "4",
      "firstName": "Greg",
      "fullName": "Rep. Stanton, Greg [D-AZ-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Stanton",
      "party": "D",
      "sponsorshipDate": "2025-12-18",
      "state": "AZ"
    },
    {
      "bioguideId": "C001059",
      "district": "21",
      "firstName": "Jim",
      "fullName": "Rep. Costa, Jim [D-CA-21]",
      "isOriginalCosponsor": "True",
      "lastName": "Costa",
      "party": "D",
      "sponsorshipDate": "2025-12-18",
      "state": "CA"
    },
    {
      "bioguideId": "C001127",
      "district": "20",
      "firstName": "Sheila",
      "fullName": "Rep. Cherfilus-McCormick, Sheila [D-FL-20]",
      "isOriginalCosponsor": "True",
      "lastName": "Cherfilus-McCormick",
      "party": "D",
      "sponsorshipDate": "2025-12-18",
      "state": "FL"
    },
    {
      "bioguideId": "D000631",
      "district": "4",
      "firstName": "Madeleine",
      "fullName": "Rep. Dean, Madeleine [D-PA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Dean",
      "party": "D",
      "sponsorshipDate": "2025-12-18",
      "state": "PA"
    },
    {
      "bioguideId": "A000380",
      "district": "1",
      "firstName": "Gabe",
      "fullName": "Rep. Amo, Gabe [D-RI-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Amo",
      "party": "D",
      "sponsorshipDate": "2025-12-18",
      "state": "RI"
    },
    {
      "bioguideId": "M001217",
      "district": "23",
      "firstName": "Jared",
      "fullName": "Rep. Moskowitz, Jared [D-FL-23]",
      "isOriginalCosponsor": "True",
      "lastName": "Moskowitz",
      "party": "D",
      "sponsorshipDate": "2025-12-18",
      "state": "FL"
    },
    {
      "bioguideId": "O000176",
      "district": "2",
      "firstName": "Johnny",
      "fullName": "Rep. Olszewski, Johnny [D-MD-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Olszewski",
      "party": "D",
      "sponsorshipDate": "2025-12-18",
      "state": "MD"
    },
    {
      "bioguideId": "K000391",
      "district": "8",
      "firstName": "Raja",
      "fullName": "Rep. Krishnamoorthi, Raja [D-IL-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Krishnamoorthi",
      "party": "D",
      "sponsorshipDate": "2025-12-18",
      "state": "IL"
    },
    {
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2025-12-18",
      "state": "NJ"
    },
    {
      "bioguideId": "S000344",
      "district": "32",
      "firstName": "Brad",
      "fullName": "Rep. Sherman, Brad [D-CA-32]",
      "isOriginalCosponsor": "True",
      "lastName": "Sherman",
      "party": "D",
      "sponsorshipDate": "2025-12-18",
      "state": "CA"
    },
    {
      "bioguideId": "M000312",
      "district": "2",
      "firstName": "James",
      "fullName": "Rep. McGovern, James P. [D-MA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "McGovern",
      "middleName": "P.",
      "party": "D",
      "sponsorshipDate": "2026-01-07",
      "state": "MA"
    },
    {
      "bioguideId": "J000310",
      "district": "32",
      "firstName": "Julie",
      "fullName": "Rep. Johnson, Julie [D-TX-32]",
      "isOriginalCosponsor": "False",
      "lastName": "Johnson",
      "party": "D",
      "sponsorshipDate": "2026-01-07",
      "state": "TX"
    },
    {
      "bioguideId": "M001223",
      "district": "2",
      "firstName": "Seth",
      "fullName": "Rep. Magaziner, Seth [D-RI-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Magaziner",
      "party": "D",
      "sponsorshipDate": "2026-04-29",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6879ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6879\nIN THE HOUSE OF REPRESENTATIVES\nDecember 18, 2025 Mr. Meeks (for himself, Ms. Kamlager-Dove , Mr. Castro of Texas , Ms. Titus , Mr. Stanton , Mr. Costa , Mrs. Cherfilus-McCormick , Ms. Dean of Pennsylvania , Mr. Amo , Mr. Moskowitz , Mr. Olszewski , Mr. Krishnamoorthi , Mr. Gottheimer , and Mr. Sherman ) introduced the following bill; which was referred to the Committee on Foreign Affairs\nA BILL\nTo prohibit sales of the most advanced artificial intelligence chips to countries of concern and facilitate the safe and efficient transfer of chips to approved United States persons abroad.\n#### 1. Short title\nThis Act may be cited as the Restoring Export and Security Trade Restrictions for Integrated Circuit Technologies Act or the RESTRICT Act .\n#### 2. Prohibition on exports of advanced integrated circuits to countries of concern\n##### (a) In general\nPart I of the Export Control Reform Act of 2018 ( 50 U.S.C. 4811 et seq. ) is amended by inserting after section 1758 the following:\n1758A. Control of exports of advanced integrated circuits (a) Definitions In this section: (1) Advanced integrated circuit or product (A) In general Subject to subparagraph (B), the term advanced integrated circuit means an integrated circuit, computer, or other product containing such a circuit\u2014 (i) classified under Export Control Classification Number 3A090 or 4A090 or a .z Export Control Classification Number on January 1, 2025; or (ii) that is functionally equivalent or substantially similar to a circuit, computer, or product described in clause (i); and (iii) that is designed or marketed for data centers. (B) Authority to update definition Beginning 24 months after the date of the enactment of this section, to keep pace with technological advancements in computing, the Under Secretary of Commerce for Industry and Security may revise the definition of advanced integrated circuit through notice in the Federal Register, so long as\u2014 (i) the revision poses no adverse impact on the national security of the United States; and (ii) the Under Secretary has consulted with the Committee on Foreign Affairs of the House of Representatives and the Committee on Banking, Housing, and Urban Affairs of the Senate on the proposed change to the definition at least 30 days prior to making the change. (2) Commerce control list The term Commerce Control List means the list set forth in Supplement No. 1 to part 774 of the Export Administration Regulations. (3) Country of concern The term country of concern means\u2014 (A) a country listed in Country Group D:5 in Supplement No. 1 to part 740 of the Export Administration Regulations on January 1, 2025; (B) the Macau Special Administrative Region of the People\u2019s Republic of China; or (C) the Hong Kong Special Administrative Region of the People\u2019s Republic of China. (4) Covered country The term covered country means a country listed in Country Group D in Supplement No. 1 to part 740 of the Export Administration Regulations on January 1, 2025. (5) Approved United States person The term approved United States person means any United States person designated as an approved United States person pursuant to the regulations outlined in subsection (d)(2). (b) License requirement The Under Secretary of Commerce for Industry and Security shall require a license for the export, reexport, or in-country transfer of an advanced integrated circuit or product to a covered country. (c) License policy for countries of concern The Under Secretary of Commerce for Industry and Security shall deny a license for the export, reexport, or in-country transfer of an advanced integrated circuit or product to an entity that is primarily located or headquartered in, or the ultimate parent company of which is headquartered in, a country of concern. (d) Exemption from certain license requirement for approved United States persons (1) In general The license requirement under subsection (b) shall not apply to the export, reexport, or in-country transfer of an advanced integrated circuit or product if the advanced integrated circuit or product\u2014 (A) is destined for a country that is not a country of concern; and (B) remains under the ownership and control of an approved United States person. (2) Implementation Not later than 90 days after the date of the enactment of this section, the Under Secretary of Commerce for Industry and Security shall prescribe regulations\u2014 (A) establishing clear standards and requirements a United States person is mandated to meet to obtain a designation as an approved United States person, which shall include\u2014 (i) a requirement that not more than 10 percent of the ultimate beneficial ownership of the United States person may be held, directly or indirectly, by any entity that primarily resides or is domiciled in a country of concern; (ii) physical security, cybersecurity, remote access security, and other measures designed to prevent the misuse, illicit access, illicit transfer, or diversion of advanced integrated circuits and products; (iii) robust know your customer standards; and (iv) annual audit or attestation requirements to ensure compliance with clauses (i), (ii), and (iii); and (B) describing the process by which the Under Secretary shall approve such a designation. (e) Sunset This section shall terminate on the date that is five years after the date of the enactment of this section. .\n##### (b) Clerical amendments\nThe John S. McCain National Defense Authorization Act for Fiscal Year 2019 is amended\u2014\n**(1)**\nin the table of contents in section 2(b), by inserting after the item relating to section 1758 the following:\nSec. 1758A. Control of exports of advanced integrated circuits. ; and\n**(2)**\nin the table of contents for title XVII of division A, by inserting after the item relating to section 1758 the following:\nSec. 1758A. Control of exports of advanced integrated circuits. .",
      "versionDate": "2025-12-18",
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
        "name": "Foreign Trade and International Finance",
        "updateDate": "2026-01-21T16:27:12Z"
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
      "date": "2025-12-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6879ih.xml"
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
      "title": "RESTRICT Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-21T05:23:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "RESTRICT Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-21T05:23:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Restoring Export and Security Trade Restrictions for Integrated Circuit Technologies Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-21T05:23:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To prohibit sales of the most advanced artificial intelligence chips to countries of concern and facilitate the safe and efficient transfer of chips to approved United States persons abroad.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-21T05:18:30Z"
    }
  ]
}
```
