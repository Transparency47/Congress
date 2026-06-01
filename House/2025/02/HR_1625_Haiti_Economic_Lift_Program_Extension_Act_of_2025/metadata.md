# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1625?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1625
- Title: Haiti Economic Lift Program Extension Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 1625
- Origin chamber: House
- Introduced date: 2025-02-26
- Update date: 2026-02-05T17:34:00Z
- Update date including text: 2026-02-05T17:34:00Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-26: Introduced in House
- 2025-02-26 - IntroReferral: Introduced in House
- 2025-02-26 - IntroReferral: Introduced in House
- 2025-02-26 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-02-26: Introduced in House

## Actions

- 2025-02-26 - IntroReferral: Introduced in House
- 2025-02-26 - IntroReferral: Introduced in House
- 2025-02-26 - IntroReferral: Referred to the House Committee on Ways and Means.

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
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1625",
    "number": "1625",
    "originChamber": "House",
    "policyArea": {
      "name": "Foreign Trade and International Finance"
    },
    "sponsors": [
      {
        "bioguideId": "M001210",
        "district": "3",
        "firstName": "Gregory",
        "fullName": "Rep. Murphy, Gregory F. [R-NC-3]",
        "lastName": "Murphy",
        "party": "R",
        "state": "NC"
      }
    ],
    "title": "Haiti Economic Lift Program Extension Act of 2025",
    "type": "HR",
    "updateDate": "2026-02-05T17:34:00Z",
    "updateDateIncludingText": "2026-02-05T17:34:00Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-26",
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
      "actionDate": "2025-02-26",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-26",
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
          "date": "2025-02-26T15:01:00Z",
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
      "bioguideId": "C001127",
      "district": "20",
      "firstName": "Sheila",
      "fullName": "Rep. Cherfilus-McCormick, Sheila [D-FL-20]",
      "isOriginalCosponsor": "True",
      "lastName": "Cherfilus-McCormick",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "FL"
    },
    {
      "bioguideId": "S000168",
      "district": "27",
      "firstName": "Maria",
      "fullName": "Rep. Salazar, Maria Elvira [R-FL-27]",
      "isOriginalCosponsor": "True",
      "lastName": "Salazar",
      "middleName": "Elvira",
      "party": "R",
      "sponsorshipDate": "2025-02-26",
      "state": "FL"
    },
    {
      "bioguideId": "W000808",
      "district": "24",
      "firstName": "Frederica",
      "fullName": "Rep. Wilson, Frederica S. [D-FL-24]",
      "isOriginalCosponsor": "True",
      "lastName": "Wilson",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "FL"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2025-02-26",
      "state": "NY"
    },
    {
      "bioguideId": "C001110",
      "district": "46",
      "firstName": "J.",
      "fullName": "Rep. Correa, J. Luis [D-CA-46]",
      "isOriginalCosponsor": "True",
      "lastName": "Correa",
      "middleName": "Luis",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "CA"
    },
    {
      "bioguideId": "W000797",
      "district": "25",
      "firstName": "Debbie",
      "fullName": "Rep. Wasserman Schultz, Debbie [D-FL-25]",
      "isOriginalCosponsor": "True",
      "lastName": "Wasserman Schultz",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "FL"
    },
    {
      "bioguideId": "F000462",
      "district": "22",
      "firstName": "Lois",
      "fullName": "Rep. Frankel, Lois [D-FL-22]",
      "isOriginalCosponsor": "True",
      "lastName": "Frankel",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "FL"
    },
    {
      "bioguideId": "M001188",
      "district": "6",
      "firstName": "Grace",
      "fullName": "Rep. Meng, Grace [D-NY-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Meng",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "NY"
    },
    {
      "bioguideId": "D000600",
      "district": "26",
      "firstName": "Mario",
      "fullName": "Rep. Diaz-Balart, Mario [R-FL-26]",
      "isOriginalCosponsor": "False",
      "lastName": "Diaz-Balart",
      "party": "R",
      "sponsorshipDate": "2025-02-27",
      "state": "FL"
    },
    {
      "bioguideId": "B001260",
      "district": "16",
      "firstName": "Vern",
      "fullName": "Rep. Buchanan, Vern [R-FL-16]",
      "isOriginalCosponsor": "False",
      "lastName": "Buchanan",
      "party": "R",
      "sponsorshipDate": "2025-03-05",
      "state": "FL"
    },
    {
      "bioguideId": "M000317",
      "district": "11",
      "firstName": "Nicole",
      "fullName": "Rep. Malliotakis, Nicole [R-NY-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Malliotakis",
      "party": "R",
      "sponsorshipDate": "2025-03-10",
      "state": "NY"
    },
    {
      "bioguideId": "M001205",
      "district": "1",
      "firstName": "Carol",
      "fullName": "Rep. Miller, Carol D. [R-WV-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Miller",
      "middleName": "D.",
      "party": "R",
      "sponsorshipDate": "2025-03-10",
      "state": "WV"
    },
    {
      "bioguideId": "R000609",
      "district": "5",
      "firstName": "John",
      "fullName": "Rep. Rutherford, John H. [R-FL-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Rutherford",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2025-03-11",
      "state": "FL"
    },
    {
      "bioguideId": "G000593",
      "district": "28",
      "firstName": "Carlos",
      "fullName": "Rep. Gimenez, Carlos A. [R-FL-28]",
      "isOriginalCosponsor": "False",
      "lastName": "Gimenez",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-03-14",
      "state": "FL"
    },
    {
      "bioguideId": "M001222",
      "district": "7",
      "firstName": "Max",
      "fullName": "Rep. Miller, Max L. [R-OH-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Miller",
      "middleName": "L.",
      "party": "R",
      "sponsorshipDate": "2025-09-03",
      "state": "OH"
    },
    {
      "bioguideId": "M001224",
      "district": "1",
      "firstName": "Nathaniel",
      "fullName": "Rep. Moran, Nathaniel [R-TX-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Moran",
      "party": "R",
      "sponsorshipDate": "2025-09-30",
      "state": "TX"
    },
    {
      "bioguideId": "V000138",
      "district": "7",
      "firstName": "Eugene",
      "fullName": "Rep. Vindman, Eugene Simon [D-VA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Vindman",
      "middleName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-11-04",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1625ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1625\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 26, 2025 Mr. Murphy (for himself, Mrs. Cherfilus-McCormick , Ms. Salazar , Ms. Wilson of Florida , Mr. Lawler , Mr. Correa , Ms. Wasserman Schultz , Ms. Lois Frankel of Florida , and Ms. Meng ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo extend duty-free treatment provided with respect to imports from Haiti under the Caribbean Basin Economic Recovery Act, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Haiti Economic Lift Program Extension Act of 2025 .\n#### 2. Extension of special rules for Haiti under Caribbean Basin Economic Recovery Act\nSection 213A of the Caribbean Basin Economic Recovery Act ( 19 U.S.C. 2703a ) is amended\u2014\n**(1)**\nin subsection (b)\u2014\n**(A)**\nin paragraph (1)\u2014\n**(i)**\nby amending subparagraph (B)(v)(I) to read as follows:\n(I) Applicable percentage The term applicable percentage means 60 percent or more on and after December 20, 2017. ; and\n**(ii)**\nby amending subparagraph (C) to read as follows:\n(C) Quantitative limitations The preferential treatment described in subparagraph (A) shall be extended, during each period after the initial applicable 1-year period, to not more than 1.25 percent of the aggregate square meter equivalents of all apparel articles imported into the United States in the most recent 12-month period for which data are available. ; and\n**(B)**\nin paragraph (2), by striking in each of the 16 succeeding 1-year periods each place it appears and inserting in any of the succeeding 1-year periods ; and\n**(2)**\nby amending subsection (h) to read as follows:\n(h) Termination The duty-free treatment provided under this section shall remain in effect until September 30, 2035. .\n#### 3. Restoration of eligibility of certain articles for preferential treatment\n##### (a) In general\nThe President shall proclaim such modifications to the Harmonized Tariff Schedule of the United States as may be necessary to restore the eligibility of articles described in subsection (b) for preferential treatment under section 213A of the Caribbean Basin Economic Recovery Act ( 19 U.S.C. 2703a ).\n##### (b) Articles described\nAn article described in this subsection is an article that\u2014\n**(1)**\nwas eligible for preferential treatment under section 213A of the Caribbean Basin Economic Recovery Act ( 19 U.S.C. 2703a ) on December 20, 2006; and\n**(2)**\nbecame ineligible for such treatment after that date and before the date of the enactment of this Act as a result of revisions to the Harmonized Tariff Schedule.\n##### (c) Effective date of proclamation\nA proclamation under subsection (a) shall take effect not earlier than 2 business days after the President submits to the Committee on Finance of the Senate and the Committee on Ways and Means of the House of Representatives a report on the proclamation and the reasons for the modifications to the Harmonized Tariff Schedule under the proclamation.",
      "versionDate": "2025-02-26",
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
        "actionDate": "2026-02-03",
        "text": "Became Public Law No: 119-75."
      },
      "number": "7148",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Consolidated Appropriations Act, 2026",
      "type": "HR"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-02-26",
        "text": "Read twice and referred to the Committee on Finance."
      },
      "number": "742",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Haiti Economic Lift Program Extension Act of 2025",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Caribbean area",
            "updateDate": "2025-07-24T14:41:02Z"
          },
          {
            "name": "Haiti",
            "updateDate": "2025-07-24T14:40:54Z"
          },
          {
            "name": "Tariffs",
            "updateDate": "2025-07-24T14:40:58Z"
          }
        ]
      },
      "policyArea": {
        "name": "Foreign Trade and International Finance",
        "updateDate": "2025-05-09T15:31:13Z"
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
          "measure-id": "id119hr1625",
          "measure-number": "1625",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-26",
          "originChamber": "HOUSE",
          "update-date": "2025-07-02"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1625v00",
            "update-date": "2025-07-02"
          },
          "action-date": "2025-02-26",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Haiti Economic Lift Program Extension Act of 2025</strong></p><p>This bill extends through FY2035 the special duty-free rules for various apparel products imported from Haiti, including the duty-free treatment provided for a limited amount (referred to as tariff preference levels) of certain apparel products assembled in and imported from Haiti.</p><p>The bill directs the President to\u00a0proclaim such modifications\u00a0to the Harmonized Tariff Schedule of the United States (HTS) that may be necessary to restore preferential treatment to articles that became ineligible for such treatment due to prior\u00a0revisions to the HTS.</p>"
        },
        "title": "Haiti Economic Lift Program Extension Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1625.xml",
    "summary": {
      "actionDate": "2025-02-26",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Haiti Economic Lift Program Extension Act of 2025</strong></p><p>This bill extends through FY2035 the special duty-free rules for various apparel products imported from Haiti, including the duty-free treatment provided for a limited amount (referred to as tariff preference levels) of certain apparel products assembled in and imported from Haiti.</p><p>The bill directs the President to\u00a0proclaim such modifications\u00a0to the Harmonized Tariff Schedule of the United States (HTS) that may be necessary to restore preferential treatment to articles that became ineligible for such treatment due to prior\u00a0revisions to the HTS.</p>",
      "updateDate": "2025-07-02",
      "versionCode": "id119hr1625"
    },
    "title": "Haiti Economic Lift Program Extension Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-02-26",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Haiti Economic Lift Program Extension Act of 2025</strong></p><p>This bill extends through FY2035 the special duty-free rules for various apparel products imported from Haiti, including the duty-free treatment provided for a limited amount (referred to as tariff preference levels) of certain apparel products assembled in and imported from Haiti.</p><p>The bill directs the President to\u00a0proclaim such modifications\u00a0to the Harmonized Tariff Schedule of the United States (HTS) that may be necessary to restore preferential treatment to articles that became ineligible for such treatment due to prior\u00a0revisions to the HTS.</p>",
      "updateDate": "2025-07-02",
      "versionCode": "id119hr1625"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1625ih.xml"
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
      "title": "Haiti Economic Lift Program Extension Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-17T12:53:31Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Haiti Economic Lift Program Extension Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-17T12:53:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To extend duty-free treatment provided with respect to imports from Haiti under the Caribbean Basin Economic Recovery Act, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-17T12:48:52Z"
    }
  ]
}
```
