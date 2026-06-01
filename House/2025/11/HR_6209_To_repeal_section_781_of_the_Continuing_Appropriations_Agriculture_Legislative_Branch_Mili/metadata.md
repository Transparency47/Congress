# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6209?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6209
- Title: American Hemp Protection Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 6209
- Origin chamber: House
- Introduced date: 2025-11-20
- Update date: 2026-05-16T08:07:00Z
- Update date including text: 2026-05-16T08:07:00Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-11-20: Introduced in House
- 2025-11-20 - IntroReferral: Introduced in House
- 2025-11-20 - IntroReferral: Introduced in House
- 2025-11-20 - IntroReferral: Referred to the House Committee on Agriculture.
- 2026-01-13 - Committee: Referred to the Subcommittee on Commodity Markets, Digital Assets, and Rural Development.
- Latest action: 2025-11-20: Introduced in House

## Actions

- 2025-11-20 - IntroReferral: Introduced in House
- 2025-11-20 - IntroReferral: Introduced in House
- 2025-11-20 - IntroReferral: Referred to the House Committee on Agriculture.
- 2026-01-13 - Committee: Referred to the Subcommittee on Commodity Markets, Digital Assets, and Rural Development.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-20",
    "latestAction": {
      "actionDate": "2025-11-20",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6209",
    "number": "6209",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "M000194",
        "district": "1",
        "firstName": "Nancy",
        "fullName": "Rep. Mace, Nancy [R-SC-1]",
        "lastName": "Mace",
        "party": "R",
        "state": "SC"
      }
    ],
    "title": "American Hemp Protection Act of 2025",
    "type": "HR",
    "updateDate": "2026-05-16T08:07:00Z",
    "updateDateIncludingText": "2026-05-16T08:07:00Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-01-13",
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
      "actionCode": "H11100",
      "actionDate": "2025-11-20",
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
      "actionDate": "2025-11-20",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-11-20",
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
          "date": "2025-11-20T15:10:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2026-01-13T19:59:04Z",
              "name": "Referred to"
            }
          },
          "name": "Commodity Markets, Digital Assets, and Rural Development Subcommittee",
          "systemCode": "hsag22"
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
      "bioguideId": "M001184",
      "district": "4",
      "firstName": "Thomas",
      "fullName": "Rep. Massie, Thomas [R-KY-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Massie",
      "party": "R",
      "sponsorshipDate": "2025-11-20",
      "state": "KY"
    },
    {
      "bioguideId": "L000397",
      "district": "18",
      "firstName": "Zoe",
      "fullName": "Rep. Lofgren, Zoe [D-CA-18]",
      "isOriginalCosponsor": "True",
      "lastName": "Lofgren",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "CA"
    },
    {
      "bioguideId": "B001307",
      "district": "4",
      "firstName": "James",
      "fullName": "Rep. Baird, James R. [R-IN-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Baird",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-11-20",
      "state": "IN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6209ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6209\nIN THE HOUSE OF REPRESENTATIVES\nNovember 20, 2025 Ms. Mace (for herself, Mr. Massie , Ms. Lofgren , and Mr. Baird ) introduced the following bill; which was referred to the Committee on Agriculture\nA BILL\nTo repeal section 781 of the Continuing Appropriations, Agriculture, Legislative Branch, Military Construction and Veterans Affairs, and Extensions Act, 2026, relating to amendments to the Agricultural Marketing Act of 1946, with respect to hemp.\n#### 1. Short title\nThis Act may be cited as the American Hemp Protection Act of 2025 .\n#### 2. Repeal of amendments to Agricultural Marketing Act of 1946, with respect to hemp\nEffective November 12, 2025, section 781 of the Continuing Appropriations, Agriculture, Legislative Branch, Military Construction and Veterans Affairs, and Extensions Act, 2026 ( Public Law 119\u201337 ) is repealed.",
      "versionDate": "2025-11-20",
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
        "updateDate": "2025-12-09T19:37:25Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-11-20",
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
          "measure-id": "id119hr6209",
          "measure-number": "6209",
          "measure-type": "hr",
          "orig-publish-date": "2025-11-20",
          "originChamber": "HOUSE",
          "update-date": "2026-03-03"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr6209v00",
            "update-date": "2026-03-03"
          },
          "action-date": "2025-11-20",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>American Hemp Protection Act of 2025</strong></p><p>This bill repeals changes to the regulation of hemp products, which reimpose certain\u00a0federal controls over some hemp products.</p><p>Specifically,\u00a0Congress enacted the FY2026 agriculture appropriations act (P.L. 119-37) on November 12, 2025. Effective November 12, 2026, the act modifies the statutory definition of hemp products that are considered to be lawful. This bill repeals the changes.</p><p>As background, the 2018 farm bill excluded hemp from the Controlled Substances Act definition of marijuana and defined <em>hemp</em>. As a result, hemp and hemp-derived products at or below the 0.3% delta-9 tetrahydrocannabinol (THC, the psychoactive component of marijuana) concentration threshold were no longer regulated as Schedule I controlled substances. Registration with the Drug Enforcement Administration was no longer required to cultivate or handle hemp and hemp-derived products. However, hemp remained subject to Department of Agriculture and Food and Drug Administration regulation.</p><p>The 2025\u00a0changes to the definition of hemp, include</p><ul><li>changing the limit to a total THC concentration of not more than 0.3% on a dry weight basis rather than only delta-9 THC,</li><li>explicitly including industrial hemp,</li><li>excluding seeds from a cannabis plant that exceed a certain THC concentration, and</li><li>excluding various types of hemp-derived\u00a0cannabinoid products.</li></ul><p><em>Cannabinoids</em> refer to unique chemical compounds that are found in hemp and marijuana (e.g., THC) and are known to exhibit a range of psychological and physiological effects.</p>"
        },
        "title": "American Hemp Protection Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr6209.xml",
    "summary": {
      "actionDate": "2025-11-20",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>American Hemp Protection Act of 2025</strong></p><p>This bill repeals changes to the regulation of hemp products, which reimpose certain\u00a0federal controls over some hemp products.</p><p>Specifically,\u00a0Congress enacted the FY2026 agriculture appropriations act (P.L. 119-37) on November 12, 2025. Effective November 12, 2026, the act modifies the statutory definition of hemp products that are considered to be lawful. This bill repeals the changes.</p><p>As background, the 2018 farm bill excluded hemp from the Controlled Substances Act definition of marijuana and defined <em>hemp</em>. As a result, hemp and hemp-derived products at or below the 0.3% delta-9 tetrahydrocannabinol (THC, the psychoactive component of marijuana) concentration threshold were no longer regulated as Schedule I controlled substances. Registration with the Drug Enforcement Administration was no longer required to cultivate or handle hemp and hemp-derived products. However, hemp remained subject to Department of Agriculture and Food and Drug Administration regulation.</p><p>The 2025\u00a0changes to the definition of hemp, include</p><ul><li>changing the limit to a total THC concentration of not more than 0.3% on a dry weight basis rather than only delta-9 THC,</li><li>explicitly including industrial hemp,</li><li>excluding seeds from a cannabis plant that exceed a certain THC concentration, and</li><li>excluding various types of hemp-derived\u00a0cannabinoid products.</li></ul><p><em>Cannabinoids</em> refer to unique chemical compounds that are found in hemp and marijuana (e.g., THC) and are known to exhibit a range of psychological and physiological effects.</p>",
      "updateDate": "2026-03-03",
      "versionCode": "id119hr6209"
    },
    "title": "American Hemp Protection Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-11-20",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>American Hemp Protection Act of 2025</strong></p><p>This bill repeals changes to the regulation of hemp products, which reimpose certain\u00a0federal controls over some hemp products.</p><p>Specifically,\u00a0Congress enacted the FY2026 agriculture appropriations act (P.L. 119-37) on November 12, 2025. Effective November 12, 2026, the act modifies the statutory definition of hemp products that are considered to be lawful. This bill repeals the changes.</p><p>As background, the 2018 farm bill excluded hemp from the Controlled Substances Act definition of marijuana and defined <em>hemp</em>. As a result, hemp and hemp-derived products at or below the 0.3% delta-9 tetrahydrocannabinol (THC, the psychoactive component of marijuana) concentration threshold were no longer regulated as Schedule I controlled substances. Registration with the Drug Enforcement Administration was no longer required to cultivate or handle hemp and hemp-derived products. However, hemp remained subject to Department of Agriculture and Food and Drug Administration regulation.</p><p>The 2025\u00a0changes to the definition of hemp, include</p><ul><li>changing the limit to a total THC concentration of not more than 0.3% on a dry weight basis rather than only delta-9 THC,</li><li>explicitly including industrial hemp,</li><li>excluding seeds from a cannabis plant that exceed a certain THC concentration, and</li><li>excluding various types of hemp-derived\u00a0cannabinoid products.</li></ul><p><em>Cannabinoids</em> refer to unique chemical compounds that are found in hemp and marijuana (e.g., THC) and are known to exhibit a range of psychological and physiological effects.</p>",
      "updateDate": "2026-03-03",
      "versionCode": "id119hr6209"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-11-20",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6209ih.xml"
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
      "title": "American Hemp Protection Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-09T10:23:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "American Hemp Protection Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-09T10:23:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To repeal section 781 of the Continuing Appropriations, Agriculture, Legislative Branch, Military Construction and Veterans Affairs, and Extensions Act, 2026, relating to amendments to the Agricultural Marketing Act of 1946, with respect to hemp.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-09T10:18:20Z"
    }
  ]
}
```
