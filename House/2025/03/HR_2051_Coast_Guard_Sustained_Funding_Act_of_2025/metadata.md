# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2051?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2051
- Title: Coast Guard Sustained Funding Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 2051
- Origin chamber: House
- Introduced date: 2025-03-11
- Update date: 2025-10-02T13:46:56Z
- Update date including text: 2025-10-02T13:46:56Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-03-11: Introduced in House
- 2025-03-11 - IntroReferral: Introduced in House
- 2025-03-11 - IntroReferral: Introduced in House
- 2025-03-11 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-03-11 - Committee: Referred to the Subcommittee on Coast Guard and Maritime Transportation.
- Latest action: 2025-03-11: Introduced in House

## Actions

- 2025-03-11 - IntroReferral: Introduced in House
- 2025-03-11 - IntroReferral: Introduced in House
- 2025-03-11 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-03-11 - Committee: Referred to the Subcommittee on Coast Guard and Maritime Transportation.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-11",
    "latestAction": {
      "actionDate": "2025-03-11",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2051",
    "number": "2051",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "G000590",
        "district": "7",
        "firstName": "Mark",
        "fullName": "Rep. Green, Mark E. [R-TN-7]",
        "lastName": "Green",
        "party": "R",
        "state": "TN"
      }
    ],
    "title": "Coast Guard Sustained Funding Act of 2025",
    "type": "HR",
    "updateDate": "2025-10-02T13:46:56Z",
    "updateDateIncludingText": "2025-10-02T13:46:56Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-11",
      "committees": {
        "item": {
          "name": "Coast Guard and Maritime Transportation Subcommittee",
          "systemCode": "hspw07"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Coast Guard and Maritime Transportation.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-11",
      "committees": {
        "item": {
          "name": "Transportation and Infrastructure Committee",
          "systemCode": "hspw00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Transportation and Infrastructure.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-03-11",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-11",
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
          "date": "2025-03-11T14:05:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-03-11T22:07:18Z",
              "name": "Referred to"
            }
          },
          "name": "Coast Guard and Maritime Transportation Subcommittee",
          "systemCode": "hspw07"
        }
      },
      "systemCode": "hspw00",
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
      "bioguideId": "G000593",
      "district": "28",
      "firstName": "Carlos",
      "fullName": "Rep. Gimenez, Carlos A. [R-FL-28]",
      "isOriginalCosponsor": "True",
      "lastName": "Gimenez",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-03-11",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2051ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2051\nIN THE HOUSE OF REPRESENTATIVES\nMarch 11, 2025 Mr. Green of Tennessee (for himself and Mr. Gimenez ) introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo amend title 14, United States Code, to make appropriations for Coast Guard pay in the event an appropriations Act expires before the enactment of a new appropriations Act, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Coast Guard Sustained Funding Act of 2025 .\n#### 2. Pay; continuation during lapse in appropriations\n##### (a) In general\nChapter 27 of title 14, United States Code, is amended by adding at the end the following:\n2780. Pay; continuation during lapse in appropriations (a) In general In the case of any period in which there is a Coast Guard-specific funding lapse, there are appropriated such sums as may be necessary\u2014 (1) to provide pay and allowances to military members of the Coast Guard, including the reserve component thereof, who perform active service or inactive-duty training during such period; (2) to provide pay and benefits to qualified civilian employees of the Coast Guard; and (3) to provide pay and benefits to qualified contract employees of the Coast Guard. (b) Application of Anti-Deficiency Act Section 1341 of title 31 (commonly referred to as the Anti-Deficiency Act ) shall apply to operations carried out under this section, except\u2014 (1) in the case of law that expressly authorizes incurring obligations in advance of appropriations; (2) operations that involve emergencies involving the safety of human life or the protection of property; and (3) with respect to functions necessary to discharge the congressional duties of the President. (c) Coast Guard-Specific funding lapse For purposes of this section, a Coast Guard-specific funding lapse occurs in any case in which a general appropriation bill providing appropriations for the Coast Guard for a fiscal year is not enacted before the beginning of such fiscal year (and no joint resolution making continuing appropriations for the Coast Guard is in effect). (d) Termination Appropriations and funds made available and authority granted for any fiscal year for any purpose under subsection (a) shall be available until whichever of the following first occurs: (1) The enactment into law of an appropriation (including a continuing appropriation) for such purpose. (2) The enactment into law of the applicable regular or continuing appropriations resolution or other Act without any appropriation for such purpose. (e) Definitions In this section: (1) Qualified civilian employee The term qualified civilian employee means a civilian employee of the Coast Guard who the Commandant determines is\u2014 (A) providing support to members of the Coast Guard or another Armed Force; or (B) performing work as an excepted employee or an employee performing emergency work, as such terms are defined by the Office of Personnel Management. (2) Qualified contract employee of the coast guard The term qualified contract employee of the Coast Guard means an individual performing work under a contract who the Commandant determines is\u2014 (A) providing support to military members or qualified civilian employees of the Coast Guard or another Armed Force; or (B) required to perform work during a lapse in appropriations. .\n##### (b) Clerical amendment\nThe analysis for chapter 27 of title 14, United States Code, is amended by adding at the end the following:\n2780. Pay; continuation during lapse in appropriations. .",
      "versionDate": "2025-03-11",
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
        "name": "Transportation and Public Works",
        "updateDate": "2025-05-06T15:38:39Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-11",
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
          "measure-id": "id119hr2051",
          "measure-number": "2051",
          "measure-type": "hr",
          "orig-publish-date": "2025-03-11",
          "originChamber": "HOUSE",
          "update-date": "2025-10-02"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr2051v00",
            "update-date": "2025-10-02"
          },
          "action-date": "2025-03-11",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Coast Guard Sustained Funding Act of 2025 </strong></p><p>This bill provides continuing appropriations to the Coast Guard for pay and benefits when there is a Coast Guard-specific funding lapse.</p><p>Under the bill, a\u00a0<em>Coast Guard-specific funding lapse</em> occurs when a bill providing appropriations for the Coast Guard for a fiscal year has not been enacted before the beginning of that fiscal year, and no joint resolution providing continuing appropriations for the Coast Guard is in effect.</p><p>If a Coast Guard-specific funding lapse occurs, the bill provides appropriations to the Coast Guard for (1) pay and allowances for military members of the Coast Guard, including reserve components, who perform active service or inactive-duty training; and (2) pay and benefits for certain civilian and contract employees who are providing support to members of the Coast Guard or another Armed Force and are working during the funding lapse.\u00a0</p>"
        },
        "title": "Coast Guard Sustained Funding Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr2051.xml",
    "summary": {
      "actionDate": "2025-03-11",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Coast Guard Sustained Funding Act of 2025 </strong></p><p>This bill provides continuing appropriations to the Coast Guard for pay and benefits when there is a Coast Guard-specific funding lapse.</p><p>Under the bill, a\u00a0<em>Coast Guard-specific funding lapse</em> occurs when a bill providing appropriations for the Coast Guard for a fiscal year has not been enacted before the beginning of that fiscal year, and no joint resolution providing continuing appropriations for the Coast Guard is in effect.</p><p>If a Coast Guard-specific funding lapse occurs, the bill provides appropriations to the Coast Guard for (1) pay and allowances for military members of the Coast Guard, including reserve components, who perform active service or inactive-duty training; and (2) pay and benefits for certain civilian and contract employees who are providing support to members of the Coast Guard or another Armed Force and are working during the funding lapse.\u00a0</p>",
      "updateDate": "2025-10-02",
      "versionCode": "id119hr2051"
    },
    "title": "Coast Guard Sustained Funding Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-03-11",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Coast Guard Sustained Funding Act of 2025 </strong></p><p>This bill provides continuing appropriations to the Coast Guard for pay and benefits when there is a Coast Guard-specific funding lapse.</p><p>Under the bill, a\u00a0<em>Coast Guard-specific funding lapse</em> occurs when a bill providing appropriations for the Coast Guard for a fiscal year has not been enacted before the beginning of that fiscal year, and no joint resolution providing continuing appropriations for the Coast Guard is in effect.</p><p>If a Coast Guard-specific funding lapse occurs, the bill provides appropriations to the Coast Guard for (1) pay and allowances for military members of the Coast Guard, including reserve components, who perform active service or inactive-duty training; and (2) pay and benefits for certain civilian and contract employees who are providing support to members of the Coast Guard or another Armed Force and are working during the funding lapse.\u00a0</p>",
      "updateDate": "2025-10-02",
      "versionCode": "id119hr2051"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2051ih.xml"
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
      "title": "Coast Guard Sustained Funding Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-26T02:08:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Coast Guard Sustained Funding Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-26T02:08:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 14, United States Code, to make appropriations for Coast Guard pay in the event an appropriations Act expires before the enactment of a new appropriations Act, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-26T02:03:46Z"
    }
  ]
}
```
