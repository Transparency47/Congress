# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/748?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/748
- Title: RELIEVE Act
- Congress: 119
- Bill type: HR
- Bill number: 748
- Origin chamber: House
- Introduced date: 2025-01-28
- Update date: 2026-03-25T08:06:09Z
- Update date including text: 2026-03-25T08:06:09Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-28: Introduced in House
- 2025-01-28 - IntroReferral: Introduced in House
- 2025-01-28 - IntroReferral: Introduced in House
- 2025-01-28 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-12-19 - Committee: Referred to the Subcommittee on Health.
- Latest action: 2025-01-28: Introduced in House

## Actions

- 2025-01-28 - IntroReferral: Introduced in House
- 2025-01-28 - IntroReferral: Introduced in House
- 2025-01-28 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-12-19 - Committee: Referred to the Subcommittee on Health.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/748",
    "number": "748",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "B001301",
        "district": "1",
        "firstName": "Jack",
        "fullName": "Rep. Bergman, Jack [R-MI-1]",
        "lastName": "Bergman",
        "party": "R",
        "state": "MI"
      }
    ],
    "title": "RELIEVE Act",
    "type": "HR",
    "updateDate": "2026-03-25T08:06:09Z",
    "updateDateIncludingText": "2026-03-25T08:06:09Z"
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
      "actionDate": "2025-01-28",
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
          "date": "2025-01-28T16:01:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-12-19T19:06:04Z",
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
      "bioguideId": "P000614",
      "district": "1",
      "firstName": "Chris",
      "fullName": "Rep. Pappas, Chris [D-NH-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Pappas",
      "party": "D",
      "sponsorshipDate": "2025-01-28",
      "state": "NH"
    },
    {
      "bioguideId": "V000133",
      "district": "2",
      "firstName": "Jefferson",
      "fullName": "Rep. Van Drew, Jefferson [R-NJ-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Drew",
      "party": "R",
      "sponsorshipDate": "2025-02-13",
      "state": "NJ"
    },
    {
      "bioguideId": "L000590",
      "district": "3",
      "firstName": "Susie",
      "fullName": "Rep. Lee, Susie [D-NV-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Lee",
      "party": "D",
      "sponsorshipDate": "2025-04-24",
      "state": "NV"
    },
    {
      "bioguideId": "M001237",
      "district": "8",
      "firstName": "Kristen",
      "fullName": "Rep. McDonald Rivet, Kristen [D-MI-8]",
      "isOriginalCosponsor": "False",
      "lastName": "McDonald Rivet",
      "party": "D",
      "sponsorshipDate": "2025-12-18",
      "state": "MI"
    },
    {
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2026-03-24",
      "state": "NJ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr748ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 748\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 28, 2025 Mr. Bergman (for himself and Mr. Pappas ) introduced the following bill; which was referred to the Committee on Veterans' Affairs\nA BILL\nTo amend title 38, United States Code, to make certain improvements relating to the eligibility of veterans to receive reimbursement for emergency treatment furnished through the Veterans Community Care program, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Removing Extraneous Loopholes Insuring Every Veteran Emergency Act or the RELIEVE Act .\n#### 2. Eligibility requirements for reimbursement for emergency treatment furnished to veterans\n##### (a) Eligibility requirements\nSection 1725(b)(2)(B) of title 38, United States Code, is amended by inserting , unless such emergency treatment was furnished during the 60-day period following the date on which the veteran enrolled in the health care system specified in subparagraph (A), in which case no requirement for prior receipt of care shall apply before the period.\n##### (b) Applicability\nThe amendment made by subsection (a) shall apply with respect to emergency treatment furnished on or after the date that is one year after the date of the enactment of this Act.",
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
            "name": "Emergency medical services and trauma care",
            "updateDate": "2025-03-27T15:21:27Z"
          },
          {
            "name": "Health care costs and insurance",
            "updateDate": "2025-03-27T15:21:22Z"
          },
          {
            "name": "Veterans' medical care",
            "updateDate": "2025-03-27T15:21:17Z"
          }
        ]
      },
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2025-02-25T14:58:38Z"
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
          "measure-id": "id119hr748",
          "measure-number": "748",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-28",
          "originChamber": "HOUSE",
          "update-date": "2025-03-06"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr748v00",
            "update-date": "2025-03-06"
          },
          "action-date": "2025-01-28",
          "action-desc": "Introduced in House",
          "summary-text": "<p><b>Removing Extraneous Loopholes Insuring Every Veteran Emergency Act or the RELIEVE Act</b></p> <p>This bill expands eligibility for Department of Veterans Affairs (VA) reimbursement of emergency treatment for veterans who are treated in a non-VA facility. Specifically, the bill waives the requirement that a veteran must have received VA care within the 24-month period preceding the furnishing of emergency treatment if the veteran receives such emergency treatment within the 60-day period following their enrollment in the VA health care system.</p>"
        },
        "title": "RELIEVE Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr748.xml",
    "summary": {
      "actionDate": "2025-01-28",
      "actionDesc": "Introduced in House",
      "text": "<p><b>Removing Extraneous Loopholes Insuring Every Veteran Emergency Act or the RELIEVE Act</b></p> <p>This bill expands eligibility for Department of Veterans Affairs (VA) reimbursement of emergency treatment for veterans who are treated in a non-VA facility. Specifically, the bill waives the requirement that a veteran must have received VA care within the 24-month period preceding the furnishing of emergency treatment if the veteran receives such emergency treatment within the 60-day period following their enrollment in the VA health care system.</p>",
      "updateDate": "2025-03-06",
      "versionCode": "id119hr748"
    },
    "title": "RELIEVE Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-28",
      "actionDesc": "Introduced in House",
      "text": "<p><b>Removing Extraneous Loopholes Insuring Every Veteran Emergency Act or the RELIEVE Act</b></p> <p>This bill expands eligibility for Department of Veterans Affairs (VA) reimbursement of emergency treatment for veterans who are treated in a non-VA facility. Specifically, the bill waives the requirement that a veteran must have received VA care within the 24-month period preceding the furnishing of emergency treatment if the veteran receives such emergency treatment within the 60-day period following their enrollment in the VA health care system.</p>",
      "updateDate": "2025-03-06",
      "versionCode": "id119hr748"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr748ih.xml"
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
      "title": "RELIEVE Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-22T08:08:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "RELIEVE Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-22T08:08:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Removing Extraneous Loopholes Insuring Every Veteran Emergency Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-22T08:08:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 38, United States Code, to make certain improvements relating to the eligibility of veterans to receive reimbursement for emergency treatment furnished through the Veterans Community Care program, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-22T08:03:51Z"
    }
  ]
}
```
