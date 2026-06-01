# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1872?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1872
- Title: Fairness in Veterans’ Education Act
- Congress: 119
- Bill type: HR
- Bill number: 1872
- Origin chamber: House
- Introduced date: 2025-03-05
- Update date: 2026-02-04T05:06:17Z
- Update date including text: 2026-02-04T05:06:17Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-03-05: Introduced in House
- 2025-03-05 - IntroReferral: Introduced in House
- 2025-03-05 - IntroReferral: Introduced in House
- 2025-03-05 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-03-10 - Committee: Referred to the Subcommittee on Economic Opportunity.
- 2025-03-10 - Committee: Subcommittee Hearings Held
- 2025-04-09 - Committee: Forwarded by Subcommittee to Full Committee (Amended) by Voice Vote.
- 2025-04-09 - Committee: Subcommittee Consideration and Mark-up Session Held
- Latest action: 2025-03-05: Introduced in House

## Actions

- 2025-03-05 - IntroReferral: Introduced in House
- 2025-03-05 - IntroReferral: Introduced in House
- 2025-03-05 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-03-10 - Committee: Referred to the Subcommittee on Economic Opportunity.
- 2025-03-10 - Committee: Subcommittee Hearings Held
- 2025-04-09 - Committee: Forwarded by Subcommittee to Full Committee (Amended) by Voice Vote.
- 2025-04-09 - Committee: Subcommittee Consideration and Mark-up Session Held

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-05",
    "latestAction": {
      "actionDate": "2025-03-05",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1872",
    "number": "1872",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "J000304",
        "district": "13",
        "firstName": "Ronny",
        "fullName": "Rep. Jackson, Ronny [R-TX-13]",
        "lastName": "Jackson",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "Fairness in Veterans\u2019 Education Act",
    "type": "HR",
    "updateDate": "2026-02-04T05:06:17Z",
    "updateDateIncludingText": "2026-02-04T05:06:17Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-04-09",
      "committees": {
        "item": {
          "name": "Economic Opportunity Subcommittee",
          "systemCode": "hsvr10"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Forwarded by Subcommittee to Full Committee (Amended) by Voice Vote.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-04-09",
      "committees": {
        "item": {
          "name": "Economic Opportunity Subcommittee",
          "systemCode": "hsvr10"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Subcommittee Consideration and Mark-up Session Held",
      "type": "Committee"
    },
    {
      "actionDate": "2025-03-10",
      "committees": {
        "item": {
          "name": "Economic Opportunity Subcommittee",
          "systemCode": "hsvr10"
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
      "actionDate": "2025-03-10",
      "committees": {
        "item": {
          "name": "Economic Opportunity Subcommittee",
          "systemCode": "hsvr10"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Economic Opportunity.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-05",
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
      "actionDate": "2025-03-05",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-05",
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
          "date": "2025-03-05T15:03:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": [
              {
                "date": "2025-04-09T21:02:58Z",
                "name": "Reported by"
              },
              {
                "date": "2025-04-09T20:49:23Z",
                "name": "Markup by"
              },
              {
                "date": "2025-03-10T19:16:53Z",
                "name": "Hearings By (subcommittee)"
              },
              {
                "date": "2025-03-10T19:16:45Z",
                "name": "Referred to"
              }
            ]
          },
          "name": "Economic Opportunity Subcommittee",
          "systemCode": "hsvr10"
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
      "bioguideId": "V000135",
      "district": "3",
      "firstName": "Derrick",
      "fullName": "Rep. Van Orden, Derrick [R-WI-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Orden",
      "party": "R",
      "sponsorshipDate": "2025-03-05",
      "state": "WI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1872ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1872\nIN THE HOUSE OF REPRESENTATIVES\nMarch 5, 2025 Mr. Jackson of Texas (for himself and Mr. Van Orden ) introduced the following bill; which was referred to the Committee on Veterans' Affairs\nA BILL\nTo amend title 38, United States Code, to ensure that the Secretary of Veterans Affairs repays members of the Armed Forces for certain contributions made by such members towards Post-9/11 Educational Assistance.\n#### 1. Short title\nThis Act may be cited as the Fairness in Veterans\u2019 Education Act .\n#### 2. Repayment of members of the Armed Forces for contributions toward Post-9/11 Educational Assistance\n##### (a) In general\nSection 3327(f)(3) of title 38, United States Code, is amended by striking together and all that follows through (as applicable), .\n##### (b) Effective date\nThe amendment made by subsection (a) shall take effect on August 1, 2025.",
      "versionDate": "2025-03-05",
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
        "actionDate": "2025-12-09",
        "text": "Placed on Senate Legislative Calendar under General Orders. Calendar No. 288."
      },
      "number": "972",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Fairness in Veterans' Education Act of 2025",
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
            "name": "Higher education",
            "updateDate": "2025-04-01T15:31:27Z"
          },
          {
            "name": "Military personnel and dependents",
            "updateDate": "2025-04-01T15:31:22Z"
          },
          {
            "name": "Veterans' education, employment, rehabilitation",
            "updateDate": "2025-04-01T15:31:13Z"
          }
        ]
      },
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2025-03-25T18:08:50Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-05",
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
          "measure-id": "id119hr1872",
          "measure-number": "1872",
          "measure-type": "hr",
          "orig-publish-date": "2025-03-05",
          "originChamber": "HOUSE",
          "update-date": "2025-03-26"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1872v00",
            "update-date": "2025-03-26"
          },
          "action-date": "2025-03-05",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Fairness in Veterans\u2019 Education Act</strong></p><p>This bill modifies the process for repaying service members and veterans who paid to keep benefits under the Montgomery GI Bill, but later chose to utilize Post-9/11 GI Bill benefits. Specifically, the bill removes the requirement for the Department of Veterans Affairs (VA) to issue the repayments with the last monthly housing stipend under the Post-9/11 GI Bill. This requirement has limited the repayments to individuals who are receiving stipends. Under the bill, the VA must make such a repayment before the exhaustion of the individual's entitlement to education assistance.</p>"
        },
        "title": "Fairness in Veterans\u2019 Education Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1872.xml",
    "summary": {
      "actionDate": "2025-03-05",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Fairness in Veterans\u2019 Education Act</strong></p><p>This bill modifies the process for repaying service members and veterans who paid to keep benefits under the Montgomery GI Bill, but later chose to utilize Post-9/11 GI Bill benefits. Specifically, the bill removes the requirement for the Department of Veterans Affairs (VA) to issue the repayments with the last monthly housing stipend under the Post-9/11 GI Bill. This requirement has limited the repayments to individuals who are receiving stipends. Under the bill, the VA must make such a repayment before the exhaustion of the individual's entitlement to education assistance.</p>",
      "updateDate": "2025-03-26",
      "versionCode": "id119hr1872"
    },
    "title": "Fairness in Veterans\u2019 Education Act"
  },
  "summaries": [
    {
      "actionDate": "2025-03-05",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Fairness in Veterans\u2019 Education Act</strong></p><p>This bill modifies the process for repaying service members and veterans who paid to keep benefits under the Montgomery GI Bill, but later chose to utilize Post-9/11 GI Bill benefits. Specifically, the bill removes the requirement for the Department of Veterans Affairs (VA) to issue the repayments with the last monthly housing stipend under the Post-9/11 GI Bill. This requirement has limited the repayments to individuals who are receiving stipends. Under the bill, the VA must make such a repayment before the exhaustion of the individual's entitlement to education assistance.</p>",
      "updateDate": "2025-03-26",
      "versionCode": "id119hr1872"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1872ih.xml"
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
      "title": "Fairness in Veterans\u2019 Education Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-24T13:53:27Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Fairness in Veterans\u2019 Education Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-24T13:53:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 38, United States Code, to ensure that the Secretary of Veterans Affairs repays members of the Armed Forces for certain contributions made by such members towards Post-9/11 Educational Assistance.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-24T13:48:29Z"
    }
  ]
}
```
