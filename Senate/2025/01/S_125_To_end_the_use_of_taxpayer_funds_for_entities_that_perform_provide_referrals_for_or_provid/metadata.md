# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/125?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/125
- Title: End Taxpayer Funding for Abortion Providers Act
- Congress: 119
- Bill type: S
- Bill number: 125
- Origin chamber: Senate
- Introduced date: 2025-01-16
- Update date: 2025-04-21T12:24:17Z
- Update date including text: 2025-04-21T12:24:17Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-16: Introduced in Senate
- 2025-01-16 - IntroReferral: Introduced in Senate
- 2025-01-16 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- Latest action: 2025-01-16: Introduced in Senate

## Actions

- 2025-01-16 - IntroReferral: Introduced in Senate
- 2025-01-16 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-16",
    "latestAction": {
      "actionDate": "2025-01-16",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/125",
    "number": "125",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "H001089",
        "district": "",
        "firstName": "Josh",
        "fullName": "Sen. Hawley, Josh [R-MO]",
        "lastName": "Hawley",
        "party": "R",
        "state": "MO"
      }
    ],
    "title": "End Taxpayer Funding for Abortion Providers Act",
    "type": "S",
    "updateDate": "2025-04-21T12:24:17Z",
    "updateDateIncludingText": "2025-04-21T12:24:17Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-01-16",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-01-16",
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
          "date": "2025-01-16T18:55:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Health, Education, Labor, and Pensions Committee",
      "systemCode": "sshr00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s125is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 125\nIN THE SENATE OF THE UNITED STATES\nJanuary 16, 2025 Mr. Hawley introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo end the use of taxpayer funds for entities that perform, provide referrals for, or provide funding for, abortions, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the End Taxpayer Funding for Abortion Providers Act .\n#### 2. Prohibition\n##### (a) In general\nNotwithstanding any other provision of law, no Federal funds may be made available to an entity, or to any of its affiliates, subsidiaries, successors, or clinics, that performs abortions, provides referrals for abortion, or provides funding to other entities that perform abortions. Federal statutory law adopted after the effective date described in subsection (d) is subject to this section unless such law explicitly excludes such application by reference to this section.\n##### (b) Exceptions\nSubsection (a) shall not apply with respect to an abortion if\u2014\n**(1)**\nthe pregnancy is the result of rape or incest; or\n**(2)**\na physician certifies that the woman suffers from a physical condition that would place the woman in danger of death unless an abortion is performed.\n##### (c) Rule of construction\nNothing in this section shall be construed to affect any limitation contained in an appropriations Act relating to abortion.\n##### (d) Effective date\nThis section shall take effect 60 days after the date of enactment of this Act.",
      "versionDate": "2025-01-16",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Abortion",
            "updateDate": "2025-03-13T15:59:43Z"
          },
          {
            "name": "Health programs administration and funding",
            "updateDate": "2025-03-13T15:59:49Z"
          }
        ]
      },
      "policyArea": {
        "name": "Health",
        "updateDate": "2025-02-19T20:29:12Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-16",
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
          "measure-id": "id119s125",
          "measure-number": "125",
          "measure-type": "s",
          "orig-publish-date": "2025-01-16",
          "originChamber": "SENATE",
          "update-date": "2025-03-14"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s125v00",
            "update-date": "2025-03-14"
          },
          "action-date": "2025-01-16",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>End Taxpayer Funding for Abortion Providers Act</strong></p><p>This bill prohibits federal funding for\u00a0entities, or their affiliates, that perform abortions, provide referrals for abortions, or provide funding to others that perform abortions. It provides exceptions for abortions\u00a0(1) in the case of\u00a0rape or incest, or (2) when a physician certifies there is a danger of death to the woman without an abortion.\u00a0</p><p>The bill\u2019s prohibition applies to any federal statutory law adopted after the bill\u2019s effective date, unless such law contains an explicit exemption.\u00a0</p>"
        },
        "title": "End Taxpayer Funding for Abortion Providers Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s125.xml",
    "summary": {
      "actionDate": "2025-01-16",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>End Taxpayer Funding for Abortion Providers Act</strong></p><p>This bill prohibits federal funding for\u00a0entities, or their affiliates, that perform abortions, provide referrals for abortions, or provide funding to others that perform abortions. It provides exceptions for abortions\u00a0(1) in the case of\u00a0rape or incest, or (2) when a physician certifies there is a danger of death to the woman without an abortion.\u00a0</p><p>The bill\u2019s prohibition applies to any federal statutory law adopted after the bill\u2019s effective date, unless such law contains an explicit exemption.\u00a0</p>",
      "updateDate": "2025-03-14",
      "versionCode": "id119s125"
    },
    "title": "End Taxpayer Funding for Abortion Providers Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-16",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>End Taxpayer Funding for Abortion Providers Act</strong></p><p>This bill prohibits federal funding for\u00a0entities, or their affiliates, that perform abortions, provide referrals for abortions, or provide funding to others that perform abortions. It provides exceptions for abortions\u00a0(1) in the case of\u00a0rape or incest, or (2) when a physician certifies there is a danger of death to the woman without an abortion.\u00a0</p><p>The bill\u2019s prohibition applies to any federal statutory law adopted after the bill\u2019s effective date, unless such law contains an explicit exemption.\u00a0</p>",
      "updateDate": "2025-03-14",
      "versionCode": "id119s125"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-16",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s125is.xml"
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
      "title": "End Taxpayer Funding for Abortion Providers Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-19T03:23:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "End Taxpayer Funding for Abortion Providers Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-19T03:23:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to end the use of taxpayer funds for entities that perform, provide referrals for, or provide funding for, abortions, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-19T03:18:25Z"
    }
  ]
}
```
