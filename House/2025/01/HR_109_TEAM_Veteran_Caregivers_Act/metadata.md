# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/109?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/109
- Title: TEAM Veteran Caregivers Act
- Congress: 119
- Bill type: HR
- Bill number: 109
- Origin chamber: House
- Introduced date: 2025-01-03
- Update date: 2025-12-20T09:06:47Z
- Update date including text: 2025-12-20T09:06:47Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-03: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-12-19 - Committee: Referred to the Subcommittee on Health.
- Latest action: 2025-01-03: Introduced in House

## Actions

- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-12-19 - Committee: Referred to the Subcommittee on Health.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-03",
    "latestAction": {
      "actionDate": "2025-01-03",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/109",
    "number": "109",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "B001302",
        "district": "5",
        "firstName": "Andy",
        "fullName": "Rep. Biggs, Andy [R-AZ-5]",
        "lastName": "Biggs",
        "party": "R",
        "state": "AZ"
      }
    ],
    "title": "TEAM Veteran Caregivers Act",
    "type": "HR",
    "updateDate": "2025-12-20T09:06:47Z",
    "updateDateIncludingText": "2025-12-20T09:06:47Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-19",
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
      "actionDate": "2025-01-03",
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
      "actionDate": "2025-01-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-01-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-03",
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
          "date": "2025-01-03T16:28:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-12-19T18:59:55Z",
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr109ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 109\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 3, 2025 Mr. Biggs of Arizona introduced the following bill; which was referred to the Committee on Veterans' Affairs\nA BILL\nTo require the Secretary of Veterans Affairs to formally recognize caregivers of veterans, notify veterans and caregivers of clinical determinations relating to eligibility for caregiver programs, and temporarily extend benefits for veterans who are determined ineligible for the family caregiver program, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Transparency and Effective Accountability Measures for Veteran Caregivers Act or the TEAM Veteran Caregivers Act .\n#### 2. Modification of administration of caregiver program of Department of Veterans Affairs\n##### (a) Official designation of caregivers\n**(1) In general**\nThe Secretary of Veterans Affairs shall formally recognize all caregivers of veterans by identifying any caregiver of a veteran in the health record of the veteran.\n**(2) Inclusion**\nCaregivers recognized under paragraph (1) shall include\u2014\n**(A)**\nfamily caregivers participating in the program of comprehensive assistance for family caregivers under subsection (a) of section 1720G of title 38, United States Code; and\n**(B)**\ncaregivers participating in the program of support services for caregivers under subsection (b) of such section.\n##### (b) Notification letters regarding clinical determinations\n**(1) In general**\nThe Secretary, using a standardized letter, shall notify veterans and caregivers of veterans regarding any clinical determinations made relating to claims, tier reduction, or termination of assistance under, or eligibility for, a caregiver program under subsection (a) or (b) of section 1720G of title 38, United States Code.\n**(2) Elements**\nNotifications under paragraph (1) shall include the elements required for notices of decisions under section 5104(b) of title 38, United States Code, to the extent that those elements apply to determinations under paragraph (1).\n##### (c) Temporary extension of benefits for family caregiver program\n**(1) In general**\nUpon determining that a veteran who was receiving services under the program of comprehensive assistance for family caregivers under subsection (a) of section 1720G of title 38, United States Code, is no longer clinically eligible for purposes of such program, the Secretary shall extend benefits under such program, including stipends under paragraph (3)(A)(ii)(V) of such subsection, for not less than 90 days after the date of notification under subsection (b) that the veteran is no longer clinically eligible.\n**(2) Exclusion**\nParagraph (1) shall not apply to the termination of caregiver benefits\u2014\n**(A)**\nif the Secretary determines that the family caregiver committed fraud or abused or neglected the veteran;\n**(B)**\nif the family caregiver was designated under section 1720G(a)(7) of title 38, United States Code, as the primary provider of personal care services for the veteran and another primary provider is designated within 90 days after the date of termination, in which case benefits for the terminated primary provider will terminate the day before the date on which the new primary provider is designated;\n**(C)**\nif another individual is designated to be a family caregiver within 90 days after the date of termination, such that there are three family caregivers assigned to the veteran, in which case benefits for the terminated family caregiver will terminate the day before the date on which the new family caregiver is designated;\n**(D)**\nthe terminated individual had been living with the veteran and moves out, or the terminated individual abandons or terminates his or her relationship with the veteran; or\n**(E)**\nupon request of the family caregiver or the veteran.",
      "versionDate": "2025-01-03",
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
            "name": "Family services",
            "updateDate": "2025-02-05T21:06:15Z"
          },
          {
            "name": "Health care coverage and access",
            "updateDate": "2025-02-05T21:06:15Z"
          },
          {
            "name": "Health information and medical records",
            "updateDate": "2025-02-05T21:06:15Z"
          },
          {
            "name": "Military personnel and dependents",
            "updateDate": "2025-02-05T21:06:15Z"
          },
          {
            "name": "Veterans' medical care",
            "updateDate": "2025-02-05T21:06:15Z"
          }
        ]
      },
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2025-01-31T16:51:57Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-03",
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
          "measure-id": "id119hr109",
          "measure-number": "109",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-03",
          "originChamber": "HOUSE",
          "update-date": "2025-02-03"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr109v00",
            "update-date": "2025-02-03"
          },
          "action-date": "2025-01-03",
          "action-desc": "Introduced in House",
          "summary-text": "<p><b>Transparency and Effective Accountability Measures for Veteran Caregivers Act or the TEAM Veteran Caregivers Act</b></p> <p>The bill revises the administration of Department of Veterans Affairs (VA) caregiver programs. Specifically, the bill requires the VA to formally recognize caregivers of veterans by identifying any caregiver in the health record of the veteran. Such caregivers covered by the bill include those participating in the Program of Comprehensive Assistance for Family Caregivers and those participating in the Program of General Caregiver Support Services.</p> <p>The bill requires the VA to notify veterans and their caregivers regarding any clinical determinations made relating to claims, tier reduction, or termination of assistance under, or eligibility for, the specified caregiver programs. The notifications must be standardized and contain specified details regarding the decisions.</p> <p>The bill also requires the VA to temporarily extend benefits under the Program of Comprehensive Assistance for Family Caregivers for at least 90 days after the receipt of notice that a veteran is no longer clinically eligible for the program. Such an extension shall not apply to the termination of caregiver benefits (1) if the VA determines the caregiver committed fraud or abused or neglected the veteran, (2) if another primary provider or individual caregiver is designated within 90 days after the termination, (3) if the terminated individual moves out or abandons their relationship with the veteran, or (4) upon request of the caregiver or veteran. </p>"
        },
        "title": "TEAM Veteran Caregivers Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr109.xml",
    "summary": {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in House",
      "text": "<p><b>Transparency and Effective Accountability Measures for Veteran Caregivers Act or the TEAM Veteran Caregivers Act</b></p> <p>The bill revises the administration of Department of Veterans Affairs (VA) caregiver programs. Specifically, the bill requires the VA to formally recognize caregivers of veterans by identifying any caregiver in the health record of the veteran. Such caregivers covered by the bill include those participating in the Program of Comprehensive Assistance for Family Caregivers and those participating in the Program of General Caregiver Support Services.</p> <p>The bill requires the VA to notify veterans and their caregivers regarding any clinical determinations made relating to claims, tier reduction, or termination of assistance under, or eligibility for, the specified caregiver programs. The notifications must be standardized and contain specified details regarding the decisions.</p> <p>The bill also requires the VA to temporarily extend benefits under the Program of Comprehensive Assistance for Family Caregivers for at least 90 days after the receipt of notice that a veteran is no longer clinically eligible for the program. Such an extension shall not apply to the termination of caregiver benefits (1) if the VA determines the caregiver committed fraud or abused or neglected the veteran, (2) if another primary provider or individual caregiver is designated within 90 days after the termination, (3) if the terminated individual moves out or abandons their relationship with the veteran, or (4) upon request of the caregiver or veteran. </p>",
      "updateDate": "2025-02-03",
      "versionCode": "id119hr109"
    },
    "title": "TEAM Veteran Caregivers Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in House",
      "text": "<p><b>Transparency and Effective Accountability Measures for Veteran Caregivers Act or the TEAM Veteran Caregivers Act</b></p> <p>The bill revises the administration of Department of Veterans Affairs (VA) caregiver programs. Specifically, the bill requires the VA to formally recognize caregivers of veterans by identifying any caregiver in the health record of the veteran. Such caregivers covered by the bill include those participating in the Program of Comprehensive Assistance for Family Caregivers and those participating in the Program of General Caregiver Support Services.</p> <p>The bill requires the VA to notify veterans and their caregivers regarding any clinical determinations made relating to claims, tier reduction, or termination of assistance under, or eligibility for, the specified caregiver programs. The notifications must be standardized and contain specified details regarding the decisions.</p> <p>The bill also requires the VA to temporarily extend benefits under the Program of Comprehensive Assistance for Family Caregivers for at least 90 days after the receipt of notice that a veteran is no longer clinically eligible for the program. Such an extension shall not apply to the termination of caregiver benefits (1) if the VA determines the caregiver committed fraud or abused or neglected the veteran, (2) if another primary provider or individual caregiver is designated within 90 days after the termination, (3) if the terminated individual moves out or abandons their relationship with the veteran, or (4) upon request of the caregiver or veteran. </p>",
      "updateDate": "2025-02-03",
      "versionCode": "id119hr109"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr109ih.xml"
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
      "title": "TEAM Veteran Caregivers Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-01-30T05:08:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "TEAM Veteran Caregivers Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-01-30T05:08:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Transparency and Effective Accountability Measures for Veteran Caregivers Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-01-30T05:08:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the Secretary of Veterans Affairs to formally recognize caregivers of veterans, notify veterans and caregivers of clinical determinations relating to eligibility for caregiver programs, and temporarily extend benefits for veterans who are determined ineligible for the family caregiver program, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-01-30T05:03:24Z"
    }
  ]
}
```
