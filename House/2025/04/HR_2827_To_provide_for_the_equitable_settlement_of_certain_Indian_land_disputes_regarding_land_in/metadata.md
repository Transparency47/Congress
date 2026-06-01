# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2827?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2827
- Title: To provide for the equitable settlement of certain Indian land disputes regarding land in Illinois, and for other purposes.
- Congress: 119
- Bill type: HR
- Bill number: 2827
- Origin chamber: House
- Introduced date: 2025-04-10
- Update date: 2026-03-05T09:07:08Z
- Update date including text: 2026-03-05T09:07:08Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-04-10: Introduced in House
- 2025-04-10 - IntroReferral: Introduced in House
- 2025-04-10 - IntroReferral: Introduced in House
- 2025-04-10 - IntroReferral: Referred to the House Committee on Natural Resources.
- 2026-02-25 - Committee: Referred to the Subcommittee on Indian and Insular Affairs.
- 2026-03-04 - Committee: Subcommittee Hearings Held
- Latest action: 2025-04-10: Introduced in House

## Actions

- 2025-04-10 - IntroReferral: Introduced in House
- 2025-04-10 - IntroReferral: Introduced in House
- 2025-04-10 - IntroReferral: Referred to the House Committee on Natural Resources.
- 2026-02-25 - Committee: Referred to the Subcommittee on Indian and Insular Affairs.
- 2026-03-04 - Committee: Subcommittee Hearings Held

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-10",
    "latestAction": {
      "actionDate": "2025-04-10",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2827",
    "number": "2827",
    "originChamber": "House",
    "policyArea": {
      "name": "Native Americans"
    },
    "sponsors": [
      {
        "bioguideId": "C001053",
        "district": "4",
        "firstName": "Tom",
        "fullName": "Rep. Cole, Tom [R-OK-4]",
        "lastName": "Cole",
        "party": "R",
        "state": "OK"
      }
    ],
    "title": "To provide for the equitable settlement of certain Indian land disputes regarding land in Illinois, and for other purposes.",
    "type": "HR",
    "updateDate": "2026-03-05T09:07:08Z",
    "updateDateIncludingText": "2026-03-05T09:07:08Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-04",
      "committees": {
        "item": {
          "name": "Indian and Insular Affairs Subcommittee",
          "systemCode": "hsii24"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Subcommittee Hearings Held",
      "type": "Committee"
    },
    {
      "actionDate": "2026-02-25",
      "committees": {
        "item": {
          "name": "Indian and Insular Affairs Subcommittee",
          "systemCode": "hsii24"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Indian and Insular Affairs.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-10",
      "committees": {
        "item": {
          "name": "Natural Resources Committee",
          "systemCode": "hsii00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Natural Resources.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-04-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-10",
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
          "date": "2025-04-10T13:12:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Natural Resources Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": [
              {
                "date": "2026-03-04T15:15:00Z",
                "name": "Hearings By (subcommittee)"
              },
              {
                "date": "2026-02-25T15:00:00Z",
                "name": "Referred to"
              }
            ]
          },
          "name": "Indian and Insular Affairs Subcommittee",
          "systemCode": "hsii24"
        }
      },
      "systemCode": "hsii00",
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
      "bioguideId": "M001143",
      "district": "4",
      "firstName": "Betty",
      "fullName": "Rep. McCollum, Betty [D-MN-4]",
      "isOriginalCosponsor": "True",
      "lastName": "McCollum",
      "party": "D",
      "sponsorshipDate": "2025-04-10",
      "state": "MN"
    },
    {
      "bioguideId": "B001295",
      "district": "12",
      "firstName": "Mike",
      "fullName": "Rep. Bost, Mike [R-IL-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Bost",
      "party": "R",
      "sponsorshipDate": "2025-04-10",
      "state": "IL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2827ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2827\nIN THE HOUSE OF REPRESENTATIVES\nApril 10, 2025 Mr. Cole (for himself, Ms. McCollum , and Mr. Bost ) introduced the following bill; which was referred to the Committee on Natural Resources\nA BILL\nTo provide for the equitable settlement of certain Indian land disputes regarding land in Illinois, and for other purposes.\n#### 1. Settlement of claims\n##### (a) Jurisdiction conferred on the united states court of federal claims\n**(1) In general**\nNotwithstanding any other provision of law, the United States Court of Federal Claims shall have jurisdiction to hear, determine, and render judgment on a land claim of the Miami Tribe of Oklahoma under its Treaty with the United States of America signed at Grouseland August 21, 1805 (7 Stat. 91) (commonly known as the Treaty of Grouseland ), without regard to the statute of limitations, including section 2501 of title 28, United States Code, and any delay-based defense, no matter how characterized.\n**(2) Jurisdiction expiration**\nNot later than 1 year after the date of enactment of this Act, the jurisdiction conferred to the United States Court of Federal Claims under paragraph (1) shall expire unless the Miami Tribe of Oklahoma files a land claim under that paragraph.\n##### (b) Extinguishment of title and claims\nExcept for a claim filed under subsection (a)(1), all other claims, including any and all future claims, of the Miami Tribe of Oklahoma, or any member, descendant, or predecessor in interest to the Miami Tribe of Oklahoma, to land in the State of Illinois are extinguished.",
      "versionDate": "2025-04-10",
      "versionType": "Introduced in House"
    }
  ]
}
```

## API Data: relatedbills

```json
{
  "relatedBills": [
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-12-16",
        "actionTime": "12:21:28",
        "text": "Held at the desk."
      },
      "number": "550",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "A bill to provide for the equitable settlement of certain Indian land disputes regarding land in Illinois, and for other purposes.",
      "type": "S"
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
            "name": "Drug trafficking and controlled substances",
            "updateDate": "2025-05-09T17:37:30Z"
          },
          {
            "name": "Health programs administration and funding",
            "updateDate": "2025-05-09T17:37:30Z"
          },
          {
            "name": "Health technology, devices, supplies",
            "updateDate": "2025-05-09T17:37:30Z"
          },
          {
            "name": "Medical tests and diagnostic methods",
            "updateDate": "2025-05-09T17:37:30Z"
          }
        ]
      },
      "policyArea": {
        "name": "Native Americans",
        "updateDate": "2025-05-12T19:18:37Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-04-10",
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
          "measure-id": "id119hr2827",
          "measure-number": "2827",
          "measure-type": "hr",
          "orig-publish-date": "2025-04-10",
          "originChamber": "HOUSE",
          "update-date": "2025-06-16"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr2827v00",
            "update-date": "2025-06-16"
          },
          "action-date": "2025-04-10",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This bill confers jurisdiction to the U.S. Court of Federal Claims for the Miami Tribe of Oklahoma's land claim arising under the Treaty of Grouseland. The court must render judgement without regard to the statute of limitations or any delay-based defense. This jurisdiction expires unless such a claim is filed within one year.</p> All other claims, including any future claims, of the tribe to land in Illinois are extinguished."
        },
        "title": "To provide for the equitable settlement of certain Indian land disputes regarding land in Illinois, and for other purposes."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr2827.xml",
    "summary": {
      "actionDate": "2025-04-10",
      "actionDesc": "Introduced in House",
      "text": "<p>This bill confers jurisdiction to the U.S. Court of Federal Claims for the Miami Tribe of Oklahoma's land claim arising under the Treaty of Grouseland. The court must render judgement without regard to the statute of limitations or any delay-based defense. This jurisdiction expires unless such a claim is filed within one year.</p> All other claims, including any future claims, of the tribe to land in Illinois are extinguished.",
      "updateDate": "2025-06-16",
      "versionCode": "id119hr2827"
    },
    "title": "To provide for the equitable settlement of certain Indian land disputes regarding land in Illinois, and for other purposes."
  },
  "summaries": [
    {
      "actionDate": "2025-04-10",
      "actionDesc": "Introduced in House",
      "text": "<p>This bill confers jurisdiction to the U.S. Court of Federal Claims for the Miami Tribe of Oklahoma's land claim arising under the Treaty of Grouseland. The court must render judgement without regard to the statute of limitations or any delay-based defense. This jurisdiction expires unless such a claim is filed within one year.</p> All other claims, including any future claims, of the tribe to land in Illinois are extinguished.",
      "updateDate": "2025-06-16",
      "versionCode": "id119hr2827"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-04-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2827ih.xml"
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
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To provide for the equitable settlement of certain Indian land disputes regarding land in Illinois, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-24T04:48:27Z"
    },
    {
      "title": "To provide for the equitable settlement of certain Indian land disputes regarding land in Illinois, and for other purposes.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-11T08:06:37Z"
    }
  ]
}
```
