# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/737?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/737
- Title: Extraordinary Measures Transparency Act
- Congress: 119
- Bill type: HR
- Bill number: 737
- Origin chamber: House
- Introduced date: 2025-01-24
- Update date: 2025-06-13T18:07:54Z
- Update date including text: 2025-06-13T18:07:54Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-24: Introduced in House
- 2025-01-24 - IntroReferral: Introduced in House
- 2025-01-24 - IntroReferral: Introduced in House
- 2025-01-24 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-01-24: Introduced in House

## Actions

- 2025-01-24 - IntroReferral: Introduced in House
- 2025-01-24 - IntroReferral: Introduced in House
- 2025-01-24 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-24",
    "latestAction": {
      "actionDate": "2025-01-24",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/737",
    "number": "737",
    "originChamber": "House",
    "policyArea": {
      "name": "Economics and Public Finance"
    },
    "sponsors": [
      {
        "bioguideId": "N000193",
        "district": "3",
        "firstName": "Zachary",
        "fullName": "Rep. Nunn, Zachary [R-IA-3]",
        "lastName": "Nunn",
        "party": "R",
        "state": "IA"
      }
    ],
    "title": "Extraordinary Measures Transparency Act",
    "type": "HR",
    "updateDate": "2025-06-13T18:07:54Z",
    "updateDateIncludingText": "2025-06-13T18:07:54Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-24",
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
      "actionDate": "2025-01-24",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-24",
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
          "date": "2025-01-24T14:02:00Z",
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
      "bioguideId": "D000230",
      "district": "1",
      "firstName": "Donald",
      "fullName": "Rep. Davis, Donald G. [D-NC-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Davis",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2025-01-24",
      "state": "NC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr737ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 737\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 24, 2025 Mr. Nunn of Iowa (for himself and Mr. Davis of North Carolina ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo require the Secretary of the Treasury to issue reports with respect to extraordinary measures, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Extraordinary Measures Transparency Act .\n#### 2. Reports on extraordinary measures\n##### (a) In general\nSubchapter II of chapter 31 of title 31, United States Code, is amended by adding at the end the following:\n3131. Reports on extraordinary measures (a) Report 30 days before reaching debt limit If the Secretary of the Treasury determines that the public debt will reach the debt limit in 30 days, the Secretary shall issue a report to the Congress that contains\u2014 (1) a description of the extraordinary measures that the Secretary intends to use if the debt limit is not raised; (2) an estimate of the cost of such extraordinary measures; (3) a projection of how long such extraordinary measures will fund the Federal Government; and (4) a projection of the administrative cost of taking such extraordinary measures. (b) Daily report while using extraordinary measures The Secretary shall, during any period in which the Secretary is using extraordinary measures, issue a daily report to the Congress that contains a list of which extraordinary measures were taken, including a list of how much money was transferred and from which accounts the money was transferred. (c) Report after using extraordinary measures At the end of a period in which the Secretary was using extraordinary measures, the Secretary shall issue a report to the Congress that contains\u2014 (1) a summary of the extraordinary measures used; and (2) the administrative cost of taking such extraordinary measures. (d) Definitions For purposes of this section: (1) Administrative cost With respect to extraordinary measures, the term administrative cost means\u2014 (A) the personnel and consultant costs required to engage in the extraordinary measures; (B) any fees the Government has to pay in connection with the extraordinary measures; and (C) such other costs as the Secretary determines appropriate. (2) Debt limit The term debt limit means the limit specified under section 3101, as modified by section 3101A. (3) Extraordinary measures The term extraordinary measures means\u2014 (A) directing or approving the issuance of debt by the Federal Financing Bank for the purpose of entering into an exchange transaction for debt that is subject to the limit under this chapter; (B) suspending investments in the Government Securities Investment Fund of the Thrift Savings Fund; (C) suspending investments in the stabilization fund established under section 5302; (D) suspending new investments in the Civil Service Retirement and Disability Fund or the Postal Service Retiree Health Benefits Fund; (E) selling or redeeming securities, obligations, or other invested assets of the Civil Service Retirement and Disability Fund or the Postal Service Retiree Health Benefits Fund before maturity; (F) suspending sales of State and Local Government Series Treasury securities; and (G) such other measures as the Secretary determines appropriate. (4) Secretary The term Secretary means the Secretary of the Treasury. .\n##### (b) Clerical amendment\nThe table of analysis for chapter 31 of title 31, United States Code, is amended by inserting after the item relating to section 3130 the following:\n3131. Reports on extraordinary measures. .",
      "versionDate": "2025-01-24",
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
            "name": "Budget deficits and national debt",
            "updateDate": "2025-06-13T18:07:48Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2025-06-13T18:07:19Z"
          },
          {
            "name": "Department of the Treasury",
            "updateDate": "2025-06-13T18:07:30Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2025-06-13T18:07:54Z"
          }
        ]
      },
      "policyArea": {
        "name": "Economics and Public Finance",
        "updateDate": "2025-05-02T16:39:37Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-24",
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
          "measure-id": "id119hr737",
          "measure-number": "737",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-24",
          "originChamber": "HOUSE",
          "update-date": "2025-05-02"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr737v00",
            "update-date": "2025-05-02"
          },
          "action-date": "2025-01-24",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Extraordinary Measures Transparency Act</strong></p><p>This bill requires the Department of the Treasury to report to Congress regarding extraordinary measures used to avoid exceeding the federal debt limit.</p><p>(The term <em>extraordinary measures</em> refers to a series of actions that Treasury may implement to allow the United States to borrow additional funds without exceeding the debt limit. The measures often include suspensions of debt sales and suspensions or redemptions of investments in certain government funds.)</p><p>If Treasury determines that the public debt will reach the limit in 30 days, Treasury must submit a report to Congress that includes</p><ul><li>a description of the extraordinary measures that Treasury intends to use if the debt limit is not raised,</li><li>an estimate of the cost of the measures,</li><li>a projection of how long the measures will fund the federal government, and</li><li>a projection of the administrative cost of taking the measures.</li></ul><p>Treasury must also submit specified daily reports to Congress when the measures are being used. After using the measures, Treasury must report to Congress regarding the measures that were used and the administrative cost of the measures.</p>"
        },
        "title": "Extraordinary Measures Transparency Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr737.xml",
    "summary": {
      "actionDate": "2025-01-24",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Extraordinary Measures Transparency Act</strong></p><p>This bill requires the Department of the Treasury to report to Congress regarding extraordinary measures used to avoid exceeding the federal debt limit.</p><p>(The term <em>extraordinary measures</em> refers to a series of actions that Treasury may implement to allow the United States to borrow additional funds without exceeding the debt limit. The measures often include suspensions of debt sales and suspensions or redemptions of investments in certain government funds.)</p><p>If Treasury determines that the public debt will reach the limit in 30 days, Treasury must submit a report to Congress that includes</p><ul><li>a description of the extraordinary measures that Treasury intends to use if the debt limit is not raised,</li><li>an estimate of the cost of the measures,</li><li>a projection of how long the measures will fund the federal government, and</li><li>a projection of the administrative cost of taking the measures.</li></ul><p>Treasury must also submit specified daily reports to Congress when the measures are being used. After using the measures, Treasury must report to Congress regarding the measures that were used and the administrative cost of the measures.</p>",
      "updateDate": "2025-05-02",
      "versionCode": "id119hr737"
    },
    "title": "Extraordinary Measures Transparency Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-24",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Extraordinary Measures Transparency Act</strong></p><p>This bill requires the Department of the Treasury to report to Congress regarding extraordinary measures used to avoid exceeding the federal debt limit.</p><p>(The term <em>extraordinary measures</em> refers to a series of actions that Treasury may implement to allow the United States to borrow additional funds without exceeding the debt limit. The measures often include suspensions of debt sales and suspensions or redemptions of investments in certain government funds.)</p><p>If Treasury determines that the public debt will reach the limit in 30 days, Treasury must submit a report to Congress that includes</p><ul><li>a description of the extraordinary measures that Treasury intends to use if the debt limit is not raised,</li><li>an estimate of the cost of the measures,</li><li>a projection of how long the measures will fund the federal government, and</li><li>a projection of the administrative cost of taking the measures.</li></ul><p>Treasury must also submit specified daily reports to Congress when the measures are being used. After using the measures, Treasury must report to Congress regarding the measures that were used and the administrative cost of the measures.</p>",
      "updateDate": "2025-05-02",
      "versionCode": "id119hr737"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-24",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr737ih.xml"
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
      "title": "Extraordinary Measures Transparency Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-26T03:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Extraordinary Measures Transparency Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-26T03:23:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the Secretary of the Treasury to issue reports with respect to extraordinary measures, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-26T03:18:19Z"
    }
  ]
}
```
