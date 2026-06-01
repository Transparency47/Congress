# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/555?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/555
- Title: Veterans Affairs Transfer of Information and Sharing of Disability Examination Procedures With DOD Doctors Act
- Congress: 119
- Bill type: HR
- Bill number: 555
- Origin chamber: House
- Introduced date: 2025-01-16
- Update date: 2026-04-10T17:01:15Z
- Update date including text: 2026-04-10T17:01:15Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-16: Introduced in House
- 2025-01-16 - IntroReferral: Introduced in House
- 2025-01-16 - IntroReferral: Introduced in House
- 2025-01-16 - IntroReferral: Referred to the Committee on Armed Services, and in addition to the Committee on Veterans' Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-01-16 - IntroReferral: Referred to the Committee on Armed Services, and in addition to the Committee on Veterans' Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-02-20 - Committee: Referred to the Subcommittee on Disability Assistance and Memorial Affairs.
- Latest action: 2025-01-16: Introduced in House

## Actions

- 2025-01-16 - IntroReferral: Introduced in House
- 2025-01-16 - IntroReferral: Introduced in House
- 2025-01-16 - IntroReferral: Referred to the Committee on Armed Services, and in addition to the Committee on Veterans' Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-01-16 - IntroReferral: Referred to the Committee on Armed Services, and in addition to the Committee on Veterans' Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-02-20 - Committee: Referred to the Subcommittee on Disability Assistance and Memorial Affairs.

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
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/555",
    "number": "555",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
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
    "title": "Veterans Affairs Transfer of Information and Sharing of Disability Examination Procedures With DOD Doctors Act",
    "type": "HR",
    "updateDate": "2026-04-10T17:01:15Z",
    "updateDateIncludingText": "2026-04-10T17:01:15Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-20",
      "committees": {
        "item": {
          "name": "Disability Assistance and Memorial Affairs Subcommittee",
          "systemCode": "hsvr09"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Disability Assistance and Memorial Affairs.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-16",
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
      "text": "Referred to the Committee on Armed Services, and in addition to the Committee on Veterans' Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-16",
      "committees": {
        "item": {
          "name": "Armed Services Committee",
          "systemCode": "hsas00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Armed Services, and in addition to the Committee on Veterans' Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-01-16",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-16",
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
          "date": "2025-01-16T14:02:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-02-20T22:39:03Z",
              "name": "Referred to"
            }
          },
          "name": "Disability Assistance and Memorial Affairs Subcommittee",
          "systemCode": "hsvr09"
        }
      },
      "systemCode": "hsvr00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-01-16T14:02:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Armed Services Committee",
      "systemCode": "hsas00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr555ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 555\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 16, 2025 Mr. Wittman introduced the following bill; which was referred to the Committee on Armed Services , and in addition to the Committee on Veterans' Affairs , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend title 10, United States Code, to include a single comprehensive disability examination as part of the required Department of Defense physical examination for separating members of the Armed Forces, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Veterans Affairs Transfer of Information and Sharing of Disability Examination Procedures With DOD Doctors Act .\n#### 2. Inclusion of single comprehensive disability examination as part of required Department of Defense physical examination for separating members of the Armed Forces\nSection 1145(a)(5) of title 10, United States Code, is amended by adding at the end the following new subparagraphs:\n(E) If a member of the Armed Forces who is required to receive a physical examination under subparagraph (A) has or is believed to have a medical condition that will or may make the member eligible for disability compensation and benefits from the Department of Veterans Affairs, the physical examination shall be performed by a health care provider who is certified by the Secretary of Veterans Affairs to determine such eligibility. If such a condition is discovered during the physical examination and the health care provider performing the examination is not certified by the Secretary of Veterans Affairs, the examination shall be completed by a health care provider certified by the Secretary of Veterans Affairs. (F) An eligibility determination made as part of a physical examination under subparagraph (C) shall be binding on the Department of Veterans Affairs and be used as the basis for assigning a disability rating for the separating member. .\n#### 3. Department of Defense and Department of Veterans Affairs joint recordkeeping system\nThe Secretary of Veterans Affairs and the Secretary of Defense shall jointly establish a system to be used by both the Department of Defense and the Department of Veterans Affairs to establish and maintain the medical and personnel records of members of the Armed Forces and veterans. Such system shall provide for data sharing between the Department of Defense and the Department of Veterans Affairs.",
      "versionDate": "2025-01-16",
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
            "name": "Data collection, sharing, protection",
            "updateDate": "2026-04-10T17:01:14Z"
          },
          {
            "name": "Department of Veterans Affairs",
            "updateDate": "2025-03-13T16:01:26Z"
          },
          {
            "name": "Disability and paralysis",
            "updateDate": "2025-03-13T16:01:26Z"
          },
          {
            "name": "Disability assistance",
            "updateDate": "2025-03-13T16:01:26Z"
          },
          {
            "name": "Health information and medical records",
            "updateDate": "2025-03-13T16:01:26Z"
          },
          {
            "name": "Health personnel",
            "updateDate": "2025-03-13T16:01:26Z"
          },
          {
            "name": "Medical tests and diagnostic methods",
            "updateDate": "2025-03-13T16:01:26Z"
          },
          {
            "name": "Military personnel and dependents",
            "updateDate": "2025-03-13T16:01:26Z"
          },
          {
            "name": "Personnel records",
            "updateDate": "2025-03-13T16:01:26Z"
          },
          {
            "name": "Veterans' medical care",
            "updateDate": "2025-03-13T16:01:26Z"
          },
          {
            "name": "Veterans' pensions and compensation",
            "updateDate": "2025-03-13T16:01:26Z"
          }
        ]
      },
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2025-02-19T18:05:16Z"
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
          "measure-id": "id119hr555",
          "measure-number": "555",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-16",
          "originChamber": "HOUSE",
          "update-date": "2025-03-03"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr555v00",
            "update-date": "2025-03-03"
          },
          "action-date": "2025-01-16",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Veterans Affairs Transfer of Information and Sharing of Disability Examination Procedures With DOD Doctors Act</strong></p> <p>This bill addresses the sharing of medical information and disability examination procedures between the Departments of Defense (DOD) and Veterans Affairs (VA). It requires that if a member of the Armed Forces who is required to receive a physical examination upon separation from active duty has or is believed to have a medical condition that may make the member eligible for veterans' disability compensation and benefits, the examination must be performed by a VA-certified health care provider.</p><p>If the condition is discovered during the physical examination and the examining health care provider is not VA-certified, the examination must be completed by a VA-certified provider. </p> <p>An eligibility determination made as part of such an examination shall be binding on the VA and be used as the basis for assigning the member's disability rating.</p> <p>The VA and DOD shall jointly establish a system to share data and maintain the medical and personnel records of Armed Forces members and veterans.</p>"
        },
        "title": "Veterans Affairs Transfer of Information and Sharing of Disability Examination Procedures With DOD Doctors Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr555.xml",
    "summary": {
      "actionDate": "2025-01-16",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Veterans Affairs Transfer of Information and Sharing of Disability Examination Procedures With DOD Doctors Act</strong></p> <p>This bill addresses the sharing of medical information and disability examination procedures between the Departments of Defense (DOD) and Veterans Affairs (VA). It requires that if a member of the Armed Forces who is required to receive a physical examination upon separation from active duty has or is believed to have a medical condition that may make the member eligible for veterans' disability compensation and benefits, the examination must be performed by a VA-certified health care provider.</p><p>If the condition is discovered during the physical examination and the examining health care provider is not VA-certified, the examination must be completed by a VA-certified provider. </p> <p>An eligibility determination made as part of such an examination shall be binding on the VA and be used as the basis for assigning the member's disability rating.</p> <p>The VA and DOD shall jointly establish a system to share data and maintain the medical and personnel records of Armed Forces members and veterans.</p>",
      "updateDate": "2025-03-03",
      "versionCode": "id119hr555"
    },
    "title": "Veterans Affairs Transfer of Information and Sharing of Disability Examination Procedures With DOD Doctors Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-16",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Veterans Affairs Transfer of Information and Sharing of Disability Examination Procedures With DOD Doctors Act</strong></p> <p>This bill addresses the sharing of medical information and disability examination procedures between the Departments of Defense (DOD) and Veterans Affairs (VA). It requires that if a member of the Armed Forces who is required to receive a physical examination upon separation from active duty has or is believed to have a medical condition that may make the member eligible for veterans' disability compensation and benefits, the examination must be performed by a VA-certified health care provider.</p><p>If the condition is discovered during the physical examination and the examining health care provider is not VA-certified, the examination must be completed by a VA-certified provider. </p> <p>An eligibility determination made as part of such an examination shall be binding on the VA and be used as the basis for assigning the member's disability rating.</p> <p>The VA and DOD shall jointly establish a system to share data and maintain the medical and personnel records of Armed Forces members and veterans.</p>",
      "updateDate": "2025-03-03",
      "versionCode": "id119hr555"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr555ih.xml"
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
      "title": "Veterans Affairs Transfer of Information and Sharing of Disability Examination Procedures With DOD Doctors Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-14T11:08:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Veterans Affairs Transfer of Information and Sharing of Disability Examination Procedures With DOD Doctors Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-14T11:08:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 10, United States Code, to include a single comprehensive disability examination as part of the required Department of Defense physical examination for separating members of the Armed Forces, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-14T11:03:21Z"
    }
  ]
}
```
