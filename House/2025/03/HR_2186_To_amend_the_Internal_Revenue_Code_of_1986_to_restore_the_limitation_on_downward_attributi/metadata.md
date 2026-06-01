# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2186?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2186
- Title: To amend the Internal Revenue Code of 1986 to restore the limitation on downward attribution of stock ownership in applying constructive ownership rules.
- Congress: 119
- Bill type: HR
- Bill number: 2186
- Origin chamber: House
- Introduced date: 2025-03-18
- Update date: 2025-12-30T17:32:50Z
- Update date including text: 2025-12-30T17:32:50Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-03-18: Introduced in House
- 2025-03-18 - IntroReferral: Introduced in House
- 2025-03-18 - IntroReferral: Introduced in House
- 2025-03-18 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-03-18: Introduced in House

## Actions

- 2025-03-18 - IntroReferral: Introduced in House
- 2025-03-18 - IntroReferral: Introduced in House
- 2025-03-18 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-18",
    "latestAction": {
      "actionDate": "2025-03-18",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2186",
    "number": "2186",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "E000298",
        "district": "4",
        "firstName": "Ron",
        "fullName": "Rep. Estes, Ron [R-KS-4]",
        "lastName": "Estes",
        "party": "R",
        "state": "KS"
      }
    ],
    "title": "To amend the Internal Revenue Code of 1986 to restore the limitation on downward attribution of stock ownership in applying constructive ownership rules.",
    "type": "HR",
    "updateDate": "2025-12-30T17:32:50Z",
    "updateDateIncludingText": "2025-12-30T17:32:50Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-18",
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
      "actionDate": "2025-03-18",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-18",
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
          "date": "2025-03-18T16:04:45Z",
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
      "bioguideId": "M001160",
      "district": "4",
      "firstName": "Gwen",
      "fullName": "Rep. Moore, Gwen [D-WI-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Moore",
      "party": "D",
      "sponsorshipDate": "2025-03-18",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2186ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2186\nIN THE HOUSE OF REPRESENTATIVES\nMarch 18, 2025 Mr. Estes (for himself and Ms. Moore of Wisconsin ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to restore the limitation on downward attribution of stock ownership in applying constructive ownership rules.\n#### 1. Restoration of limitation on downward attribution of stock ownership in applying constructive ownership rules\n##### (a) In general\nSection 958(b) of the Internal Revenue Code of 1986 is amended\u2014\n**(1)**\nby inserting after paragraph (3) the following:\n(4) Subparagraphs (A), (B), and (C) of section 318(a)(3) shall not be applied so as to consider a United States person as owning stock which is owned by a person who is not a United States person. , and\n**(2)**\nby striking Paragraph (1) in the last sentence and inserting Paragraphs (1) and (4) .\n##### (b) Foreign controlled United States shareholders\nSubpart F of part III of subchapter N of chapter 1 of such Code is amended by inserting after section 951A the following new section:\n951B. Amounts included in gross income of foreign controlled United States shareholders (a) In general In the case of any foreign controlled United States shareholder of a foreign controlled foreign corporation\u2014 (1) this subpart (other than sections 951A, 951(b), and 957) shall be applied with respect to such shareholder (separately from, and in addition to, the application of this subpart without regard to this section)\u2014 (A) by substituting foreign controlled United States shareholder for United States shareholder each place it appears therein, and (B) by substituting foreign controlled foreign corporation for controlled foreign corporation each place it appears therein, and (2) section 951A shall be applied with respect to such shareholder\u2014 (A) by treating each reference to United States shareholder in such section as including a reference to such shareholder, and (B) by treating each reference to controlled foreign corporation in such section as including a reference to such foreign controlled foreign corporation. (b) Foreign controlled United States shareholder For purposes of this section, the term foreign controlled United States shareholder means, with respect to any foreign corporation, any United States person which would be a United States shareholder with respect to such foreign corporation if\u2014 (1) section 951(b) were applied by substituting more than 50 percent for 10 percent or more , and (2) section 958(b) were applied without regard to paragraph (4) thereof. (c) Foreign controlled foreign corporation For purposes of this section, the term foreign controlled foreign corporation means a foreign corporation, other than a controlled foreign corporation, which would be a controlled foreign corporation if section 957(a) were applied\u2014 (1) by substituting foreign controlled United States shareholders for United States shareholders , and (2) by substituting section 958(b) (other than paragraph (4) thereof) for section 958(b) . (d) Regulations The Secretary shall prescribe such regulations or other guidance as may be necessary or appropriate to carry out the purposes of this section, including regulations or other guidance\u2014 (1) to treat a foreign controlled United States shareholder or a foreign controlled foreign corporation as a United States shareholder or as a controlled foreign corporation, respectively, for purposes of provisions of this title other than this subpart, and (2) to prevent the avoidance of the purposes of this section. .\n##### (c) Clerical amendment\nThe table of sections for subpart F of part III of subchapter N of chapter 1 is amended by inserting after the item relating to section 951A the following new item:\nSec. 951B. Amounts included in gross income of foreign controlled United States shareholders. .\n##### (d) Effective date\nThe amendments made by this section shall apply to\u2014\n**(1)**\nthe last taxable year of foreign corporations beginning before January 1, 2025, and each subsequent taxable year of such foreign corporations, and\n**(2)**\ntaxable years of United States persons in which or with which such taxable years of foreign corporations end.\n##### (e) No inference\nThe amendments made by this section shall not be construed to create any inference with respect to the proper application of any provision of the Internal Revenue Code of 1986 with respect to taxable years beginning before the taxable years to which such amendments apply.",
      "versionDate": "2025-03-18",
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
        "actionDate": "2025-07-04",
        "text": "Became Public Law No: 119-21."
      },
      "number": "1",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "An act to provide for reconciliation pursuant to title II of H. Con. Res. 14.",
      "type": "HR"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-05-06",
        "text": "Read twice and referred to the Committee on Finance."
      },
      "number": "1605",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "International Competition for American Jobs Act",
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
        "name": "Taxation",
        "updateDate": "2025-05-08T19:39:33Z"
      }
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2186ih.xml"
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
      "title": "To amend the Internal Revenue Code of 1986 to restore the limitation on downward attribution of stock ownership in applying constructive ownership rules.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-04T04:48:23Z"
    },
    {
      "title": "To amend the Internal Revenue Code of 1986 to restore the limitation on downward attribution of stock ownership in applying constructive ownership rules.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-19T08:06:07Z"
    }
  ]
}
```
