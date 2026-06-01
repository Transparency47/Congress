# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1290?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/1290
- Title: Veterans Mental Health Crisis Referral Enhancement Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 1290
- Origin chamber: House
- Introduced date: 2025-02-13
- Update date: 2025-06-13T18:55:02Z
- Update date including text: 2025-06-13T18:55:02Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-13: Introduced in House
- 2025-02-13 - IntroReferral: Introduced in House
- 2025-02-13 - IntroReferral: Introduced in House
- 2025-02-13 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-03-14 - Committee: Referred to the Subcommittee on Health.
- Latest action: 2025-02-13: Introduced in House

## Actions

- 2025-02-13 - IntroReferral: Introduced in House
- 2025-02-13 - IntroReferral: Introduced in House
- 2025-02-13 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-03-14 - Committee: Referred to the Subcommittee on Health.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-13",
    "latestAction": {
      "actionDate": "2025-02-13",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/1290",
    "number": "1290",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "B001260",
        "district": "16",
        "firstName": "Vern",
        "fullName": "Rep. Buchanan, Vern [R-FL-16]",
        "lastName": "Buchanan",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "Veterans Mental Health Crisis Referral Enhancement Act of 2025",
    "type": "HR",
    "updateDate": "2025-06-13T18:55:02Z",
    "updateDateIncludingText": "2025-06-13T18:55:02Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-14",
      "committees": {
        "item": {
          "name": "Health Subcommittee",
          "systemCode": "hsvr03"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Health.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-13",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "hsvr00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Veterans' Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-02-13",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-13",
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
          "date": "2025-02-13T14:04:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-03-14T17:52:30Z",
              "name": "Referred to"
            }
          },
          "name": "Health Subcommittee",
          "systemCode": "hsvr03"
        }
      },
      "systemCode": "hsvr00",
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
      "bioguideId": "M001210",
      "district": "3",
      "firstName": "Gregory",
      "fullName": "Rep. Murphy, Gregory F. [R-NC-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Murphy",
      "middleName": "F.",
      "party": "R",
      "sponsorshipDate": "2025-02-13",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1290ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1290\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 13, 2025 Mr. Buchanan (for himself and Mr. Murphy ) introduced the following bill; which was referred to the Committee on Veterans' Affairs\nA BILL\nTo direct the Secretary of Veterans Affairs to carry out a pilot program under which the Department of Veterans Affairs refers veterans experiencing mental health crises to approved non-Department mental health care providers, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Veterans Mental Health Crisis Referral Enhancement Act of 2025 .\n#### 2. Department of Veterans Affairs pilot program on mental health referrals\n##### (a) Pilot program\nBeginning not later than 180 days after the date of the enactment of this Act, the Secretary of Veterans Affairs shall carry out a three-year pilot program under which Vet Centers and medical facilities of the Department provide veterans experiencing mental health crises with referrals to non-Department mental health care providers approved by the Secretary.\n##### (b) Locations\nThe Secretary shall select at least three geographic locations at which to carry out the pilot program required under subsection (a).\n##### (c) Requirements\nIn carrying out the pilot program under subsection (a), the Secretary shall\u2014\n**(1)**\ndevelop and maintain a referral system to connect veterans experiencing mental health crises with non-Department mental health care providers within one week;\n**(2)**\ndevelop criteria for the approval of non-Department mental health care providers for purposes of referrals under the program;\n**(3)**\nhire any additional employees required to facilitate referrals under the system; and\n**(4)**\nprovide appropriate training to employees of Vet Centers and medical facilities of the Department on the referral system.\n##### (d) Reports\n**(1) Annual reports**\nNot later than six months after the last day of each year during which the Secretary carries out the pilot program under subsection (a), the Secretary shall submit to Congress a report on the implementation and outcomes of the pilot program. Each such report shall include the following for the year covered by the report:\n**(A)**\nThe number of veterans referred to non-Department mental health care providers under the pilot program.\n**(B)**\nThe average wait time for a veteran to receive mental health care after receiving a referral under the pilot program.\n**(C)**\nAn evaluation of veteran satisfaction with the mental health care received through the referral system.\n**(2) Final report**\nNot later than 180 days after the conclusion of the pilot program, the Secretary shall submit to Congress a final report containing an evaluation of the effectiveness of the program and the recommendations of the Secretary with respect to expanding or modifying the referral system developed under the program.\n##### (e) Authorization of appropriations\nThere is authorized to be appropriated to carry out the pilot program required under subsection (a) $3,000,000 for each of fiscal years 2025 through 2027.",
      "versionDate": "2025-02-13",
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
            "name": "Congressional oversight",
            "updateDate": "2025-06-13T18:54:56Z"
          },
          {
            "name": "Health care coverage and access",
            "updateDate": "2025-06-13T18:55:02Z"
          },
          {
            "name": "Mental health",
            "updateDate": "2025-06-13T18:54:45Z"
          },
          {
            "name": "Veterans' medical care",
            "updateDate": "2025-06-13T18:54:51Z"
          }
        ]
      },
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2025-03-20T16:38:40Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-13",
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
          "measure-id": "id119hr1290",
          "measure-number": "1290",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-13",
          "originChamber": "HOUSE",
          "update-date": "2025-03-26"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1290v00",
            "update-date": "2025-03-26"
          },
          "action-date": "2025-02-13",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Veterans Mental Health Crisis Referral Enhancement Act of 2025</strong></p><p>This bill requires the Department of Veterans Affairs (VA) to implement a three-year pilot program under which Vet Centers and VA medical facilities provide veterans who are experiencing mental health crises with referrals to approved non-VA mental health care providers.</p><p>The VA must\u00a0report on the implementation, outcomes, and effectiveness of the pilot program.</p>"
        },
        "title": "Veterans Mental Health Crisis Referral Enhancement Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1290.xml",
    "summary": {
      "actionDate": "2025-02-13",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Veterans Mental Health Crisis Referral Enhancement Act of 2025</strong></p><p>This bill requires the Department of Veterans Affairs (VA) to implement a three-year pilot program under which Vet Centers and VA medical facilities provide veterans who are experiencing mental health crises with referrals to approved non-VA mental health care providers.</p><p>The VA must\u00a0report on the implementation, outcomes, and effectiveness of the pilot program.</p>",
      "updateDate": "2025-03-26",
      "versionCode": "id119hr1290"
    },
    "title": "Veterans Mental Health Crisis Referral Enhancement Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-02-13",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Veterans Mental Health Crisis Referral Enhancement Act of 2025</strong></p><p>This bill requires the Department of Veterans Affairs (VA) to implement a three-year pilot program under which Vet Centers and VA medical facilities provide veterans who are experiencing mental health crises with referrals to approved non-VA mental health care providers.</p><p>The VA must\u00a0report on the implementation, outcomes, and effectiveness of the pilot program.</p>",
      "updateDate": "2025-03-26",
      "versionCode": "id119hr1290"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-13",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1290ih.xml"
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
      "title": "Veterans Mental Health Crisis Referral Enhancement Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-13T04:23:38Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Veterans Mental Health Crisis Referral Enhancement Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-13T04:23:27Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Secretary of Veterans Affairs to carry out a pilot program under which the Department of Veterans Affairs refers veterans experiencing mental health crises to approved non-Department mental health care providers, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-13T04:20:55Z"
    }
  ]
}
```
