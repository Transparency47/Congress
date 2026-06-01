# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1198?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1198
- Title: Let’s Get to Work Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 1198
- Origin chamber: House
- Introduced date: 2025-02-11
- Update date: 2026-02-07T21:06:13Z
- Update date including text: 2026-02-07T21:06:13Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-11: Introduced in House
- 2025-02-11 - IntroReferral: Introduced in House
- 2025-02-11 - IntroReferral: Introduced in House
- 2025-02-11 - IntroReferral: Referred to the Committee on Agriculture, and in addition to the Committee on Financial Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-02-11 - IntroReferral: Referred to the Committee on Agriculture, and in addition to the Committee on Financial Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-03-14 - Committee: Referred to the Subcommittee on Nutrition and Foreign Agriculture.
- Latest action: 2025-02-11: Introduced in House

## Actions

- 2025-02-11 - IntroReferral: Introduced in House
- 2025-02-11 - IntroReferral: Introduced in House
- 2025-02-11 - IntroReferral: Referred to the Committee on Agriculture, and in addition to the Committee on Financial Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-02-11 - IntroReferral: Referred to the Committee on Agriculture, and in addition to the Committee on Financial Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-03-14 - Committee: Referred to the Subcommittee on Nutrition and Foreign Agriculture.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-11",
    "latestAction": {
      "actionDate": "2025-02-11",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1198",
    "number": "1198",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "K000403",
        "district": "3",
        "firstName": "Mike",
        "fullName": "Rep. Kennedy, Mike [R-UT-3]",
        "lastName": "Kennedy",
        "party": "R",
        "state": "UT"
      }
    ],
    "title": "Let\u2019s Get to Work Act of 2025",
    "type": "HR",
    "updateDate": "2026-02-07T21:06:13Z",
    "updateDateIncludingText": "2026-02-07T21:06:13Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-14",
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
      "actionDate": "2025-02-11",
      "committees": {
        "item": {
          "name": "Financial Services Committee",
          "systemCode": "hsba00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Agriculture, and in addition to the Committee on Financial Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-11",
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
      "text": "Referred to the Committee on Agriculture, and in addition to the Committee on Financial Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-02-11",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-11",
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
          "date": "2025-02-11T15:04:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-03-14T20:36:56Z",
              "name": "Referred to"
            }
          },
          "name": "Nutrition and Foreign Agriculture Subcommittee",
          "systemCode": "hsag03"
        }
      },
      "systemCode": "hsag00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-02-11T15:04:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Financial Services Committee",
      "systemCode": "hsba00",
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
      "bioguideId": "B001317",
      "district": "2",
      "firstName": "Josh",
      "fullName": "Rep. Brecheen, Josh [R-OK-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Brecheen",
      "party": "R",
      "sponsorshipDate": "2025-02-11",
      "state": "OK"
    },
    {
      "bioguideId": "B001314",
      "district": "4",
      "firstName": "Aaron",
      "fullName": "Rep. Bean, Aaron [R-FL-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Bean",
      "party": "R",
      "sponsorshipDate": "2025-02-13",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1198ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1198\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 11, 2025 Mr. Kennedy of Utah (for himself and Mr. Brecheen ) introduced the following bill; which was referred to the Committee on Agriculture , and in addition to the Committee on Financial Services , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend the Food and Nutrition Act of 2008 to modify work requirements under the supplemental nutrition assistance program, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Let\u2019s Get to Work Act of 2025 .\n#### 2. SNAP work requirements\n##### (a) In general\nSection 6(o) of the Food and Nutrition Act of 2008 ( 7 U.S.C. 2015(o) ) is amended\u2014\n**(1)**\nin paragraph (2), in the matter preceding subparagraph (A), by inserting , or, in the case of a parent or other member of a household with responsibility for a dependent child, 6 months (consecutive or otherwise), before during which ;\n**(2)**\nin paragraph (3)\u2014\n**(A)**\nin subparagraph (A), by striking clause (ii) and inserting the following:\n(ii) over 60 years of age; ;\n**(B)**\nin subparagraph (C), by inserting under 6 years of age before the semicolon at the end;\n**(C)**\nin subparagraph (G), by striking or at the end;\n**(D)**\nin subparagraph (H), by striking the period at the end and inserting ; or ; and\n**(E)**\nby adding at the end the following:\n(I) (i) responsible for a dependent individual; and (ii) married to, and resides with, an individual who is in compliance with the requirements of paragraph (2). ; and\n**(3)**\nin paragraph (6)\u2014\n**(A)**\nin subparagraph (B), by striking (I) and inserting (H) ;\n**(B)**\nin subparagraph (C), by striking (G) and (I) and inserting (F) and (H) ;\n**(C)**\nin subparagraph (D), by striking (G) through (I) and inserting (F) through (H) ;\n**(D)**\nby striking subparagraph (F);\n**(E)**\nby redesignating subparagraphs (G) through (J) as subparagraphs (F) through (I), respectively; and\n**(F)**\nin subparagraph (F) (as so redesignated), by striking (C), (D),, (E), or (F) and inserting (C), (D), or (E) .\n##### (b) Conforming amendment\nSection 16(h)(1)(E)(ii)(I) of the Food and Nutrition Act of 2008 ( 7 U.S.C. 2025(h)(1)(E)(ii)(I) ) is amended by striking 3-month period and inserting 3-month or 6-month period, as applicable, .\n#### 3. Work requirements for public housing and tenant-based rental assistance\n##### (a) Public housing\nSection 3 of the United States Housing Act of 1937 ( 42 U.S.C. 1437a ) is amended by adding at the end the following:\n(e) Work requirements for families The requirements described in section 6(o) of the Food and Nutrition Act of 2008 ( 7 U.S.C. 2015(o) ) shall apply with respect to any individual who\u2014 (1) is a member of a family residing in a public housing dwelling; and (2) is not exempted from those requirements under paragraph (3) of such section. .\n##### (b) Tenant-Based rental assistance\nSection 8(o) of the United States Housing Act of 1937 ( 42 U.S.C. 1437f(o) ) is amended by adding at the end the following:\n(22) Work requirements for families The requirements described in section 6(o) of the Food and Nutrition Act of 2008 ( 7 U.S.C. 2015(o) ) shall apply with respect to any individual who\u2014 (A) is a member of a family receiving tenant-based assistance; and (B) is not exempted from those requirements under paragraph (3) of such section. .",
      "versionDate": "2025-02-11",
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
        "actionDate": "2025-01-14",
        "text": "Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry."
      },
      "number": "87",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Let's Get to Work Act of 2025",
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
        "name": "Agriculture and Food",
        "updateDate": "2025-03-20T19:42:32Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-11",
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
          "measure-id": "id119hr1198",
          "measure-number": "1198",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-11",
          "originChamber": "HOUSE",
          "update-date": "2025-05-28"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1198v00",
            "update-date": "2025-05-28"
          },
          "action-date": "2025-02-11",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Let's Get to Work Act of 2025</strong></p><p>This bill modifies and expands work requirements under the Supplemental Nutrition Assistance Program (SNAP) and certain housing programs of the Department of Housing and Urban Development (HUD).</p><p>Specifically, the bill expands the applicability of the work requirements for SNAP recipients who are able-bodied adults without dependents (ABAWDs). As background, SNAP recipients who are ABAWDs have work-related requirements in addition to the general SNAP work registration and employment and training requirements.</p><p>The bill applies the work requirements for ABAWDs to adults who are not over 60 years old, whereas these requirements currently apply to adults who are not over 55 years old.</p><p>Further, the\u00a0ABAWD exemption for a parent or household member with responsibility for a dependent child is restricted under the bill to a dependent child under the age of\u00a0six. Currently, the child must be under the age of 18.\u00a0</p><p>The bill allows a member of a household with responsibility for a dependent child to participate in SNAP\u00a0for up to 6 months (currently 3 months) over a 36-month period without meeting the ABAWD work requirements.</p><p>The bill also includes an exception for an individual who (1) is responsible for a dependent individual, and (2) is married to and resides with an individual who complies with the SNAP work requirements.</p><p>Additionally, the bill establishes work requirements for families residing in public housing by applying the SNAP work requirements for ABAWDs to the HUD public housing and tenant-based rental assistance (voucher) programs.</p>"
        },
        "title": "Let\u2019s Get to Work Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1198.xml",
    "summary": {
      "actionDate": "2025-02-11",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Let's Get to Work Act of 2025</strong></p><p>This bill modifies and expands work requirements under the Supplemental Nutrition Assistance Program (SNAP) and certain housing programs of the Department of Housing and Urban Development (HUD).</p><p>Specifically, the bill expands the applicability of the work requirements for SNAP recipients who are able-bodied adults without dependents (ABAWDs). As background, SNAP recipients who are ABAWDs have work-related requirements in addition to the general SNAP work registration and employment and training requirements.</p><p>The bill applies the work requirements for ABAWDs to adults who are not over 60 years old, whereas these requirements currently apply to adults who are not over 55 years old.</p><p>Further, the\u00a0ABAWD exemption for a parent or household member with responsibility for a dependent child is restricted under the bill to a dependent child under the age of\u00a0six. Currently, the child must be under the age of 18.\u00a0</p><p>The bill allows a member of a household with responsibility for a dependent child to participate in SNAP\u00a0for up to 6 months (currently 3 months) over a 36-month period without meeting the ABAWD work requirements.</p><p>The bill also includes an exception for an individual who (1) is responsible for a dependent individual, and (2) is married to and resides with an individual who complies with the SNAP work requirements.</p><p>Additionally, the bill establishes work requirements for families residing in public housing by applying the SNAP work requirements for ABAWDs to the HUD public housing and tenant-based rental assistance (voucher) programs.</p>",
      "updateDate": "2025-05-28",
      "versionCode": "id119hr1198"
    },
    "title": "Let\u2019s Get to Work Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-02-11",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Let's Get to Work Act of 2025</strong></p><p>This bill modifies and expands work requirements under the Supplemental Nutrition Assistance Program (SNAP) and certain housing programs of the Department of Housing and Urban Development (HUD).</p><p>Specifically, the bill expands the applicability of the work requirements for SNAP recipients who are able-bodied adults without dependents (ABAWDs). As background, SNAP recipients who are ABAWDs have work-related requirements in addition to the general SNAP work registration and employment and training requirements.</p><p>The bill applies the work requirements for ABAWDs to adults who are not over 60 years old, whereas these requirements currently apply to adults who are not over 55 years old.</p><p>Further, the\u00a0ABAWD exemption for a parent or household member with responsibility for a dependent child is restricted under the bill to a dependent child under the age of\u00a0six. Currently, the child must be under the age of 18.\u00a0</p><p>The bill allows a member of a household with responsibility for a dependent child to participate in SNAP\u00a0for up to 6 months (currently 3 months) over a 36-month period without meeting the ABAWD work requirements.</p><p>The bill also includes an exception for an individual who (1) is responsible for a dependent individual, and (2) is married to and resides with an individual who complies with the SNAP work requirements.</p><p>Additionally, the bill establishes work requirements for families residing in public housing by applying the SNAP work requirements for ABAWDs to the HUD public housing and tenant-based rental assistance (voucher) programs.</p>",
      "updateDate": "2025-05-28",
      "versionCode": "id119hr1198"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1198ih.xml"
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
      "title": "Let\u2019s Get to Work Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-13T01:08:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Let\u2019s Get to Work Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-13T01:08:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Food and Nutrition Act of 2008 to modify work requirements under the supplemental nutrition assistance program, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-13T01:03:20Z"
    }
  ]
}
```
