# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/75?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/sres/75
- Title: A resolution expressing the sense of the Senate that member countries of NATO must commit at least 2 percent of their national gross domestic product to national defense spending to hold leadership or benefit at the expense of those countries who meet their obligations.
- Congress: 119
- Bill type: SRES
- Bill number: 75
- Origin chamber: Senate
- Introduced date: 2025-02-12
- Update date: 2025-07-18T10:56:29Z
- Update date including text: 2025-07-18T10:56:29Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-12: Introduced in Senate
- 2025-02-12 - IntroReferral: Introduced in Senate
- 2025-02-12 - IntroReferral: Referred to the Committee on Foreign Relations. (text: CR S931)
- Latest action: 2025-02-12: Introduced in Senate

## Actions

- 2025-02-12 - IntroReferral: Introduced in Senate
- 2025-02-12 - IntroReferral: Referred to the Committee on Foreign Relations. (text: CR S931)

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
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/sres/75",
    "number": "75",
    "originChamber": "Senate",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "T000476",
        "district": "",
        "firstName": "Thomas",
        "fullName": "Sen. Tillis, Thomas [R-NC]",
        "lastName": "Tillis",
        "party": "R",
        "state": "NC"
      }
    ],
    "title": "A resolution expressing the sense of the Senate that member countries of NATO must commit at least 2 percent of their national gross domestic product to national defense spending to hold leadership or benefit at the expense of those countries who meet their obligations.",
    "type": "SRES",
    "updateDate": "2025-07-18T10:56:29Z",
    "updateDateIncludingText": "2025-07-18T10:56:29Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-12",
      "committees": {
        "item": {
          "name": "Foreign Relations Committee",
          "systemCode": "ssfr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Referred to the Committee on Foreign Relations. (text: CR S931)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-02-12",
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
          "date": "2025-02-12T15:34:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Foreign Relations Committee",
      "systemCode": "ssfr00",
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
      "bioguideId": "J000312",
      "firstName": "James",
      "fullName": "Sen. Justice, James C. [R-WV]",
      "isOriginalCosponsor": "True",
      "lastName": "Justice",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2025-02-12",
      "state": "WV"
    },
    {
      "bioguideId": "C001056",
      "firstName": "John",
      "fullName": "Sen. Cornyn, John [R-TX]",
      "isOriginalCosponsor": "True",
      "lastName": "Cornyn",
      "party": "R",
      "sponsorshipDate": "2025-02-12",
      "state": "TX"
    },
    {
      "bioguideId": "S001232",
      "firstName": "Tim",
      "fullName": "Sen. Sheehy, Tim [R-MT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sheehy",
      "party": "R",
      "sponsorshipDate": "2025-02-12",
      "state": "MT"
    },
    {
      "bioguideId": "L000577",
      "firstName": "Mike",
      "fullName": "Sen. Lee, Mike [R-UT]",
      "isOriginalCosponsor": "True",
      "lastName": "Lee",
      "party": "R",
      "sponsorshipDate": "2025-02-12",
      "state": "UT"
    },
    {
      "bioguideId": "D000618",
      "firstName": "Steve",
      "fullName": "Sen. Daines, Steve [R-MT]",
      "isOriginalCosponsor": "True",
      "lastName": "Daines",
      "party": "R",
      "sponsorshipDate": "2025-02-12",
      "state": "MT"
    },
    {
      "bioguideId": "C001047",
      "firstName": "Shelley",
      "fullName": "Sen. Capito, Shelley Moore [R-WV]",
      "isOriginalCosponsor": "True",
      "lastName": "Capito",
      "middleName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-02-12",
      "state": "WV"
    },
    {
      "bioguideId": "G000359",
      "firstName": "Lindsey",
      "fullName": "Sen. Graham, Lindsey [R-SC]",
      "isOriginalCosponsor": "False",
      "lastName": "Graham",
      "party": "R",
      "sponsorshipDate": "2025-02-19",
      "state": "SC"
    },
    {
      "bioguideId": "B001236",
      "firstName": "John",
      "fullName": "Sen. Boozman, John [R-AR]",
      "isOriginalCosponsor": "False",
      "lastName": "Boozman",
      "party": "R",
      "sponsorshipDate": "2025-07-17",
      "state": "AR"
    },
    {
      "bioguideId": "M001243",
      "firstName": "David",
      "fullName": "Sen. McCormick, David [R-PA]",
      "isOriginalCosponsor": "False",
      "lastName": "McCormick",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2025-07-17",
      "state": "PA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres75is.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 75\nIN THE SENATE OF THE UNITED STATES\nFebruary 12, 2025 Mr. Tillis (for himself, Mr. Justice , Mr. Cornyn , Mr. Sheehy , Mr. Lee , Mr. Daines , and Mrs. Capito ) submitted the following resolution; which was referred to the Committee on Foreign Relations\nRESOLUTION\nExpressing the sense of the Senate that member countries of NATO must commit at least 2 percent of their national gross domestic product to national defense spending to hold leadership or benefit at the expense of those counties who meet their obligations.\nThat it is the sense of the Senate that\u2014\n**(1)**\nany citizen of a member country of the North Atlantic Treaty Organization (commonly known as NATO ) that is not meeting its commitment to spend 2 percent of its gross domestic product (referred to in this resolution as GDP ) on national defense should not be allowed to hold any position within the leadership of NATO, including positions such as\u2014\n**(A)**\nthe Secretary General of NATO;\n**(B)**\nthe Deputy Secretary General of NATO;\n**(C)**\nany Assistant Secretaries General of NATO;\n**(D)**\nthe NATO Spokesperson; and\n**(E)**\nany uniformed military leadership or command positions within the structure of NATO at the 2-star (OF\u20137) level or above; and\n**(2)**\nany member country of NATO that fails to meet its commitment to spend 2 percent of its GDP on national defense should not be allowed to host any significant formal or informal meetings, conferences, or summits of NATO at the ministerial level or above, outside established routine corporate processes of NATO that direct military operations or coordination at a headquarters location, that would provide substantial economic benefit to the economy and enable the ability for that member country to receive international recognition, including\u2014\n**(A)**\nthe NATO Summit;\n**(B)**\nmeetings of NATO Ministers of Foreign Affairs;\n**(C)**\nNATO Parliamentary Assembly sessions; and\n**(D)**\nthe NATO Youth Summit or similar events.",
      "versionDate": "2025-02-12",
      "versionType": "IS"
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
        "name": "International Affairs",
        "updateDate": "2025-02-20T14:53:05Z"
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
          "measure-id": "id119sres75",
          "measure-number": "75",
          "measure-type": "sres",
          "orig-publish-date": "2025-02-12",
          "originChamber": "SENATE",
          "update-date": "2025-04-08"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119sres75v00",
            "update-date": "2025-04-08"
          },
          "action-date": "2025-02-12",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p>This resolution expresses the sense of the Senate that any NATO member country that does not meet its commitment to spend 2% of its gross domestic product on national defense should not be allowed to host certain NATO meetings that provide substantial economic benefits and international recognition, such as the NATO Summit and NATO Parliamentary Assembly sessions. The resolution also expresses that citizens of such countries should not be allowed to hold NATO leadership positions, such as Secretary General or military positions at the two-star level or above.</p>"
        },
        "title": "A resolution expressing the sense of the Senate that member countries of NATO must commit at least 2 percent of their national gross domestic product to national defense spending to hold leadership or benefit at the expense of those countries who meet their obligations."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/sres/BILLSUM-119sres75.xml",
    "summary": {
      "actionDate": "2025-02-12",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This resolution expresses the sense of the Senate that any NATO member country that does not meet its commitment to spend 2% of its gross domestic product on national defense should not be allowed to host certain NATO meetings that provide substantial economic benefits and international recognition, such as the NATO Summit and NATO Parliamentary Assembly sessions. The resolution also expresses that citizens of such countries should not be allowed to hold NATO leadership positions, such as Secretary General or military positions at the two-star level or above.</p>",
      "updateDate": "2025-04-08",
      "versionCode": "id119sres75"
    },
    "title": "A resolution expressing the sense of the Senate that member countries of NATO must commit at least 2 percent of their national gross domestic product to national defense spending to hold leadership or benefit at the expense of those countries who meet their obligations."
  },
  "summaries": [
    {
      "actionDate": "2025-02-12",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This resolution expresses the sense of the Senate that any NATO member country that does not meet its commitment to spend 2% of its gross domestic product on national defense should not be allowed to host certain NATO meetings that provide substantial economic benefits and international recognition, such as the NATO Summit and NATO Parliamentary Assembly sessions. The resolution also expresses that citizens of such countries should not be allowed to hold NATO leadership positions, such as Secretary General or military positions at the two-star level or above.</p>",
      "updateDate": "2025-04-08",
      "versionCode": "id119sres75"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres75is.xml"
        }
      ],
      "type": "IS"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A resolution expressing the sense of the Senate that member countries of NATO must commit at least 2 percent of their national gross domestic product to national defense spending to hold leadership or benefit at the expense of those countries who meet their obligations.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-15T05:18:46Z"
    },
    {
      "title": "A resolution expressing the sense of the Senate that member countries of NATO must commit at least 2 percent of their national gross domestic product to national defense spending to hold leadership or benefit at the expense of those countries who meet their obligations.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-13T11:56:15Z"
    }
  ]
}
```
