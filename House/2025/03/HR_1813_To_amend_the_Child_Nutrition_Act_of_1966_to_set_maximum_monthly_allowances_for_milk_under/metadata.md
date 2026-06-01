# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1813?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1813
- Title: To amend the Child Nutrition Act of 1966 to set maximum monthly allowances for milk under the special supplemental nutrition program for women, infants, and children.
- Congress: 119
- Bill type: HR
- Bill number: 1813
- Origin chamber: House
- Introduced date: 2025-03-03
- Update date: 2026-02-19T17:27:14Z
- Update date including text: 2026-02-19T17:27:14Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-03-03: Introduced in House
- 2025-03-03 - IntroReferral: Introduced in House
- 2025-03-03 - IntroReferral: Introduced in House
- 2025-03-03 - IntroReferral: Referred to the House Committee on Education and Workforce.
- Latest action: 2025-03-03: Introduced in House

## Actions

- 2025-03-03 - IntroReferral: Introduced in House
- 2025-03-03 - IntroReferral: Introduced in House
- 2025-03-03 - IntroReferral: Referred to the House Committee on Education and Workforce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-03",
    "latestAction": {
      "actionDate": "2025-03-03",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1813",
    "number": "1813",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "V000135",
        "district": "3",
        "firstName": "Derrick",
        "fullName": "Rep. Van Orden, Derrick [R-WI-3]",
        "lastName": "Van Orden",
        "party": "R",
        "state": "WI"
      }
    ],
    "title": "To amend the Child Nutrition Act of 1966 to set maximum monthly allowances for milk under the special supplemental nutrition program for women, infants, and children.",
    "type": "HR",
    "updateDate": "2026-02-19T17:27:14Z",
    "updateDateIncludingText": "2026-02-19T17:27:14Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-03",
      "committees": {
        "item": {
          "name": "Education and Workforce Committee",
          "systemCode": "hsed00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Education and Workforce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-03-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-03",
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
          "date": "2025-03-03T17:03:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Education and Workforce Committee",
      "systemCode": "hsed00",
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
      "bioguideId": "H001090",
      "district": "9",
      "firstName": "Josh",
      "fullName": "Rep. Harder, Josh [D-CA-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Harder",
      "party": "D",
      "sponsorshipDate": "2025-03-03",
      "state": "CA"
    },
    {
      "bioguideId": "S001196",
      "district": "21",
      "firstName": "Elise",
      "fullName": "Rep. Stefanik, Elise M. [R-NY-21]",
      "isOriginalCosponsor": "False",
      "lastName": "Stefanik",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-06-09",
      "state": "NY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1813ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1813\nIN THE HOUSE OF REPRESENTATIVES\nMarch 3, 2025 Mr. Van Orden (for himself and Mr. Harder of California ) introduced the following bill; which was referred to the Committee on Education and Workforce\nA BILL\nTo amend the Child Nutrition Act of 1966 to set maximum monthly allowances for milk under the special supplemental nutrition program for women, infants, and children.\n#### 1. Maximum monthly allowances of milk under WIC\nSection 17 of the Child Nutrition Act of 1966 ( 42 U.S.C. 1786 ) is amended by adding at the end the following:\n(t) Maximum monthly allowances of milk The maximum monthly allowances of milk for the following food packages described in section 246.10(e) of title 7, Code of Federal Regulations are: (1) For Food Package IV, 16 quarts. (2) For Food Package V, 22 quarts. (3) For Food Package VI, 22 quarts. (4) For Food Package VII, 24 quarts. .",
      "versionDate": "2025-03-03",
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
        "updateDate": "2025-03-28T15:16:37Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-03",
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
          "measure-id": "id119hr1813",
          "measure-number": "1813",
          "measure-type": "hr",
          "orig-publish-date": "2025-03-03",
          "originChamber": "HOUSE",
          "update-date": "2026-02-19"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1813v00",
            "update-date": "2026-02-19"
          },
          "action-date": "2025-03-03",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This bill provides statutory authority for, and increases, the maximum monthly allowances for milk under the Special Supplemental Nutrition Program for Women, Infants, and Children (WIC).</p><p>The\u00a0WIC food packages provide supplemental foods designed to address the specific nutritional needs of income-eligible pregnant, breastfeeding, and non-breastfeeding postpartum individuals, infants, and children up to five years of age who are at nutritional risk. Currently, federal regulations list seven WIC food packages, which specify eligible foods (e.g., milk, fruits and vegetables) and their quantities (i.e., a maximum monthly allowance). Specifically, Food Package IV applies to children who are one\u00a0year through\u00a0four\u00a0years old. Food Packages V through VII apply to pregnant, breastfeeding, and non-breastfeeding postpartum individuals.</p><p>For Food Packages IV through\u00a0VII, the bill establishes a maximum monthly allowance for milk of 16 to 24 quarts, depending on the food package, compared to 12 to 16 quarts under current regulations.</p>"
        },
        "title": "To amend the Child Nutrition Act of 1966 to set maximum monthly allowances for milk under the special supplemental nutrition program for women, infants, and children."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1813.xml",
    "summary": {
      "actionDate": "2025-03-03",
      "actionDesc": "Introduced in House",
      "text": "<p>This bill provides statutory authority for, and increases, the maximum monthly allowances for milk under the Special Supplemental Nutrition Program for Women, Infants, and Children (WIC).</p><p>The\u00a0WIC food packages provide supplemental foods designed to address the specific nutritional needs of income-eligible pregnant, breastfeeding, and non-breastfeeding postpartum individuals, infants, and children up to five years of age who are at nutritional risk. Currently, federal regulations list seven WIC food packages, which specify eligible foods (e.g., milk, fruits and vegetables) and their quantities (i.e., a maximum monthly allowance). Specifically, Food Package IV applies to children who are one\u00a0year through\u00a0four\u00a0years old. Food Packages V through VII apply to pregnant, breastfeeding, and non-breastfeeding postpartum individuals.</p><p>For Food Packages IV through\u00a0VII, the bill establishes a maximum monthly allowance for milk of 16 to 24 quarts, depending on the food package, compared to 12 to 16 quarts under current regulations.</p>",
      "updateDate": "2026-02-19",
      "versionCode": "id119hr1813"
    },
    "title": "To amend the Child Nutrition Act of 1966 to set maximum monthly allowances for milk under the special supplemental nutrition program for women, infants, and children."
  },
  "summaries": [
    {
      "actionDate": "2025-03-03",
      "actionDesc": "Introduced in House",
      "text": "<p>This bill provides statutory authority for, and increases, the maximum monthly allowances for milk under the Special Supplemental Nutrition Program for Women, Infants, and Children (WIC).</p><p>The\u00a0WIC food packages provide supplemental foods designed to address the specific nutritional needs of income-eligible pregnant, breastfeeding, and non-breastfeeding postpartum individuals, infants, and children up to five years of age who are at nutritional risk. Currently, federal regulations list seven WIC food packages, which specify eligible foods (e.g., milk, fruits and vegetables) and their quantities (i.e., a maximum monthly allowance). Specifically, Food Package IV applies to children who are one\u00a0year through\u00a0four\u00a0years old. Food Packages V through VII apply to pregnant, breastfeeding, and non-breastfeeding postpartum individuals.</p><p>For Food Packages IV through\u00a0VII, the bill establishes a maximum monthly allowance for milk of 16 to 24 quarts, depending on the food package, compared to 12 to 16 quarts under current regulations.</p>",
      "updateDate": "2026-02-19",
      "versionCode": "id119hr1813"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1813ih.xml"
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
      "title": "To amend the Child Nutrition Act of 1966 to set maximum monthly allowances for milk under the special supplemental nutrition program for women, infants, and children.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-21T03:48:20Z"
    },
    {
      "title": "To amend the Child Nutrition Act of 1966 to set maximum monthly allowances for milk under the special supplemental nutrition program for women, infants, and children.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-04T09:05:47Z"
    }
  ]
}
```
