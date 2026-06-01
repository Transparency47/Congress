# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3204?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3204
- Title: Preventive Health Savings Act
- Congress: 119
- Bill type: S
- Bill number: 3204
- Origin chamber: Senate
- Introduced date: 2025-11-19
- Update date: 2025-12-18T14:15:10Z
- Update date including text: 2025-12-18T14:15:10Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-11-19: Introduced in Senate
- 2025-11-19 - IntroReferral: Introduced in Senate
- 2025-11-19 - IntroReferral: Read twice and referred to the Committee on the Budget.
- Latest action: 2025-11-19: Introduced in Senate

## Actions

- 2025-11-19 - IntroReferral: Introduced in Senate
- 2025-11-19 - IntroReferral: Read twice and referred to the Committee on the Budget.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-19",
    "latestAction": {
      "actionDate": "2025-11-19",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3204",
    "number": "3204",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Economics and Public Finance"
    },
    "sponsors": [
      {
        "bioguideId": "K000383",
        "district": "",
        "firstName": "Angus",
        "fullName": "Sen. King, Angus S., Jr. [I-ME]",
        "lastName": "King",
        "party": "I",
        "state": "ME"
      }
    ],
    "title": "Preventive Health Savings Act",
    "type": "S",
    "updateDate": "2025-12-18T14:15:10Z",
    "updateDateIncludingText": "2025-12-18T14:15:10Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-11-19",
      "committees": {
        "item": {
          "name": "Budget Committee",
          "systemCode": "ssbu00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on the Budget.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-11-19",
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
          "date": "2025-11-19T19:58:54Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Budget Committee",
      "systemCode": "ssbu00",
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
      "bioguideId": "C000880",
      "firstName": "Mike",
      "fullName": "Sen. Crapo, Mike [R-ID]",
      "isOriginalCosponsor": "True",
      "lastName": "Crapo",
      "party": "R",
      "sponsorshipDate": "2025-11-19",
      "state": "ID"
    },
    {
      "bioguideId": "V000128",
      "firstName": "Chris",
      "fullName": "Sen. Van Hollen, Chris [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Hollen",
      "party": "D",
      "sponsorshipDate": "2025-11-19",
      "state": "MD"
    },
    {
      "bioguideId": "C001096",
      "firstName": "Kevin",
      "fullName": "Sen. Cramer, Kevin [R-ND]",
      "isOriginalCosponsor": "True",
      "lastName": "Cramer",
      "party": "R",
      "sponsorshipDate": "2025-11-19",
      "state": "ND"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3204is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3204\nIN THE SENATE OF THE UNITED STATES\nNovember 19, 2025 Mr. King (for himself, Mr. Crapo , Mr. Van Hollen , and Mr. Cramer ) introduced the following bill; which was read twice and referred to the Committee on the Budget\nA BILL\nTo amend the Congressional Budget Act of 1974 respecting the scoring of preventive health savings.\n#### 1. Short title\nThis Act may be cited as the Preventive Health Savings Act .\n#### 2. Scoring of preventive health savings\nSection 202 of the Congressional Budget and Impoundment Control Act of 1974 ( 2 U.S.C. 602 ) is amended by adding at the end the following:\n(h) Scoring of preventive health savings (1) Determination by the director Upon a request by the chairman and ranking minority member of the Committee on the Budget of the Senate and chairman and ranking minority member of the committee of primary jurisdiction of the Senate or by the chairman and ranking minority member of the Committee on the Budget of the House of Representatives and the chairman and ranking minority member of the committee of primary jurisdiction of the House of Representatives, the Director shall determine if proposed legislation would result in net reductions in budget outlays in budgetary outyears through the use of preventive health care. (2) Projections If the Director determines that proposed legislation would result in net reductions in budget outlays as described in paragraph (1), the Director\u2014 (A) shall include, in any projection prepared by the Director on such proposed legislation, a description and estimate of the reductions in budget outlays in the budgetary outyears and a description of the basis for such conclusions; and (B) may prepare a budget projection that includes some or all of the budgetary outyears, notwithstanding the time periods for projections described in subsection (e) and sections 308, 402, and 424. (3) Limitation Any estimate provided by the Director pursuant to paragraph (1) shall be used as a supplementary estimate and may not be used to determine compliance with the Congressional Budget Act of 1974 or any other budgetary enforcement controls. (4) Definitions As used in this subsection\u2014 (A) the term budgetary outyears means the 2 consecutive 10-year periods beginning with the first fiscal year that is 10 years after the current fiscal year; and (B) the term preventive health care means an action that focuses on the health of the public, individuals, and defined populations in order to protect, promote, and maintain health and wellness and prevent disease, disability, and premature death, including through the promotion and use of effective, innovative health care interventions that are demonstrated by credible and publicly available evidence from epidemiological projection models, clinical trials, observational studies in humans, longitudinal studies, and meta-analysis. .",
      "versionDate": "2025-11-19",
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
        "actionDate": "2025-07-16",
        "text": "Referred to the House Committee on the Budget."
      },
      "number": "4464",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Preventive Health Savings Act",
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
        "name": "Economics and Public Finance",
        "updateDate": "2025-12-17T15:35:22Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-11-19",
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
          "measure-id": "id119s3204",
          "measure-number": "3204",
          "measure-type": "s",
          "orig-publish-date": "2025-11-19",
          "originChamber": "SENATE",
          "update-date": "2025-12-18"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s3204v00",
            "update-date": "2025-12-18"
          },
          "action-date": "2025-11-19",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Preventive Health Savings Act</strong></p><p>This bill requires the Congressional Budget Office (CBO), upon receiving a request from Congress, to determine if proposed legislation would reduce spending outside of the 10-year budget window through the use of preventive health care.</p><p>Under the bill, the term <em>preventive health care</em> generally refers to an action that focuses on the health of the public, individuals, and defined populations in order to protect, promote, and maintain health and wellness and prevent disease, disability, and premature death.</p><p>If CBO determines that the proposed legislation would result in net reductions in budget outlays from the use of preventive health care, any CBO projection regarding the legislation must include (1) a description and estimate of the reductions in outlays, and (2) a description of the basis for these conclusions.\u00a0</p><p>Any estimate provided by CBO pursuant to this bill must be used as a supplementary estimate and may not be used to determine compliance with the Congressional Budget Act of 1974 or any other budgetary enforcement controls.</p>"
        },
        "title": "Preventive Health Savings Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s3204.xml",
    "summary": {
      "actionDate": "2025-11-19",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Preventive Health Savings Act</strong></p><p>This bill requires the Congressional Budget Office (CBO), upon receiving a request from Congress, to determine if proposed legislation would reduce spending outside of the 10-year budget window through the use of preventive health care.</p><p>Under the bill, the term <em>preventive health care</em> generally refers to an action that focuses on the health of the public, individuals, and defined populations in order to protect, promote, and maintain health and wellness and prevent disease, disability, and premature death.</p><p>If CBO determines that the proposed legislation would result in net reductions in budget outlays from the use of preventive health care, any CBO projection regarding the legislation must include (1) a description and estimate of the reductions in outlays, and (2) a description of the basis for these conclusions.\u00a0</p><p>Any estimate provided by CBO pursuant to this bill must be used as a supplementary estimate and may not be used to determine compliance with the Congressional Budget Act of 1974 or any other budgetary enforcement controls.</p>",
      "updateDate": "2025-12-18",
      "versionCode": "id119s3204"
    },
    "title": "Preventive Health Savings Act"
  },
  "summaries": [
    {
      "actionDate": "2025-11-19",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Preventive Health Savings Act</strong></p><p>This bill requires the Congressional Budget Office (CBO), upon receiving a request from Congress, to determine if proposed legislation would reduce spending outside of the 10-year budget window through the use of preventive health care.</p><p>Under the bill, the term <em>preventive health care</em> generally refers to an action that focuses on the health of the public, individuals, and defined populations in order to protect, promote, and maintain health and wellness and prevent disease, disability, and premature death.</p><p>If CBO determines that the proposed legislation would result in net reductions in budget outlays from the use of preventive health care, any CBO projection regarding the legislation must include (1) a description and estimate of the reductions in outlays, and (2) a description of the basis for these conclusions.\u00a0</p><p>Any estimate provided by CBO pursuant to this bill must be used as a supplementary estimate and may not be used to determine compliance with the Congressional Budget Act of 1974 or any other budgetary enforcement controls.</p>",
      "updateDate": "2025-12-18",
      "versionCode": "id119s3204"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-11-19",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3204is.xml"
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
      "title": "Preventive Health Savings Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-17T04:23:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Preventive Health Savings Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-17T04:23:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Congressional Budget Act of 1974 respecting the scoring of preventive health savings.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-17T04:18:21Z"
    }
  ]
}
```
