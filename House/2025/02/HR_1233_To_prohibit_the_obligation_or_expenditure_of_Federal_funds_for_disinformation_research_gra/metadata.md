# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1233?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/1233
- Title: To prohibit the obligation or expenditure of Federal funds for disinformation research grants, and for other purposes.
- Congress: 119
- Bill type: HR
- Bill number: 1233
- Origin chamber: House
- Introduced date: 2025-02-12
- Update date: 2025-07-28T20:42:08Z
- Update date including text: 2025-07-28T20:42:08Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-12: Introduced in House
- 2025-02-12 - IntroReferral: Introduced in House
- 2025-02-12 - IntroReferral: Introduced in House
- 2025-02-12 - IntroReferral: Referred to the House Committee on Science, Space, and Technology.
- Latest action: 2025-02-12: Introduced in House

## Actions

- 2025-02-12 - IntroReferral: Introduced in House
- 2025-02-12 - IntroReferral: Introduced in House
- 2025-02-12 - IntroReferral: Referred to the House Committee on Science, Space, and Technology.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-12",
    "latestAction": {
      "actionDate": "2025-02-12",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/1233",
    "number": "1233",
    "originChamber": "House",
    "policyArea": {
      "name": "Science, Technology, Communications"
    },
    "sponsors": [
      {
        "bioguideId": "M001184",
        "district": "4",
        "firstName": "Thomas",
        "fullName": "Rep. Massie, Thomas [R-KY-4]",
        "lastName": "Massie",
        "party": "R",
        "state": "KY"
      }
    ],
    "title": "To prohibit the obligation or expenditure of Federal funds for disinformation research grants, and for other purposes.",
    "type": "HR",
    "updateDate": "2025-07-28T20:42:08Z",
    "updateDateIncludingText": "2025-07-28T20:42:08Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-12",
      "committees": {
        "item": {
          "name": "Science, Space, and Technology Committee",
          "systemCode": "hssy00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Science, Space, and Technology.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-02-12",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-12",
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
          "date": "2025-02-12T15:07:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Science, Space, and Technology Committee",
      "systemCode": "hssy00",
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
      "bioguideId": "B001302",
      "district": "5",
      "firstName": "Andy",
      "fullName": "Rep. Biggs, Andy [R-AZ-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Biggs",
      "party": "R",
      "sponsorshipDate": "2025-02-12",
      "state": "AZ"
    },
    {
      "bioguideId": "B000825",
      "district": "4",
      "firstName": "Lauren",
      "fullName": "Rep. Boebert, Lauren [R-CO-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Boebert",
      "party": "R",
      "sponsorshipDate": "2025-02-12",
      "state": "CO"
    },
    {
      "bioguideId": "B001316",
      "district": "7",
      "firstName": "Eric",
      "fullName": "Rep. Burlison, Eric [R-MO-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Burlison",
      "party": "R",
      "sponsorshipDate": "2025-02-12",
      "state": "MO"
    },
    {
      "bioguideId": "D000626",
      "district": "8",
      "firstName": "Warren",
      "fullName": "Rep. Davidson, Warren [R-OH-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Davidson",
      "party": "R",
      "sponsorshipDate": "2025-02-12",
      "state": "OH"
    },
    {
      "bioguideId": "G000565",
      "district": "9",
      "firstName": "Paul",
      "fullName": "Rep. Gosar, Paul A. [R-AZ-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Gosar",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-02-12",
      "state": "AZ"
    },
    {
      "bioguideId": "G000596",
      "district": "14",
      "firstName": "Marjorie",
      "fullName": "Rep. Greene, Marjorie Taylor [R-GA-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Greene",
      "middleName": "Taylor",
      "party": "R",
      "sponsorshipDate": "2025-02-12",
      "state": "GA"
    },
    {
      "bioguideId": "O000175",
      "district": "5",
      "firstName": "Andrew",
      "fullName": "Rep. Ogles, Andrew [R-TN-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Ogles",
      "party": "R",
      "sponsorshipDate": "2025-02-12",
      "state": "TN"
    },
    {
      "bioguideId": "P000605",
      "district": "10",
      "firstName": "Scott",
      "fullName": "Rep. Perry, Scott [R-PA-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Perry",
      "party": "R",
      "sponsorshipDate": "2025-02-12",
      "state": "PA"
    },
    {
      "bioguideId": "R000614",
      "district": "21",
      "firstName": "Chip",
      "fullName": "Rep. Roy, Chip [R-TX-21]",
      "isOriginalCosponsor": "True",
      "lastName": "Roy",
      "party": "R",
      "sponsorshipDate": "2025-02-12",
      "state": "TX"
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
      "sponsorshipDate": "2025-02-12",
      "state": "TX"
    },
    {
      "bioguideId": "M001177",
      "district": "5",
      "firstName": "Tom",
      "fullName": "Rep. McClintock, Tom [R-CA-5]",
      "isOriginalCosponsor": "False",
      "lastName": "McClintock",
      "party": "R",
      "sponsorshipDate": "2025-02-13",
      "state": "CA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1233ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1233\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 12, 2025 Mr. Massie (for himself, Mr. Biggs of Arizona , Ms. Boebert , Mr. Burlison , Mr. Davidson , Mr. Gosar , Ms. Greene of Georgia , Mr. Ogles , Mr. Perry , Mr. Roy , and Mr. Weber of Texas ) introduced the following bill; which was referred to the Committee on Science, Space, and Technology\nA BILL\nTo prohibit the obligation or expenditure of Federal funds for disinformation research grants, and for other purposes.\n#### 1. Prohibition\nNo Federal funds may be obligated or expended by any Federal department or agency for the following:\n**(1)**\nDisinformation research grants.\n**(2)**\nSecure and Trustworthy Cyberspace grants.\n**(3)**\nPrograms within the National Science Foundation\u2019s Track F: Trust and Authenticity in Communications Systems.",
      "versionDate": "2025-02-12",
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
        "name": "Science, Technology, Communications",
        "updateDate": "2025-03-13T12:28:45Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-12",
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
          "measure-id": "id119hr1233",
          "measure-number": "1233",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-12",
          "originChamber": "HOUSE",
          "update-date": "2025-07-28"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1233v00",
            "update-date": "2025-07-28"
          },
          "action-date": "2025-02-12",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This bill prohibits federal funding for (1) disinformation research grants, (2) the National Science Foundation (NSF) Secure and Trustworthy Cyberspace grant program, and (3) programs within the NSF Convergence Accelerator grant program\u2019s Track F: Trust and Authenticity in Communications Systems. \u00a0</p><p>The Secure and Trustworthy Cyberspace grant program provides grants to support research and education on various topics in cybersecurity and privacy, including cryptography, hardware security, and information integrity. The Convergence Accelerator\u2019s Track F projects focused on tools and techniques to prevent, mitigate, and adapt to the unanticipated negative effects of, and potential manipulation of, communications systems (e.g., misinformation).</p>"
        },
        "title": "To prohibit the obligation or expenditure of Federal funds for disinformation research grants, and for other purposes."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1233.xml",
    "summary": {
      "actionDate": "2025-02-12",
      "actionDesc": "Introduced in House",
      "text": "<p>This bill prohibits federal funding for (1) disinformation research grants, (2) the National Science Foundation (NSF) Secure and Trustworthy Cyberspace grant program, and (3) programs within the NSF Convergence Accelerator grant program\u2019s Track F: Trust and Authenticity in Communications Systems. \u00a0</p><p>The Secure and Trustworthy Cyberspace grant program provides grants to support research and education on various topics in cybersecurity and privacy, including cryptography, hardware security, and information integrity. The Convergence Accelerator\u2019s Track F projects focused on tools and techniques to prevent, mitigate, and adapt to the unanticipated negative effects of, and potential manipulation of, communications systems (e.g., misinformation).</p>",
      "updateDate": "2025-07-28",
      "versionCode": "id119hr1233"
    },
    "title": "To prohibit the obligation or expenditure of Federal funds for disinformation research grants, and for other purposes."
  },
  "summaries": [
    {
      "actionDate": "2025-02-12",
      "actionDesc": "Introduced in House",
      "text": "<p>This bill prohibits federal funding for (1) disinformation research grants, (2) the National Science Foundation (NSF) Secure and Trustworthy Cyberspace grant program, and (3) programs within the NSF Convergence Accelerator grant program\u2019s Track F: Trust and Authenticity in Communications Systems. \u00a0</p><p>The Secure and Trustworthy Cyberspace grant program provides grants to support research and education on various topics in cybersecurity and privacy, including cryptography, hardware security, and information integrity. The Convergence Accelerator\u2019s Track F projects focused on tools and techniques to prevent, mitigate, and adapt to the unanticipated negative effects of, and potential manipulation of, communications systems (e.g., misinformation).</p>",
      "updateDate": "2025-07-28",
      "versionCode": "id119hr1233"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1233ih.xml"
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
      "title": "To prohibit the obligation or expenditure of Federal funds for disinformation research grants, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-12T11:18:27Z"
    },
    {
      "title": "To prohibit the obligation or expenditure of Federal funds for disinformation research grants, and for other purposes.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-13T09:06:21Z"
    }
  ]
}
```
