# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2524?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/2524
- Title: REPEAL CBO Requirements Act
- Congress: 119
- Bill type: HR
- Bill number: 2524
- Origin chamber: House
- Introduced date: 2025-03-31
- Update date: 2025-05-14T15:10:44Z
- Update date including text: 2025-05-14T15:10:44Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-03-31: Introduced in House
- 2025-03-31 - IntroReferral: Introduced in House
- 2025-03-31 - IntroReferral: Introduced in House
- 2025-03-31 - IntroReferral: Referred to the Committee on Rules, and in addition to the Committee on the Budget, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-03-31 - IntroReferral: Referred to the Committee on Rules, and in addition to the Committee on the Budget, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-03-31: Introduced in House

## Actions

- 2025-03-31 - IntroReferral: Introduced in House
- 2025-03-31 - IntroReferral: Introduced in House
- 2025-03-31 - IntroReferral: Referred to the Committee on Rules, and in addition to the Committee on the Budget, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-03-31 - IntroReferral: Referred to the Committee on Rules, and in addition to the Committee on the Budget, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-31",
    "latestAction": {
      "actionDate": "2025-03-31",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/2524",
    "number": "2524",
    "originChamber": "House",
    "policyArea": {
      "name": "Economics and Public Finance"
    },
    "sponsors": [
      {
        "bioguideId": "T000478",
        "district": "24",
        "firstName": "Claudia",
        "fullName": "Rep. Tenney, Claudia [R-NY-24]",
        "lastName": "Tenney",
        "party": "R",
        "state": "NY"
      }
    ],
    "title": "REPEAL CBO Requirements Act",
    "type": "HR",
    "updateDate": "2025-05-14T15:10:44Z",
    "updateDateIncludingText": "2025-05-14T15:10:44Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-31",
      "committees": {
        "item": {
          "name": "Budget Committee",
          "systemCode": "hsbu00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Rules, and in addition to the Committee on the Budget, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-31",
      "committees": {
        "item": {
          "name": "Rules Committee",
          "systemCode": "hsru00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Rules, and in addition to the Committee on the Budget, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-03-31",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-31",
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
          "date": "2025-03-31T16:04:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Budget Committee",
      "systemCode": "hsbu00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-03-31T16:03:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Rules Committee",
      "systemCode": "hsru00",
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
      "bioguideId": "C001129",
      "district": "10",
      "firstName": "Mike",
      "fullName": "Rep. Collins, Mike [R-GA-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Collins",
      "party": "R",
      "sponsorshipDate": "2025-03-31",
      "state": "GA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2524ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2524\nIN THE HOUSE OF REPRESENTATIVES\nMarch 31, 2025 Ms. Tenney (for herself and Mr. Collins ) introduced the following bill; which was referred to the Committee on Rules , and in addition to the Committee on the Budget , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend the Congressional Budget and Impoundment Control Act of 1974 to provide that Congress may request estimates of legislation from reputable accounting firms for purposes of budget enforcement, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Replacing Exploitative Partisan Estimates with Alternatives by Liquidating Congressional Budget Office Requirements or the REPEAL CBO Requirements Act .\n#### 2. Budget estimates by reputable accounting firms\n##### (a) In general\nSection 402 of the Congressional Budget and Impoundment Control Act of 1985 ( 2 U.S.C. 653 ) is amended\u2014\n**(1)**\nby striking The Director and inserting (a) In general .\u2014The Director ; and\n**(2)**\nby adding at the end the following:\n(b) Estimate by accounting firms (A) In general Notwithstanding any other provision of law, the chair of any committee of the House of Representatives or the Senate (except the Committee on Appropriations of each House) may, instead of an estimate under subsection (a), obtain an estimate for any bill or resolution of a public character reported by such committee from a private reputable accounting firm. (B) Application (i) In general Any estimate obtained under subparagraph (A) shall be used in lieu of an estimate prepared by the Congressional Budget Office under subsection (a) for budget enforcement with respect to the applicable bill or joint resolution, including for purposes of this Act, the Balanced Budget and Emergency Deficit Control Act of 1985, the Statutory Pay-As-You-Go Act of 2010, any concurrent resolution on the budget, the Rules of the House of Representatives, and the Standing Rules of the Senate (including for purposes of reconciliation). (ii) CBO estimate not required If an estimate is obtained under subparagraph (A), then the Office shall not prepare an estimate for the applicable measure under subsection (a). (C) Definition of private reputable accounting firm In this subsection, the term private reputable accounting firm means any of the ten public accounting firms registered with the Public Company Accounting Oversight Board with the largest net revenue during the previous year. .\n##### (b) Conforming amendment\nSection 312(a) of such Act is amended by adding at the end the following: The estimates by a private reputable accounting firm under section 402(b) may be used by either such Committee for purposes of carrying out this subsection. .",
      "versionDate": "2025-03-31",
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
        "name": "Economics and Public Finance",
        "updateDate": "2025-05-13T15:28:53Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-31",
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
          "measure-id": "id119hr2524",
          "measure-number": "2524",
          "measure-type": "hr",
          "orig-publish-date": "2025-03-31",
          "originChamber": "HOUSE",
          "update-date": "2025-05-14"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr2524v00",
            "update-date": "2025-05-14"
          },
          "action-date": "2025-03-31",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Replacing Exploitative Partisan Estimates with Alternatives by Liquidating Congressional Budget Office Requirements or the REPEAL CBO Requirements Act</strong></p><p>This bill allows\u00a0certain\u00a0congressional committees to obtain cost estimates for legislation from private reputable accounting firms rather than the Congressional Budget Office (CBO).</p><p>Under current law, CBO is generally required to produce cost estimates for most bills that are reported by congressional committees. This bill allows chairs of congressional committees (except the appropriations committees) to obtain estimates for reported legislation from a private reputable accounting firm instead of\u00a0CBO. Under the bill, a <em>private reputable accounting firm</em> means any of the 10 public accounting firms registered with the Public Company Accounting Oversight Board with the largest net revenue during the previous year.</p><p>If a committee chair obtains an estimate from a private accounting firm pursuant to this bill, (1) the estimate must be used for budget enforcement purposes, and (2) CBO may not prepare an estimate for the applicable measure.</p>"
        },
        "title": "REPEAL CBO Requirements Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr2524.xml",
    "summary": {
      "actionDate": "2025-03-31",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Replacing Exploitative Partisan Estimates with Alternatives by Liquidating Congressional Budget Office Requirements or the REPEAL CBO Requirements Act</strong></p><p>This bill allows\u00a0certain\u00a0congressional committees to obtain cost estimates for legislation from private reputable accounting firms rather than the Congressional Budget Office (CBO).</p><p>Under current law, CBO is generally required to produce cost estimates for most bills that are reported by congressional committees. This bill allows chairs of congressional committees (except the appropriations committees) to obtain estimates for reported legislation from a private reputable accounting firm instead of\u00a0CBO. Under the bill, a <em>private reputable accounting firm</em> means any of the 10 public accounting firms registered with the Public Company Accounting Oversight Board with the largest net revenue during the previous year.</p><p>If a committee chair obtains an estimate from a private accounting firm pursuant to this bill, (1) the estimate must be used for budget enforcement purposes, and (2) CBO may not prepare an estimate for the applicable measure.</p>",
      "updateDate": "2025-05-14",
      "versionCode": "id119hr2524"
    },
    "title": "REPEAL CBO Requirements Act"
  },
  "summaries": [
    {
      "actionDate": "2025-03-31",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Replacing Exploitative Partisan Estimates with Alternatives by Liquidating Congressional Budget Office Requirements or the REPEAL CBO Requirements Act</strong></p><p>This bill allows\u00a0certain\u00a0congressional committees to obtain cost estimates for legislation from private reputable accounting firms rather than the Congressional Budget Office (CBO).</p><p>Under current law, CBO is generally required to produce cost estimates for most bills that are reported by congressional committees. This bill allows chairs of congressional committees (except the appropriations committees) to obtain estimates for reported legislation from a private reputable accounting firm instead of\u00a0CBO. Under the bill, a <em>private reputable accounting firm</em> means any of the 10 public accounting firms registered with the Public Company Accounting Oversight Board with the largest net revenue during the previous year.</p><p>If a committee chair obtains an estimate from a private accounting firm pursuant to this bill, (1) the estimate must be used for budget enforcement purposes, and (2) CBO may not prepare an estimate for the applicable measure.</p>",
      "updateDate": "2025-05-14",
      "versionCode": "id119hr2524"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-31",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2524ih.xml"
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
      "title": "REPEAL CBO Requirements Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-08T04:23:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "REPEAL CBO Requirements Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-08T04:23:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Replacing Exploitative Partisan Estimates with Alternatives by Liquidating Congressional Budget Office Requirements",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-08T04:23:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Congressional Budget and Impoundment Control Act of 1974 to provide that Congress may request estimates of legislation from reputable accounting firms for purposes of budget enforcement, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-08T04:18:29Z"
    }
  ]
}
```
