# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2181?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2181
- Title: Securing Our Propane Supply Act
- Congress: 119
- Bill type: S
- Bill number: 2181
- Origin chamber: Senate
- Introduced date: 2025-06-26
- Update date: 2026-03-24T12:48:03Z
- Update date including text: 2026-03-24T12:48:03Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-06-26: Introduced in Senate
- 2025-06-26 - IntroReferral: Introduced in Senate
- 2025-06-26 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.
- Latest action: 2025-06-26: Introduced in Senate

## Actions

- 2025-06-26 - IntroReferral: Introduced in Senate
- 2025-06-26 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-26",
    "latestAction": {
      "actionDate": "2025-06-26",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2181",
    "number": "2181",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Energy"
    },
    "sponsors": [
      {
        "bioguideId": "P000595",
        "district": "",
        "firstName": "Gary",
        "fullName": "Sen. Peters, Gary C. [D-MI]",
        "lastName": "Peters",
        "party": "D",
        "state": "MI"
      }
    ],
    "title": "Securing Our Propane Supply Act",
    "type": "S",
    "updateDate": "2026-03-24T12:48:03Z",
    "updateDateIncludingText": "2026-03-24T12:48:03Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-06-26",
      "committees": {
        "item": {
          "name": "Energy and Natural Resources Committee",
          "systemCode": "sseg00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Energy and Natural Resources.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-06-26",
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
          "date": "2025-06-26T20:08:37Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Energy and Natural Resources Committee",
      "systemCode": "sseg00",
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
      "bioguideId": "D000618",
      "firstName": "Steve",
      "fullName": "Sen. Daines, Steve [R-MT]",
      "isOriginalCosponsor": "True",
      "lastName": "Daines",
      "party": "R",
      "sponsorshipDate": "2025-06-26",
      "state": "MT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2181is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2181\nIN THE SENATE OF THE UNITED STATES\nJune 26 (legislative day, June 24), 2025 Mr. Peters (for himself and Mr. Daines ) introduced the following bill; which was read twice and referred to the Committee on Energy and Natural Resources\nA BILL\nTo require the Secretary of Energy to conduct a study to determine the feasibility and effectiveness of establishing a national strategic propane reserve.\n#### 1. Short title\nThis Act may be cited as the Securing Our Propane Supply Act .\n#### 2. Department of Energy study on establishing national strategic propane reserve\n##### (a) Study\n**(1) In general**\nNot later than 180 days after the date of enactment of this Act, the Secretary of Energy, in consultation with the Administrator of the Energy Information Administration, shall complete a study to determine the feasibility and effectiveness of establishing a national strategic propane reserve, separate from the Strategic Petroleum Reserve established under part B of title I of the Energy Policy and Conservation Act ( 42 U.S.C. 6231 et seq. ).\n**(2) Elements**\nThe study under paragraph (1) shall include\u2014\n**(A)**\nan assessment of the current state of the propane supply chain in the United States to meet current and forecasted consumer demands;\n**(B)**\nan assessment of the risks of regional propane supply disruptions, including\u2014\n**(i)**\npast causes of disruptions;\n**(ii)**\npossible causes of disruptions in the future; and\n**(iii)**\nwhether disruptions justify the establishment of a national strategic propane reserve;\n**(C)**\nan evaluation of\u2014\n**(i)**\nappropriate and most suitable locations for a strategic propane reserve;\n**(ii)**\nthe quantity of propane storage that would be appropriate at each such location; and\n**(iii)**\nthe suitability of existing infrastructure to facilitate transportation and delivery of propane from a strategic propane reserve during a drawdown;\n**(D)**\nan evaluation of the additional infrastructure needed for a strategic propane reserve to function properly;\n**(E)**\nconsideration of the means by which a strategic propane reserve would prevent and manage degradation of the propane in storage;\n**(F)**\nan evaluation of appropriate triggers (including price and supply) for making available propane from a strategic reserve;\n**(G)**\nan evaluation of the appropriate manner of acquiring propane and propane storage for a strategic reserve, while minimizing market implications, including an assessment of\u2014\n**(i)**\nunutilized and under-utilized storage; and\n**(ii)**\nnew storage opportunities;\n**(H)**\nan evaluation of the appropriate transactions (including direct sales, exchanges, or other options) for delivering propane in a strategic reserve to the market when a release is triggered;\n**(I)**\nan evaluation of likely consumers (including individuals, agricultural producers, and the Armed Forces) of propane from a strategic reserve, including\u2014\n**(i)**\nidentification and categorization of those consumers;\n**(ii)**\na State-by-State breakdown of propane usage by those consumers; and\n**(iii)**\nan evaluation of the expected impacts of a strategic propane reserve on those categories of consumers and States;\n**(J)**\nan evaluation of the market implications of establishing and administering a strategic propane reserve, including an assessment of potential price and supply effects; and\n**(K)**\nidentification, preliminary assessment, and evaluation of alternatives to a strategic propane reserve that could provide supply and price relief during regional propane supply disruptions.\n**(3) Recommendations**\nIn conducting the study under this subsection, the Secretary of Energy shall develop recommendations with respect to each element of the study described in paragraph (2) regarding\u2014\n**(A)**\nwhether a national strategic propane reserve should be established; and\n**(B)**\nif such a reserve should be established, the most practicable method of establishment.\n##### (b) Plan\nNot later than 180 days after the date of completion of the study under subsection (a), the Secretary of Energy shall develop a plan for implementing the recommendations developed under paragraph (3) of that subsection.\n##### (c) Industry coordination\nIn conducting the study under subsection (a) and developing the plan under subsection (b), the Secretary of Energy is encouraged to coordinate with entities in the propane industry, including representatives from the entire propane supply chain.\n##### (d) Submission to Congress\nThe Secretary of Energy shall submit to the Committee on Energy and Natural Resources of the Senate and the Committee on Energy and Commerce of the House of Representatives a report describing\u2014\n**(1)**\nthe study completed under subsection (a); and\n**(2)**\nthe plan developed under subsection (b).\n##### (e) Protection of national security information\nBefore submitting the report under subsection (d), or otherwise publishing the study completed under subsection (a) or the plan developed under subsection (b), the Secretary of Energy shall adopt such procedures with respect to confidentiality (including procedures for redaction of information) as the Secretary determines to be necessary to ensure the protection of classified information relating to specific vulnerabilities to United States energy security or reliability.",
      "versionDate": "2025-06-26",
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
        "name": "Energy",
        "updateDate": "2025-07-25T12:15:50Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-06-26",
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
          "measure-id": "id119s2181",
          "measure-number": "2181",
          "measure-type": "s",
          "orig-publish-date": "2025-06-26",
          "originChamber": "SENATE",
          "update-date": "2026-05-07"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s2181v00",
            "update-date": "2026-05-07"
          },
          "action-date": "2025-06-26",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Securing Our Propane Supply Act</strong></p><p>This bill requires the Department of Energy (DOE) to study and evaluate methods of\u00a0addressing disruptions to propane supplies, which are used to heat homes. Specifically, DOE must study the feasibility and effectiveness of establishing a national strategic propane reserve that is separate from the Strategic Petroleum Reserve. If the study recommends the establishment of\u00a0a reserve, then DOE must develop an implementation plan. The plan must include the most practicable method for establishing the reserve.</p>"
        },
        "title": "Securing Our Propane Supply Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s2181.xml",
    "summary": {
      "actionDate": "2025-06-26",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Securing Our Propane Supply Act</strong></p><p>This bill requires the Department of Energy (DOE) to study and evaluate methods of\u00a0addressing disruptions to propane supplies, which are used to heat homes. Specifically, DOE must study the feasibility and effectiveness of establishing a national strategic propane reserve that is separate from the Strategic Petroleum Reserve. If the study recommends the establishment of\u00a0a reserve, then DOE must develop an implementation plan. The plan must include the most practicable method for establishing the reserve.</p>",
      "updateDate": "2026-05-07",
      "versionCode": "id119s2181"
    },
    "title": "Securing Our Propane Supply Act"
  },
  "summaries": [
    {
      "actionDate": "2025-06-26",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Securing Our Propane Supply Act</strong></p><p>This bill requires the Department of Energy (DOE) to study and evaluate methods of\u00a0addressing disruptions to propane supplies, which are used to heat homes. Specifically, DOE must study the feasibility and effectiveness of establishing a national strategic propane reserve that is separate from the Strategic Petroleum Reserve. If the study recommends the establishment of\u00a0a reserve, then DOE must develop an implementation plan. The plan must include the most practicable method for establishing the reserve.</p>",
      "updateDate": "2026-05-07",
      "versionCode": "id119s2181"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-06-26",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2181is.xml"
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
      "title": "Securing Our Propane Supply Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-16T03:38:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Securing Our Propane Supply Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-16T03:38:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require the Secretary of Energy to conduct a study to determine the feasibility and effectiveness of establishing a national strategic propane reserve.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-16T03:33:21Z"
    }
  ]
}
```
