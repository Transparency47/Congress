# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1246?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1246
- Title: Investing in Rural America Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 1246
- Origin chamber: House
- Introduced date: 2025-02-12
- Update date: 2026-03-10T08:05:45Z
- Update date including text: 2026-03-10T08:05:45Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-12: Introduced in House
- 2025-02-12 - IntroReferral: Introduced in House
- 2025-02-12 - IntroReferral: Introduced in House
- 2025-02-12 - IntroReferral: Referred to the House Committee on Agriculture.
- 2025-03-20 - Committee: Referred to the Subcommittee on Commodity Markets, Digital Assets, and Rural Development.
- 2025-03-20 - Committee: Referred to the Subcommittee on General Farm Commodities, Risk Management, and Credit.
- Latest action: 2025-02-12: Introduced in House

## Actions

- 2025-02-12 - IntroReferral: Introduced in House
- 2025-02-12 - IntroReferral: Introduced in House
- 2025-02-12 - IntroReferral: Referred to the House Committee on Agriculture.
- 2025-03-20 - Committee: Referred to the Subcommittee on Commodity Markets, Digital Assets, and Rural Development.
- 2025-03-20 - Committee: Referred to the Subcommittee on General Farm Commodities, Risk Management, and Credit.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-12",
    "latestAction": {
      "actionDate": "2025-02-12",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1246",
    "number": "1246",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "F000470",
        "district": "7",
        "firstName": "Michelle",
        "fullName": "Rep. Fischbach, Michelle [R-MN-7]",
        "lastName": "Fischbach",
        "party": "R",
        "state": "MN"
      }
    ],
    "title": "Investing in Rural America Act of 2025",
    "type": "HR",
    "updateDate": "2026-03-10T08:05:45Z",
    "updateDateIncludingText": "2026-03-10T08:05:45Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-20",
      "committees": {
        "item": {
          "name": "Commodity Markets, Digital Assets, and Rural Development Subcommittee",
          "systemCode": "hsag22"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Commodity Markets, Digital Assets, and Rural Development.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-03-20",
      "committees": {
        "item": {
          "name": "General Farm Commodities, Risk Management, and Credit Subcommittee",
          "systemCode": "hsag16"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on General Farm Commodities, Risk Management, and Credit.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-12",
      "committees": {
        "item": {
          "name": "Agriculture Committee",
          "systemCode": "hsag00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Agriculture.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-02-12",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-12",
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
          "date": "2025-02-12T15:01:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
      "subcommittees": {
        "item": [
          {
            "activities": {
              "item": {
                "date": "2025-03-20T20:38:16Z",
                "name": "Referred to"
              }
            },
            "name": "Commodity Markets, Digital Assets, and Rural Development Subcommittee",
            "systemCode": "hsag22"
          },
          {
            "activities": {
              "item": {
                "date": "2025-03-20T20:38:16Z",
                "name": "Referred to"
              }
            },
            "name": "General Farm Commodities, Risk Management, and Credit Subcommittee",
            "systemCode": "hsag16"
          }
        ]
      },
      "systemCode": "hsag00",
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
      "bioguideId": "F000475",
      "district": "1",
      "firstName": "Brad",
      "fullName": "Rep. Finstad, Brad [R-MN-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Finstad",
      "party": "R",
      "sponsorshipDate": "2025-02-12",
      "state": "MN"
    },
    {
      "bioguideId": "D000230",
      "district": "1",
      "firstName": "Donald",
      "fullName": "Rep. Davis, Donald G. [D-NC-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Davis",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2025-02-12",
      "state": "NC"
    },
    {
      "bioguideId": "B000490",
      "district": "2",
      "firstName": "Sanford",
      "fullName": "Rep. Bishop, Sanford D. [D-GA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Bishop",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2025-03-03",
      "state": "GA"
    },
    {
      "bioguideId": "M000871",
      "district": "1",
      "firstName": "Tracey",
      "fullName": "Rep. Mann, Tracey [R-KS-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Mann",
      "party": "R",
      "sponsorshipDate": "2025-03-10",
      "state": "KS"
    },
    {
      "bioguideId": "S001225",
      "district": "17",
      "firstName": "Eric",
      "fullName": "Rep. Sorensen, Eric [D-IL-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Sorensen",
      "party": "D",
      "sponsorshipDate": "2025-03-11",
      "state": "IL"
    },
    {
      "bioguideId": "B001315",
      "district": "13",
      "firstName": "Nikki",
      "fullName": "Rep. Budzinski, Nikki [D-IL-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Budzinski",
      "party": "D",
      "sponsorshipDate": "2025-05-05",
      "state": "IL"
    },
    {
      "bioguideId": "W000804",
      "district": "1",
      "firstName": "Robert",
      "fullName": "Rep. Wittman, Robert J. [R-VA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Wittman",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-06-03",
      "state": "VA"
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
      "sponsorshipDate": "2025-06-03",
      "state": "VA"
    },
    {
      "bioguideId": "N000193",
      "district": "3",
      "firstName": "Zachary",
      "fullName": "Rep. Nunn, Zachary [R-IA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Nunn",
      "party": "R",
      "sponsorshipDate": "2025-06-09",
      "state": "IA"
    },
    {
      "bioguideId": "T000487",
      "district": "2",
      "firstName": "Jill",
      "fullName": "Rep. Tokuda, Jill N. [D-HI-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Tokuda",
      "middleName": "N.",
      "party": "D",
      "sponsorshipDate": "2025-06-11",
      "state": "HI"
    },
    {
      "bioguideId": "V000135",
      "district": "3",
      "firstName": "Derrick",
      "fullName": "Rep. Van Orden, Derrick [R-WI-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Orden",
      "party": "R",
      "sponsorshipDate": "2025-06-11",
      "state": "WI"
    },
    {
      "bioguideId": "C001130",
      "district": "30",
      "firstName": "Jasmine",
      "fullName": "Rep. Crockett, Jasmine [D-TX-30]",
      "isOriginalCosponsor": "False",
      "lastName": "Crockett",
      "party": "D",
      "sponsorshipDate": "2025-06-20",
      "state": "TX"
    },
    {
      "bioguideId": "W000829",
      "district": "8",
      "firstName": "Tony",
      "fullName": "Rep. Wied, Tony [R-WI-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Wied",
      "party": "R",
      "sponsorshipDate": "2025-06-25",
      "state": "WI"
    },
    {
      "bioguideId": "V000129",
      "district": "22",
      "firstName": "David",
      "fullName": "Rep. Valadao, David G. [R-CA-22]",
      "isOriginalCosponsor": "False",
      "lastName": "Valadao",
      "middleName": "G.",
      "party": "R",
      "sponsorshipDate": "2025-07-02",
      "state": "CA"
    },
    {
      "bioguideId": "T000165",
      "district": "7",
      "firstName": "Thomas",
      "fullName": "Rep. Tiffany, Thomas P. [R-WI-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Tiffany",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2025-07-17",
      "state": "WI"
    },
    {
      "bioguideId": "S001212",
      "district": "8",
      "firstName": "Pete",
      "fullName": "Rep. Stauber, Pete [R-MN-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Stauber",
      "party": "R",
      "sponsorshipDate": "2025-09-03",
      "state": "MN"
    },
    {
      "bioguideId": "H001090",
      "district": "9",
      "firstName": "Josh",
      "fullName": "Rep. Harder, Josh [D-CA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Harder",
      "party": "D",
      "sponsorshipDate": "2025-10-03",
      "state": "CA"
    },
    {
      "bioguideId": "M001232",
      "district": "6",
      "firstName": "April",
      "fullName": "Rep. McClain Delaney, April [D-MD-6]",
      "isOriginalCosponsor": "False",
      "lastName": "McClain Delaney",
      "party": "D",
      "sponsorshipDate": "2025-10-08",
      "state": "MD"
    },
    {
      "bioguideId": "B001307",
      "district": "4",
      "firstName": "James",
      "fullName": "Rep. Baird, James R. [R-IN-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Baird",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-11-17",
      "state": "IN"
    },
    {
      "bioguideId": "A000379",
      "district": "4",
      "firstName": "Mark",
      "fullName": "Rep. Alford, Mark [R-MO-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Alford",
      "party": "R",
      "sponsorshipDate": "2025-11-17",
      "state": "MO"
    },
    {
      "bioguideId": "C001039",
      "district": "3",
      "firstName": "Kat",
      "fullName": "Rep. Cammack, Kat [R-FL-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Cammack",
      "party": "R",
      "sponsorshipDate": "2025-12-10",
      "state": "FL"
    },
    {
      "bioguideId": "H001103",
      "district": "0",
      "firstName": "Pablo",
      "fullName": "Rescom. Hern\u00e1ndez, Pablo Jose [D-PR-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Hern\u00e1ndez",
      "middleName": "Jose",
      "party": "D",
      "sponsorshipDate": "2025-12-15",
      "state": "PR"
    },
    {
      "bioguideId": "M001237",
      "district": "8",
      "firstName": "Kristen",
      "fullName": "Rep. McDonald Rivet, Kristen [D-MI-8]",
      "isOriginalCosponsor": "False",
      "lastName": "McDonald Rivet",
      "party": "D",
      "sponsorshipDate": "2025-12-16",
      "state": "MI"
    },
    {
      "bioguideId": "M001216",
      "district": "7",
      "firstName": "Cory",
      "fullName": "Rep. Mills, Cory [R-FL-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Mills",
      "party": "R",
      "sponsorshipDate": "2026-02-12",
      "state": "FL"
    },
    {
      "bioguideId": "B001257",
      "district": "12",
      "firstName": "Gus",
      "fullName": "Rep. Bilirakis, Gus M. [R-FL-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Bilirakis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2026-03-05",
      "state": "FL"
    },
    {
      "bioguideId": "F000484",
      "district": "6",
      "firstName": "Randy",
      "fullName": "Rep. Fine, Randy [R-FL-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Fine",
      "party": "R",
      "sponsorshipDate": "2026-03-09",
      "state": "FL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1246ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1246\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 12, 2025 Mrs. Fischbach (for herself, Mr. Finstad , and Mr. Davis of North Carolina ) introduced the following bill; which was referred to the Committee on Agriculture\nA BILL\nTo amend the Farm Credit Act of 1971 to provide support for facilities providing healthcare, education, child care, public safety, and other vital services in rural areas.\n#### 1. Short title\nThis Act may be cited as the Investing in Rural America Act of 2025 .\n#### 2. Authority of farm credit system institutions to provide financial support for essential rural community facilities projects\n##### (a) In general\nThe Farm Credit Act of 1971 is amended by inserting after section 4.18A ( 12 U.S.C. 2206a ) the following:\n4.18. Essential community facilities (a) In general A Farm Credit Bank, direct lender association, or bank for cooperatives chartered under this Act may, for the purpose of making available capital to develop, build, maintain, improve, or provide related equipment or other support for essential community facilities in rural areas, make and participate in loans and commitments, and extend other technical and financial assistance for projects for essential community facilities eligible for financing under section 306(a) of the Consolidated Farm and Rural Development Act. (b) Eligibility Only an entity eligible for financing under section 306(a) of the Consolidated Farm and Rural Development Act may receive financing or any other assistance under subsection (a) of this section. (c) Limitations (1) Financing A Farm Credit System institution described in subsection (a) shall not provide financing or assistance under this section in an aggregate amount that exceeds 15 percent of the total of all outstanding loans of the institution. (2) Offer requirement (A) In general A Farm Credit System institution shall not provide financing or assistance under this section unless the institution\u2014 (i) has offered, under reasonable terms and conditions acceptable to the borrower involved, an interest in the financing to at least 1 domestic lending institution not referred to in subsection (a) other than the Department of Agriculture; and (ii) has reported the offer to the Farm Credit Administration. (B) Rural community bank priority In offering an interest in a financing to a domestic lending institution described in subparagraph (A)(i), the Farm Credit System institution shall give priority to community banks located in the service area of the essential community facility being financed. (d) Annual report to Congress Within 1 year after the date of the enactment of this section and annually thereafter, the Farm Credit Administration shall provide a report to the Committee on Agriculture of the House of Representatives and the Committee on Agriculture, Nutrition, and Forestry of the Senate on the activities undertaken pursuant to this section by Farm Credit System institutions during the period covered by the report, including through partnerships between such an institution and other lending institutions, which shall also be posted on the website of the Farm Credit Administration. .\n##### (b) Effective date\nThe amendment made by subsection (a) shall take effect on October 1, 2025.",
      "versionDate": "2025-02-12",
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
        "actionDate": "2026-03-04",
        "text": "Ordered to be Reported (Amended) by the Yeas and Nays: 34 - 17."
      },
      "number": "7567",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Farm, Food, and National Security Act of 2026",
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
        "name": "Agriculture and Food",
        "updateDate": "2025-03-20T19:45:06Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-12",
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
          "measure-id": "id119hr1246",
          "measure-number": "1246",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-12",
          "originChamber": "HOUSE",
          "update-date": "2025-05-14"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1246v00",
            "update-date": "2025-05-14"
          },
          "action-date": "2025-02-12",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Investing in Rural America Act of 2025</strong></p><p>This bill allows Farm Credit System (FCS) institutions to make and participate in loans and commitments (and extend other technical and financial assistance) for essential community facility\u00a0projects as part of the Department of Agriculture's\u00a0Community Facilities Direct Loan & Grant Program. This program provides funding to develop essential community facilities in rural areas.</p><p>The\u00a0FCS financing and technical assistance\u00a0may be provided in order to make capital available to develop, build, maintain, improve, or provide related equipment or\u00a0other support for essential community facilities in rural communities (e.g., certain facilities that provide healthcare, community support, public safety, educational, or utility services).</p><p>Under the bill, the\u00a0financing provided by an FCS institution may not\u00a0exceed 15% of the total of all outstanding loans of the institution.\u00a0Further, an FCS institution must (1) offer at least one non-FCS lending institution an interest in the financing under reasonable terms and conditions acceptable to the borrower, and (2) report the offer to the\u00a0Farm Credit Administration (FCA).</p><p>The FCA must submit an annual report to Congress on the activities undertaken by FCS institutions under this bill, including through the partnerships between FCS institutions and other lending institutions. The FCA must post the report on the administration's website.</p>"
        },
        "title": "Investing in Rural America Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1246.xml",
    "summary": {
      "actionDate": "2025-02-12",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Investing in Rural America Act of 2025</strong></p><p>This bill allows Farm Credit System (FCS) institutions to make and participate in loans and commitments (and extend other technical and financial assistance) for essential community facility\u00a0projects as part of the Department of Agriculture's\u00a0Community Facilities Direct Loan & Grant Program. This program provides funding to develop essential community facilities in rural areas.</p><p>The\u00a0FCS financing and technical assistance\u00a0may be provided in order to make capital available to develop, build, maintain, improve, or provide related equipment or\u00a0other support for essential community facilities in rural communities (e.g., certain facilities that provide healthcare, community support, public safety, educational, or utility services).</p><p>Under the bill, the\u00a0financing provided by an FCS institution may not\u00a0exceed 15% of the total of all outstanding loans of the institution.\u00a0Further, an FCS institution must (1) offer at least one non-FCS lending institution an interest in the financing under reasonable terms and conditions acceptable to the borrower, and (2) report the offer to the\u00a0Farm Credit Administration (FCA).</p><p>The FCA must submit an annual report to Congress on the activities undertaken by FCS institutions under this bill, including through the partnerships between FCS institutions and other lending institutions. The FCA must post the report on the administration's website.</p>",
      "updateDate": "2025-05-14",
      "versionCode": "id119hr1246"
    },
    "title": "Investing in Rural America Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-02-12",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Investing in Rural America Act of 2025</strong></p><p>This bill allows Farm Credit System (FCS) institutions to make and participate in loans and commitments (and extend other technical and financial assistance) for essential community facility\u00a0projects as part of the Department of Agriculture's\u00a0Community Facilities Direct Loan & Grant Program. This program provides funding to develop essential community facilities in rural areas.</p><p>The\u00a0FCS financing and technical assistance\u00a0may be provided in order to make capital available to develop, build, maintain, improve, or provide related equipment or\u00a0other support for essential community facilities in rural communities (e.g., certain facilities that provide healthcare, community support, public safety, educational, or utility services).</p><p>Under the bill, the\u00a0financing provided by an FCS institution may not\u00a0exceed 15% of the total of all outstanding loans of the institution.\u00a0Further, an FCS institution must (1) offer at least one non-FCS lending institution an interest in the financing under reasonable terms and conditions acceptable to the borrower, and (2) report the offer to the\u00a0Farm Credit Administration (FCA).</p><p>The FCA must submit an annual report to Congress on the activities undertaken by FCS institutions under this bill, including through the partnerships between FCS institutions and other lending institutions. The FCA must post the report on the administration's website.</p>",
      "updateDate": "2025-05-14",
      "versionCode": "id119hr1246"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1246ih.xml"
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
      "title": "Investing in Rural America Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-14T09:23:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Investing in Rural America Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-14T09:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Farm Credit Act of 1971 to provide support for facilities providing healthcare, education, child care, public safety, and other vital services in rural areas.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-14T09:18:24Z"
    }
  ]
}
```
