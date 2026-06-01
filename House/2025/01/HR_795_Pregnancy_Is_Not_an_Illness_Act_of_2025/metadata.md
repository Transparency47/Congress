# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/795?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/795
- Title: Pregnancy Is Not an Illness Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 795
- Origin chamber: House
- Introduced date: 2025-01-28
- Update date: 2025-05-09T08:06:05Z
- Update date including text: 2025-05-09T08:06:05Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-28: Introduced in House
- 2025-01-28 - IntroReferral: Introduced in House
- 2025-01-28 - IntroReferral: Introduced in House
- 2025-01-28 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-01-28: Introduced in House

## Actions

- 2025-01-28 - IntroReferral: Introduced in House
- 2025-01-28 - IntroReferral: Introduced in House
- 2025-01-28 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-28",
    "latestAction": {
      "actionDate": "2025-01-28",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/795",
    "number": "795",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "M001211",
        "district": "15",
        "firstName": "Mary",
        "fullName": "Rep. Miller, Mary E. [R-IL-15]",
        "lastName": "Miller",
        "party": "R",
        "state": "IL"
      }
    ],
    "title": "Pregnancy Is Not an Illness Act of 2025",
    "type": "HR",
    "updateDate": "2025-05-09T08:06:05Z",
    "updateDateIncludingText": "2025-05-09T08:06:05Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-28",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Energy and Commerce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-01-28",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-28",
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
          "date": "2025-01-28T16:10:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
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
      "bioguideId": "B001291",
      "district": "36",
      "firstName": "Brian",
      "fullName": "Rep. Babin, Brian [R-TX-36]",
      "isOriginalCosponsor": "True",
      "lastName": "Babin",
      "party": "R",
      "sponsorshipDate": "2025-01-28",
      "state": "TX"
    },
    {
      "bioguideId": "M001235",
      "district": "2",
      "firstName": "Riley",
      "fullName": "Rep. Moore, Riley [R-WV-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Moore",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-01-28",
      "state": "WV"
    },
    {
      "bioguideId": "O000175",
      "district": "5",
      "firstName": "Andrew",
      "fullName": "Rep. Ogles, Andrew [R-TN-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Ogles",
      "party": "R",
      "sponsorshipDate": "2025-01-28",
      "state": "TN"
    },
    {
      "bioguideId": "W000806",
      "district": "11",
      "firstName": "Daniel",
      "fullName": "Rep. Webster, Daniel [R-FL-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Webster",
      "party": "R",
      "sponsorshipDate": "2025-01-28",
      "state": "FL"
    },
    {
      "bioguideId": "T000478",
      "district": "24",
      "firstName": "Claudia",
      "fullName": "Rep. Tenney, Claudia [R-NY-24]",
      "isOriginalCosponsor": "True",
      "lastName": "Tenney",
      "party": "R",
      "sponsorshipDate": "2025-01-28",
      "state": "NY"
    },
    {
      "bioguideId": "H001052",
      "district": "1",
      "firstName": "Andy",
      "fullName": "Rep. Harris, Andy [R-MD-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Harris",
      "party": "R",
      "sponsorshipDate": "2025-01-28",
      "state": "MD"
    },
    {
      "bioguideId": "W000814",
      "district": "14",
      "firstName": "Randy",
      "fullName": "Rep. Weber, Randy K. Sr. [R-TX-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Weber",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-01-28",
      "state": "TX"
    },
    {
      "bioguideId": "H001102",
      "district": "8",
      "firstName": "Mark",
      "fullName": "Rep. Harris, Mark [R-NC-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Harris",
      "party": "R",
      "sponsorshipDate": "2025-02-04",
      "state": "NC"
    },
    {
      "bioguideId": "G000590",
      "district": "7",
      "firstName": "Mark",
      "fullName": "Rep. Green, Mark E. [R-TN-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Green",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-03-18",
      "state": "TN"
    },
    {
      "bioguideId": "B001317",
      "district": "2",
      "firstName": "Josh",
      "fullName": "Rep. Brecheen, Josh [R-OK-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Brecheen",
      "party": "R",
      "sponsorshipDate": "2025-05-07",
      "state": "OK"
    },
    {
      "bioguideId": "M001239",
      "district": "5",
      "firstName": "John",
      "fullName": "Rep. McGuire, John J. [R-VA-5]",
      "isOriginalCosponsor": "False",
      "lastName": "McGuire",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-05-08",
      "state": "VA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr795ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 795\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 28, 2025 Mrs. Miller of Illinois (for herself, Mr. Babin , Mr. Moore of West Virginia , Mr. Ogles , Mr. Webster of Florida , Ms. Tenney , Mr. Harris of Maryland , and Mr. Weber of Texas ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo prohibit the Department of Health and Human Services from treating pregnancy as an illness for purposes of approving abortion drugs.\n#### 1. Short title\nThis Act may be cited as the Pregnancy Is Not an Illness Act of 2025 .\n#### 2. Prohibition against treating pregnancy as illness for purposes of approving abortion drugs\n##### (a) Prohibition\nThe Department of Health and Human Services, including the Food and Drug Administration, shall not treat pregnancy as an illness for purposes of\u2014\n**(1)**\napproving any abortion drug under section 505 of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 355 ); or\n**(2)**\nimposing or maintaining any risk evaluation and mitigation strategy for an abortion drug under section 505\u20131 of such Act ( 21 U.S.C. 355\u20131 ).\n##### (b) Nullification of approvals in effect\n**(1) In general**\nAny prohibited approval of an abortion drug is hereby nullified.\n**(2) Prohibited approval defined**\nIn this subsection, the term prohibited approval of an abortion drug \u2014\n**(A)**\nmeans any approval of an abortion drug under section 505 of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 355 ) that relied in whole or in part on the treatment of pregnancy as illness; and\n**(B)**\nincludes the approval of mifepristone in effect under such section 505 on the day before the date of enactment of this Act.",
      "versionDate": "2025-01-28",
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
            "name": "Abortion",
            "updateDate": "2025-03-27T15:47:11Z"
          },
          {
            "name": "Drug safety, medical device, and laboratory regulation",
            "updateDate": "2025-03-27T15:47:11Z"
          },
          {
            "name": "Prescription drugs",
            "updateDate": "2025-03-27T15:47:11Z"
          },
          {
            "name": "Sex and reproductive health",
            "updateDate": "2025-03-27T15:47:11Z"
          },
          {
            "name": "Women's health",
            "updateDate": "2025-03-27T15:47:11Z"
          }
        ]
      },
      "policyArea": {
        "name": "Health",
        "updateDate": "2025-03-01T17:17:18Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-28",
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
          "measure-id": "id119hr795",
          "measure-number": "795",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-28",
          "originChamber": "HOUSE",
          "update-date": "2025-04-24"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr795v00",
            "update-date": "2025-04-24"
          },
          "action-date": "2025-01-28",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Pregnancy Is Not an Illness Act of 2025</strong></p><p>This bill prohibits the Food and Drug Administration (FDA) from treating pregnancy as an illness for the purposes of approving any abortion drug or imposing a risk evaluation and mitigation strategy for an abortion drug. The bill also nullifies FDA approval of any abortion drug that relied at all on the treatment of pregnancy as an illness, and specifically nullifies the FDA\u2019s approval of the abortion drug\u00a0mifepristone in effect before the bill is enacted.</p>"
        },
        "title": "Pregnancy Is Not an Illness Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr795.xml",
    "summary": {
      "actionDate": "2025-01-28",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Pregnancy Is Not an Illness Act of 2025</strong></p><p>This bill prohibits the Food and Drug Administration (FDA) from treating pregnancy as an illness for the purposes of approving any abortion drug or imposing a risk evaluation and mitigation strategy for an abortion drug. The bill also nullifies FDA approval of any abortion drug that relied at all on the treatment of pregnancy as an illness, and specifically nullifies the FDA\u2019s approval of the abortion drug\u00a0mifepristone in effect before the bill is enacted.</p>",
      "updateDate": "2025-04-24",
      "versionCode": "id119hr795"
    },
    "title": "Pregnancy Is Not an Illness Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-01-28",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Pregnancy Is Not an Illness Act of 2025</strong></p><p>This bill prohibits the Food and Drug Administration (FDA) from treating pregnancy as an illness for the purposes of approving any abortion drug or imposing a risk evaluation and mitigation strategy for an abortion drug. The bill also nullifies FDA approval of any abortion drug that relied at all on the treatment of pregnancy as an illness, and specifically nullifies the FDA\u2019s approval of the abortion drug\u00a0mifepristone in effect before the bill is enacted.</p>",
      "updateDate": "2025-04-24",
      "versionCode": "id119hr795"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-28",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr795ih.xml"
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
      "title": "Pregnancy Is Not an Illness Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-26T05:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Pregnancy Is Not an Illness Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-26T05:23:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To prohibit the Department of Health and Human Services from treating pregnancy as an illness for purposes of approving abortion drugs.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-26T05:18:21Z"
    }
  ]
}
```
