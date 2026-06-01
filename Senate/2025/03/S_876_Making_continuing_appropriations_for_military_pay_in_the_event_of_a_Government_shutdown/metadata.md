# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/876?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/876
- Title: Pay Our Military Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 876
- Origin chamber: Senate
- Introduced date: 2025-03-06
- Update date: 2025-12-05T21:32:19Z
- Update date including text: 2025-12-05T21:32:19Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-03-06: Introduced in Senate
- 2025-03-06 - IntroReferral: Introduced in Senate
- 2025-03-06 - IntroReferral: Read twice and referred to the Committee on Armed Services.
- Latest action: 2025-03-06: Introduced in Senate

## Actions

- 2025-03-06 - IntroReferral: Introduced in Senate
- 2025-03-06 - IntroReferral: Read twice and referred to the Committee on Armed Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-06",
    "latestAction": {
      "actionDate": "2025-03-06",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/876",
    "number": "876",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "S001198",
        "district": "",
        "firstName": "Dan",
        "fullName": "Sen. Sullivan, Dan [R-AK]",
        "lastName": "Sullivan",
        "party": "R",
        "state": "AK"
      }
    ],
    "title": "Pay Our Military Act of 2025",
    "type": "S",
    "updateDate": "2025-12-05T21:32:19Z",
    "updateDateIncludingText": "2025-12-05T21:32:19Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-06",
      "committees": {
        "item": {
          "name": "Armed Services Committee",
          "systemCode": "ssas00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Armed Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-03-06",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in Senate",
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
          "date": "2025-03-06T15:50:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Armed Services Committee",
      "systemCode": "ssas00",
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
      "bioguideId": "M001153",
      "firstName": "Lisa",
      "fullName": "Sen. Murkowski, Lisa [R-AK]",
      "isOriginalCosponsor": "False",
      "lastName": "Murkowski",
      "party": "R",
      "sponsorshipDate": "2025-03-11",
      "state": "AK"
    },
    {
      "bioguideId": "C001098",
      "firstName": "Ted",
      "fullName": "Sen. Cruz, Ted [R-TX]",
      "isOriginalCosponsor": "False",
      "lastName": "Cruz",
      "party": "R",
      "sponsorshipDate": "2025-03-13",
      "state": "TX"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s876is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 876\nIN THE SENATE OF THE UNITED STATES\nMarch 6, 2025 Mr. Sullivan introduced the following bill; which was read twice and referred to the Committee on Armed Services\nA BILL\nMaking continuing appropriations for military pay in the event of a Government shutdown.\n#### 1. Short title\nThis Act may be cited as the Pay Our Military Act of 2025 .\n#### 2. Continuing appropriations for members of the Armed Forces\n##### (a) In general\nThere are hereby appropriated for fiscal year 2025, out of any money in the Treasury not otherwise appropriated, for any period during which interim or full-year appropriations for fiscal year 2025 are not in effect\u2014\n**(1)**\nsuch sums as are necessary to provide pay and allowances to members of the Armed Forces (as defined in section 101(a)(4) of title 10, United States Code), including reserve components thereof, who perform active service during such period;\n**(2)**\nsuch sums as are necessary to provide pay and allowances to the civilian personnel of the Department of Defense (and the Department of Homeland Security in the case of the Coast Guard) whom the Secretary concerned determines are providing support to members of the Armed Forces described in paragraph (1); and\n**(3)**\nsuch sums as are necessary to provide pay and allowances to contractors of the Department of Defense (and the Department of Homeland Security in the case of the Coast Guard) whom the Secretary concerned determines are providing support to members of the Armed Forces described in paragraph (1).\n##### (b) Secretary concerned defined\nIn this section, the term Secretary concerned means\u2014\n**(1)**\nthe Secretary of Defense with respect to matters concerning the Department of Defense; and\n**(2)**\nthe Secretary of Homeland Security with respect to matters concerning the Coast Guard.\n#### 3. Termination\nAppropriations and funds made available and authority granted pursuant to this Act shall be available until whichever of the following first occurs:\n**(1)**\nThe enactment into law of an appropriation (including a continuing appropriation) for any purpose for which amounts are made available in section 2.\n**(2)**\nThe enactment into law of the applicable regular or continuing appropriations resolution or other Act without any appropriation for such purpose.\n**(3)**\nJanuary 1, 2026.",
      "versionDate": "2025-03-06",
      "versionType": "Introduced in Senate"
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
        "actionDate": "2025-10-30",
        "text": "Referred to the Committee on Appropriations by unanimous consent."
      },
      "number": "3002",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Pay Our Military Act of 2025",
      "type": "S"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-03-06",
        "text": "Referred to the House Committee on Appropriations."
      },
      "number": "1932",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Pay Our Troops Act of 2025",
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
        "updateDate": "2025-05-06T15:46:33Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-06",
    "originChamber": "Senate",
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
          "measure-id": "id119s876",
          "measure-number": "876",
          "measure-type": "s",
          "orig-publish-date": "2025-03-06",
          "originChamber": "SENATE",
          "update-date": "2025-07-03"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s876v00",
            "update-date": "2025-07-03"
          },
          "action-date": "2025-03-06",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Pay Our Military Act of 2025</strong></p><p>This bill provides continuing appropriations for military pay for any period during which interim or full-year appropriations for FY2025 are not in effect (i.e., a government shutdown).</p><p>Specifically, the bill provides FY2025 continuing appropriations for the pay and allowances of (1) members of the Armed Forces, including reserve components, who perform active service during the period; and (2) civilian personnel and contractors of the Department of Defense (and the Department of Homeland Security in the case of the Coast Guard) who are providing support to such members of the Armed Forces.</p><p>If a government shutdown occurs, the bill provides the continuing appropriations until the earlier of (1) the enactment into law of specified appropriations legislation, or (2) January 1, 2026.\u00a0</p>"
        },
        "title": "Pay Our Military Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s876.xml",
    "summary": {
      "actionDate": "2025-03-06",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Pay Our Military Act of 2025</strong></p><p>This bill provides continuing appropriations for military pay for any period during which interim or full-year appropriations for FY2025 are not in effect (i.e., a government shutdown).</p><p>Specifically, the bill provides FY2025 continuing appropriations for the pay and allowances of (1) members of the Armed Forces, including reserve components, who perform active service during the period; and (2) civilian personnel and contractors of the Department of Defense (and the Department of Homeland Security in the case of the Coast Guard) who are providing support to such members of the Armed Forces.</p><p>If a government shutdown occurs, the bill provides the continuing appropriations until the earlier of (1) the enactment into law of specified appropriations legislation, or (2) January 1, 2026.\u00a0</p>",
      "updateDate": "2025-07-03",
      "versionCode": "id119s876"
    },
    "title": "Pay Our Military Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-03-06",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Pay Our Military Act of 2025</strong></p><p>This bill provides continuing appropriations for military pay for any period during which interim or full-year appropriations for FY2025 are not in effect (i.e., a government shutdown).</p><p>Specifically, the bill provides FY2025 continuing appropriations for the pay and allowances of (1) members of the Armed Forces, including reserve components, who perform active service during the period; and (2) civilian personnel and contractors of the Department of Defense (and the Department of Homeland Security in the case of the Coast Guard) who are providing support to such members of the Armed Forces.</p><p>If a government shutdown occurs, the bill provides the continuing appropriations until the earlier of (1) the enactment into law of specified appropriations legislation, or (2) January 1, 2026.\u00a0</p>",
      "updateDate": "2025-07-03",
      "versionCode": "id119s876"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-06",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s876is.xml"
        }
      ],
      "type": "Introduced in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Pay Our Military Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-26T02:08:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Pay Our Military Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-26T02:08:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill making continuing appropriations for military pay in the event of a Government shutdown.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-26T02:03:26Z"
    }
  ]
}
```
