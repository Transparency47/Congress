# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7010?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7010
- Title: To amend the Agriculture, Rural Development, Food and Drug Administration, and Related Agency Appropriations Act, 2026, to delay the implementation of amendments made by such Act to the hemp production provisions of the Agricultural Marketing Act of 1946.
- Congress: 119
- Bill type: HR
- Bill number: 7010
- Origin chamber: House
- Introduced date: 2026-01-12
- Update date: 2026-05-22T08:08:25Z
- Update date including text: 2026-05-29T16:27:22Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2026-01-12: Introduced in House
- 2026-01-12 - IntroReferral: Introduced in House
- 2026-01-12 - IntroReferral: Introduced in House
- 2026-01-12 - IntroReferral: Referred to the House Committee on Agriculture.
- 2026-05-20 - Committee: Referred to the Subcommittee on Forestry and Horticulture.
- Latest action: 2026-01-12: Introduced in House

## Actions

- 2026-01-12 - IntroReferral: Introduced in House
- 2026-01-12 - IntroReferral: Introduced in House
- 2026-01-12 - IntroReferral: Referred to the House Committee on Agriculture.
- 2026-05-20 - Committee: Referred to the Subcommittee on Forestry and Horticulture.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-12",
    "latestAction": {
      "actionDate": "2026-01-12",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7010",
    "number": "7010",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "B001307",
        "district": "4",
        "firstName": "James",
        "fullName": "Rep. Baird, James R. [R-IN-4]",
        "lastName": "Baird",
        "party": "R",
        "state": "IN"
      }
    ],
    "title": "To amend the Agriculture, Rural Development, Food and Drug Administration, and Related Agency Appropriations Act, 2026, to delay the implementation of amendments made by such Act to the hemp production provisions of the Agricultural Marketing Act of 1946.",
    "type": "HR",
    "updateDate": "2026-05-22T08:08:25Z",
    "updateDateIncludingText": "2026-05-29T16:27:22Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-05-20",
      "committees": {
        "item": {
          "name": "Forestry and Horticulture Subcommittee",
          "systemCode": "hsag15"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Forestry and Horticulture.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-01-12",
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
      "actionDate": "2026-01-12",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-01-12",
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
          "date": "2026-01-12T17:03:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2026-05-20T14:41:58Z",
              "name": "Referred to"
            }
          },
          "name": "Forestry and Horticulture Subcommittee",
          "systemCode": "hsag15"
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
      "bioguideId": "C001108",
      "district": "1",
      "firstName": "James",
      "fullName": "Rep. Comer, James [R-KY-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Comer",
      "party": "R",
      "sponsorshipDate": "2026-01-12",
      "state": "KY"
    },
    {
      "bioguideId": "E000300",
      "district": "8",
      "firstName": "Gabe",
      "fullName": "Rep. Evans, Gabe [R-CO-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Evans",
      "party": "R",
      "sponsorshipDate": "2026-01-12",
      "state": "CO"
    },
    {
      "bioguideId": "M001236",
      "district": "14",
      "firstName": "Tim",
      "fullName": "Rep. Moore, Tim [R-NC-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Moore",
      "party": "R",
      "sponsorshipDate": "2026-01-12",
      "state": "NC"
    },
    {
      "bioguideId": "C001119",
      "district": "2",
      "firstName": "Angie",
      "fullName": "Rep. Craig, Angie [D-MN-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Craig",
      "party": "D",
      "sponsorshipDate": "2026-01-12",
      "state": "MN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7010ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7010\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 12, 2026 Mr. Baird (for himself, Mr. Comer , Mr. Evans of Colorado , Mr. Moore of North Carolina , and Ms. Craig ) introduced the following bill; which was referred to the Committee on Agriculture\nA BILL\nTo amend the Agriculture, Rural Development, Food and Drug Administration, and Related Agency Appropriations Act, 2026, to delay the implementation of amendments made by such Act to the hemp production provisions of the Agricultural Marketing Act of 1946.\n#### 1. Delayed implementation of amendments to hemp production provisions\nSection 781 of the Agriculture, Rural Development, Food and Drug Administration, and Related Agency Appropriations Act, 2026 ( Public Law 119\u201337 ; 139 Stat. 558) is amended, in the matter preceding paragraph (1), by striking 365 days and inserting 3 years .",
      "versionDate": "2026-01-12",
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
        "actionDate": "2026-05-20",
        "text": "Referred to the Subcommittee on Forestry and Horticulture."
      },
      "number": "7024",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Hemp Planting Predictability Act",
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
        "updateDate": "2026-01-14T16:11:53Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2026-01-12",
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
          "measure-id": "id119hr7010",
          "measure-number": "7010",
          "measure-type": "hr",
          "orig-publish-date": "2026-01-12",
          "originChamber": "HOUSE",
          "update-date": "2026-02-24"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr7010v00",
            "update-date": "2026-02-24"
          },
          "action-date": "2026-01-12",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong></strong>This bill extends by two years the implementation of changes to the regulation of hemp products, which\u00a0reimpose certain\u00a0federal controls over some hemp products.</p><p>Specifically,\u00a0Congress enacted the FY2026 agriculture appropriations act (P.L. 119-37) on November 12, 2025. Effective November 12, 2026, the act modifies the statutory definition of hemp products that are considered to be lawful. This bill extends the effective date to November 12, 2028.</p><p>As background, the 2018 farm bill excluded hemp from the Controlled Substances Act definition of marijuana and defined <em>hemp</em>. As a result, hemp and hemp-derived products at or below the 0.3% delta-9 tetrahydrocannabinol (THC, the psychoactive component of marijuana) concentration threshold were no longer regulated as Schedule I controlled substances and registration with the Drug Enforcement Administration was no longer required to cultivate or handle hemp and hemp-derived products. However, hemp remained subject to Department of Agriculture and Food and Drug Administration regulation.</p><p>The 2025\u00a0changes to the definition of hemp, include</p><ul><li>changing the limit to a total THC concentration of not more than 0.3% on a dry weight basis rather than only delta-9 THC,</li><li>explicitly including industrial hemp,</li><li>excluding seeds from a cannabis plant that exceed a certain THC concentration, and</li><li>excluding various types of hemp-derived\u00a0cannabinoid products.</li></ul><p><em>Cannabinoids</em> refer to unique chemical compounds that are found in hemp and marijuana (e.g., THC) and are known to exhibit a range of psychological and physiological effects.</p>"
        },
        "title": "To amend the Agriculture, Rural Development, Food and Drug Administration, and Related Agency Appropriations Act, 2026, to delay the implementation of amendments made by such Act to the hemp production provisions of the Agricultural Marketing Act of 1946."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr7010.xml",
    "summary": {
      "actionDate": "2026-01-12",
      "actionDesc": "Introduced in House",
      "text": "<p><strong></strong>This bill extends by two years the implementation of changes to the regulation of hemp products, which\u00a0reimpose certain\u00a0federal controls over some hemp products.</p><p>Specifically,\u00a0Congress enacted the FY2026 agriculture appropriations act (P.L. 119-37) on November 12, 2025. Effective November 12, 2026, the act modifies the statutory definition of hemp products that are considered to be lawful. This bill extends the effective date to November 12, 2028.</p><p>As background, the 2018 farm bill excluded hemp from the Controlled Substances Act definition of marijuana and defined <em>hemp</em>. As a result, hemp and hemp-derived products at or below the 0.3% delta-9 tetrahydrocannabinol (THC, the psychoactive component of marijuana) concentration threshold were no longer regulated as Schedule I controlled substances and registration with the Drug Enforcement Administration was no longer required to cultivate or handle hemp and hemp-derived products. However, hemp remained subject to Department of Agriculture and Food and Drug Administration regulation.</p><p>The 2025\u00a0changes to the definition of hemp, include</p><ul><li>changing the limit to a total THC concentration of not more than 0.3% on a dry weight basis rather than only delta-9 THC,</li><li>explicitly including industrial hemp,</li><li>excluding seeds from a cannabis plant that exceed a certain THC concentration, and</li><li>excluding various types of hemp-derived\u00a0cannabinoid products.</li></ul><p><em>Cannabinoids</em> refer to unique chemical compounds that are found in hemp and marijuana (e.g., THC) and are known to exhibit a range of psychological and physiological effects.</p>",
      "updateDate": "2026-02-24",
      "versionCode": "id119hr7010"
    },
    "title": "To amend the Agriculture, Rural Development, Food and Drug Administration, and Related Agency Appropriations Act, 2026, to delay the implementation of amendments made by such Act to the hemp production provisions of the Agricultural Marketing Act of 1946."
  },
  "summaries": [
    {
      "actionDate": "2026-01-12",
      "actionDesc": "Introduced in House",
      "text": "<p><strong></strong>This bill extends by two years the implementation of changes to the regulation of hemp products, which\u00a0reimpose certain\u00a0federal controls over some hemp products.</p><p>Specifically,\u00a0Congress enacted the FY2026 agriculture appropriations act (P.L. 119-37) on November 12, 2025. Effective November 12, 2026, the act modifies the statutory definition of hemp products that are considered to be lawful. This bill extends the effective date to November 12, 2028.</p><p>As background, the 2018 farm bill excluded hemp from the Controlled Substances Act definition of marijuana and defined <em>hemp</em>. As a result, hemp and hemp-derived products at or below the 0.3% delta-9 tetrahydrocannabinol (THC, the psychoactive component of marijuana) concentration threshold were no longer regulated as Schedule I controlled substances and registration with the Drug Enforcement Administration was no longer required to cultivate or handle hemp and hemp-derived products. However, hemp remained subject to Department of Agriculture and Food and Drug Administration regulation.</p><p>The 2025\u00a0changes to the definition of hemp, include</p><ul><li>changing the limit to a total THC concentration of not more than 0.3% on a dry weight basis rather than only delta-9 THC,</li><li>explicitly including industrial hemp,</li><li>excluding seeds from a cannabis plant that exceed a certain THC concentration, and</li><li>excluding various types of hemp-derived\u00a0cannabinoid products.</li></ul><p><em>Cannabinoids</em> refer to unique chemical compounds that are found in hemp and marijuana (e.g., THC) and are known to exhibit a range of psychological and physiological effects.</p>",
      "updateDate": "2026-02-24",
      "versionCode": "id119hr7010"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2026-01-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7010ih.xml"
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
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Agriculture, Rural Development, Food and Drug Administration, and Related Agency Appropriations Act, 2026, to delay the implementation of amendments made by such Act to the hemp production provisions of the Agricultural Marketing Act of 1946.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-13T09:18:32Z"
    },
    {
      "title": "To amend the Agriculture, Rural Development, Food and Drug Administration, and Related Agency Appropriations Act, 2026, to delay the implementation of amendments made by such Act to the hemp production provisions of the Agricultural Marketing Act of 1946.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-13T09:05:29Z"
    }
  ]
}
```
