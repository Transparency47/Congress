# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1880?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1880
- Title: CDFI Bond Guarantee Program Improvement Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1880
- Origin chamber: Senate
- Introduced date: 2025-05-22
- Update date: 2026-05-27T18:38:11Z
- Update date including text: 2026-05-27T18:38:11Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-05-22: Introduced in Senate
- 2025-05-22 - IntroReferral: Introduced in Senate
- 2025-05-22 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.
- Latest action: 2025-05-22: Introduced in Senate

## Actions

- 2025-05-22 - IntroReferral: Introduced in Senate
- 2025-05-22 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-22",
    "latestAction": {
      "actionDate": "2025-05-22",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1880",
    "number": "1880",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "S001203",
        "district": "",
        "firstName": "Tina",
        "fullName": "Sen. Smith, Tina [D-MN]",
        "lastName": "Smith",
        "party": "D",
        "state": "MN"
      }
    ],
    "title": "CDFI Bond Guarantee Program Improvement Act of 2025",
    "type": "S",
    "updateDate": "2026-05-27T18:38:11Z",
    "updateDateIncludingText": "2026-05-27T18:38:11Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-22",
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
      "actionDate": "2025-05-22",
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
          "date": "2025-05-22T17:51:53Z",
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
      "bioguideId": "R000605",
      "firstName": "Mike",
      "fullName": "Sen. Rounds, Mike [R-SD]",
      "isOriginalCosponsor": "True",
      "lastName": "Rounds",
      "party": "R",
      "sponsorshipDate": "2025-05-22",
      "state": "SD"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2025-05-22",
      "state": "NJ"
    },
    {
      "bioguideId": "D000618",
      "firstName": "Steve",
      "fullName": "Sen. Daines, Steve [R-MT]",
      "isOriginalCosponsor": "True",
      "lastName": "Daines",
      "party": "R",
      "sponsorshipDate": "2025-05-22",
      "state": "MT"
    },
    {
      "bioguideId": "S001232",
      "firstName": "Tim",
      "fullName": "Sen. Sheehy, Tim [R-MT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sheehy",
      "party": "R",
      "sponsorshipDate": "2025-05-22",
      "state": "MT"
    },
    {
      "bioguideId": "H000273",
      "firstName": "John",
      "fullName": "Sen. Hickenlooper, John W. [D-CO]",
      "isOriginalCosponsor": "True",
      "lastName": "Hickenlooper",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2025-05-22",
      "state": "CO"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2025-05-22",
      "state": "MN"
    },
    {
      "bioguideId": "H001079",
      "firstName": "Cindy",
      "fullName": "Sen. Hyde-Smith, Cindy [R-MS]",
      "isOriginalCosponsor": "True",
      "lastName": "Hyde-Smith",
      "party": "R",
      "sponsorshipDate": "2025-05-22",
      "state": "MS"
    },
    {
      "bioguideId": "G000574",
      "firstName": "Ruben",
      "fullName": "Sen. Gallego, Ruben [D-AZ]",
      "isOriginalCosponsor": "True",
      "lastName": "Gallego",
      "party": "D",
      "sponsorshipDate": "2025-05-22",
      "state": "AZ"
    },
    {
      "bioguideId": "L000571",
      "firstName": "Cynthia",
      "fullName": "Sen. Lummis, Cynthia M. [R-WY]",
      "isOriginalCosponsor": "True",
      "lastName": "Lummis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-05-22",
      "state": "WY"
    },
    {
      "bioguideId": "B001303",
      "firstName": "Lisa",
      "fullName": "Sen. Blunt Rochester, Lisa [D-DE]",
      "isOriginalCosponsor": "True",
      "lastName": "Blunt Rochester",
      "party": "D",
      "sponsorshipDate": "2025-05-22",
      "state": "DE"
    },
    {
      "bioguideId": "C000880",
      "firstName": "Mike",
      "fullName": "Sen. Crapo, Mike [R-ID]",
      "isOriginalCosponsor": "True",
      "lastName": "Crapo",
      "party": "R",
      "sponsorshipDate": "2025-05-22",
      "state": "ID"
    },
    {
      "bioguideId": "W000805",
      "firstName": "Mark",
      "fullName": "Sen. Warner, Mark R. [D-VA]",
      "isOriginalCosponsor": "False",
      "lastName": "Warner",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-09-11",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1880is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1880\nIN THE SENATE OF THE UNITED STATES\nMay 22, 2025 Ms. Smith (for herself, Mr. Rounds , Mr. Booker , Mr. Daines , Mr. Sheehy , Mr. Hickenlooper , Ms. Klobuchar , Mrs. Hyde-Smith , Mr. Gallego , Ms. Lummis , Ms. Blunt Rochester , and Mr. Crapo ) introduced the following bill; which was read twice and referred to the Committee on Banking, Housing, and Urban Affairs\nA BILL\nTo amend the Community Development Banking and Financial Institutions Act of 1994 to reauthorize and improve the community development financial institutions bond guarantee program, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the CDFI Bond Guarantee Program Improvement Act of 2025 .\n#### 2. Sense of Congress\nIt is the sense of Congress that the authority to guarantee bonds under section 114A of the Community Development Banking and Financial Institutions Act of 1994 ( 12 U.S.C. 4713a ) (commonly referred to as the CDFI Bond Guarantee Program ) provides community development financial institutions with a sustainable source of long-term capital and furthers the mission of the Community Development Financial Institutions Fund (established under section 104(a) of such Act ( 12 U.S.C. 4703(a) ) to increase economic opportunity and promote community development investments for underserved populations and distressed communities in the United States.\n#### 3. Guarantees for bonds and notes issued for community or economic development purposes\n##### (a) In general\nSection 114A of the Community Development Banking and Financial Institutions Act of 1994 ( 12 U.S.C. 4713a ) is amended\u2014\n**(1)**\nin subsection (c)(2), by striking , multiplied by an amount equal to the outstanding principal balance of issued notes or bonds ;\n**(2)**\nby amending subsection (e)(2) to read as follows:\n(2) Limitation on guarantee amount The Secretary may not guarantee any amount under the program equal to less than $25,000,000, but the total of all such guarantees in any fiscal year may not exceed $1,000,000,000. ; and\n**(3)**\nin subsection (k), by striking September 30, 2014 and inserting the date that is 4 years after the date of enactment of the CDFI Bond Guarantee Program Improvement Act of 2025 .\n##### (b) Clerical amendment\nThe table of contents in section 1(b) of the Riegle Community Development and Regulatory Improvement Act of 1994 ( Public Law 103\u2013315 ; 108 Stat. 2160) is amended by inserting after the item relating to section 114 the following:\nSec. 114A. Guarantees for bonds and notes issued for community or economic development purposes. .\n#### 4. Report on the CDFI bond guarantee program\nNot later than 1 year after the date of enactment of this Act, and not later than 3 years after such date of enactment, the Secretary of the Treasury shall issue a report to the Committee on Banking, Housing, and Urban Affairs of the Senate and the Committee on Financial Services of the House of Representatives on the effectiveness of the CDFI bond guarantee program established under section 114A of the Community Development Banking and Financial Institutions Act of 1994 ( 12 U.S.C. 4713a ).",
      "versionDate": "2025-05-22",
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
        "name": "Finance and Financial Sector",
        "updateDate": "2025-06-13T17:56:07Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-05-22",
    "originChamber": "Senate",
    "payload": {
      "dublinCore": {
        "contributor": "Congressional Research Service, Library of Congress",
        "description": "This file contains bill summaries for federal legislation. A bill summary describes the most significant provisions of a piece of legislation and details the effects the legislative text may have on current law and federal programs. Bill summaries are authored by the Congressional Research Service (CRS) of the Library of Congress. As stated in Public Law 91-510 (2 USC 166 (d)(6)), one of the duties of CRS is \"to prepare summaries and digests of bills and resolutions of a public general nature introduced in the Senate or House of Representatives\". For more information, refer to the User Guide that accompanies this file.",
        "format": "text/xml",
        "language": "EN",
        "rights": "Pursuant to Title 17 Section 105 of the United States Code, this file is not subject to copyright protection and is in the public domain."
      },
      "item": {
        "@attributes": {
          "congress": "119",
          "measure-id": "id119s1880",
          "measure-number": "1880",
          "measure-type": "s",
          "orig-publish-date": "2025-05-22",
          "originChamber": "SENATE",
          "update-date": "2026-05-27"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s1880v00",
            "update-date": "2026-05-27"
          },
          "action-date": "2025-05-22",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>CDFI Bond Guarantee Program Improvement Act of 2025</strong></p><p>This bill reauthorizes the Community Development Financial Institutions (CDFI) Bond Guarantee Program for four years and revises it to allow for a greater number of participants.\u00a0</p><p>CDFIs are financial institutions serving low-income communities. Designation as a CDFI allows an institution to participate in programs such as the CDFI Bond Guarantee Program. The program provides CDFIs with financing for community and economic development projects through federal credit subsidies that allow CDFIs to issue bonds.</p><p>The bill (1) reduces the program\u2019s minimum loan amount from $100 million to $25 million, (2) eliminates the cap on the annual number of guarantees, and (3) revises\u00a0the maximum amount that may be held in a\u00a0CDFI's relending account for secondary loans.</p>"
        },
        "title": "CDFI Bond Guarantee Program Improvement Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s1880.xml",
    "summary": {
      "actionDate": "2025-05-22",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>CDFI Bond Guarantee Program Improvement Act of 2025</strong></p><p>This bill reauthorizes the Community Development Financial Institutions (CDFI) Bond Guarantee Program for four years and revises it to allow for a greater number of participants.\u00a0</p><p>CDFIs are financial institutions serving low-income communities. Designation as a CDFI allows an institution to participate in programs such as the CDFI Bond Guarantee Program. The program provides CDFIs with financing for community and economic development projects through federal credit subsidies that allow CDFIs to issue bonds.</p><p>The bill (1) reduces the program\u2019s minimum loan amount from $100 million to $25 million, (2) eliminates the cap on the annual number of guarantees, and (3) revises\u00a0the maximum amount that may be held in a\u00a0CDFI's relending account for secondary loans.</p>",
      "updateDate": "2026-05-27",
      "versionCode": "id119s1880"
    },
    "title": "CDFI Bond Guarantee Program Improvement Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-05-22",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>CDFI Bond Guarantee Program Improvement Act of 2025</strong></p><p>This bill reauthorizes the Community Development Financial Institutions (CDFI) Bond Guarantee Program for four years and revises it to allow for a greater number of participants.\u00a0</p><p>CDFIs are financial institutions serving low-income communities. Designation as a CDFI allows an institution to participate in programs such as the CDFI Bond Guarantee Program. The program provides CDFIs with financing for community and economic development projects through federal credit subsidies that allow CDFIs to issue bonds.</p><p>The bill (1) reduces the program\u2019s minimum loan amount from $100 million to $25 million, (2) eliminates the cap on the annual number of guarantees, and (3) revises\u00a0the maximum amount that may be held in a\u00a0CDFI's relending account for secondary loans.</p>",
      "updateDate": "2026-05-27",
      "versionCode": "id119s1880"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-05-22",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1880is.xml"
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
      "title": "CDFI Bond Guarantee Program Improvement Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-12T11:03:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "CDFI Bond Guarantee Program Improvement Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-04T03:23:26Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Community Development Banking and Financial Institutions Act of 1994 to reauthorize and improve the community development financial institutions bond guarantee program, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-04T03:18:41Z"
    }
  ]
}
```
