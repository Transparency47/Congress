# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/756?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/756
- Title: Freedom to Invest in Tomorrow’s Workforce Act
- Congress: 119
- Bill type: S
- Bill number: 756
- Origin chamber: Senate
- Introduced date: 2025-02-26
- Update date: 2025-12-06T06:38:13Z
- Update date including text: 2025-12-06T06:38:13Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-26: Introduced in Senate
- 2025-02-26 - IntroReferral: Introduced in Senate
- 2025-02-26 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-02-26: Introduced in Senate

## Actions

- 2025-02-26 - IntroReferral: Introduced in Senate
- 2025-02-26 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-26",
    "latestAction": {
      "actionDate": "2025-02-26",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/756",
    "number": "756",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "K000367",
        "district": "",
        "firstName": "Amy",
        "fullName": "Sen. Klobuchar, Amy [D-MN]",
        "lastName": "Klobuchar",
        "party": "D",
        "state": "MN"
      }
    ],
    "title": "Freedom to Invest in Tomorrow\u2019s Workforce Act",
    "type": "S",
    "updateDate": "2025-12-06T06:38:13Z",
    "updateDateIncludingText": "2025-12-06T06:38:13Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-26",
      "committees": {
        "item": {
          "name": "Finance Committee",
          "systemCode": "ssfi00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Finance.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-02-26",
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
          "date": "2025-02-26T21:18:13Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Finance Committee",
      "systemCode": "ssfi00",
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
      "bioguideId": "M001198",
      "firstName": "Roger",
      "fullName": "Sen. Marshall, Roger [R-KS]",
      "isOriginalCosponsor": "True",
      "lastName": "Marshall",
      "party": "R",
      "sponsorshipDate": "2025-02-26",
      "state": "KS"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "VT"
    },
    {
      "bioguideId": "C001035",
      "firstName": "Susan",
      "fullName": "Sen. Collins, Susan M. [R-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "Collins",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-02-26",
      "state": "ME"
    },
    {
      "bioguideId": "H000273",
      "firstName": "John",
      "fullName": "Sen. Hickenlooper, John W. [D-CO]",
      "isOriginalCosponsor": "False",
      "lastName": "Hickenlooper",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2025-04-28",
      "state": "CO"
    },
    {
      "bioguideId": "T000476",
      "firstName": "Thomas",
      "fullName": "Sen. Tillis, Thomas [R-NC]",
      "isOriginalCosponsor": "False",
      "lastName": "Tillis",
      "middleName": "Roland",
      "party": "R",
      "sponsorshipDate": "2025-04-28",
      "state": "NC"
    },
    {
      "bioguideId": "K000383",
      "firstName": "Angus",
      "fullName": "Sen. King, Angus S., Jr. [I-ME]",
      "isOriginalCosponsor": "False",
      "lastName": "King",
      "middleName": "S.",
      "party": "I",
      "sponsorshipDate": "2025-04-28",
      "state": "ME"
    },
    {
      "bioguideId": "S001198",
      "firstName": "Dan",
      "fullName": "Sen. Sullivan, Dan [R-AK]",
      "isOriginalCosponsor": "False",
      "lastName": "Sullivan",
      "party": "R",
      "sponsorshipDate": "2025-04-28",
      "state": "AK"
    },
    {
      "bioguideId": "K000377",
      "firstName": "Mark",
      "fullName": "Sen. Kelly, Mark [D-AZ]",
      "isOriginalCosponsor": "False",
      "lastName": "Kelly",
      "party": "D",
      "sponsorshipDate": "2025-04-28",
      "state": "AZ"
    },
    {
      "bioguideId": "T000278",
      "firstName": "Tommy",
      "fullName": "Sen. Tuberville, Tommy [R-AL]",
      "isOriginalCosponsor": "False",
      "lastName": "Tuberville",
      "party": "R",
      "sponsorshipDate": "2025-04-30",
      "state": "AL"
    },
    {
      "bioguideId": "F000479",
      "firstName": "John",
      "fullName": "Sen. Fetterman, John [D-PA]",
      "isOriginalCosponsor": "False",
      "lastName": "Fetterman",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-04-30",
      "state": "PA"
    },
    {
      "bioguideId": "S001227",
      "firstName": "Eric",
      "fullName": "Sen. Schmitt, Eric [R-MO]",
      "isOriginalCosponsor": "False",
      "lastName": "Schmitt",
      "middleName": "S.",
      "party": "R",
      "sponsorshipDate": "2025-04-30",
      "state": "MO"
    },
    {
      "bioguideId": "D000622",
      "firstName": "Tammy",
      "fullName": "Sen. Duckworth, Tammy [D-IL]",
      "isOriginalCosponsor": "False",
      "lastName": "Duckworth",
      "party": "D",
      "sponsorshipDate": "2025-04-30",
      "state": "IL"
    },
    {
      "bioguideId": "B001319",
      "firstName": "Katie",
      "fullName": "Sen. Britt, Katie Boyd [R-AL]",
      "isOriginalCosponsor": "False",
      "lastName": "Britt",
      "party": "R",
      "sponsorshipDate": "2025-04-30",
      "state": "AL"
    },
    {
      "bioguideId": "M000934",
      "firstName": "Jerry",
      "fullName": "Sen. Moran, Jerry [R-KS]",
      "isOriginalCosponsor": "False",
      "lastName": "Moran",
      "party": "R",
      "sponsorshipDate": "2025-05-21",
      "state": "KS"
    },
    {
      "bioguideId": "H001079",
      "firstName": "Cindy",
      "fullName": "Sen. Hyde-Smith, Cindy [R-MS]",
      "isOriginalCosponsor": "False",
      "lastName": "Hyde-Smith",
      "party": "R",
      "sponsorshipDate": "2025-06-03",
      "state": "MS"
    },
    {
      "bioguideId": "R000608",
      "firstName": "Jacky",
      "fullName": "Sen. Rosen, Jacky [D-NV]",
      "isOriginalCosponsor": "False",
      "lastName": "Rosen",
      "party": "D",
      "sponsorshipDate": "2025-06-05",
      "state": "NV"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s756is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 756\nIN THE SENATE OF THE UNITED STATES\nFebruary 26, 2025 Ms. Klobuchar (for herself, Mr. Marshall , Mr. Welch , and Ms. Collins ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend the Internal Revenue Code of 1986 to treat certain postsecondary credentialing expenses as qualified higher education expenses for purposes of 529 accounts.\n#### 1. Short title\nThis Act may be cited as the Freedom to Invest in Tomorrow\u2019s Workforce Act .\n#### 2. Certain postsecondary credentialing expenses treated as qualified higher education expenses for purposes of 529 accounts\n##### (a) In general\nSection 529(e)(3) of the Internal Revenue Code of 1986 is amended by adding at the end the following new subparagraph:\n(C) Certain postsecondary credentialing expenses The term qualified higher education expenses includes qualified postsecondary credentialing expenses (as defined in subsection (f)). .\n##### (b) Qualified postsecondary credentialing expenses\nSection 529 of such Code is amended by redesignating subsection (f) as subsection (g) and by inserting after subsection (e) the following new subsection:\n(f) Qualified postsecondary credentialing expenses For purposes of this section\u2014 (1) In general The term qualified postsecondary credentialing expenses means\u2014 (A) tuition, fees, books, supplies, and equipment required for the enrollment or attendance of a designated beneficiary in a recognized postsecondary credential program, or any other expense incurred in connection with enrollment in or attendance at a recognized postsecondary credential program if such expense would, if incurred in connection with enrollment or attendance at an eligible educational institution, be covered under subsection (e)(3)(A), (B) fees for testing if such testing is required to obtain or maintain a recognized postsecondary credential, and (C) fees for continuing education if such education is required to maintain a recognized postsecondary credential. (2) Recognized postsecondary credential program The term recognized postsecondary credential program means any program to obtain a recognized postsecondary credential if\u2014 (A) such program is included on a State list prepared under section 122(d) of the Workforce Innovation and Opportunity Act ( 29 U.S.C. 3152(d) ), (B) such program is listed in the public directory of the Web Enabled Approval Management System (WEAMS) of the Veterans Benefits Administration, or successor directory such program, (C) an examination (developed or administered by an organization widely recognized as providing reputable credentials in the occupation) is required to obtain or maintain such credential and such organization recognizes such program as providing training or education which prepares individuals to take such examination, or (D) such program is identified by the Secretary, after consultation with the Secretary of Labor, as being a reputable program for obtaining a recognized postsecondary credential for purposes of this subparagraph. (3) Recognized postsecondary credential The term recognized postsecondary credential means\u2014 (A) any postsecondary employment credential that is industry recognized and is\u2014 (i) any postsecondary employment credential issued by a program that is accredited by the Institute for Credentialing Excellence, the National Commission on Certifying Agencies, or the American National Standards Institute, (ii) any postsecondary employment credential that is included in the Credentialing Opportunities On-Line (COOL) directory of credentialing programs (or successor directory) maintained by the Department of Defense or by any branch of the Armed Forces, or (iii) any postsecondary employment credential identified for purposes of this clause by the Secretary, after consultation with the Secretary of Labor, as being industry recognized, (B) any certificate of completion of an apprenticeship that is registered and certified with the Secretary of Labor under the Act of August 16, 1937 (commonly known as the National Apprenticeship Act ; 50 Stat. 664, chapter 663; 29 U.S.C. 50 et seq. ), (C) any occupational or professional license issued or recognized by a State or the Federal Government (and any certification that satisfies a condition for obtaining such a license), and (D) any recognized postsecondary credential as defined in section 3(52) of the Workforce Innovation and Opportunity Act ( 29 U.S.C. 3102(52) ), provided through a program described in paragraph (2)(A). .\n##### (c) Effective date\nThe amendments made by this section shall apply to distributions made after the date of the enactment of this Act.",
      "versionDate": "2025-02-26",
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
        "actionDate": "2025-02-07",
        "text": "Referred to the House Committee on Ways and Means."
      },
      "number": "1151",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Freedom to Invest in Tomorrow\u2019s Workforce Act",
      "type": "HR"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-07-04",
        "text": "Became Public Law No: 119-21."
      },
      "number": "1",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "An act to provide for reconciliation pursuant to title II of H. Con. Res. 14.",
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
        "name": "Taxation",
        "updateDate": "2025-05-07T19:55:19Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-26",
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
          "measure-id": "id119s756",
          "measure-number": "756",
          "measure-type": "s",
          "orig-publish-date": "2025-02-26",
          "originChamber": "SENATE",
          "update-date": "2025-09-24"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s756v00",
            "update-date": "2025-09-24"
          },
          "action-date": "2025-02-26",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Freedom to Invest in Tomorrow\u2019s Workforce Act</strong></p><p>This bill expands the expenses eligible for tax-free withdrawals from a qualified tuition program (known as a 529 plan) to include tuition, fees (including test fees), books, supplies, equipment, and other expenses related to the enrollment or attendance in a recognized\u00a0postsecondary credentialing program.</p><p>Under the bill, a recognized\u00a0postsecondary credentialing program includes certain programs identified by a state as providing training services, a program listed in the Web Enabled Approval Management System (WEAMS) maintained by the Department of Veterans Affairs, certain examinations required to obtain or maintain a credential, and other reputable credentialing programs.</p><p>Further, under the bill, such programs must be designed for an individual to obtain</p><ul><li>an industry-recognized postsecondary employment credential (e.g., project management professional certificate, advanced emergency medical technician certificate, and welding supervisor certificate),</li><li>a certificate of completion of a registered and certified apprenticeship,</li><li>an occupational or professional license issued or recognized by a state or the federal government (and any certification required for obtaining such license), or</li><li>an associate or baccalaureate degree.\u00a0</li></ul>"
        },
        "title": "Freedom to Invest in Tomorrow\u2019s Workforce Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s756.xml",
    "summary": {
      "actionDate": "2025-02-26",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Freedom to Invest in Tomorrow\u2019s Workforce Act</strong></p><p>This bill expands the expenses eligible for tax-free withdrawals from a qualified tuition program (known as a 529 plan) to include tuition, fees (including test fees), books, supplies, equipment, and other expenses related to the enrollment or attendance in a recognized\u00a0postsecondary credentialing program.</p><p>Under the bill, a recognized\u00a0postsecondary credentialing program includes certain programs identified by a state as providing training services, a program listed in the Web Enabled Approval Management System (WEAMS) maintained by the Department of Veterans Affairs, certain examinations required to obtain or maintain a credential, and other reputable credentialing programs.</p><p>Further, under the bill, such programs must be designed for an individual to obtain</p><ul><li>an industry-recognized postsecondary employment credential (e.g., project management professional certificate, advanced emergency medical technician certificate, and welding supervisor certificate),</li><li>a certificate of completion of a registered and certified apprenticeship,</li><li>an occupational or professional license issued or recognized by a state or the federal government (and any certification required for obtaining such license), or</li><li>an associate or baccalaureate degree.\u00a0</li></ul>",
      "updateDate": "2025-09-24",
      "versionCode": "id119s756"
    },
    "title": "Freedom to Invest in Tomorrow\u2019s Workforce Act"
  },
  "summaries": [
    {
      "actionDate": "2025-02-26",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Freedom to Invest in Tomorrow\u2019s Workforce Act</strong></p><p>This bill expands the expenses eligible for tax-free withdrawals from a qualified tuition program (known as a 529 plan) to include tuition, fees (including test fees), books, supplies, equipment, and other expenses related to the enrollment or attendance in a recognized\u00a0postsecondary credentialing program.</p><p>Under the bill, a recognized\u00a0postsecondary credentialing program includes certain programs identified by a state as providing training services, a program listed in the Web Enabled Approval Management System (WEAMS) maintained by the Department of Veterans Affairs, certain examinations required to obtain or maintain a credential, and other reputable credentialing programs.</p><p>Further, under the bill, such programs must be designed for an individual to obtain</p><ul><li>an industry-recognized postsecondary employment credential (e.g., project management professional certificate, advanced emergency medical technician certificate, and welding supervisor certificate),</li><li>a certificate of completion of a registered and certified apprenticeship,</li><li>an occupational or professional license issued or recognized by a state or the federal government (and any certification required for obtaining such license), or</li><li>an associate or baccalaureate degree.\u00a0</li></ul>",
      "updateDate": "2025-09-24",
      "versionCode": "id119s756"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-26",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s756is.xml"
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
      "title": "Freedom to Invest in Tomorrow\u2019s Workforce Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-06T11:03:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Freedom to Invest in Tomorrow\u2019s Workforce Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-21T04:08:26Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Internal Revenue Code of 1986 to treat certain postsecondary credentialing expenses as qualified higher education expenses for purposes of 529 accounts.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-21T04:04:32Z"
    }
  ]
}
```
