# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3686?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3686
- Title: Hemp Planting Predictability Act
- Congress: 119
- Bill type: S
- Bill number: 3686
- Origin chamber: Senate
- Introduced date: 2026-01-15
- Update date: 2026-02-24T16:00:42Z
- Update date including text: 2026-05-29T16:27:22Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2026-01-15: Introduced in Senate
- 2026-01-15 - IntroReferral: Introduced in Senate
- 2026-01-15 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.
- Latest action: 2026-01-15: Introduced in Senate

## Actions

- 2026-01-15 - IntroReferral: Introduced in Senate
- 2026-01-15 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-15",
    "latestAction": {
      "actionDate": "2026-01-15",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3686",
    "number": "3686",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Agriculture and Food"
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
    "title": "Hemp Planting Predictability Act",
    "type": "S",
    "updateDate": "2026-02-24T16:00:42Z",
    "updateDateIncludingText": "2026-05-29T16:27:22Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-01-15",
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
      "actionDate": "2026-01-15",
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
          "date": "2026-01-15T22:27:55Z",
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
      "bioguideId": "P000603",
      "firstName": "Rand",
      "fullName": "Sen. Paul, Rand [R-KY]",
      "isOriginalCosponsor": "True",
      "lastName": "Paul",
      "party": "R",
      "sponsorshipDate": "2026-01-15",
      "state": "KY"
    },
    {
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2026-01-15",
      "state": "OR"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3686is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 3686\nIN THE SENATE OF THE UNITED STATES\nJanuary 15, 2026 Ms. Klobuchar (for herself, Mr. Paul , and Mr. Merkley ) introduced the following bill; which was read twice and referred to the Committee on Agriculture, Nutrition, and Forestry\nA BILL\nTo amend the Agriculture, Rural Development, Food and Drug Administration, and Related Agency Appropriations Act, 2026, to delay the implementation of amendments made by that Act to the hemp production provisions of the Agricultural Marketing Act of 1946.\n#### 1. Short title\nThis Act may be cited as the Hemp Planting Predictability Act .\n#### 2. Delayed implementation of amendments to hemp production provisions\nSection 781 of the Agriculture, Rural Development, Food and Drug Administration, and Related Agency Appropriations Act, 2026 ( 7 U.S.C. 1639o note; Public Law 119\u201337 ), is amended, in the matter preceding paragraph (1), by striking 365 days and inserting 3 years .",
      "versionDate": "2026-01-15",
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
        "updateDate": "2026-02-11T21:36:14Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2026-01-15",
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
          "measure-id": "id119s3686",
          "measure-number": "3686",
          "measure-type": "s",
          "orig-publish-date": "2026-01-15",
          "originChamber": "SENATE",
          "update-date": "2026-02-24"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s3686v00",
            "update-date": "2026-02-24"
          },
          "action-date": "2026-01-15",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Hemp Planting Predictability Act</strong></p><p>This bill extends by two years the implementation of changes to the regulation of hemp products, which\u00a0reimpose certain\u00a0federal controls over some hemp products.</p><p>Specifically,\u00a0Congress enacted the FY2026 agriculture appropriations act (P.L. 119-37) on November 12, 2025. Effective November 12, 2026, the act modifies the statutory definition of hemp products that are considered to be lawful. This bill extends the effective date to November 12, 2028.</p><p>As background, the 2018 farm bill excluded hemp from the Controlled Substances Act definition of marijuana and defined <em>hemp</em>. As a result, hemp and hemp-derived products at or below the 0.3% delta-9 tetrahydrocannabinol (THC, the psychoactive component of marijuana) concentration threshold were no longer regulated as Schedule I controlled substances and registration with the Drug Enforcement Administration was no longer required to cultivate or handle hemp and hemp-derived products. However, hemp remained subject to Department of Agriculture and Food and Drug Administration regulation.</p><p>The 2025\u00a0changes to the definition of hemp, include</p><ul><li>changing the limit to a total THC concentration of not more than 0.3% on a dry weight basis rather than only delta-9 THC,</li><li>explicitly including industrial hemp,</li><li>excluding seeds from a cannabis plant that exceed a certain THC concentration, and</li><li>excluding various types of hemp-derived\u00a0cannabinoid products.</li></ul><p><em>Cannabinoids</em> refer to unique chemical compounds that are found in hemp and marijuana (e.g., THC) and are known to exhibit a range of psychological and physiological effects.</p>"
        },
        "title": "Hemp Planting Predictability Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s3686.xml",
    "summary": {
      "actionDate": "2026-01-15",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Hemp Planting Predictability Act</strong></p><p>This bill extends by two years the implementation of changes to the regulation of hemp products, which\u00a0reimpose certain\u00a0federal controls over some hemp products.</p><p>Specifically,\u00a0Congress enacted the FY2026 agriculture appropriations act (P.L. 119-37) on November 12, 2025. Effective November 12, 2026, the act modifies the statutory definition of hemp products that are considered to be lawful. This bill extends the effective date to November 12, 2028.</p><p>As background, the 2018 farm bill excluded hemp from the Controlled Substances Act definition of marijuana and defined <em>hemp</em>. As a result, hemp and hemp-derived products at or below the 0.3% delta-9 tetrahydrocannabinol (THC, the psychoactive component of marijuana) concentration threshold were no longer regulated as Schedule I controlled substances and registration with the Drug Enforcement Administration was no longer required to cultivate or handle hemp and hemp-derived products. However, hemp remained subject to Department of Agriculture and Food and Drug Administration regulation.</p><p>The 2025\u00a0changes to the definition of hemp, include</p><ul><li>changing the limit to a total THC concentration of not more than 0.3% on a dry weight basis rather than only delta-9 THC,</li><li>explicitly including industrial hemp,</li><li>excluding seeds from a cannabis plant that exceed a certain THC concentration, and</li><li>excluding various types of hemp-derived\u00a0cannabinoid products.</li></ul><p><em>Cannabinoids</em> refer to unique chemical compounds that are found in hemp and marijuana (e.g., THC) and are known to exhibit a range of psychological and physiological effects.</p>",
      "updateDate": "2026-02-24",
      "versionCode": "id119s3686"
    },
    "title": "Hemp Planting Predictability Act"
  },
  "summaries": [
    {
      "actionDate": "2026-01-15",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Hemp Planting Predictability Act</strong></p><p>This bill extends by two years the implementation of changes to the regulation of hemp products, which\u00a0reimpose certain\u00a0federal controls over some hemp products.</p><p>Specifically,\u00a0Congress enacted the FY2026 agriculture appropriations act (P.L. 119-37) on November 12, 2025. Effective November 12, 2026, the act modifies the statutory definition of hemp products that are considered to be lawful. This bill extends the effective date to November 12, 2028.</p><p>As background, the 2018 farm bill excluded hemp from the Controlled Substances Act definition of marijuana and defined <em>hemp</em>. As a result, hemp and hemp-derived products at or below the 0.3% delta-9 tetrahydrocannabinol (THC, the psychoactive component of marijuana) concentration threshold were no longer regulated as Schedule I controlled substances and registration with the Drug Enforcement Administration was no longer required to cultivate or handle hemp and hemp-derived products. However, hemp remained subject to Department of Agriculture and Food and Drug Administration regulation.</p><p>The 2025\u00a0changes to the definition of hemp, include</p><ul><li>changing the limit to a total THC concentration of not more than 0.3% on a dry weight basis rather than only delta-9 THC,</li><li>explicitly including industrial hemp,</li><li>excluding seeds from a cannabis plant that exceed a certain THC concentration, and</li><li>excluding various types of hemp-derived\u00a0cannabinoid products.</li></ul><p><em>Cannabinoids</em> refer to unique chemical compounds that are found in hemp and marijuana (e.g., THC) and are known to exhibit a range of psychological and physiological effects.</p>",
      "updateDate": "2026-02-24",
      "versionCode": "id119s3686"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2026-01-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3686is.xml"
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
      "title": "Hemp Planting Predictability Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-06T03:23:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Hemp Planting Predictability Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-06T03:23:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Agriculture, Rural Development, Food and Drug Administration, and Related Agency Appropriations Act, 2026, to delay the implementation of amendments made by that Act to the hemp production provisions of the Agricultural Marketing Act of 1946.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-06T03:18:25Z"
    }
  ]
}
```
