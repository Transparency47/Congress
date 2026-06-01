# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1550?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1550
- Title: Improving SCRA Benefit Utilization Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1550
- Origin chamber: Senate
- Introduced date: 2025-05-01
- Update date: 2026-03-03T17:34:34Z
- Update date including text: 2026-03-03T17:34:34Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-05-01: Introduced in Senate
- 2025-05-01 - IntroReferral: Introduced in Senate
- 2025-05-01 - IntroReferral: Read twice and referred to the Committee on Armed Services.
- Latest action: 2025-05-01: Introduced in Senate

## Actions

- 2025-05-01 - IntroReferral: Introduced in Senate
- 2025-05-01 - IntroReferral: Read twice and referred to the Committee on Armed Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-01",
    "latestAction": {
      "actionDate": "2025-05-01",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1550",
    "number": "1550",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "O000174",
        "district": "",
        "firstName": "Jon",
        "fullName": "Sen. Ossoff, Jon [D-GA]",
        "lastName": "Ossoff",
        "party": "D",
        "state": "GA"
      }
    ],
    "title": "Improving SCRA Benefit Utilization Act of 2025",
    "type": "S",
    "updateDate": "2026-03-03T17:34:34Z",
    "updateDateIncludingText": "2026-03-03T17:34:34Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-01",
      "committees": {
        "item": {
          "name": "Armed Services Committee",
          "systemCode": "ssas00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Armed Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-05-01",
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
          "date": "2025-05-01T15:34:23Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Armed Services Committee",
      "systemCode": "ssas00",
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
      "bioguideId": "S001217",
      "firstName": "Rick",
      "fullName": "Sen. Scott, Rick [R-FL]",
      "isOriginalCosponsor": "True",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-05-01",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1550is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1550\nIN THE SENATE OF THE UNITED STATES\nMay 1, 2025 Mr. Ossoff (for himself and Mr. Scott of Florida ) introduced the following bill; which was read twice and referred to the Committee on Armed Services\nA BILL\nTo amend title 10, United States Code, to include training regarding financial protections under the Servicemembers Civil Relief Act in certain financial literacy training programs for members of the Armed Forces, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Improving SCRA Benefit Utilization Act of 2025 .\n#### 2. Financial literacy training regarding the Servicemembers Civil Relief Act\nSection 992 of title 10, United States Code, is amended\u2014\n**(1)**\nin subsection (a)(1)\u2014\n**(A)**\nby redesignating subparagraphs (D) and (E) as subparagraphs (E) and (F), respectively; and\n**(B)**\nby inserting, after subparagraph (C), the following new subparagraph (D):\n(D) consumer financial protections afforded to members and their dependents under the law, including protections regarding interest rate limits under section 207 of the Servicemembers Civil Relief Act ( 50 U.S.C. 3937 ); ; and\n**(2)**\nin subsection (d)(1), by inserting (including with regards to knowledge and use of protections regarding interest rates under section 207 of the Servicemembers Civil Relief Act ( 50 U.S.C. 3937 )) after preparedness .\n#### 3. Notification of benefits under the Servicemembers Civil Relief Act to servicemembers called or ordered to active duty or to active service\nSection 105 of the Servicemembers Civil Relief Act ( 50 U.S.C. 3915 ) is amended\u2014\n**(1)**\nby striking the period at the end and inserting , including\u2014 ; and\n**(2)**\nby adding at the end the following new paragraphs:\n(1) at the time a person first enters military service; and (2) in the case of a person who is a member of a reserve component\u2014 (A) at the time the person first enters service in the reserve component; and (B) at any time when the person is mobilized or otherwise individually called or ordered to active duty for a period of more than 30 days. .\n#### 4. Financial institution obligation to apply maximum rate of interest on all servicemember debts incurred before military service\nSection 207(b) of the Servicemembers Civil Relief Act ( 50 U.S.C. 3937 ) is amended\u2014\n**(1)**\nin paragraph (2)\u2014\n**(A)**\nby striking the creditor shall treat the debt in accordance with subsection (a), effective as of the date on which the servicemember is called to military service. and inserting the creditor shall\u2014 ; and\n**(B)**\nby adding at the end the following new subparagraphs:\n(A) treat the debt in accordance with subsection (a), effective as of the date on which the servicemember is called to military service; and (B) treat any other obligation or liability of the servicemember to the creditor in accordance with subsection (a), whether or not such obligation or liability was specifically mentioned in a notice provided by the servicemember under paragraph (1)(A). ; and\n**(2)**\nby adding at the end the following new paragraph:\n(3) Submission of documents A creditor shall provide all necessary mechanisms to ensure that a servicemember is able to submit any documents required in order for an obligation or liability of the servicemember to be subject to the interest rate limitation in subsection (a) either online, by mail, or by fax, at the election of the servicemember. .",
      "versionDate": "2025-05-01",
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
        "actionDate": "2026-02-24",
        "text": "Forwarded by Subcommittee to Full Committee by Voice Vote."
      },
      "number": "3159",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Improving SCRA Benefit Utilization Act",
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
        "name": "Armed Forces and National Security",
        "updateDate": "2025-06-04T15:40:26Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-05-01",
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
          "measure-id": "id119s1550",
          "measure-number": "1550",
          "measure-type": "s",
          "orig-publish-date": "2025-05-01",
          "originChamber": "SENATE",
          "update-date": "2026-03-03"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s1550v00",
            "update-date": "2026-03-03"
          },
          "action-date": "2025-05-01",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Improving SCRA Benefit Utilization Act of 2025</strong></p><p>This bill expands interest rate protections under the\u00a0Servicemembers Civil Relief Act (SCRA) and requires expanded training for and outreach to servicemembers regarding financial literacy and SCRA protections.</p><p>The SCRA caps the maximum interest charged on any debt incurred by a servicemember prior to entering active duty at 6% annually if the servicemember's ability to pay is materially affected by active-duty status; servicemembers must provide notice and other documentation to creditors to receive this cap.</p><p>The bill requires creditors to apply this\u00a0cap to all of a\u00a0servicemember\u2019s obligations or liabilities with that creditor, regardless of whether a certain obligation or liability was specifically mentioned in the required notice provided by the member to invoke SCRA rights.\u00a0Further, the bill requires creditors to provide all necessary mechanisms to ensure a\u00a0servicemember is able to submit any required documentation.</p><p>The bill also requires that the financial literacy training program provided to servicemembers\u00a0include information about consumer financial protections afforded to such members and their dependents, including protections regarding interest rate limits under the\u00a0SCRA.\u00a0</p><p>Additionally, the bill requires the military department concerned to provide written notice of benefits under the\u00a0SCRA to servicemembers at the time they first enter military service and, for members of the reserve components, at the time they first enter service in the reserves and at any time when they are mobilized or ordered to active duty for more than 30 days.</p>"
        },
        "title": "Improving SCRA Benefit Utilization Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s1550.xml",
    "summary": {
      "actionDate": "2025-05-01",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Improving SCRA Benefit Utilization Act of 2025</strong></p><p>This bill expands interest rate protections under the\u00a0Servicemembers Civil Relief Act (SCRA) and requires expanded training for and outreach to servicemembers regarding financial literacy and SCRA protections.</p><p>The SCRA caps the maximum interest charged on any debt incurred by a servicemember prior to entering active duty at 6% annually if the servicemember's ability to pay is materially affected by active-duty status; servicemembers must provide notice and other documentation to creditors to receive this cap.</p><p>The bill requires creditors to apply this\u00a0cap to all of a\u00a0servicemember\u2019s obligations or liabilities with that creditor, regardless of whether a certain obligation or liability was specifically mentioned in the required notice provided by the member to invoke SCRA rights.\u00a0Further, the bill requires creditors to provide all necessary mechanisms to ensure a\u00a0servicemember is able to submit any required documentation.</p><p>The bill also requires that the financial literacy training program provided to servicemembers\u00a0include information about consumer financial protections afforded to such members and their dependents, including protections regarding interest rate limits under the\u00a0SCRA.\u00a0</p><p>Additionally, the bill requires the military department concerned to provide written notice of benefits under the\u00a0SCRA to servicemembers at the time they first enter military service and, for members of the reserve components, at the time they first enter service in the reserves and at any time when they are mobilized or ordered to active duty for more than 30 days.</p>",
      "updateDate": "2026-03-03",
      "versionCode": "id119s1550"
    },
    "title": "Improving SCRA Benefit Utilization Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-05-01",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Improving SCRA Benefit Utilization Act of 2025</strong></p><p>This bill expands interest rate protections under the\u00a0Servicemembers Civil Relief Act (SCRA) and requires expanded training for and outreach to servicemembers regarding financial literacy and SCRA protections.</p><p>The SCRA caps the maximum interest charged on any debt incurred by a servicemember prior to entering active duty at 6% annually if the servicemember's ability to pay is materially affected by active-duty status; servicemembers must provide notice and other documentation to creditors to receive this cap.</p><p>The bill requires creditors to apply this\u00a0cap to all of a\u00a0servicemember\u2019s obligations or liabilities with that creditor, regardless of whether a certain obligation or liability was specifically mentioned in the required notice provided by the member to invoke SCRA rights.\u00a0Further, the bill requires creditors to provide all necessary mechanisms to ensure a\u00a0servicemember is able to submit any required documentation.</p><p>The bill also requires that the financial literacy training program provided to servicemembers\u00a0include information about consumer financial protections afforded to such members and their dependents, including protections regarding interest rate limits under the\u00a0SCRA.\u00a0</p><p>Additionally, the bill requires the military department concerned to provide written notice of benefits under the\u00a0SCRA to servicemembers at the time they first enter military service and, for members of the reserve components, at the time they first enter service in the reserves and at any time when they are mobilized or ordered to active duty for more than 30 days.</p>",
      "updateDate": "2026-03-03",
      "versionCode": "id119s1550"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-05-01",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1550is.xml"
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
      "title": "Improving SCRA Benefit Utilization Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-14T04:23:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Improving SCRA Benefit Utilization Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-14T04:23:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title 10, United States Code, to include training regarding financial protections under the Servicemembers Civil Relief Act in certain financial literacy training programs for members of the Armed Forces, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-14T04:18:52Z"
    }
  ]
}
```
