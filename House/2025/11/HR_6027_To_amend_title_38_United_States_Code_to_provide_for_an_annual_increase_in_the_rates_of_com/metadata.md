# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6027?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6027
- Title: To amend title 38, United States Code, to provide for an annual increase in the rates of compensation for veterans with service-connected disabilities and the rates of dependency and indemnity compensation for the survivors of certain disabled veterans, and for other purposes.
- Congress: 119
- Bill type: HR
- Bill number: 6027
- Origin chamber: House
- Introduced date: 2025-11-12
- Update date: 2026-05-13T17:08:02Z
- Update date including text: 2026-05-13T17:08:02Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-11-12: Introduced in House
- 2025-11-12 - IntroReferral: Introduced in House
- 2025-11-12 - IntroReferral: Introduced in House
- 2025-11-12 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-11-17 - Committee: Referred to the Subcommittee on Disability Assistance and Memorial Affairs.
- Latest action: 2025-11-12: Introduced in House

## Actions

- 2025-11-12 - IntroReferral: Introduced in House
- 2025-11-12 - IntroReferral: Introduced in House
- 2025-11-12 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-11-17 - Committee: Referred to the Subcommittee on Disability Assistance and Memorial Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-12",
    "latestAction": {
      "actionDate": "2025-11-12",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6027",
    "number": "6027",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "G000583",
        "district": "5",
        "firstName": "Josh",
        "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
        "lastName": "Gottheimer",
        "party": "D",
        "state": "NJ"
      }
    ],
    "title": "To amend title 38, United States Code, to provide for an annual increase in the rates of compensation for veterans with service-connected disabilities and the rates of dependency and indemnity compensation for the survivors of certain disabled veterans, and for other purposes.",
    "type": "HR",
    "updateDate": "2026-05-13T17:08:02Z",
    "updateDateIncludingText": "2026-05-13T17:08:02Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-11-17",
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
      "actionDate": "2025-11-12",
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
      "actionDate": "2025-11-12",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-11-12",
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
          "date": "2025-11-12T17:01:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-11-17T18:22:56Z",
              "name": "Referred to"
            }
          },
          "name": "Disability Assistance and Memorial Affairs Subcommittee",
          "systemCode": "hsvr09"
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
      "bioguideId": "B001298",
      "district": "2",
      "firstName": "Don",
      "fullName": "Rep. Bacon, Don [R-NE-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Bacon",
      "party": "R",
      "sponsorshipDate": "2025-11-12",
      "state": "NE"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6027ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6027\nIN THE HOUSE OF REPRESENTATIVES\nNovember 12, 2025 Mr. Gottheimer (for himself and Mr. Bacon ) introduced the following bill; which was referred to the Committee on Veterans' Affairs\nA BILL\nTo amend title 38, United States Code, to provide for an annual increase in the rates of compensation for veterans with service-connected disabilities and the rates of dependency and indemnity compensation for the survivors of certain disabled veterans, and for other purposes.\n#### 1. Annual increase in rates of Department of Veterans Affairs disability compensation and dependency and indemnity compensation\n##### (a) In general\nChapter 1 of title 38, United States Code, is amended by adding at the end the following new section:\n120. Annual increase in disability compensation and dependency and indemnity compensation (a) Rate adjustment Effective on December 1 of each year, the Secretary shall increase, in accordance with subsection (c), the dollar amounts in effect on November 30 of that year, for the payment of disability compensation and dependency and indemnity compensation under the provisions specified in subsection (b). (b) Amounts To be increased The dollar amounts to be increased pursuant to subsection (a) are the following: (1) Wartime disability compensation Each of the dollar amounts under section 1114 of this title. (2) Additional compensation for dependents Each of the dollar amounts under section 1115(1) of this title. (3) Clothing allowance The dollar amount under section 1162 of this title. (4) Dependency and indemnity compensation to surviving spouse Each of the dollar amounts under subsections (a) through (d) of section 1311 of this title. (5) Dependency and indemnity compensation to children Each of the dollar amounts under sections 1313(a) and 1314 of this title. (c) Determination of Increase Each dollar amount described in subsection (b) shall be increased by the same percentage as the percentage by which benefit amounts payable under title II of the Social Security Act ( 42 U.S.C. 401 et seq. ) are increased effective December 1 of such year as a result of a determination under section 215(i) of such Act ( 42 U.S.C. 415(i) ). (d) Special rule The Secretary may adjust administratively, consistent with the increases made under subsection (a), the rates of disability compensation payable to persons under section 10 of Public Law 85\u2013857 (72 Stat. 1263) who have not received compensation under chapter 11 of this title. (e) Publication of adjusted rates Each fiscal year, the Secretary shall publish in the Federal Register the amounts specified in subsection (b), as increased under subsection (a), not later than the date on which the matters specified in section 215(i)(2)(D) of the Social Security Act ( 42 U.S.C. 415(i)(2)(D) ) are required to be published by reason of a determination made under section 215(i) of such Act during that fiscal year. .\n##### (b) Clerical amendment\nThe table of sections at the beginning of such chapter is amended by inserting after the item relating to section 119 the following new item:\n120. Annual increase in disability compensation and dependency and indemnity compensation. .\n##### (c) Effective date\nSection 120 of title 38, United States Code, as added by subsection (a), shall take effect on the date that is 180 days after the date of the enactment of this Act.",
      "versionDate": "2025-11-12",
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
        "actionDate": "2026-04-28",
        "text": "Referred to the House Committee on Veterans' Affairs."
      },
      "number": "8552",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Veterans\u2019 Compensation Cost-of-Living Adjustment Act of 2026",
      "type": "HR"
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
        "name": "Armed Forces and National Security",
        "updateDate": "2025-11-18T16:24:46Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-11-12",
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
          "measure-id": "id119hr6027",
          "measure-number": "6027",
          "measure-type": "hr",
          "orig-publish-date": "2025-11-12",
          "originChamber": "HOUSE",
          "update-date": "2026-02-24"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr6027v00",
            "update-date": "2026-02-24"
          },
          "action-date": "2025-11-12",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This bill requires the Department of Veterans Affairs (VA) to increase the amounts payable for wartime disability compensation, additional compensation for dependents, the clothing allowance for certain disabled veterans, and dependency and indemnity compensation for surviving spouses and children.\u00a0Specifically, the VA must increase the amounts by the same percentage as the cost-of-living increase in benefits for Social Security recipients that is effective on December 1 of each year. The bill requires the VA to publish the amounts payable, as increased, in the Federal Register.</p><p>The VA is authorized to make a similar adjustment to the rates of disability compensation payable to persons who have not received compensation for service-connected disability or death.</p>"
        },
        "title": "To amend title 38, United States Code, to provide for an annual increase in the rates of compensation for veterans with service-connected disabilities and the rates of dependency and indemnity compensation for the survivors of certain disabled veterans, and for other purposes."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr6027.xml",
    "summary": {
      "actionDate": "2025-11-12",
      "actionDesc": "Introduced in House",
      "text": "<p>This bill requires the Department of Veterans Affairs (VA) to increase the amounts payable for wartime disability compensation, additional compensation for dependents, the clothing allowance for certain disabled veterans, and dependency and indemnity compensation for surviving spouses and children.\u00a0Specifically, the VA must increase the amounts by the same percentage as the cost-of-living increase in benefits for Social Security recipients that is effective on December 1 of each year. The bill requires the VA to publish the amounts payable, as increased, in the Federal Register.</p><p>The VA is authorized to make a similar adjustment to the rates of disability compensation payable to persons who have not received compensation for service-connected disability or death.</p>",
      "updateDate": "2026-02-24",
      "versionCode": "id119hr6027"
    },
    "title": "To amend title 38, United States Code, to provide for an annual increase in the rates of compensation for veterans with service-connected disabilities and the rates of dependency and indemnity compensation for the survivors of certain disabled veterans, and for other purposes."
  },
  "summaries": [
    {
      "actionDate": "2025-11-12",
      "actionDesc": "Introduced in House",
      "text": "<p>This bill requires the Department of Veterans Affairs (VA) to increase the amounts payable for wartime disability compensation, additional compensation for dependents, the clothing allowance for certain disabled veterans, and dependency and indemnity compensation for surviving spouses and children.\u00a0Specifically, the VA must increase the amounts by the same percentage as the cost-of-living increase in benefits for Social Security recipients that is effective on December 1 of each year. The bill requires the VA to publish the amounts payable, as increased, in the Federal Register.</p><p>The VA is authorized to make a similar adjustment to the rates of disability compensation payable to persons who have not received compensation for service-connected disability or death.</p>",
      "updateDate": "2026-02-24",
      "versionCode": "id119hr6027"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-11-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6027ih.xml"
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
      "title": "To amend title 38, United States Code, to provide for an annual increase in the rates of compensation for veterans with service-connected disabilities and the rates of dependency and indemnity compensation for the survivors of certain disabled veterans, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-14T10:18:27Z"
    },
    {
      "title": "To amend title 38, United States Code, to provide for an annual increase in the rates of compensation for veterans with service-connected disabilities and the rates of dependency and indemnity compensation for the survivors of certain disabled veterans, and for other purposes.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-13T09:05:36Z"
    }
  ]
}
```
