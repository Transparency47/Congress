# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1528?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/1528
- Title: America Works Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 1528
- Origin chamber: House
- Introduced date: 2025-02-24
- Update date: 2025-05-06T19:15:22Z
- Update date including text: 2025-05-06T19:15:22Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-24: Introduced in House
- 2025-02-24 - IntroReferral: Introduced in House
- 2025-02-24 - IntroReferral: Introduced in House
- 2025-02-24 - IntroReferral: Referred to the House Committee on Agriculture.
- 2025-03-28 - Committee: Referred to the Subcommittee on Nutrition and Foreign Agriculture.
- Latest action: 2025-02-24: Introduced in House

## Actions

- 2025-02-24 - IntroReferral: Introduced in House
- 2025-02-24 - IntroReferral: Introduced in House
- 2025-02-24 - IntroReferral: Referred to the House Committee on Agriculture.
- 2025-03-28 - Committee: Referred to the Subcommittee on Nutrition and Foreign Agriculture.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-24",
    "latestAction": {
      "actionDate": "2025-02-24",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/1528",
    "number": "1528",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "J000301",
        "district": "",
        "firstName": "Dusty",
        "fullName": "Rep. Johnson, Dusty [R-SD-At Large]",
        "lastName": "Johnson",
        "party": "R",
        "state": "SD"
      }
    ],
    "title": "America Works Act of 2025",
    "type": "HR",
    "updateDate": "2025-05-06T19:15:22Z",
    "updateDateIncludingText": "2025-05-06T19:15:22Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-28",
      "committees": {
        "item": {
          "name": "Nutrition and Foreign Agriculture Subcommittee",
          "systemCode": "hsag03"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Nutrition and Foreign Agriculture.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-24",
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
      "actionDate": "2025-02-24",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-24",
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
          "date": "2025-02-24T17:04:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-03-28T20:43:35Z",
              "name": "Referred to"
            }
          },
          "name": "Nutrition and Foreign Agriculture Subcommittee",
          "systemCode": "hsag03"
        }
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
      "bioguideId": "F000446",
      "district": "4",
      "firstName": "Randy",
      "fullName": "Rep. Feenstra, Randy [R-IA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Feenstra",
      "party": "R",
      "sponsorshipDate": "2025-02-24",
      "state": "IA"
    },
    {
      "bioguideId": "D000626",
      "district": "8",
      "firstName": "Warren",
      "fullName": "Rep. Davidson, Warren [R-OH-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Davidson",
      "party": "R",
      "sponsorshipDate": "2025-02-24",
      "state": "OH"
    },
    {
      "bioguideId": "L000578",
      "district": "1",
      "firstName": "Doug",
      "fullName": "Rep. LaMalfa, Doug [R-CA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "LaMalfa",
      "party": "R",
      "sponsorshipDate": "2025-02-24",
      "state": "CA"
    },
    {
      "bioguideId": "F000475",
      "district": "1",
      "firstName": "Brad",
      "fullName": "Rep. Finstad, Brad [R-MN-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Finstad",
      "party": "R",
      "sponsorshipDate": "2025-02-24",
      "state": "MN"
    },
    {
      "bioguideId": "W000814",
      "district": "14",
      "firstName": "Randy",
      "fullName": "Rep. Weber, Randy K. Sr. [R-TX-14]",
      "isOriginalCosponsor": "False",
      "lastName": "Weber",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-03-05",
      "state": "TX"
    },
    {
      "bioguideId": "F000472",
      "district": "18",
      "firstName": "Scott",
      "fullName": "Rep. Franklin, Scott [R-FL-18]",
      "isOriginalCosponsor": "False",
      "lastName": "Franklin",
      "party": "R",
      "sponsorshipDate": "2025-03-05",
      "state": "FL"
    },
    {
      "bioguideId": "F000450",
      "district": "5",
      "firstName": "Virginia",
      "fullName": "Rep. Foxx, Virginia [R-NC-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Foxx",
      "party": "R",
      "sponsorshipDate": "2025-03-05",
      "state": "NC"
    },
    {
      "bioguideId": "T000480",
      "district": "4",
      "firstName": "William",
      "fullName": "Rep. Timmons, William R. [R-SC-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Timmons",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-03-11",
      "state": "SC"
    },
    {
      "bioguideId": "H001102",
      "district": "8",
      "firstName": "Mark",
      "fullName": "Rep. Harris, Mark [R-NC-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Harris",
      "party": "R",
      "sponsorshipDate": "2025-04-02",
      "state": "NC"
    },
    {
      "bioguideId": "W000829",
      "district": "8",
      "firstName": "Tony",
      "fullName": "Rep. Wied, Tony [R-WI-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Wied",
      "party": "R",
      "sponsorshipDate": "2025-05-01",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1528ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1528\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 24, 2025 Mr. Johnson of South Dakota (for himself, Mr. Feenstra , Mr. Davidson , Mr. LaMalfa , and Mr. Finstad ) introduced the following bill; which was referred to the Committee on Agriculture\nA BILL\nTo amend the Food and Nutrition Act of 2008 to standardize work requirements for able-bodied adults enrolled in the supplemental nutrition assistance program.\n#### 1. Short title\nThis Act may be cited as the America Works Act of 2025 .\n#### 2. Amendments\n##### (a) Amendments to the food and nutrition act of 2008\nSection 6(o) of the Food and Nutrition Act of 2008 is amended\u2014\n**(1)**\nby amending paragraph (3) to read as follows:\n(3) Exception Paragraph (2) shall not apply to an individual if the individual is\u2014 (A) under 18 or over 65 years of age; (B) medically certified as physically or mentally unfit for employment; (C) is a parent or other member of a household with responsibility for a dependent child under 7 years of age; (D) otherwise exempt under subsection (d)(2); or (E) a pregnant woman. , and\n**(2)**\nby amending subparagraph (4)(A) to read as follows:\n(A) In general On the request of a State agency and with the support of the chief executive officer of the State, the Secretary may waive the applicability of paragraph (2) to any group of individuals in the State if the Secretary makes the determination that the county or county-equivalent in which the individuals reside has an unemployment rate of over 10 percent. , and\n##### (b) Conforming amendment\nSection 311 of title II of division C of the Fiscal Responsibility Act of 2023 ( Public Law 118\u20135 ; 137 STAT. 36) is amended by striking subsection (b).",
      "versionDate": "2025-02-24",
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
        "name": "Agriculture and Food",
        "updateDate": "2025-03-28T15:12:20Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-24",
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
          "measure-id": "id119hr1528",
          "measure-number": "1528",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-24",
          "originChamber": "HOUSE",
          "update-date": "2025-05-06"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1528v00",
            "update-date": "2025-05-06"
          },
          "action-date": "2025-02-24",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>America Works Act of 2025</strong></p><p>This bill expands the applicability of work requirements for Supplemental Nutrition Assistance Program (SNAP) recipients who are able-bodied adults without dependents (ABAWDs). As background, these SNAP recipients have work-related requirements in addition to the general SNAP work registration and employment and training requirements.</p><p>Specifically, the bill amends the exemptions to this requirement.</p><p>First, the bill applies the work requirements for ABAWDs to adults who are not over 65 years old, whereas these requirements currently apply to adults who are not over 55 years old.</p><p>Second, the ABAWD exemption for a parent or household member with responsibility for a dependent child is restricted to a dependent child under the age of seven. Currently, the child must be under the age of 18.</p><p>Third, the bill repeals the ABAWD exemptions\u00a0for homeless individuals, veterans, and certain foster care individuals (those who are 24 years old or younger and were in foster care on the date of attaining 18 years of age or a higher age).</p><p>In addition, under current law, an ABAWD waiver program allows state exemptions based on an area having an unemployment rate of over 10% or an insufficient number of jobs. The bill amends the exemption to require the unemployment rate to be based on the rate for the\u00a0county, instead of the area.\u00a0Further, the bill repeals the provision that allows a state exemption if that area does not have a sufficient number of jobs.</p><p>\u00a0</p>"
        },
        "title": "America Works Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1528.xml",
    "summary": {
      "actionDate": "2025-02-24",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>America Works Act of 2025</strong></p><p>This bill expands the applicability of work requirements for Supplemental Nutrition Assistance Program (SNAP) recipients who are able-bodied adults without dependents (ABAWDs). As background, these SNAP recipients have work-related requirements in addition to the general SNAP work registration and employment and training requirements.</p><p>Specifically, the bill amends the exemptions to this requirement.</p><p>First, the bill applies the work requirements for ABAWDs to adults who are not over 65 years old, whereas these requirements currently apply to adults who are not over 55 years old.</p><p>Second, the ABAWD exemption for a parent or household member with responsibility for a dependent child is restricted to a dependent child under the age of seven. Currently, the child must be under the age of 18.</p><p>Third, the bill repeals the ABAWD exemptions\u00a0for homeless individuals, veterans, and certain foster care individuals (those who are 24 years old or younger and were in foster care on the date of attaining 18 years of age or a higher age).</p><p>In addition, under current law, an ABAWD waiver program allows state exemptions based on an area having an unemployment rate of over 10% or an insufficient number of jobs. The bill amends the exemption to require the unemployment rate to be based on the rate for the\u00a0county, instead of the area.\u00a0Further, the bill repeals the provision that allows a state exemption if that area does not have a sufficient number of jobs.</p><p>\u00a0</p>",
      "updateDate": "2025-05-06",
      "versionCode": "id119hr1528"
    },
    "title": "America Works Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-02-24",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>America Works Act of 2025</strong></p><p>This bill expands the applicability of work requirements for Supplemental Nutrition Assistance Program (SNAP) recipients who are able-bodied adults without dependents (ABAWDs). As background, these SNAP recipients have work-related requirements in addition to the general SNAP work registration and employment and training requirements.</p><p>Specifically, the bill amends the exemptions to this requirement.</p><p>First, the bill applies the work requirements for ABAWDs to adults who are not over 65 years old, whereas these requirements currently apply to adults who are not over 55 years old.</p><p>Second, the ABAWD exemption for a parent or household member with responsibility for a dependent child is restricted to a dependent child under the age of seven. Currently, the child must be under the age of 18.</p><p>Third, the bill repeals the ABAWD exemptions\u00a0for homeless individuals, veterans, and certain foster care individuals (those who are 24 years old or younger and were in foster care on the date of attaining 18 years of age or a higher age).</p><p>In addition, under current law, an ABAWD waiver program allows state exemptions based on an area having an unemployment rate of over 10% or an insufficient number of jobs. The bill amends the exemption to require the unemployment rate to be based on the rate for the\u00a0county, instead of the area.\u00a0Further, the bill repeals the provision that allows a state exemption if that area does not have a sufficient number of jobs.</p><p>\u00a0</p>",
      "updateDate": "2025-05-06",
      "versionCode": "id119hr1528"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-24",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1528ih.xml"
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
      "title": "America Works Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-03T13:59:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "America Works Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-17T12:53:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Food and Nutrition Act of 2008 to standardize work requirements for able-bodied adults enrolled in the supplemental nutrition assistance program.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-17T12:48:25Z"
    }
  ]
}
```
