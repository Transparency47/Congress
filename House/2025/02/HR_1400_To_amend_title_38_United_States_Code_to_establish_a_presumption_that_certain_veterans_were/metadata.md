# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1400?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1400
- Title: To amend title 38, United States Code, to establish a presumption that certain veterans were exposed to radiation and other toxins at the Nevada Test and Training Range for purposes of the treatment of certain disabilities under the laws administered by the Secretary of Veterans Affairs, and for other purposes.
- Congress: 119
- Bill type: HR
- Bill number: 1400
- Origin chamber: House
- Introduced date: 2025-02-18
- Update date: 2026-03-13T08:05:23Z
- Update date including text: 2026-03-13T08:05:23Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-18: Introduced in House
- 2025-02-18 - IntroReferral: Introduced in House
- 2025-02-18 - IntroReferral: Introduced in House
- 2025-02-18 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-03-21 - Committee: Referred to the Subcommittee on Disability Assistance and Memorial Affairs.
- Latest action: 2025-02-18: Introduced in House

## Actions

- 2025-02-18 - IntroReferral: Introduced in House
- 2025-02-18 - IntroReferral: Introduced in House
- 2025-02-18 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-03-21 - Committee: Referred to the Subcommittee on Disability Assistance and Memorial Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-18",
    "latestAction": {
      "actionDate": "2025-02-18",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1400",
    "number": "1400",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "A000369",
        "district": "2",
        "firstName": "Mark",
        "fullName": "Rep. Amodei, Mark E. [R-NV-2]",
        "lastName": "Amodei",
        "party": "R",
        "state": "NV"
      }
    ],
    "title": "To amend title 38, United States Code, to establish a presumption that certain veterans were exposed to radiation and other toxins at the Nevada Test and Training Range for purposes of the treatment of certain disabilities under the laws administered by the Secretary of Veterans Affairs, and for other purposes.",
    "type": "HR",
    "updateDate": "2026-03-13T08:05:23Z",
    "updateDateIncludingText": "2026-03-13T08:05:23Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-21",
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
      "actionDate": "2025-02-18",
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
      "actionDate": "2025-02-18",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-18",
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
          "date": "2025-02-18T18:00:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-03-21T17:55:47Z",
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
      "bioguideId": "L000590",
      "district": "3",
      "firstName": "Susie",
      "fullName": "Rep. Lee, Susie [D-NV-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Lee",
      "party": "D",
      "sponsorshipDate": "2025-02-18",
      "state": "NV"
    },
    {
      "bioguideId": "S000250",
      "district": "17",
      "firstName": "Pete",
      "fullName": "Rep. Sessions, Pete [R-TX-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Sessions",
      "party": "R",
      "sponsorshipDate": "2025-02-21",
      "state": "TX"
    },
    {
      "bioguideId": "F000110",
      "district": "6",
      "firstName": "CLEO",
      "fullName": "Rep. Fields, Cleo [D-LA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "FIELDS",
      "party": "D",
      "sponsorshipDate": "2025-03-27",
      "state": "LA"
    },
    {
      "bioguideId": "T000468",
      "district": "1",
      "firstName": "Dina",
      "fullName": "Rep. Titus, Dina [D-NV-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Titus",
      "party": "D",
      "sponsorshipDate": "2025-03-31",
      "state": "NV"
    },
    {
      "bioguideId": "B001315",
      "district": "13",
      "firstName": "Nikki",
      "fullName": "Rep. Budzinski, Nikki [D-IL-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Budzinski",
      "party": "D",
      "sponsorshipDate": "2025-04-07",
      "state": "IL"
    },
    {
      "bioguideId": "H001066",
      "district": "4",
      "firstName": "Steven",
      "fullName": "Rep. Horsford, Steven [D-NV-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Horsford",
      "party": "D",
      "sponsorshipDate": "2025-04-14",
      "state": "NV"
    },
    {
      "bioguideId": "G000600",
      "district": "3",
      "firstName": "Marie",
      "fullName": "Rep. Perez, Marie Gluesenkamp [D-WA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Perez",
      "middleName": "Gluesenkamp",
      "party": "D",
      "sponsorshipDate": "2025-05-06",
      "state": "WA"
    },
    {
      "bioguideId": "K000402",
      "district": "26",
      "firstName": "Timothy",
      "fullName": "Rep. Kennedy, Timothy M. [D-NY-26]",
      "isOriginalCosponsor": "False",
      "lastName": "Kennedy",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-05-19",
      "state": "NY"
    },
    {
      "bioguideId": "V000138",
      "district": "7",
      "firstName": "Eugene",
      "fullName": "Rep. Vindman, Eugene Simon [D-VA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Vindman",
      "middleName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-10-17",
      "state": "VA"
    },
    {
      "bioguideId": "R000603",
      "district": "7",
      "firstName": "David",
      "fullName": "Rep. Rouzer, David [R-NC-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Rouzer",
      "party": "R",
      "sponsorshipDate": "2026-01-12",
      "state": "NC"
    },
    {
      "bioguideId": "V000133",
      "district": "2",
      "firstName": "Jefferson",
      "fullName": "Rep. Van Drew, Jefferson [R-NJ-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Drew",
      "party": "R",
      "sponsorshipDate": "2026-03-12",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1400ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1400\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 18, 2025 Mr. Amodei of Nevada (for himself and Ms. Lee of Nevada ) introduced the following bill; which was referred to the Committee on Veterans' Affairs\nA BILL\nTo amend title 38, United States Code, to establish a presumption that certain veterans were exposed to radiation and other toxins at the Nevada Test and Training Range for purposes of the treatment of certain disabilities under the laws administered by the Secretary of Veterans Affairs, and for other purposes.\n#### 1. Treatment as radiation-risk activities\nSection 1112(c)(3) of title 38, United States Code, is amended\u2014\n**(1)**\nin subparagraph (B) by adding at the end the following new clause:\n(viii) At any time on or after January 1, 1972, and before January 1, 2005, onsite participation in any aspect of the development, construction, operation, or maintenance of a military installation (as defined in section 2801 of title 10) at a covered location at the Nevada Test and Training Range. ; and\n**(2)**\nby adding at the end the following new subparagraph:\n(C) The term covered location at the Nevada Test and Training Range means a location at the Nevada Test and Training Range, Nevada, including a location at Indian Springs Auxiliary Airfield, but not including a location Nellis Air Force Base or Creech Air Force Base. .\n#### 2. Presumptions of toxic exposure\nSection 1119(c) of such title is amended\u2014\n**(1)**\nin paragraph (1)\u2014\n**(A)**\nby redesignating subparagraphs (A) and (B) as subparagraphs (B) and (C), respectively; and\n**(B)**\nby inserting before subsection (B), as so redesignated, the following:\n(A) on or after January 1, 1972, and before January 1, 2005, performed active military, naval, air, or space service while assigned to a duty station in, including airspace above, a covered location at the Nevada Test and Training Range, Nevada; ; and\n**(2)**\nby adding at the end the following new paragraph:\n(4) The term covered location at the Nevada Test and Training Range means a location at the Nevada Test and Training Range, Nevada, including a location at Indian Springs Auxiliary Airfield, but not including a location Nellis Air Force Base or Creech Air Force Base. .\n#### 3. Presumption of service connection\nSection 1120(b) of such title is amended\u2014\n**(1)**\nby redesignating paragraph (15) as paragraph (16); and\n**(2)**\nby inserting after paragraph (14) the following new paragraph:\n(15) Only in the case of a covered veteran described in section 1119(c)(1)(A), lipomas and tumor related conditions. .",
      "versionDate": "2025-02-18",
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
            "name": "Nevada",
            "updateDate": "2025-07-09T13:59:14Z"
          },
          {
            "name": "Radiation",
            "updateDate": "2025-07-09T13:59:18Z"
          },
          {
            "name": "Radioactive wastes and releases",
            "updateDate": "2025-07-09T13:59:21Z"
          },
          {
            "name": "Veterans' pensions and compensation",
            "updateDate": "2025-07-09T13:59:09Z"
          }
        ]
      },
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2025-03-20T16:50:32Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-18",
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
          "measure-id": "id119hr1400",
          "measure-number": "1400",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-18",
          "originChamber": "HOUSE",
          "update-date": "2026-03-04"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1400v00",
            "update-date": "2026-03-04"
          },
          "action-date": "2025-02-18",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This bill establishes eligibility for certain disability compensation and benefits for individuals who served at the Nevada Test and Training Range (NTTR).</p><p>The bill establishes that onsite participation on or after January 1, 1972, and before January 1, 2005, at certain\u00a0NTTR locations where there was a potential of toxic exposure is a radiation-risk activity, therefore providing a presumption of service-connection for specified conditions. The bill specifies the covered NTTR locations include a location at Indian Springs Auxiliary Airfield but do not include a location at Nellis Air Force Base or Creech Air Force Base.</p><p>The bill also establishes a presumption of toxic exposure for veterans who performed active service at such NTTR locations, including airspace above such locations. Additionally,\u00a0lipomas and tumor related conditions must be considered as service-connected conditions for veterans who served at the NTTR locations.</p>"
        },
        "title": "To amend title 38, United States Code, to establish a presumption that certain veterans were exposed to radiation and other toxins at the Nevada Test and Training Range for purposes of the treatment of certain disabilities under the laws administered by the Secretary of Veterans Affairs, and for other purposes."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1400.xml",
    "summary": {
      "actionDate": "2025-02-18",
      "actionDesc": "Introduced in House",
      "text": "<p>This bill establishes eligibility for certain disability compensation and benefits for individuals who served at the Nevada Test and Training Range (NTTR).</p><p>The bill establishes that onsite participation on or after January 1, 1972, and before January 1, 2005, at certain\u00a0NTTR locations where there was a potential of toxic exposure is a radiation-risk activity, therefore providing a presumption of service-connection for specified conditions. The bill specifies the covered NTTR locations include a location at Indian Springs Auxiliary Airfield but do not include a location at Nellis Air Force Base or Creech Air Force Base.</p><p>The bill also establishes a presumption of toxic exposure for veterans who performed active service at such NTTR locations, including airspace above such locations. Additionally,\u00a0lipomas and tumor related conditions must be considered as service-connected conditions for veterans who served at the NTTR locations.</p>",
      "updateDate": "2026-03-04",
      "versionCode": "id119hr1400"
    },
    "title": "To amend title 38, United States Code, to establish a presumption that certain veterans were exposed to radiation and other toxins at the Nevada Test and Training Range for purposes of the treatment of certain disabilities under the laws administered by the Secretary of Veterans Affairs, and for other purposes."
  },
  "summaries": [
    {
      "actionDate": "2025-02-18",
      "actionDesc": "Introduced in House",
      "text": "<p>This bill establishes eligibility for certain disability compensation and benefits for individuals who served at the Nevada Test and Training Range (NTTR).</p><p>The bill establishes that onsite participation on or after January 1, 1972, and before January 1, 2005, at certain\u00a0NTTR locations where there was a potential of toxic exposure is a radiation-risk activity, therefore providing a presumption of service-connection for specified conditions. The bill specifies the covered NTTR locations include a location at Indian Springs Auxiliary Airfield but do not include a location at Nellis Air Force Base or Creech Air Force Base.</p><p>The bill also establishes a presumption of toxic exposure for veterans who performed active service at such NTTR locations, including airspace above such locations. Additionally,\u00a0lipomas and tumor related conditions must be considered as service-connected conditions for veterans who served at the NTTR locations.</p>",
      "updateDate": "2026-03-04",
      "versionCode": "id119hr1400"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1400ih.xml"
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
      "title": "To amend title 38, United States Code, to establish a presumption that certain veterans were exposed to radiation and other toxins at the Nevada Test and Training Range for purposes of the treatment of certain disabilities under the laws administered by the Secretary of Veterans Affairs, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-19T03:03:25Z"
    },
    {
      "title": "To amend title 38, United States Code, to establish a presumption that certain veterans were exposed to radiation and other toxins at the Nevada Test and Training Range for purposes of the treatment of certain disabilities under the laws administered by the Secretary of Veterans Affairs, and for other purposes.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-19T09:05:28Z"
    }
  ]
}
```
