# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4430?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4430
- Title: White House Safety and Security Act of 2026
- Congress: 119
- Bill type: S
- Bill number: 4430
- Origin chamber: Senate
- Introduced date: 2026-04-29
- Update date: 2026-05-14T16:51:42Z
- Update date including text: 2026-05-14T16:51:42Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2026-04-29: Introduced in Senate
- 2026-04-29 - IntroReferral: Introduced in Senate
- 2026-04-29 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2026-04-29: Introduced in Senate

## Actions

- 2026-04-29 - IntroReferral: Introduced in Senate
- 2026-04-29 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-29",
    "latestAction": {
      "actionDate": "2026-04-29",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4430",
    "number": "4430",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "G000359",
        "district": "",
        "firstName": "Lindsey",
        "fullName": "Sen. Graham, Lindsey [R-SC]",
        "lastName": "Graham",
        "party": "R",
        "state": "SC"
      }
    ],
    "title": "White House Safety and Security Act of 2026",
    "type": "S",
    "updateDate": "2026-05-14T16:51:42Z",
    "updateDateIncludingText": "2026-05-14T16:51:42Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-04-29",
      "committees": {
        "item": {
          "name": "Finance Committee",
          "systemCode": "ssfi00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Finance.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-04-29",
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
          "date": "2026-04-29T16:58:22Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Finance Committee",
      "systemCode": "ssfi00",
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
      "bioguideId": "B001319",
      "firstName": "Katie",
      "fullName": "Sen. Britt, Katie Boyd [R-AL]",
      "isOriginalCosponsor": "True",
      "lastName": "Britt",
      "party": "R",
      "sponsorshipDate": "2026-04-29",
      "state": "AL"
    },
    {
      "bioguideId": "S001227",
      "firstName": "Eric",
      "fullName": "Sen. Schmitt, Eric [R-MO]",
      "isOriginalCosponsor": "True",
      "lastName": "Schmitt",
      "middleName": "S.",
      "party": "R",
      "sponsorshipDate": "2026-04-29",
      "state": "MO"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4430is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4430\nIN THE SENATE OF THE UNITED STATES\nApril 29, 2026 Mr. Graham (for himself, Mrs. Britt , and Mr. Schmitt ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo authorize the East Wing Modernization Project, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the White House Safety and Security Act of 2026 .\n#### 2. Authorization of East Wing Modernization Project\n##### (a) Appropriation\nIn addition to amounts otherwise available, including monetary or in-kind donations in the White House Repair and Restoration account as of the date of enactment of this Act, there is appropriated to the President for fiscal year 2026, out of any money in the Treasury not otherwise appropriated, $400,000,000, to remain available until January 20, 2029, for design, construction, and other appropriate expenses to complete the East Wing Modernization Project, including a secure State Ballroom and visitor screening facility and any other related national security facility, pursuant to section 105(d) of title 3, United States Code.\n##### (b) Extension of customs user fees\n**(1) In general**\nSection 13031(j)(3) of the Consolidated Omnibus Budget Reconciliation Act of 1985 ( 19 U.S.C. 58c(j)(3) ) is amended\u2014\n**(A)**\nin subparagraph (A), by striking December 31, 2031 and inserting March 31, 2032 ; and\n**(B)**\nin subparagraph (B)(i), by striking December 31, 2031 and inserting March 31, 2032 .\n**(2) Rate for merchandise processing fees**\nSection 503 of the United States-Korea Free Trade Agreement Implementation Act ( Public Law 112\u201341 ; 19 U.S.C. 3805 note) is amended by striking December 31, 2031 and inserting March 31, 2032 .",
      "versionDate": "2026-04-29",
      "versionType": "Introduced in Senate"
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
        "name": "Government Operations and Politics",
        "updateDate": "2026-05-12T22:14:36Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2026-04-29",
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
          "measure-id": "id119s4430",
          "measure-number": "4430",
          "measure-type": "s",
          "orig-publish-date": "2026-04-29",
          "originChamber": "SENATE",
          "update-date": "2026-05-14"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s4430v00",
            "update-date": "2026-05-14"
          },
          "action-date": "2026-04-29",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>White House Safety and Security Act of 2026</strong></p><p>This bill provides appropriations to the President for the East Wing Modernization Project and extends certain customs user fees.</p><p>Specifically, the bill appropriates $400 million to the President for design, construction, and other appropriate expenses to complete the East Wing Modernization Project, including a secure State Ballroom and visitor screening facility and any other related national security facility. The funding provided by the bill remains available until January 20, 2029.</p><p>The bill also extends certain customs user fees through March 31, 2032. (Under current law, the fees are authorized through December 31, 2031).\u00a0</p>"
        },
        "title": "White House Safety and Security Act of 2026"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s4430.xml",
    "summary": {
      "actionDate": "2026-04-29",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>White House Safety and Security Act of 2026</strong></p><p>This bill provides appropriations to the President for the East Wing Modernization Project and extends certain customs user fees.</p><p>Specifically, the bill appropriates $400 million to the President for design, construction, and other appropriate expenses to complete the East Wing Modernization Project, including a secure State Ballroom and visitor screening facility and any other related national security facility. The funding provided by the bill remains available until January 20, 2029.</p><p>The bill also extends certain customs user fees through March 31, 2032. (Under current law, the fees are authorized through December 31, 2031).\u00a0</p>",
      "updateDate": "2026-05-14",
      "versionCode": "id119s4430"
    },
    "title": "White House Safety and Security Act of 2026"
  },
  "summaries": [
    {
      "actionDate": "2026-04-29",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>White House Safety and Security Act of 2026</strong></p><p>This bill provides appropriations to the President for the East Wing Modernization Project and extends certain customs user fees.</p><p>Specifically, the bill appropriates $400 million to the President for design, construction, and other appropriate expenses to complete the East Wing Modernization Project, including a secure State Ballroom and visitor screening facility and any other related national security facility. The funding provided by the bill remains available until January 20, 2029.</p><p>The bill also extends certain customs user fees through March 31, 2032. (Under current law, the fees are authorized through December 31, 2031).\u00a0</p>",
      "updateDate": "2026-05-14",
      "versionCode": "id119s4430"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2026-04-29",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4430is.xml"
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
      "title": "White House Safety and Security Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-08T04:23:28Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "White House Safety and Security Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-08T04:23:27Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to authorize the East Wing Modernization Project, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-08T04:18:39Z"
    }
  ]
}
```
