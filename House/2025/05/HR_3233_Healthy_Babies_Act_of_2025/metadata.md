# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3233?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3233
- Title: Healthy Babies Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 3233
- Origin chamber: House
- Introduced date: 2025-05-07
- Update date: 2025-12-17T11:32:01Z
- Update date including text: 2025-12-17T11:32:01Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-05-07: Introduced in House
- 2025-05-07 - IntroReferral: Introduced in House
- 2025-05-07 - IntroReferral: Introduced in House
- 2025-05-07 - IntroReferral: Referred to the House Committee on Education and Workforce.
- Latest action: 2025-05-07: Introduced in House

## Actions

- 2025-05-07 - IntroReferral: Introduced in House
- 2025-05-07 - IntroReferral: Introduced in House
- 2025-05-07 - IntroReferral: Referred to the House Committee on Education and Workforce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-07",
    "latestAction": {
      "actionDate": "2025-05-07",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3233",
    "number": "3233",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "D000594",
        "district": "15",
        "firstName": "Monica",
        "fullName": "Rep. De La Cruz, Monica [R-TX-15]",
        "lastName": "De La Cruz",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "Healthy Babies Act of 2025",
    "type": "HR",
    "updateDate": "2025-12-17T11:32:01Z",
    "updateDateIncludingText": "2025-12-17T11:32:01Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-07",
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
      "actionDate": "2025-05-07",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-05-07",
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
          "date": "2025-05-07T14:00:50Z",
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3233ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3233\nIN THE HOUSE OF REPRESENTATIVES\nMay 7, 2025 Ms. De La Cruz introduced the following bill; which was referred to the Committee on Education and Workforce\nA BILL\nTo amend the Child Nutrition Act of 1966 to direct the Secretary of Agriculture to allow infant food combinations and dinners under the special supplemental nutrition program for women, infants, and children, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Healthy Babies Act of 2025 .\n#### 2. Infant food combinations and dinners under WIC\nSection 17 of the Child Nutrition Act of 1966 ( 42 U.S.C. 1786 ) is amended by adding at the end the following:\n(t) Infant food combinations and dinners Not later than 1 year after the date of the enactment of this subsection, the Secretary shall update the regulations prescribed pursuant to subsection (f)(11)(A) to amend the supplemental foods available to include infant food combinations and dinners. .",
      "versionDate": "2025-05-07",
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
        "updateDate": "2025-06-05T13:10:12Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-05-07",
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
          "measure-id": "id119hr3233",
          "measure-number": "3233",
          "measure-type": "hr",
          "orig-publish-date": "2025-05-07",
          "originChamber": "HOUSE",
          "update-date": "2025-12-17"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr3233v00",
            "update-date": "2025-12-17"
          },
          "action-date": "2025-05-07",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Healthy Babies Act of 2025</strong></p><p>This bill requires that the Special Supplemental Nutrition Program for Women, Infants, and Children (WIC) include infant food combinations\u00a0and dinners as part of the program. (The WIC food packages provide supplemental foods designed to address the specific nutritional needs of income-eligible pregnant, breastfeeding, and non-breastfeeding postpartum individuals, infants, and children up to five years of age who are at nutritional risk.)</p><p>Specifically, the Department of Agriculture must update the regulations that prescribe\u00a0the supplemental foods that must be made available in the program.\u00a0Currently, infant food combinations\u00a0(e.g., meat and vegetables)\u00a0and dinners (e.g., spaghetti and meatballs)\u00a0are not allowed.\u00a0</p>"
        },
        "title": "Healthy Babies Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr3233.xml",
    "summary": {
      "actionDate": "2025-05-07",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Healthy Babies Act of 2025</strong></p><p>This bill requires that the Special Supplemental Nutrition Program for Women, Infants, and Children (WIC) include infant food combinations\u00a0and dinners as part of the program. (The WIC food packages provide supplemental foods designed to address the specific nutritional needs of income-eligible pregnant, breastfeeding, and non-breastfeeding postpartum individuals, infants, and children up to five years of age who are at nutritional risk.)</p><p>Specifically, the Department of Agriculture must update the regulations that prescribe\u00a0the supplemental foods that must be made available in the program.\u00a0Currently, infant food combinations\u00a0(e.g., meat and vegetables)\u00a0and dinners (e.g., spaghetti and meatballs)\u00a0are not allowed.\u00a0</p>",
      "updateDate": "2025-12-17",
      "versionCode": "id119hr3233"
    },
    "title": "Healthy Babies Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-05-07",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Healthy Babies Act of 2025</strong></p><p>This bill requires that the Special Supplemental Nutrition Program for Women, Infants, and Children (WIC) include infant food combinations\u00a0and dinners as part of the program. (The WIC food packages provide supplemental foods designed to address the specific nutritional needs of income-eligible pregnant, breastfeeding, and non-breastfeeding postpartum individuals, infants, and children up to five years of age who are at nutritional risk.)</p><p>Specifically, the Department of Agriculture must update the regulations that prescribe\u00a0the supplemental foods that must be made available in the program.\u00a0Currently, infant food combinations\u00a0(e.g., meat and vegetables)\u00a0and dinners (e.g., spaghetti and meatballs)\u00a0are not allowed.\u00a0</p>",
      "updateDate": "2025-12-17",
      "versionCode": "id119hr3233"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-05-07",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3233ih.xml"
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
      "title": "To amend the Child Nutrition Act of 1966 to direct the Secretary of Agriculture to allow infant food combinations and dinners under the special supplemental nutrition program for women, infants, and children, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-15T03:59:19Z"
    },
    {
      "title": "Healthy Babies Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-15T03:39:36Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Healthy Babies Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-15T03:38:23Z"
    }
  ]
}
```
