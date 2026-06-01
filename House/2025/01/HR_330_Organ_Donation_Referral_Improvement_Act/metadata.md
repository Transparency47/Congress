# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/330?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/330
- Title: Organ Donation Referral Improvement Act
- Congress: 119
- Bill type: HR
- Bill number: 330
- Origin chamber: House
- Introduced date: 2025-01-09
- Update date: 2025-10-04T08:05:28Z
- Update date including text: 2025-10-04T08:05:28Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-09: Introduced in House
- 2025-01-09 - IntroReferral: Introduced in House
- 2025-01-09 - IntroReferral: Introduced in House
- 2025-01-09 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-01-09: Introduced in House

## Actions

- 2025-01-09 - IntroReferral: Introduced in House
- 2025-01-09 - IntroReferral: Introduced in House
- 2025-01-09 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-09",
    "latestAction": {
      "actionDate": "2025-01-09",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/330",
    "number": "330",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "W000804",
        "district": "1",
        "firstName": "Robert",
        "fullName": "Rep. Wittman, Robert J. [R-VA-1]",
        "lastName": "Wittman",
        "party": "R",
        "state": "VA"
      }
    ],
    "title": "Organ Donation Referral Improvement Act",
    "type": "HR",
    "updateDate": "2025-10-04T08:05:28Z",
    "updateDateIncludingText": "2025-10-04T08:05:28Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-09",
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
      "actionDate": "2025-01-09",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-09",
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
          "date": "2025-01-09T14:30:05Z",
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
      "bioguideId": "M001227",
      "district": "4",
      "firstName": "Jennifer",
      "fullName": "Rep. McClellan, Jennifer L. [D-VA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "McClellan",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-01-09",
      "state": "VA"
    },
    {
      "bioguideId": "M001215",
      "district": "1",
      "firstName": "Mariannette",
      "fullName": "Rep. Miller-Meeks, Mariannette [R-IA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Miller-Meeks",
      "party": "R",
      "sponsorshipDate": "2025-01-09",
      "state": "IA"
    },
    {
      "bioguideId": "C001059",
      "district": "21",
      "firstName": "Jim",
      "fullName": "Rep. Costa, Jim [D-CA-21]",
      "isOriginalCosponsor": "True",
      "lastName": "Costa",
      "party": "D",
      "sponsorshipDate": "2025-01-09",
      "state": "CA"
    },
    {
      "bioguideId": "C001120",
      "district": "2",
      "firstName": "Dan",
      "fullName": "Rep. Crenshaw, Dan [R-TX-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Crenshaw",
      "party": "R",
      "sponsorshipDate": "2025-01-14",
      "state": "TX"
    },
    {
      "bioguideId": "B001306",
      "district": "12",
      "firstName": "Troy",
      "fullName": "Rep. Balderson, Troy [R-OH-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Balderson",
      "party": "R",
      "sponsorshipDate": "2025-02-04",
      "state": "OH"
    },
    {
      "bioguideId": "M001225",
      "district": "15",
      "firstName": "Kevin",
      "fullName": "Rep. Mullin, Kevin [D-CA-15]",
      "isOriginalCosponsor": "False",
      "lastName": "Mullin",
      "party": "D",
      "sponsorshipDate": "2025-02-10",
      "state": "CA"
    },
    {
      "bioguideId": "G000568",
      "district": "9",
      "firstName": "H.",
      "fullName": "Rep. Griffith, H. Morgan [R-VA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Griffith",
      "middleName": "Morgan",
      "party": "R",
      "sponsorshipDate": "2025-02-13",
      "state": "VA"
    },
    {
      "bioguideId": "P000048",
      "district": "11",
      "firstName": "August",
      "fullName": "Rep. Pfluger, August [R-TX-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Pfluger",
      "party": "R",
      "sponsorshipDate": "2025-02-13",
      "state": "TX"
    },
    {
      "bioguideId": "L000566",
      "district": "5",
      "firstName": "Robert",
      "fullName": "Rep. Latta, Robert E. [R-OH-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Latta",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-02-25",
      "state": "OH"
    },
    {
      "bioguideId": "V000131",
      "district": "33",
      "firstName": "Marc",
      "fullName": "Rep. Veasey, Marc A. [D-TX-33]",
      "isOriginalCosponsor": "False",
      "lastName": "Veasey",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-04-17",
      "state": "TX"
    },
    {
      "bioguideId": "T000487",
      "district": "2",
      "firstName": "Jill",
      "fullName": "Rep. Tokuda, Jill N. [D-HI-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Tokuda",
      "middleName": "N.",
      "party": "D",
      "sponsorshipDate": "2025-04-28",
      "state": "HI"
    },
    {
      "bioguideId": "N000002",
      "district": "12",
      "firstName": "Jerrold",
      "fullName": "Rep. Nadler, Jerrold [D-NY-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Nadler",
      "party": "D",
      "sponsorshipDate": "2025-05-15",
      "state": "NY"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2025-06-02",
      "state": "DC"
    },
    {
      "bioguideId": "V000138",
      "district": "7",
      "firstName": "Eugene",
      "fullName": "Rep. Vindman, Eugene Simon [D-VA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Vindman",
      "middleName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-10-03",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr330ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 330\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 9, 2025 Mr. Wittman (for himself, Ms. McClellan , Mrs. Miller-Meeks , and Mr. Costa ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo direct the Secretary of Health and Human Services, acting through the Assistant Secretary for Planning and Evaluation, to conduct a study on existing efforts of hospitals with respect to electronic automated referrals for purposes of organ donation, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Organ Donation Referral Improvement Act .\n#### 2. Studying electronic automated referral for organ donations\n##### (a) In general\nNot later than 1 year after the date of enactment of this Act, the Secretary of Health and Human Services, acting through the Assistant Secretary for Planning and Evaluation (referred to in this Act as the Secretary ), shall conduct and complete a study on existing efforts of hospitals with respect to electronic automated referrals for purposes of organ donation.\n##### (b) Study components\nThe study conducted under subsection (a) shall\u2014\n**(1)**\nidentify savings in staff time, variation in timeliness to determine eligibility for organ donation, as well as potential improvement over human interaction for the identification of potential organ donors, if any, attained through the use of electronic automated referrals;\n**(2)**\nidentify benefits, if any, in identifying potential organ donors through the use of electronic medical records and standardized clinical criteria;\n**(3)**\nreview the impact of such electronic automated referrals, without the need for manual reporting, on donation volumes;\n**(4)**\nassess published peer-reviewed clinical literature on such electronic automated referrals;\n**(5)**\nreview best practices for using such electronic automated referrals;\n**(6)**\nreview information technology practices to ensure the secure transmission of information for purposes of such referrals;\n**(7)**\ndevelop recommendations to promote the use of such electronic automated referrals; and\n**(8)**\nidentify what actions are needed to establish the use of such electronic automated referrals nationwide.\n##### (c) Report\nNot later than 1 year after the date of enactment of this Act, the Secretary shall submit to the Committee on Energy and Commerce and the Committee on Ways and Means of the House of Representatives and the Committee on Finance and the Committee on Health, Education, Labor, and Pensions of the Senate a report on the results of the study conducted under subsection (a).\n##### (d) Electronic automated referral defined\nIn this section, the term electronic automated referral means an electronic system that identifies potential deceased organ donors via clinical criteria in a patient\u2019s electronic health record and automatically refers such patients to the hospital\u2019s collaborating organ procurement organization.",
      "versionDate": "2025-01-09",
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
            "name": "Computers and information technology",
            "updateDate": "2025-02-12T19:38:48Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2025-02-12T19:38:59Z"
          },
          {
            "name": "Government studies and investigations",
            "updateDate": "2025-02-12T19:38:39Z"
          },
          {
            "name": "Hospital care",
            "updateDate": "2025-02-12T19:38:44Z"
          },
          {
            "name": "Organ and tissue donation and transplantation",
            "updateDate": "2025-02-12T19:38:54Z"
          }
        ]
      },
      "policyArea": {
        "name": "Health",
        "updateDate": "2025-02-11T18:48:05Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-09",
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
          "measure-id": "id119hr330",
          "measure-number": "330",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-09",
          "originChamber": "HOUSE",
          "update-date": "2025-03-13"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr330v00",
            "update-date": "2025-03-13"
          },
          "action-date": "2025-01-09",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Organ Donation Referral Improvement Act</strong></p><p>This bill requires the\u00a0Office of the Assistant Secretary for Planning and Evaluation (ASPE) in the\u00a0Department of Health and Human Services to conduct a study on hospitals\u2019 use of electronic automated referrals for organ donations. The bill defines <em>electronic automated referral</em> as an electronic system that uses electronic health records to identify patients who are potential organ donors and automatically refers those patients to organ procurement organizations.\u00a0</p><p>The ASPE must include specified components in the study, including identifying benefits, reviewing best practices, and developing recommendations for the use of electronic automated referrals for organ donations. </p>"
        },
        "title": "Organ Donation Referral Improvement Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr330.xml",
    "summary": {
      "actionDate": "2025-01-09",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Organ Donation Referral Improvement Act</strong></p><p>This bill requires the\u00a0Office of the Assistant Secretary for Planning and Evaluation (ASPE) in the\u00a0Department of Health and Human Services to conduct a study on hospitals\u2019 use of electronic automated referrals for organ donations. The bill defines <em>electronic automated referral</em> as an electronic system that uses electronic health records to identify patients who are potential organ donors and automatically refers those patients to organ procurement organizations.\u00a0</p><p>The ASPE must include specified components in the study, including identifying benefits, reviewing best practices, and developing recommendations for the use of electronic automated referrals for organ donations. </p>",
      "updateDate": "2025-03-13",
      "versionCode": "id119hr330"
    },
    "title": "Organ Donation Referral Improvement Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-09",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Organ Donation Referral Improvement Act</strong></p><p>This bill requires the\u00a0Office of the Assistant Secretary for Planning and Evaluation (ASPE) in the\u00a0Department of Health and Human Services to conduct a study on hospitals\u2019 use of electronic automated referrals for organ donations. The bill defines <em>electronic automated referral</em> as an electronic system that uses electronic health records to identify patients who are potential organ donors and automatically refers those patients to organ procurement organizations.\u00a0</p><p>The ASPE must include specified components in the study, including identifying benefits, reviewing best practices, and developing recommendations for the use of electronic automated referrals for organ donations. </p>",
      "updateDate": "2025-03-13",
      "versionCode": "id119hr330"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr330ih.xml"
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
      "title": "Organ Donation Referral Improvement Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-11T05:08:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Organ Donation Referral Improvement Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-11T05:08:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Secretary of Health and Human Services, acting through the Assistant Secretary for Planning and Evaluation, to conduct a study on existing efforts of hospitals with respect to electronic automated referrals for purposes of organ donation, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-11T05:03:21Z"
    }
  ]
}
```
