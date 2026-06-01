# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2833?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2833
- Title: Adoption Tax Credit Refundability Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 2833
- Origin chamber: House
- Introduced date: 2025-04-10
- Update date: 2026-03-17T16:15:51Z
- Update date including text: 2026-03-17T16:15:51Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-04-10: Introduced in House
- 2025-04-10 - IntroReferral: Introduced in House
- 2025-04-10 - IntroReferral: Introduced in House
- 2025-04-10 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-04-10: Introduced in House

## Actions

- 2025-04-10 - IntroReferral: Introduced in House
- 2025-04-10 - IntroReferral: Introduced in House
- 2025-04-10 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-10",
    "latestAction": {
      "actionDate": "2025-04-10",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2833",
    "number": "2833",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "D000096",
        "district": "7",
        "firstName": "Danny",
        "fullName": "Rep. Davis, Danny K. [D-IL-7]",
        "lastName": "Davis",
        "party": "D",
        "state": "IL"
      }
    ],
    "title": "Adoption Tax Credit Refundability Act of 2025",
    "type": "HR",
    "updateDate": "2026-03-17T16:15:51Z",
    "updateDateIncludingText": "2026-03-17T16:15:51Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-10",
      "committees": {
        "item": {
          "name": "Ways and Means Committee",
          "systemCode": "hswm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Ways and Means.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-04-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-10",
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
          "date": "2025-04-10T13:07:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
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
      "bioguideId": "M001213",
      "district": "1",
      "firstName": "Blake",
      "fullName": "Rep. Moore, Blake D. [R-UT-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Moore",
      "middleName": "D.",
      "party": "R",
      "sponsorshipDate": "2025-04-10",
      "state": "UT"
    },
    {
      "bioguideId": "M001160",
      "district": "4",
      "firstName": "Gwen",
      "fullName": "Rep. Moore, Gwen [D-WI-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Moore",
      "party": "D",
      "sponsorshipDate": "2025-04-10",
      "state": "WI"
    },
    {
      "bioguideId": "F000446",
      "district": "4",
      "firstName": "Randy",
      "fullName": "Rep. Feenstra, Randy [R-IA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Feenstra",
      "party": "R",
      "sponsorshipDate": "2025-04-10",
      "state": "IA"
    },
    {
      "bioguideId": "B001298",
      "district": "2",
      "firstName": "Don",
      "fullName": "Rep. Bacon, Don [R-NE-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Bacon",
      "party": "R",
      "sponsorshipDate": "2025-04-10",
      "state": "NE"
    },
    {
      "bioguideId": "K000400",
      "district": "37",
      "firstName": "Sydney",
      "fullName": "Rep. Kamlager-Dove, Sydney [D-CA-37]",
      "isOriginalCosponsor": "True",
      "lastName": "Kamlager-Dove",
      "party": "D",
      "sponsorshipDate": "2025-04-10",
      "state": "CA"
    },
    {
      "bioguideId": "A000055",
      "district": "4",
      "firstName": "Robert",
      "fullName": "Rep. Aderholt, Robert B. [R-AL-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Aderholt",
      "middleName": "B.",
      "party": "R",
      "sponsorshipDate": "2025-04-10",
      "state": "AL"
    },
    {
      "bioguideId": "B001292",
      "district": "8",
      "firstName": "Donald",
      "fullName": "Rep. Beyer, Donald S. [D-VA-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Beyer",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-04-10",
      "state": "VA"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-04-21",
      "state": "PA"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2025-05-29",
      "state": "DC"
    },
    {
      "bioguideId": "C001119",
      "district": "2",
      "firstName": "Angie",
      "fullName": "Rep. Craig, Angie [D-MN-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Craig",
      "party": "D",
      "sponsorshipDate": "2025-06-03",
      "state": "MN"
    },
    {
      "bioguideId": "S001212",
      "district": "8",
      "firstName": "Pete",
      "fullName": "Rep. Stauber, Pete [R-MN-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Stauber",
      "party": "R",
      "sponsorshipDate": "2025-06-03",
      "state": "MN"
    },
    {
      "bioguideId": "P000607",
      "district": "2",
      "firstName": "Mark",
      "fullName": "Rep. Pocan, Mark [D-WI-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Pocan",
      "party": "D",
      "sponsorshipDate": "2025-06-23",
      "state": "WI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2833ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2833\nIN THE HOUSE OF REPRESENTATIVES\nApril 10, 2025 Mr. Davis of Illinois (for himself, Mr. Moore of Utah , Ms. Moore of Wisconsin , Mr. Feenstra , Mr. Bacon , Ms. Kamlager-Dove , Mr. Aderholt , and Mr. Beyer ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to provide for a refundable adoption tax credit.\n#### 1. Short title\nThis Act may be cited as the Adoption Tax Credit Refundability Act of 2025 .\n#### 2. Refundable adoption tax credit\n##### (a) Credit made refundable\n**(1) Credit moved to subpart relating to refundable credits**\nThe Internal Revenue Code of 1986 is amended\u2014\n**(A)**\nby redesignating section 23 as section 36C, and\n**(B)**\nby moving section 36C (as so redesignated) from subpart A of part IV of subchapter A of chapter 1 to the location immediately before section 37 in subpart C of part IV of subchapter A of chapter 1.\n**(2) Conforming Amendments**\n**(A)**\nSection 25(e)(1)(C) of such Code is amended by striking sections 23 and 25D and inserting section 25D .\n**(B)**\nSection 36C of such Code, as so redesignated, is amended\u2014\n**(i)**\nin subsection (b)(2)(A), by striking (determined without regard to subsection (c)) ,\n**(ii)**\nby striking subsection (c), and\n**(iii)**\nby redesignating subsections (d) through (i) as subsections (c) through (h), respectively.\n**(C)**\nSection 137 of such Code is amended\u2014\n**(i)**\nin subsection (d), by striking section 23(d) and inserting section 36C(c) , and\n**(ii)**\nin subsection (e), by striking subsections (e), (f), and (g) of section 23 and inserting subsections (d), (e), and (f) of section 36C .\n**(D)**\nSection 1016(a)(26) of such Code is amended by striking 23(g) and inserting 36C(f) .\n**(E)**\nSection 6211(b)(4)(A) of such Code is amended by inserting 36C, after 36B, .\n**(F)**\nThe table of sections for subpart A of part IV of subchapter A of chapter 1 of such Code is amended by striking the item relating to section 23.\n**(G)**\nParagraph (2) of section 1324(b) of title 31, United States Code, is amended by inserting 36C, after 36B, .\n**(H)**\nParagraph (33) of section 471(a) of the Social Security Act ( 42 U.S.C. 671(a) ) is amended by striking section 23 and inserting section 36C .\n**(I)**\nThe table of sections for subpart C of part IV of subchapter A of chapter 1 of the Internal Revenue Code of 1986 is amended by inserting after the item relating to section 36B the following new item:\nSec. 36C. Adoption expenses.\n##### (b) Third-Party affidavits\nSection 36C(h) of the Internal Revenue Code of 1986, as redesignated and moved by subsection (a), is amended\u2014\n**(1)**\nby striking such regulations and inserting such regulations and guidance ,\n**(2)**\nby striking including regulations which treat and inserting\nincluding regulations and guidance which\u2014 (1) treat ,\n**(3)**\nby striking the period at the end and inserting , and , and\n**(4)**\nby adding at the end the following:\n(2) provide for a standardized third-party affidavit for purposes of verifying a legal adoption\u2014 (A) of a type with respect to which qualified adoption expenses may be paid or incurred, or (B) involving a child with special needs for purposes of subsection (a)(3). .\n##### (c) Effective date\nThe amendments made by this section shall apply to taxable years beginning after December 31, 2025.\n##### (d) Transitional rule To treat carryforward as refundable credit\nIn the case of any excess described in section 23(c) of the Internal Revenue Code of 1986 with respect to any taxpayer for the taxable year which precedes the first taxable year to which the amendments made by this section apply, such excess shall be added to the credit allowable under section 36C(a) of such Code with respect to such taxpayer for such first taxable year.",
      "versionDate": "2025-04-10",
      "versionType": "Introduced in House"
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
        "actionDate": "2025-04-10",
        "text": "Read twice and referred to the Committee on Finance."
      },
      "number": "1458",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Adoption Tax Credit Refundability Act of 2025",
      "type": "S"
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
        "updateDate": "2025-05-12T20:01:53Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-04-10",
    "originChamber": "House",
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
          "measure-id": "id119hr2833",
          "measure-number": "2833",
          "measure-type": "hr",
          "orig-publish-date": "2025-04-10",
          "originChamber": "HOUSE",
          "update-date": "2026-03-17"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr2833v00",
            "update-date": "2026-03-17"
          },
          "action-date": "2025-04-10",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Adoption Tax Credit Refundability Act of 2025</strong></p><p>This bill makes the federal adoption tax credit\u00a0refundable. The bill also requires the Internal Revenue Service to provide for a standardized third-party affidavit for purposes of verifying a legal adoption.</p><p>As background, individuals may claim a tax credit for qualified expenses to adopt a child. The maximum amount of the tax credit is $17,280 per child for 2025, which is adjusted annually for inflation. Income limitations apply. Under current law, the adoption tax credit is not refundable but may be carried forward for up to five subsequent tax years to reduce taxable income in those years.</p>"
        },
        "title": "Adoption Tax Credit Refundability Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr2833.xml",
    "summary": {
      "actionDate": "2025-04-10",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Adoption Tax Credit Refundability Act of 2025</strong></p><p>This bill makes the federal adoption tax credit\u00a0refundable. The bill also requires the Internal Revenue Service to provide for a standardized third-party affidavit for purposes of verifying a legal adoption.</p><p>As background, individuals may claim a tax credit for qualified expenses to adopt a child. The maximum amount of the tax credit is $17,280 per child for 2025, which is adjusted annually for inflation. Income limitations apply. Under current law, the adoption tax credit is not refundable but may be carried forward for up to five subsequent tax years to reduce taxable income in those years.</p>",
      "updateDate": "2026-03-17",
      "versionCode": "id119hr2833"
    },
    "title": "Adoption Tax Credit Refundability Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-04-10",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Adoption Tax Credit Refundability Act of 2025</strong></p><p>This bill makes the federal adoption tax credit\u00a0refundable. The bill also requires the Internal Revenue Service to provide for a standardized third-party affidavit for purposes of verifying a legal adoption.</p><p>As background, individuals may claim a tax credit for qualified expenses to adopt a child. The maximum amount of the tax credit is $17,280 per child for 2025, which is adjusted annually for inflation. Income limitations apply. Under current law, the adoption tax credit is not refundable but may be carried forward for up to five subsequent tax years to reduce taxable income in those years.</p>",
      "updateDate": "2026-03-17",
      "versionCode": "id119hr2833"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-04-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2833ih.xml"
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
      "title": "Adoption Tax Credit Refundability Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-24T04:53:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Adoption Tax Credit Refundability Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-24T04:53:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to provide for a refundable adoption tax credit.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-24T04:48:24Z"
    }
  ]
}
```
