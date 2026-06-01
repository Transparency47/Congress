# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1207?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/1207
- Title: Feral Swine Eradication Act
- Congress: 119
- Bill type: S
- Bill number: 1207
- Origin chamber: Senate
- Introduced date: 2025-03-31
- Update date: 2025-06-09T15:45:41Z
- Update date including text: 2025-06-09T15:45:41Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-03-31: Introduced in Senate
- 2025-03-31 - IntroReferral: Introduced in Senate
- 2025-03-31 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.
- Latest action: 2025-03-31: Introduced in Senate

## Actions

- 2025-03-31 - IntroReferral: Introduced in Senate
- 2025-03-31 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-31",
    "latestAction": {
      "actionDate": "2025-03-31",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/1207",
    "number": "1207",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "C001056",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Cornyn, John [R-TX]",
        "lastName": "Cornyn",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "Feral Swine Eradication Act",
    "type": "S",
    "updateDate": "2025-06-09T15:45:41Z",
    "updateDateIncludingText": "2025-06-09T15:45:41Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-31",
      "committees": {
        "item": {
          "name": "Agriculture, Nutrition, and Forestry Committee",
          "systemCode": "ssaf00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-03-31",
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
          "date": "2025-03-31T20:57:36Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Agriculture, Nutrition, and Forestry Committee",
      "systemCode": "ssaf00",
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
      "bioguideId": "L000570",
      "firstName": "Ben",
      "fullName": "Sen. Lujan, Ben Ray [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Luj\u00e1n",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-03-31",
      "state": "NM"
    },
    {
      "bioguideId": "T000278",
      "firstName": "Tommy",
      "fullName": "Sen. Tuberville, Tommy [R-AL]",
      "isOriginalCosponsor": "True",
      "lastName": "Tuberville",
      "party": "R",
      "sponsorshipDate": "2025-03-31",
      "state": "AL"
    },
    {
      "bioguideId": "W000790",
      "firstName": "Raphael",
      "fullName": "Sen. Warnock, Raphael G. [D-GA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warnock",
      "party": "D",
      "sponsorshipDate": "2025-03-31",
      "state": "GA"
    },
    {
      "bioguideId": "B001319",
      "firstName": "Katie",
      "fullName": "Sen. Britt, Katie Boyd [R-AL]",
      "isOriginalCosponsor": "True",
      "lastName": "Britt",
      "party": "R",
      "sponsorshipDate": "2025-03-31",
      "state": "AL"
    },
    {
      "bioguideId": "O000174",
      "firstName": "Jon",
      "fullName": "Sen. Ossoff, Jon [D-GA]",
      "isOriginalCosponsor": "True",
      "lastName": "Ossoff",
      "party": "D",
      "sponsorshipDate": "2025-03-31",
      "state": "GA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1207is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1207\nIN THE SENATE OF THE UNITED STATES\nMarch 31, 2025 Mr. Cornyn (for himself, Mr. Luj\u00e1n , Mr. Tuberville , Mr. Warnock , Mrs. Britt , and Mr. Ossoff ) introduced the following bill; which was read twice and referred to the Committee on Agriculture, Nutrition, and Forestry\nA BILL\nTo amend the Agriculture Improvement Act of 2018 to reauthorize the feral swine eradication and control pilot program, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Feral Swine Eradication Act .\n#### 2. Feral swine eradication and control program\n##### (a) In general\nSection 2408 of the Agriculture Improvement Act of 2018 ( 7 U.S.C. 8351 note; Public Law 115\u2013334 ) is amended\u2014\n**(1)**\nin the section heading, by striking pilot ;\n**(2)**\nin subsection (a), by striking pilot program and inserting program (referred to in this section as the program ) ;\n**(3)**\nin subsection (b)\u2014\n**(A)**\nin the matter preceding paragraph (1), by striking pilot ;\n**(B)**\nin each of paragraphs (1) and (2), by striking the pilot areas and inserting eligible areas ;\n**(C)**\nin paragraph (4), by striking pilot and inserting eligible ;\n**(D)**\nby redesignating paragraphs (3) and (4) as paragraphs (4) and (5), respectively; and\n**(E)**\nby inserting after paragraph (2) the following:\n(3) after the Secretary determines that feral swine have been eradicated from an eligible area, require the Animal and Plant Health Inspection Service and the Natural Resources Conservation Service to continue monitoring the eligible area for the reoccurrence of feral swine for a period of 1 year; ;\n**(4)**\nin each of subsections (c), (e), (f), and (g), by striking pilot program each place it appears and inserting program ;\n**(5)**\nin subsection (c)(1), by striking the pilot areas and inserting eligible areas ;\n**(6)**\nby striking subsection (e) and inserting the following:\n(e) Definition of eligible area In this section, the term eligible area means an area of a State in which feral swine have been identified as a threat to agriculture, native ecosystems, or human or animal health, as determined by the Secretary. ;\n**(7)**\nin subsection (g)\u2014\n**(A)**\nin paragraph (1)\u2014\n**(i)**\nby striking 2023 and and inserting 2023, ; and\n**(ii)**\nby striking the period at the end and inserting , and $75,000,000 for the period of fiscal years 2025 through 2030. ; and\n**(B)**\nin paragraph (2)\u2014\n**(i)**\nin subparagraph (A), by striking 50 and inserting 40 ; and\n**(ii)**\nin subparagraph (B), by striking 50 and inserting 60 ; and\n**(8)**\nby adding at the end the following:\n(h) Reports Not later than 2 years, and not later than 4 years and 6 months, after the date of enactment of this subsection, the Administrator of the Animal and Plant Health Inspection Service and the Chief of the Natural Resources Conservation Service, acting jointly, shall submit to the Committee on Agriculture, Nutrition, and Forestry of the Senate and the Committee on Agriculture of the House of Representatives and make publicly available on the website of the Department of Agriculture a report that\u2014 (1) describes, for the period beginning on the date of the establishment of the program and ending on the date of the submission of the report\u2014 (A) activities carried out under the program, including\u2014 (i) the number of counties in which feral swine are no longer present; and (ii) estimated reductions in agriculture and natural resource damage, and improvements to human and livestock health and safety, as a result of feral swine removal; (B) the use of funding made available under this section, including the number of counties in each State provided funding; and (C) the roles of the Animal and Plant Health Inspection Service and the Natural Resources Conservation Service and agricultural producers provided financial assistance under this section in carrying out activities under the program; and (2) includes\u2014 (A) a determination by the Administrator of the Animal and Plant Health Inspection Service and the Chief of the Natural Resources Conservation Service as to the extent to which the program has been successful; and (B) any recommendations for improvements to the program. .\n##### (b) Conforming amendment\nThe table of contents for the Agriculture Improvement Act of 2018 ( Public Law 115\u2013334 ; 132 Stat. 4491) is amended by striking the item relating to section 2408 and inserting the following:\nSec. 2408. Feral swine eradication and control program. .",
      "versionDate": "2025-03-31",
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
        "name": "Agriculture and Food",
        "updateDate": "2025-05-06T20:21:25Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-31",
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
          "measure-id": "id119s1207",
          "measure-number": "1207",
          "measure-type": "s",
          "orig-publish-date": "2025-03-31",
          "originChamber": "SENATE",
          "update-date": "2025-06-09"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s1207v00",
            "update-date": "2025-06-09"
          },
          "action-date": "2025-03-31",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Feral Swine Eradication Act</strong></p><p>This bill reauthorizes\u00a0the Feral Swine Eradication and Control Pilot Program through FY2030\u00a0and removes the pilot program designation. This Department of Agriculture (USDA) program responds to the threat feral swine pose to agriculture, native ecosystems, and human and animal health.</p><p>In addition, USDA must require\u00a0the Animal and Plant Health Inspection Service (APHIS) and the Natural Resources Conservation Service (NRCS)\u00a0to\u00a0continue monitoring an\u00a0area for reoccurrence of feral swine for one year after USDA determines that feral swine has been eradicated from\u00a0an eligible\u00a0area.</p><p>The bill requires 60% of the funds provided for the program to be allocated to APHIS and 40% of the funds to be allocated to the NRCS. (Under current law, the funds are divided evenly between APHIS and\u00a0the NRCS).\u00a0</p><p>Further, the bill includes new reporting requirements, which direct APHIS and the NRCS to submit a joint report to Congress on the program. This report must be publicly available on USDA's website.</p>"
        },
        "title": "Feral Swine Eradication Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s1207.xml",
    "summary": {
      "actionDate": "2025-03-31",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Feral Swine Eradication Act</strong></p><p>This bill reauthorizes\u00a0the Feral Swine Eradication and Control Pilot Program through FY2030\u00a0and removes the pilot program designation. This Department of Agriculture (USDA) program responds to the threat feral swine pose to agriculture, native ecosystems, and human and animal health.</p><p>In addition, USDA must require\u00a0the Animal and Plant Health Inspection Service (APHIS) and the Natural Resources Conservation Service (NRCS)\u00a0to\u00a0continue monitoring an\u00a0area for reoccurrence of feral swine for one year after USDA determines that feral swine has been eradicated from\u00a0an eligible\u00a0area.</p><p>The bill requires 60% of the funds provided for the program to be allocated to APHIS and 40% of the funds to be allocated to the NRCS. (Under current law, the funds are divided evenly between APHIS and\u00a0the NRCS).\u00a0</p><p>Further, the bill includes new reporting requirements, which direct APHIS and the NRCS to submit a joint report to Congress on the program. This report must be publicly available on USDA's website.</p>",
      "updateDate": "2025-06-09",
      "versionCode": "id119s1207"
    },
    "title": "Feral Swine Eradication Act"
  },
  "summaries": [
    {
      "actionDate": "2025-03-31",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Feral Swine Eradication Act</strong></p><p>This bill reauthorizes\u00a0the Feral Swine Eradication and Control Pilot Program through FY2030\u00a0and removes the pilot program designation. This Department of Agriculture (USDA) program responds to the threat feral swine pose to agriculture, native ecosystems, and human and animal health.</p><p>In addition, USDA must require\u00a0the Animal and Plant Health Inspection Service (APHIS) and the Natural Resources Conservation Service (NRCS)\u00a0to\u00a0continue monitoring an\u00a0area for reoccurrence of feral swine for one year after USDA determines that feral swine has been eradicated from\u00a0an eligible\u00a0area.</p><p>The bill requires 60% of the funds provided for the program to be allocated to APHIS and 40% of the funds to be allocated to the NRCS. (Under current law, the funds are divided evenly between APHIS and\u00a0the NRCS).\u00a0</p><p>Further, the bill includes new reporting requirements, which direct APHIS and the NRCS to submit a joint report to Congress on the program. This report must be publicly available on USDA's website.</p>",
      "updateDate": "2025-06-09",
      "versionCode": "id119s1207"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-31",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1207is.xml"
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
      "title": "Feral Swine Eradication Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-15T04:23:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Feral Swine Eradication Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-15T04:23:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Agriculture Improvement Act of 2018 to reauthorize the feral swine eradication and control pilot program, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-15T04:19:06Z"
    }
  ]
}
```
