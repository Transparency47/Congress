# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1105?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1105
- Title: No UPCODE Act
- Congress: 119
- Bill type: S
- Bill number: 1105
- Origin chamber: Senate
- Introduced date: 2025-03-25
- Update date: 2025-12-11T15:04:06Z
- Update date including text: 2025-12-11T15:04:06Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-03-25: Introduced in Senate
- 2025-03-25 - IntroReferral: Introduced in Senate
- 2025-03-25 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-03-25: Introduced in Senate

## Actions

- 2025-03-25 - IntroReferral: Introduced in Senate
- 2025-03-25 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-25",
    "latestAction": {
      "actionDate": "2025-03-25",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1105",
    "number": "1105",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "C001075",
        "district": "",
        "firstName": "Bill",
        "fullName": "Sen. Cassidy, Bill [R-LA]",
        "lastName": "Cassidy",
        "party": "R",
        "state": "LA"
      }
    ],
    "title": "No UPCODE Act",
    "type": "S",
    "updateDate": "2025-12-11T15:04:06Z",
    "updateDateIncludingText": "2025-12-11T15:04:06Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-25",
      "committees": {
        "item": {
          "name": "Finance Committee",
          "systemCode": "ssfi00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Finance.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-03-25",
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
          "date": "2025-03-25T15:27:16Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Finance Committee",
      "systemCode": "ssfi00",
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
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2025-03-25",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1105is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1105\nIN THE SENATE OF THE UNITED STATES\nMarch 25, 2025 Mr. Cassidy (for himself and Mr. Merkley ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend title XVIII of the Social Security Act to improve risk adjustment under Medicare Advantage.\n#### 1. Short title\nThis Act may be cited as the No Unreasonable Payments, Coding, Or Diagnoses for the Elderly Act or the No UPCODE Act .\n#### 2. Improving risk adjustment under Medicare Advantage\n##### (a) Use of 2 years of diagnostic data\nSection 1853(a)(3)(C)(iii) of the Social Security Act ( 42 U.S.C. 1395w\u201323(a)(3)(C)(iii) ) is amended\u2014\n**(1)**\nby striking methodology .\u2014Such risk and inserting \u201c methodology .\u2014\n(I) In general Subject to subclause (II), such risk ; and\n**(2)**\nby adding at the end the following new subclauses:\n(II) Use of health status data For 2026 and each subsequent year, the Secretary shall use 2 years of diagnostic data (when available) under such risk adjustment methodology. .\n##### (b) Exclusion of diagnoses collected from chart reviews and health risk assessments\n**(1) In general**\nSection 1853(a)(1)(C) of such Act ( 42 U.S.C. 1395w\u201323(a)(1)(C) ) is amended by adding at the end the following new clause:\n(iv) Exclusion of diagnoses collected from chart reviews and health risk assessments (I) In general For 2026 and each subsequent year, for purposes of establishing the payment adjustment factors and adjusting payment based on health status under clause (i), the Secretary shall not take into account a diagnosis collected from a chart review or a health risk assessment. (II) Identification of diagnoses collected from chart reviews and health risk assessments The Secretary shall establish procedures to provide for the identification and verification of diagnoses collected from chart reviews and health risk assessments. .\n##### (c) Application of coding adjustment\nSection 1853(a)(1)(C)(ii) of such Act ( 42 U.S.C. 1395w\u201323(a)(1)(C)(ii) ) is amended\u2014\n**(1)**\nin subclause (III), by striking In calculating and inserting Subject to subclause (V), in calculating ; and\n**(2)**\nby adding at the end the following new subclause:\n(V) In calculating such adjustment for 2026 and each subsequent year, the Secretary shall evaluate the impact on risk scores for Medicare Advantage enrollees of differences in coding patterns between Medicare Advantage plans and providers under parts A and B and publicly report the results of such evaluation. The Secretary shall ensure that such adjustment, which may include adjustment on a plan or contract level, fully accounts for the impact of coding pattern differences not otherwise accounted for to the extent that the Secretary identifies such differences through annual evaluation. .",
      "versionDate": "2025-03-25",
      "versionType": "Introduced in Senate"
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
        "actionDate": "2025-11-10",
        "text": "Referred to the Committee on Ways and Means, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "6010",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "To amend the Internal Revenue Code of 1986 to extend and modify the enhanced premium tax credit, and for other purposes.",
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
        "name": "Health",
        "updateDate": "2025-04-08T12:01:29Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-25",
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
          "measure-id": "id119s1105",
          "measure-number": "1105",
          "measure-type": "s",
          "orig-publish-date": "2025-03-25",
          "originChamber": "SENATE",
          "update-date": "2025-04-18"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s1105v00",
            "update-date": "2025-04-18"
          },
          "action-date": "2025-03-25",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><b>No Unreasonable Payments, Coding, Or Diagnoses for the Elderly Act or the No UPCODE Act</b></p> <p>This bill modifies certain factors that are used to determine Medicare Advantage (MA) payments, particularly relating to health status and related data. </p> <p>Specifically, the bill requires the Centers for Medicare & Medicaid Services (CMS) to use two years of diagnostic data in its risk adjustment methodology for MA payments. It also prohibits the CMS from using diagnoses that are collected from chart reviews or health risk assessments when adjusting payments based on health status. The CMS must also take into account any differences in coding patterns between MA and traditional Medicare when determining MA payment adjustments.</p>"
        },
        "title": "No UPCODE Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s1105.xml",
    "summary": {
      "actionDate": "2025-03-25",
      "actionDesc": "Introduced in Senate",
      "text": "<p><b>No Unreasonable Payments, Coding, Or Diagnoses for the Elderly Act or the No UPCODE Act</b></p> <p>This bill modifies certain factors that are used to determine Medicare Advantage (MA) payments, particularly relating to health status and related data. </p> <p>Specifically, the bill requires the Centers for Medicare & Medicaid Services (CMS) to use two years of diagnostic data in its risk adjustment methodology for MA payments. It also prohibits the CMS from using diagnoses that are collected from chart reviews or health risk assessments when adjusting payments based on health status. The CMS must also take into account any differences in coding patterns between MA and traditional Medicare when determining MA payment adjustments.</p>",
      "updateDate": "2025-04-18",
      "versionCode": "id119s1105"
    },
    "title": "No UPCODE Act"
  },
  "summaries": [
    {
      "actionDate": "2025-03-25",
      "actionDesc": "Introduced in Senate",
      "text": "<p><b>No Unreasonable Payments, Coding, Or Diagnoses for the Elderly Act or the No UPCODE Act</b></p> <p>This bill modifies certain factors that are used to determine Medicare Advantage (MA) payments, particularly relating to health status and related data. </p> <p>Specifically, the bill requires the Centers for Medicare & Medicaid Services (CMS) to use two years of diagnostic data in its risk adjustment methodology for MA payments. It also prohibits the CMS from using diagnoses that are collected from chart reviews or health risk assessments when adjusting payments based on health status. The CMS must also take into account any differences in coding patterns between MA and traditional Medicare when determining MA payment adjustments.</p>",
      "updateDate": "2025-04-18",
      "versionCode": "id119s1105"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-25",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1105is.xml"
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
      "title": "No UPCODE Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-08T02:53:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "No UPCODE Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-08T02:53:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "No Unreasonable Payments, Coding, Or Diagnoses for the Elderly Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-08T02:53:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title XVIII of the Social Security Act to improve risk adjustment under Medicare Advantage.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-08T02:48:26Z"
    }
  ]
}
```
