# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/25?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hres/25
- Title: Expunging the January 13, 2021, impeachment of President Donald John Trump.
- Congress: 119
- Bill type: HRES
- Bill number: 25
- Origin chamber: House
- Introduced date: 2025-01-09
- Update date: 2025-04-09T08:06:39Z
- Update date including text: 2025-04-09T08:06:39Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-09: Introduced in House
- 2025-01-09 - IntroReferral: Referred to the House Committee on the Judiciary.
- 2025-01-09 - Committee: Submitted in House
- 2025-01-09 - IntroReferral: Submitted in House
- Latest action: 2025-01-09: Submitted in House

## Actions

- 2025-01-09 - IntroReferral: Referred to the House Committee on the Judiciary.
- 2025-01-09 - Committee: Submitted in House
- 2025-01-09 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-09",
    "latestAction": {
      "actionDate": "2025-01-09",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hres/25",
    "number": "25",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "G000596",
        "district": "14",
        "firstName": "Marjorie",
        "fullName": "Rep. Greene, Marjorie Taylor [R-GA-14]",
        "lastName": "Greene",
        "party": "R",
        "state": "GA"
      }
    ],
    "title": "Expunging the January 13, 2021, impeachment of President Donald John Trump.",
    "type": "HRES",
    "updateDate": "2025-04-09T08:06:39Z",
    "updateDateIncludingText": "2025-04-09T08:06:39Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-09",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H12100",
      "actionDate": "2025-01-09",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "Committee"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-01-09",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
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
          "date": "2025-01-09T14:39:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
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
      "bioguideId": "M001211",
      "district": "15",
      "firstName": "Mary",
      "fullName": "Rep. Miller, Mary E. [R-IL-15]",
      "isOriginalCosponsor": "True",
      "lastName": "Miller",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-01-09",
      "state": "IL"
    },
    {
      "bioguideId": "W000814",
      "district": "14",
      "firstName": "Randy",
      "fullName": "Rep. Weber, Randy K. Sr. [R-TX-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Weber",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-01-09",
      "state": "TX"
    },
    {
      "bioguideId": "C001129",
      "district": "10",
      "firstName": "Mike",
      "fullName": "Rep. Collins, Mike [R-GA-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Collins",
      "party": "R",
      "sponsorshipDate": "2025-01-09",
      "state": "GA"
    },
    {
      "bioguideId": "C001132",
      "district": "2",
      "firstName": "Elijah",
      "fullName": "Rep. Crane, Elijah [R-AZ-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Crane",
      "party": "R",
      "sponsorshipDate": "2025-01-09",
      "state": "AZ"
    },
    {
      "bioguideId": "M000317",
      "district": "11",
      "firstName": "Nicole",
      "fullName": "Rep. Malliotakis, Nicole [R-NY-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Malliotakis",
      "party": "R",
      "sponsorshipDate": "2025-01-09",
      "state": "NY"
    },
    {
      "bioguideId": "M001219",
      "district": "0",
      "firstName": "James",
      "fullName": "Del. Moylan, James C. [R-GU]",
      "isOriginalCosponsor": "True",
      "lastName": "Moylan",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2025-01-09",
      "state": "GU"
    },
    {
      "bioguideId": "N000026",
      "district": "22",
      "firstName": "Troy",
      "fullName": "Rep. Nehls, Troy E. [R-TX-22]",
      "isOriginalCosponsor": "True",
      "lastName": "Nehls",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-01-09",
      "state": "TX"
    },
    {
      "bioguideId": "L000596",
      "district": "13",
      "firstName": "Anna Paulina",
      "fullName": "Rep. Luna, Anna Paulina [R-FL-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Luna",
      "party": "R",
      "sponsorshipDate": "2025-01-09",
      "state": "FL"
    },
    {
      "bioguideId": "V000133",
      "district": "2",
      "firstName": "Jefferson",
      "fullName": "Rep. Van Drew, Jefferson [R-NJ-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Drew",
      "party": "R",
      "sponsorshipDate": "2025-01-09",
      "state": "NJ"
    },
    {
      "bioguideId": "H001086",
      "district": "1",
      "firstName": "Diana",
      "fullName": "Rep. Harshbarger, Diana [R-TN-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Harshbarger",
      "party": "R",
      "sponsorshipDate": "2025-01-22",
      "state": "TN"
    },
    {
      "bioguideId": "S001196",
      "district": "21",
      "firstName": "Elise",
      "fullName": "Rep. Stefanik, Elise M. [R-NY-21]",
      "isOriginalCosponsor": "False",
      "lastName": "Stefanik",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-04-08",
      "state": "NY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres25ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 25\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 9, 2025 Ms. Greene of Georgia (for herself, Mrs. Miller of Illinois , Mr. Weber of Texas , Mr. Collins , Mr. Crane , Ms. Malliotakis , Mr. Moylan , Mr. Nehls , Mrs. Luna , and Mr. Van Drew ) submitted the following resolution; which was referred to the Committee on the Judiciary\nRESOLUTION\nExpunging the January 13, 2021, impeachment of President Donald John Trump.\nThat the January 13, 2021, impeachment of President Donald John Trump is expunged, as if such article had never passed the full House of Representatives, as the facts and circumstances upon which such article was based met the burden of proving neither that President Trump committed high Crimes and Misdemeanors , as set forth in section 4 of article II of the Constitution, nor that President Trump engaged in insurrection or rebellion against the United States , such that he is forever precluded from hold[ing] any office \u2026 under the United States pursuant to section 3 of the 14th Amendment to the Constitution.",
      "versionDate": "2025-01-09",
      "versionType": "IH"
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
            "name": "Civil disturbances",
            "updateDate": "2025-01-22T15:35:27Z"
          },
          {
            "name": "Congressional-executive branch relations",
            "updateDate": "2025-01-22T15:35:27Z"
          },
          {
            "name": "Government buildings, facilities, and property",
            "updateDate": "2025-01-22T15:35:27Z"
          },
          {
            "name": "Government ethics and transparency, public corruption",
            "updateDate": "2025-01-22T15:35:27Z"
          },
          {
            "name": "House of Representatives",
            "updateDate": "2025-01-22T15:35:27Z"
          },
          {
            "name": "Legislative rules and procedure",
            "updateDate": "2025-01-22T15:35:27Z"
          },
          {
            "name": "Presidents and presidential powers, Vice Presidents",
            "updateDate": "2025-01-22T15:35:27Z"
          },
          {
            "name": "Protest and dissent",
            "updateDate": "2025-01-22T15:35:27Z"
          },
          {
            "name": "Subversive activities",
            "updateDate": "2025-01-22T15:35:27Z"
          },
          {
            "name": "U.S. Capitol",
            "updateDate": "2025-01-22T15:35:27Z"
          }
        ]
      },
      "policyArea": {
        "name": "Government Operations and Politics",
        "updateDate": "2025-01-16T16:48:15Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-09",
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
          "measure-id": "id119hres25",
          "measure-number": "25",
          "measure-type": "hres",
          "orig-publish-date": "2025-01-09",
          "originChamber": "HOUSE",
          "update-date": "2025-02-03"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hres25v00",
            "update-date": "2025-02-03"
          },
          "action-date": "2025-01-09",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This resolution expunges the January 13, 2021, impeachment of President Trump.</p>"
        },
        "title": "Expunging the January 13, 2021, impeachment of President Donald John Trump."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hres/BILLSUM-119hres25.xml",
    "summary": {
      "actionDate": "2025-01-09",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution expunges the January 13, 2021, impeachment of President Trump.</p>",
      "updateDate": "2025-02-03",
      "versionCode": "id119hres25"
    },
    "title": "Expunging the January 13, 2021, impeachment of President Donald John Trump."
  },
  "summaries": [
    {
      "actionDate": "2025-01-09",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution expunges the January 13, 2021, impeachment of President Trump.</p>",
      "updateDate": "2025-02-03",
      "versionCode": "id119hres25"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres25ih.xml"
        }
      ],
      "type": "IH"
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
      "title": "Expunging the January 13, 2021, impeachment of President Donald John Trump.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-01-10T09:18:18Z"
    },
    {
      "title": "Expunging the January 13, 2021, impeachment of President Donald John Trump.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-01-10T09:05:59Z"
    }
  ]
}
```
