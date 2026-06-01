# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1389?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1389
- Title: Marriage Equality for Disabled Adults Act
- Congress: 119
- Bill type: HR
- Bill number: 1389
- Origin chamber: House
- Introduced date: 2025-02-14
- Update date: 2026-05-30T08:06:00Z
- Update date including text: 2026-05-30T08:06:00Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-14: Introduced in House
- 2025-02-14 - IntroReferral: Introduced in House
- 2025-02-14 - IntroReferral: Introduced in House
- 2025-02-14 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-02-14 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-02-14: Introduced in House

## Actions

- 2025-02-14 - IntroReferral: Introduced in House
- 2025-02-14 - IntroReferral: Introduced in House
- 2025-02-14 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-02-14 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-14",
    "latestAction": {
      "actionDate": "2025-02-14",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1389",
    "number": "1389",
    "originChamber": "House",
    "policyArea": {
      "name": "Social Welfare"
    },
    "sponsors": [
      {
        "bioguideId": "P000613",
        "district": "19",
        "firstName": "Jimmy",
        "fullName": "Rep. Panetta, Jimmy [D-CA-19]",
        "lastName": "Panetta",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Marriage Equality for Disabled Adults Act",
    "type": "HR",
    "updateDate": "2026-05-30T08:06:00Z",
    "updateDateIncludingText": "2026-05-30T08:06:00Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-14",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Ways and Means, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-14",
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
      "text": "Referred to the Committee on Ways and Means, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-02-14",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-14",
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
          "date": "2025-02-14T18:30:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-02-14T18:30:20Z",
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
      "bioguideId": "L000397",
      "district": "18",
      "firstName": "Zoe",
      "fullName": "Rep. Lofgren, Zoe [D-CA-18]",
      "isOriginalCosponsor": "True",
      "lastName": "Lofgren",
      "party": "D",
      "sponsorshipDate": "2025-02-14",
      "state": "CA"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2025-02-14",
      "state": "DC"
    },
    {
      "bioguideId": "G000598",
      "district": "42",
      "firstName": "Robert",
      "fullName": "Rep. Garcia, Robert [D-CA-42]",
      "isOriginalCosponsor": "True",
      "lastName": "Garcia",
      "party": "D",
      "sponsorshipDate": "2025-02-14",
      "state": "CA"
    },
    {
      "bioguideId": "S001145",
      "district": "9",
      "firstName": "Janice",
      "fullName": "Rep. Schakowsky, Janice D. [D-IL-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Schakowsky",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2025-02-14",
      "state": "IL"
    },
    {
      "bioguideId": "P000617",
      "district": "7",
      "firstName": "Ayanna",
      "fullName": "Rep. Pressley, Ayanna [D-MA-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Pressley",
      "party": "D",
      "sponsorshipDate": "2025-02-14",
      "state": "MA"
    },
    {
      "bioguideId": "N000002",
      "district": "12",
      "firstName": "Jerrold",
      "fullName": "Rep. Nadler, Jerrold [D-NY-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Nadler",
      "party": "D",
      "sponsorshipDate": "2025-02-14",
      "state": "NY"
    },
    {
      "bioguideId": "W000187",
      "district": "43",
      "firstName": "Maxine",
      "fullName": "Rep. Waters, Maxine [D-CA-43]",
      "isOriginalCosponsor": "False",
      "lastName": "Waters",
      "party": "D",
      "sponsorshipDate": "2025-02-25",
      "state": "CA"
    },
    {
      "bioguideId": "S001185",
      "district": "7",
      "firstName": "Terri",
      "fullName": "Rep. Sewell, Terri A. [D-AL-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Sewell",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "AL"
    },
    {
      "bioguideId": "S001221",
      "district": "3",
      "firstName": "Hillary",
      "fullName": "Rep. Scholten, Hillary J. [D-MI-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Scholten",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-04-24",
      "state": "MI"
    },
    {
      "bioguideId": "D000617",
      "district": "1",
      "firstName": "Suzan",
      "fullName": "Rep. DelBene, Suzan K. [D-WA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "DelBene",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2026-05-14",
      "state": "WA"
    },
    {
      "bioguideId": "R000599",
      "district": "25",
      "firstName": "Raul",
      "fullName": "Rep. Ruiz, Raul [D-CA-25]",
      "isOriginalCosponsor": "False",
      "lastName": "Ruiz",
      "party": "D",
      "sponsorshipDate": "2026-05-29",
      "state": "CA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1389ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1389\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 14, 2025 Mr. Panetta (for himself, Ms. Lofgren , Ms. Norton , Mr. Garcia of California , Ms. Schakowsky , Ms. Pressley , and Mr. Nadler ) introduced the following bill; which was referred to the Committee on Ways and Means , and in addition to the Committee on Energy and Commerce , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo secure the rights and dignity of marriage for Disabled Adult Children, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Marriage Equality for Disabled Adults Act .\n#### 2. Elimination of marriage restriction for disabled adult children\n##### (a) In general\nSection 202(d) of the Social Security Act ( 42 U.S.C. 402(d) ) is amended\u2014\n**(1)**\nin paragraph (1)(B), by striking was unmarried and ;\n**(2)**\nby amending paragraph (1)(D) to read as follows:\n(D) the month in which such child dies; ; and\n**(3)**\nby striking paragraph (5).\n##### (b) Conforming amendment\nSection 202(s)(2) of such Act ( 42 U.S.C. 402(s)(2) ) is amended by striking (d)(5), .\n#### 3. Modification of rules to determine marital relationships\n##### (a) In general\nSection 1614(d) of the Social Security Act ( 42 U.S.C. 1382c(d) ) is amended by striking except that and all that follows through the end of the subsection and inserting except that if two individuals have been determined to be married under section 216(h)(1) for purposes of title II they shall be considered (from and after the date of such determination or the date of their application for benefits under this title, whichever is later) to be married for purposes of this title. .\n##### (b) Conforming amendments\nTitle XVI of the Social Security Act ( 42 U.S.C. 1381 et seq. ) is amended\u2014\n**(1)**\nin section 1611(e)(3)\u2014\n**(A)**\nby striking a husband and wife each place it appears and inserting two married individuals ; and\n**(B)**\nby striking such husband and wife and inserting such married individuals ;\n**(2)**\nin section 1614(b)\u2014\n**(A)**\nin the first sentence, by striking the husband or wife of and inserting married to ; and\n**(B)**\nin the second sentence, by striking husband and wife and inserting married ; and\n**(3)**\nin section 1631(b)(1)(A)(i), by striking husband or wife and inserting spouse .\n#### 4. Income and resource deeming rules\nSection 1614(f) of the Social Security Act ( 42 U.S.C. 1382c(f) ) is amended by adding at the end the following:\n(5) Notwithstanding paragraph (1) of this subsection, for purposes of determining eligibility for, and the amount of, benefits for a married individual who is entitled to a child\u2019s insurance benefit based on a disability under section 202(d), or for the spouse of such an individual, the income and resources of the one spouse is deemed to not include any income or resources of the other spouse. .\n#### 5. Retention of Medicaid for certain married individuals\nSection 1634 of the Social Security Act ( 42 U.S.C. 1383(c) ) is amended by adding at the end the following:\n(e) In the case of a State that exercises the option under section 1902(f), any individual who\u2014 (1) is a married individual who is entitled to a child\u2019s insurance benefit based on a disability for any month under section 202(d) or the spouse of such an individual; and (2) would be eligible for medical assistance under the State plan approved under title XIX if the individual were unmarried, shall remain eligible for medical assistance under such plan for so long as the individual satisfies the criteria described in paragraphs (1) and (2). .\n#### 6. Sense of Congress\nIt is the sense of the United States Congress that\u2014\n**(1)**\nDisabled Adult Children, if married, should remain eligible for all Medicare, Medicaid, and Social Security benefits under the same terms as they would if unmarried, regardless of State of residence or State Medicaid law; specifically, this legislation should not impact a Disabled Adult Child\u2019s eligibility for any Medicaid services for which they were eligible when unmarried;\n**(2)**\nregardless of marital status, eligibility of Disabled Adult Children to receive Federal Medicare, Medicaid, and Social Security benefits should not be impacted by any holding out status as defined in section 1382c(d) of title 42, United States Code; and\n**(3)**\nDisabled Adult Children\u2019s eligibility for Social Security Disability Insurance benefits should not be conditioned on geographic location or residency in the United States.",
      "versionDate": "2025-02-14",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Disability and health-based discrimination",
            "updateDate": "2025-06-13T19:12:58Z"
          },
          {
            "name": "Disability and paralysis",
            "updateDate": "2025-06-13T19:12:58Z"
          },
          {
            "name": "Disability assistance",
            "updateDate": "2025-06-13T19:12:58Z"
          },
          {
            "name": "Family relationships",
            "updateDate": "2025-06-13T19:12:58Z"
          },
          {
            "name": "Marriage and family status",
            "updateDate": "2025-06-13T19:12:58Z"
          },
          {
            "name": "Medicaid",
            "updateDate": "2025-06-13T19:12:58Z"
          },
          {
            "name": "Poverty and welfare assistance",
            "updateDate": "2025-06-13T19:12:58Z"
          },
          {
            "name": "Social security and elderly assistance",
            "updateDate": "2025-06-13T19:12:58Z"
          },
          {
            "name": "Tax administration and collection, taxpayers",
            "updateDate": "2025-06-13T19:12:58Z"
          }
        ]
      },
      "policyArea": {
        "name": "Social Welfare",
        "updateDate": "2025-03-14T12:45:52Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-14",
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
          "measure-id": "id119hr1389",
          "measure-number": "1389",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-14",
          "originChamber": "HOUSE",
          "update-date": "2025-04-25"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1389v00",
            "update-date": "2025-04-25"
          },
          "action-date": "2025-02-14",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Marriage Equality for Disabled Adults Act</strong></p><p>This bill eliminates certain marriage-related criteria for individuals entitled to Social Security child\u2019s benefits and Supplemental Security Income (SSI).</p><p>Specifically, the bill removes the requirement that individuals receiving Social Security child\u2019s benefits be unmarried. Those eligible for Social Security child\u2019s benefits generally include the minor children of eligible or deceased workers and disabled adult children (the disabled adult children of such workers for whom the onset of disability occurred before age 22). Under current law, child beneficiaries generally lose their benefits upon marriage to an individual who is not also eligible for Social Security benefits.\u00a0</p><p>With respect to SSI, the bill removes the requirement that couples who present themselves as married in their community be considered married for purposes of SSI eligibility. The bill also exempts SSI recipients who are disabled adult children, or who marry disabled adult children, from the general requirement that the income or resources of an SSI recipient\u2019s spouse be considered in an eligibility determination. \u00a0</p><p>Further, married disabled adult children and their spouses who would otherwise be eligible for Medicaid in a state if they were unmarried must remain eligible for Medicaid regardless of their marriage.\u00a0</p>"
        },
        "title": "Marriage Equality for Disabled Adults Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1389.xml",
    "summary": {
      "actionDate": "2025-02-14",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Marriage Equality for Disabled Adults Act</strong></p><p>This bill eliminates certain marriage-related criteria for individuals entitled to Social Security child\u2019s benefits and Supplemental Security Income (SSI).</p><p>Specifically, the bill removes the requirement that individuals receiving Social Security child\u2019s benefits be unmarried. Those eligible for Social Security child\u2019s benefits generally include the minor children of eligible or deceased workers and disabled adult children (the disabled adult children of such workers for whom the onset of disability occurred before age 22). Under current law, child beneficiaries generally lose their benefits upon marriage to an individual who is not also eligible for Social Security benefits.\u00a0</p><p>With respect to SSI, the bill removes the requirement that couples who present themselves as married in their community be considered married for purposes of SSI eligibility. The bill also exempts SSI recipients who are disabled adult children, or who marry disabled adult children, from the general requirement that the income or resources of an SSI recipient\u2019s spouse be considered in an eligibility determination. \u00a0</p><p>Further, married disabled adult children and their spouses who would otherwise be eligible for Medicaid in a state if they were unmarried must remain eligible for Medicaid regardless of their marriage.\u00a0</p>",
      "updateDate": "2025-04-25",
      "versionCode": "id119hr1389"
    },
    "title": "Marriage Equality for Disabled Adults Act"
  },
  "summaries": [
    {
      "actionDate": "2025-02-14",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Marriage Equality for Disabled Adults Act</strong></p><p>This bill eliminates certain marriage-related criteria for individuals entitled to Social Security child\u2019s benefits and Supplemental Security Income (SSI).</p><p>Specifically, the bill removes the requirement that individuals receiving Social Security child\u2019s benefits be unmarried. Those eligible for Social Security child\u2019s benefits generally include the minor children of eligible or deceased workers and disabled adult children (the disabled adult children of such workers for whom the onset of disability occurred before age 22). Under current law, child beneficiaries generally lose their benefits upon marriage to an individual who is not also eligible for Social Security benefits.\u00a0</p><p>With respect to SSI, the bill removes the requirement that couples who present themselves as married in their community be considered married for purposes of SSI eligibility. The bill also exempts SSI recipients who are disabled adult children, or who marry disabled adult children, from the general requirement that the income or resources of an SSI recipient\u2019s spouse be considered in an eligibility determination. \u00a0</p><p>Further, married disabled adult children and their spouses who would otherwise be eligible for Medicaid in a state if they were unmarried must remain eligible for Medicaid regardless of their marriage.\u00a0</p>",
      "updateDate": "2025-04-25",
      "versionCode": "id119hr1389"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-14",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1389ih.xml"
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
      "title": "Marriage Equality for Disabled Adults Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-13T04:23:35Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Marriage Equality for Disabled Adults Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-13T04:23:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To secure the rights and dignity of marriage for Disabled Adult Children, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-13T04:18:59Z"
    }
  ]
}
```
