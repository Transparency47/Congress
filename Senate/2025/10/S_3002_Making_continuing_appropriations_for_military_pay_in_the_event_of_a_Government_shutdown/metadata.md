# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3002?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3002
- Title: Pay Our Military Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 3002
- Origin chamber: Senate
- Introduced date: 2025-10-09
- Update date: 2025-12-05T21:32:29Z
- Update date including text: 2025-12-05T21:32:29Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-10-09: Introduced in Senate
- 2025-10-09 - IntroReferral: Introduced in Senate
- 2025-10-09 - IntroReferral: Read twice and referred to the Committee on Armed Services.
- 2025-10-30 - IntroReferral: Referred to the Committee on Appropriations by unanimous consent.
- 2025-10-30 - Discharge: Senate Committee on Armed Services discharged by Unanimous Consent.
- 2025-10-30 - Committee: Senate Committee on Armed Services discharged by Unanimous Consent.
- Latest action: 2025-10-09: Introduced in Senate

## Actions

- 2025-10-09 - IntroReferral: Introduced in Senate
- 2025-10-09 - IntroReferral: Read twice and referred to the Committee on Armed Services.
- 2025-10-30 - IntroReferral: Referred to the Committee on Appropriations by unanimous consent.
- 2025-10-30 - Discharge: Senate Committee on Armed Services discharged by Unanimous Consent.
- 2025-10-30 - Committee: Senate Committee on Armed Services discharged by Unanimous Consent.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-10-09",
    "latestAction": {
      "actionDate": "2025-10-09",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3002",
    "number": "3002",
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
    "updateDate": "2025-12-05T21:32:29Z",
    "updateDateIncludingText": "2025-12-05T21:32:29Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-10-30",
      "committees": {
        "item": {
          "name": "Appropriations Committee",
          "systemCode": "ssap00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Referred to the Committee on Appropriations by unanimous consent.",
      "type": "IntroReferral"
    },
    {
      "actionDate": "2025-10-30",
      "committees": {
        "item": {
          "name": "Armed Services Committee",
          "systemCode": "ssas00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Senate Committee on Armed Services discharged by Unanimous Consent.",
      "type": "Discharge"
    },
    {
      "actionCode": "14500",
      "actionDate": "2025-10-30",
      "committees": {
        "item": {
          "name": "Armed Services Committee",
          "systemCode": "ssas00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Senate Committee on Armed Services discharged by Unanimous Consent.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-10-09",
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
      "actionDate": "2025-10-09",
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
          "date": "2025-10-30T19:20:46Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Appropriations Committee",
      "systemCode": "ssap00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": [
          {
            "date": "2025-10-30T19:20:24Z",
            "name": "Discharged From"
          },
          {
            "date": "2025-10-10T01:34:26Z",
            "name": "Referred To"
          }
        ]
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
      "bioguideId": "B001299",
      "firstName": "Jim",
      "fullName": "Sen. Banks, Jim [R-IN]",
      "isOriginalCosponsor": "True",
      "lastName": "Banks",
      "party": "R",
      "sponsorshipDate": "2025-10-09",
      "state": "IN"
    },
    {
      "bioguideId": "B001243",
      "firstName": "Marsha",
      "fullName": "Sen. Blackburn, Marsha [R-TN]",
      "isOriginalCosponsor": "True",
      "lastName": "Blackburn",
      "party": "R",
      "sponsorshipDate": "2025-10-09",
      "state": "TN"
    },
    {
      "bioguideId": "B001236",
      "firstName": "John",
      "fullName": "Sen. Boozman, John [R-AR]",
      "isOriginalCosponsor": "True",
      "lastName": "Boozman",
      "party": "R",
      "sponsorshipDate": "2025-10-09",
      "state": "AR"
    },
    {
      "bioguideId": "B001319",
      "firstName": "Katie",
      "fullName": "Sen. Britt, Katie Boyd [R-AL]",
      "isOriginalCosponsor": "True",
      "lastName": "Britt",
      "party": "R",
      "sponsorshipDate": "2025-10-09",
      "state": "AL"
    },
    {
      "bioguideId": "B001305",
      "firstName": "Ted",
      "fullName": "Sen. Budd, Ted [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Budd",
      "party": "R",
      "sponsorshipDate": "2025-10-09",
      "state": "NC"
    },
    {
      "bioguideId": "H001061",
      "firstName": "John",
      "fullName": "Sen. Hoeven, John [R-ND]",
      "isOriginalCosponsor": "True",
      "lastName": "Hoeven",
      "party": "R",
      "sponsorshipDate": "2025-10-09",
      "state": "ND"
    },
    {
      "bioguideId": "H001104",
      "firstName": "Jon",
      "fullName": "Sen. Husted, Jon [R-OH]",
      "isOriginalCosponsor": "True",
      "lastName": "Husted",
      "party": "R",
      "sponsorshipDate": "2025-10-09",
      "state": "OH"
    },
    {
      "bioguideId": "H001079",
      "firstName": "Cindy",
      "fullName": "Sen. Hyde-Smith, Cindy [R-MS]",
      "isOriginalCosponsor": "True",
      "lastName": "Hyde-Smith",
      "party": "R",
      "sponsorshipDate": "2025-10-09",
      "state": "MS"
    },
    {
      "bioguideId": "L000577",
      "firstName": "Mike",
      "fullName": "Sen. Lee, Mike [R-UT]",
      "isOriginalCosponsor": "True",
      "lastName": "Lee",
      "party": "R",
      "sponsorshipDate": "2025-10-09",
      "state": "UT"
    },
    {
      "bioguideId": "M001244",
      "firstName": "Ashley",
      "fullName": "Sen. Moody, Ashley [R-FL]",
      "isOriginalCosponsor": "True",
      "lastName": "Moody",
      "party": "R",
      "sponsorshipDate": "2025-10-09",
      "state": "FL"
    },
    {
      "bioguideId": "M000934",
      "firstName": "Jerry",
      "fullName": "Sen. Moran, Jerry [R-KS]",
      "isOriginalCosponsor": "True",
      "lastName": "Moran",
      "party": "R",
      "sponsorshipDate": "2025-10-09",
      "state": "KS"
    },
    {
      "bioguideId": "M001190",
      "firstName": "Markwayne",
      "fullName": "Sen. Mullin, Markwayne [R-OK]",
      "isOriginalCosponsor": "True",
      "lastName": "Mullin",
      "party": "R",
      "sponsorshipDate": "2025-10-09",
      "state": "OK"
    },
    {
      "bioguideId": "M001153",
      "firstName": "Lisa",
      "fullName": "Sen. Murkowski, Lisa [R-AK]",
      "isOriginalCosponsor": "True",
      "lastName": "Murkowski",
      "party": "R",
      "sponsorshipDate": "2025-10-09",
      "state": "AK"
    },
    {
      "bioguideId": "R000618",
      "firstName": "Pete",
      "fullName": "Sen. Ricketts, Pete [R-NE]",
      "isOriginalCosponsor": "True",
      "lastName": "Ricketts",
      "party": "R",
      "sponsorshipDate": "2025-10-09",
      "state": "NE"
    },
    {
      "bioguideId": "S001217",
      "firstName": "Rick",
      "fullName": "Sen. Scott, Rick [R-FL]",
      "isOriginalCosponsor": "True",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-10-09",
      "state": "FL"
    },
    {
      "bioguideId": "S001184",
      "firstName": "Tim",
      "fullName": "Sen. Scott, Tim [R-SC]",
      "isOriginalCosponsor": "True",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-10-09",
      "state": "SC"
    },
    {
      "bioguideId": "Y000064",
      "firstName": "Todd",
      "fullName": "Sen. Young, Todd [R-IN]",
      "isOriginalCosponsor": "True",
      "lastName": "Young",
      "party": "R",
      "sponsorshipDate": "2025-10-09",
      "state": "IN"
    },
    {
      "bioguideId": "M001243",
      "firstName": "David",
      "fullName": "Sen. McCormick, David [R-PA]",
      "isOriginalCosponsor": "True",
      "lastName": "McCormick",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2025-10-09",
      "state": "PA"
    },
    {
      "bioguideId": "C001035",
      "firstName": "Susan",
      "fullName": "Sen. Collins, Susan M. [R-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "Collins",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-10-09",
      "state": "ME"
    },
    {
      "bioguideId": "D000618",
      "firstName": "Steve",
      "fullName": "Sen. Daines, Steve [R-MT]",
      "isOriginalCosponsor": "False",
      "lastName": "Daines",
      "party": "R",
      "sponsorshipDate": "2025-10-15",
      "state": "MT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3002is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3002\nIN THE SENATE OF THE UNITED STATES\nOctober 9, 2025 Mr. Sullivan (for himself, Mr. Banks , Mrs. Blackburn , Mr. Boozman , Mrs. Britt , Mr. Budd , Mr. Hoeven , Mr. Husted , Mrs. Hyde-Smith , Mr. Lee , Mrs. Moody , Mr. Moran , Mr. Mullin , Ms. Murkowski , Mr. Ricketts , Mr. Scott of Florida , Mr. Scott of South Carolina , Mr. Young , Mr. McCormick , and Ms. Collins ) introduced the following bill; which was read twice and referred to the Committee on Armed Services\nA BILL\nMaking continuing appropriations for military pay in the event of a Government shutdown.\n#### 1. Short title\nThis Act may be cited as the Pay Our Military Act of 2025 .\n#### 2. Continuing appropriations for members of the Armed Forces\n##### (a) In general\nThere are hereby appropriated for fiscal year 2026, out of any money in the Treasury not otherwise appropriated, for any period during which interim or full-year appropriations for fiscal year 2026 are not in effect\u2014\n**(1)**\nsuch sums as are necessary to provide pay and allowances to members of the Armed Forces (as defined in section 101(a)(4) of title 10, United States Code), including reserve components thereof, who perform active service during such period;\n**(2)**\nsuch sums as are necessary to provide pay and allowances to the civilian personnel of the Department of Defense (and the Department of Homeland Security in the case of the Coast Guard) whom the Secretary concerned determines are providing support to members of the Armed Forces described in paragraph (1); and\n**(3)**\nsuch sums as are necessary to provide pay and allowances to contractors of the Department of Defense (and the Department of Homeland Security in the case of the Coast Guard) whom the Secretary concerned determines are providing support to members of the Armed Forces described in paragraph (1).\n##### (b) Secretary concerned defined\nIn this section, the term Secretary concerned means\u2014\n**(1)**\nthe Secretary of Defense with respect to matters concerning the Department of Defense; and\n**(2)**\nthe Secretary of Homeland Security with respect to matters concerning the Coast Guard.\n#### 3. Termination\nAppropriations and funds made available and authority granted pursuant to this Act shall be available until whichever of the following first occurs:\n**(1)**\nThe enactment into law of an appropriation (including a continuing appropriation) for any purpose for which amounts are made available in section 2.\n**(2)**\nThe enactment into law of the applicable regular or continuing appropriations resolution or other Act without any appropriation for such purpose.\n**(3)**\nJanuary 1, 2027.",
      "versionDate": "2025-10-09",
      "versionType": "Introduced in Senate"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3002rcs.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3002\nIN THE SENATE OF THE UNITED STATES\nOctober 9, 2025 Mr. Sullivan (for himself, Mr. Banks , Mrs. Blackburn , Mr. Boozman , Mrs. Britt , Mr. Budd , Mr. Hoeven , Mr. Husted , Mrs. Hyde-Smith , Mr. Lee , Mrs. Moody , Mr. Moran , Mr. Mullin , Ms. Murkowski , Mr. Ricketts , Mr. Scott of Florida , Mr. Scott of South Carolina , Mr. Young , Mr. McCormick , Ms. Collins , and Mr. Daines ) introduced the following bill; which was read twice and referred to the Committee on Armed Services\nOctober 30, 2025 Committee discharged; referred to the Committee on Appropriations\nA BILL\nMaking continuing appropriations for military pay in the event of a Government shutdown.\n#### 1. Short title\nThis Act may be cited as the Pay Our Military Act of 2025 .\n#### 2. Continuing appropriations for members of the Armed Forces\n##### (a) In general\nThere are hereby appropriated for fiscal year 2026, out of any money in the Treasury not otherwise appropriated, for any period during which interim or full-year appropriations for fiscal year 2026 are not in effect\u2014\n**(1)**\nsuch sums as are necessary to provide pay and allowances to members of the Armed Forces (as defined in section 101(a)(4) of title 10, United States Code), including reserve components thereof, who perform active service during such period;\n**(2)**\nsuch sums as are necessary to provide pay and allowances to the civilian personnel of the Department of Defense (and the Department of Homeland Security in the case of the Coast Guard) whom the Secretary concerned determines are providing support to members of the Armed Forces described in paragraph (1); and\n**(3)**\nsuch sums as are necessary to provide pay and allowances to contractors of the Department of Defense (and the Department of Homeland Security in the case of the Coast Guard) whom the Secretary concerned determines are providing support to members of the Armed Forces described in paragraph (1).\n##### (b) Secretary concerned defined\nIn this section, the term Secretary concerned means\u2014\n**(1)**\nthe Secretary of Defense with respect to matters concerning the Department of Defense; and\n**(2)**\nthe Secretary of Homeland Security with respect to matters concerning the Coast Guard.\n#### 3. Termination\nAppropriations and funds made available and authority granted pursuant to this Act shall be available until whichever of the following first occurs:\n**(1)**\nThe enactment into law of an appropriation (including a continuing appropriation) for any purpose for which amounts are made available in section 2.\n**(2)**\nThe enactment into law of the applicable regular or continuing appropriations resolution or other Act without any appropriation for such purpose.\n**(3)**\nJanuary 1, 2027.",
      "versionDate": "2025-10-30",
      "versionType": "Reference Change Senate"
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
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-03-06",
        "text": "Read twice and referred to the Committee on Armed Services."
      },
      "number": "876",
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
        "actionDate": "2025-09-16",
        "text": "Referred to the House Committee on Appropriations."
      },
      "number": "5401",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Pay Our Troops Act of 2026",
      "type": "HR"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-10-28",
        "text": "Read twice and referred to the Committee on Appropriations."
      },
      "number": "3060",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Paychecks for Patriots Act of 2025",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2025-10-14T13:43:08Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-10-09",
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
          "measure-id": "id119s3002",
          "measure-number": "3002",
          "measure-type": "s",
          "orig-publish-date": "2025-10-09",
          "originChamber": "SENATE",
          "update-date": "2025-10-14"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s3002v00",
            "update-date": "2025-10-14"
          },
          "action-date": "2025-10-09",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Pay Our Military Act of 2025</strong></p><p>This bill provides continuing appropriations for military pay for any period during which interim or full-year appropriations for FY2026 are not in effect (i.e., a government shutdown).</p><p>Specifically, the bill provides FY2026 continuing appropriations for the pay and allowances of (1) members of the Armed Forces, including reserve components, who perform active service during the period; and (2) civilian personnel and contractors of the Department of Defense (and the Department of Homeland Security in the case of the Coast Guard) who are providing support to such members of the Armed Forces.</p><p>If a government shutdown occurs, the bill provides the continuing appropriations until the earlier of (1) the enactment into law of specified appropriations legislation, or (2) January 1, 2027.\u00a0</p>"
        },
        "title": "Pay Our Military Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s3002.xml",
    "summary": {
      "actionDate": "2025-10-09",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Pay Our Military Act of 2025</strong></p><p>This bill provides continuing appropriations for military pay for any period during which interim or full-year appropriations for FY2026 are not in effect (i.e., a government shutdown).</p><p>Specifically, the bill provides FY2026 continuing appropriations for the pay and allowances of (1) members of the Armed Forces, including reserve components, who perform active service during the period; and (2) civilian personnel and contractors of the Department of Defense (and the Department of Homeland Security in the case of the Coast Guard) who are providing support to such members of the Armed Forces.</p><p>If a government shutdown occurs, the bill provides the continuing appropriations until the earlier of (1) the enactment into law of specified appropriations legislation, or (2) January 1, 2027.\u00a0</p>",
      "updateDate": "2025-10-14",
      "versionCode": "id119s3002"
    },
    "title": "Pay Our Military Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-10-09",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Pay Our Military Act of 2025</strong></p><p>This bill provides continuing appropriations for military pay for any period during which interim or full-year appropriations for FY2026 are not in effect (i.e., a government shutdown).</p><p>Specifically, the bill provides FY2026 continuing appropriations for the pay and allowances of (1) members of the Armed Forces, including reserve components, who perform active service during the period; and (2) civilian personnel and contractors of the Department of Defense (and the Department of Homeland Security in the case of the Coast Guard) who are providing support to such members of the Armed Forces.</p><p>If a government shutdown occurs, the bill provides the continuing appropriations until the earlier of (1) the enactment into law of specified appropriations legislation, or (2) January 1, 2027.\u00a0</p>",
      "updateDate": "2025-10-14",
      "versionCode": "id119s3002"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-10-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3002is.xml"
        }
      ],
      "type": "Introduced in Senate"
    },
    {
      "date": "2025-10-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3002rcs.xml"
        }
      ],
      "type": "Reference Change Senate"
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
      "updateDate": "2025-10-31T11:03:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Pay Our Military Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-11T02:38:12Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill making continuing appropriations for military pay in the event of a Government shutdown.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-11T02:33:16Z"
    }
  ]
}
```
