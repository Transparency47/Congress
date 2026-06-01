# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/478?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/478
- Title: Veterans 2nd Amendment Protection Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 478
- Origin chamber: Senate
- Introduced date: 2025-02-06
- Update date: 2026-05-19T11:03:43Z
- Update date including text: 2026-05-19T11:03:43Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-06: Introduced in Senate
- 2025-02-06 - IntroReferral: Introduced in Senate
- 2025-02-06 - IntroReferral: Read twice and referred to the Committee on Veterans' Affairs.
- 2025-03-11 - Committee: Committee on Veterans' Affairs. Hearings held.
- Latest action: 2025-02-06: Introduced in Senate

## Actions

- 2025-02-06 - IntroReferral: Introduced in Senate
- 2025-02-06 - IntroReferral: Read twice and referred to the Committee on Veterans' Affairs.
- 2025-03-11 - Committee: Committee on Veterans' Affairs. Hearings held.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-06",
    "latestAction": {
      "actionDate": "2025-02-06",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/478",
    "number": "478",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "K000393",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Kennedy, John [R-LA]",
        "lastName": "Kennedy",
        "party": "R",
        "state": "LA"
      }
    ],
    "title": "Veterans 2nd Amendment Protection Act of 2025",
    "type": "S",
    "updateDate": "2026-05-19T11:03:43Z",
    "updateDateIncludingText": "2026-05-19T11:03:43Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-11",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "ssva00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Veterans' Affairs. Hearings held.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-02-06",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "ssva00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Veterans' Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-02-06",
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
        "item": [
          {
            "date": "2025-03-11T14:30:08Z",
            "name": "Hearings By (full committee)"
          },
          {
            "date": "2025-03-11T14:30:08Z",
            "name": "Hearings By (full committee)"
          },
          {
            "date": "2025-02-06T22:09:22Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Veterans' Affairs Committee",
      "systemCode": "ssva00",
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
      "bioguideId": "M000934",
      "firstName": "Jerry",
      "fullName": "Sen. Moran, Jerry [R-KS]",
      "isOriginalCosponsor": "True",
      "lastName": "Moran",
      "party": "R",
      "sponsorshipDate": "2025-02-06",
      "state": "KS"
    },
    {
      "bioguideId": "G000386",
      "firstName": "Chuck",
      "fullName": "Sen. Grassley, Chuck [R-IA]",
      "isOriginalCosponsor": "True",
      "lastName": "Grassley",
      "party": "R",
      "sponsorshipDate": "2025-02-06",
      "state": "IA"
    },
    {
      "bioguideId": "D000618",
      "firstName": "Steve",
      "fullName": "Sen. Daines, Steve [R-MT]",
      "isOriginalCosponsor": "True",
      "lastName": "Daines",
      "party": "R",
      "sponsorshipDate": "2025-02-06",
      "state": "MT"
    },
    {
      "bioguideId": "B001243",
      "firstName": "Marsha",
      "fullName": "Sen. Blackburn, Marsha [R-TN]",
      "isOriginalCosponsor": "True",
      "lastName": "Blackburn",
      "party": "R",
      "sponsorshipDate": "2025-02-06",
      "state": "TN"
    },
    {
      "bioguideId": "R000618",
      "firstName": "Pete",
      "fullName": "Sen. Ricketts, Pete [R-NE]",
      "isOriginalCosponsor": "True",
      "lastName": "Ricketts",
      "party": "R",
      "sponsorshipDate": "2025-02-06",
      "state": "NE"
    },
    {
      "bioguideId": "R000605",
      "firstName": "Mike",
      "fullName": "Sen. Rounds, Mike [R-SD]",
      "isOriginalCosponsor": "True",
      "lastName": "Rounds",
      "party": "R",
      "sponsorshipDate": "2025-02-06",
      "state": "SD"
    },
    {
      "bioguideId": "C001096",
      "firstName": "Kevin",
      "fullName": "Sen. Cramer, Kevin [R-ND]",
      "isOriginalCosponsor": "True",
      "lastName": "Cramer",
      "party": "R",
      "sponsorshipDate": "2025-02-06",
      "state": "ND"
    },
    {
      "bioguideId": "B001299",
      "firstName": "Jim",
      "fullName": "Sen. Banks, Jim [R-IN]",
      "isOriginalCosponsor": "True",
      "lastName": "Banks",
      "party": "R",
      "sponsorshipDate": "2025-02-06",
      "state": "IN"
    },
    {
      "bioguideId": "T000476",
      "firstName": "Thomas",
      "fullName": "Sen. Tillis, Thomas [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Tillis",
      "middleName": "Roland",
      "party": "R",
      "sponsorshipDate": "2025-02-06",
      "state": "NC"
    },
    {
      "bioguideId": "C001075",
      "firstName": "Bill",
      "fullName": "Sen. Cassidy, Bill [R-LA]",
      "isOriginalCosponsor": "True",
      "lastName": "Cassidy",
      "party": "R",
      "sponsorshipDate": "2025-02-06",
      "state": "LA"
    },
    {
      "bioguideId": "B001236",
      "firstName": "John",
      "fullName": "Sen. Boozman, John [R-AR]",
      "isOriginalCosponsor": "True",
      "lastName": "Boozman",
      "party": "R",
      "sponsorshipDate": "2025-02-06",
      "state": "AR"
    },
    {
      "bioguideId": "S001217",
      "firstName": "Rick",
      "fullName": "Sen. Scott, Rick [R-FL]",
      "isOriginalCosponsor": "True",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-02-06",
      "state": "FL"
    },
    {
      "bioguideId": "T000278",
      "firstName": "Tommy",
      "fullName": "Sen. Tuberville, Tommy [R-AL]",
      "isOriginalCosponsor": "True",
      "lastName": "Tuberville",
      "party": "R",
      "sponsorshipDate": "2025-02-06",
      "state": "AL"
    },
    {
      "bioguideId": "M001153",
      "firstName": "Lisa",
      "fullName": "Sen. Murkowski, Lisa [R-AK]",
      "isOriginalCosponsor": "True",
      "lastName": "Murkowski",
      "party": "R",
      "sponsorshipDate": "2025-02-06",
      "state": "AK"
    },
    {
      "bioguideId": "S001232",
      "firstName": "Tim",
      "fullName": "Sen. Sheehy, Tim [R-MT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sheehy",
      "party": "R",
      "sponsorshipDate": "2025-02-06",
      "state": "MT"
    },
    {
      "bioguideId": "P000603",
      "firstName": "Rand",
      "fullName": "Sen. Paul, Rand [R-KY]",
      "isOriginalCosponsor": "False",
      "lastName": "Paul",
      "party": "R",
      "sponsorshipDate": "2025-03-25",
      "state": "KY"
    },
    {
      "bioguideId": "J000312",
      "firstName": "James",
      "fullName": "Sen. Justice, James C. [R-WV]",
      "isOriginalCosponsor": "False",
      "lastName": "Justice",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2025-04-28",
      "state": "WV"
    },
    {
      "bioguideId": "B001305",
      "firstName": "Ted",
      "fullName": "Sen. Budd, Ted [R-NC]",
      "isOriginalCosponsor": "False",
      "lastName": "Budd",
      "party": "R",
      "sponsorshipDate": "2025-04-28",
      "state": "NC"
    },
    {
      "bioguideId": "L000575",
      "firstName": "James",
      "fullName": "Sen. Lankford, James [R-OK]",
      "isOriginalCosponsor": "False",
      "lastName": "Lankford",
      "party": "R",
      "sponsorshipDate": "2025-05-05",
      "state": "OK"
    },
    {
      "bioguideId": "R000584",
      "firstName": "James",
      "fullName": "Sen. Risch, James E. [R-ID]",
      "isOriginalCosponsor": "False",
      "lastName": "Risch",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-05-05",
      "state": "ID"
    },
    {
      "bioguideId": "C000880",
      "firstName": "Mike",
      "fullName": "Sen. Crapo, Mike [R-ID]",
      "isOriginalCosponsor": "False",
      "lastName": "Crapo",
      "party": "R",
      "sponsorshipDate": "2025-05-06",
      "state": "ID"
    },
    {
      "bioguideId": "H001079",
      "firstName": "Cindy",
      "fullName": "Sen. Hyde-Smith, Cindy [R-MS]",
      "isOriginalCosponsor": "False",
      "lastName": "Hyde-Smith",
      "party": "R",
      "sponsorshipDate": "2025-05-06",
      "state": "MS"
    },
    {
      "bioguideId": "C001047",
      "firstName": "Shelley",
      "fullName": "Sen. Capito, Shelley Moore [R-WV]",
      "isOriginalCosponsor": "False",
      "lastName": "Capito",
      "middleName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-05-06",
      "state": "WV"
    },
    {
      "bioguideId": "C001056",
      "firstName": "John",
      "fullName": "Sen. Cornyn, John [R-TX]",
      "isOriginalCosponsor": "False",
      "lastName": "Cornyn",
      "party": "R",
      "sponsorshipDate": "2025-05-07",
      "state": "TX"
    },
    {
      "bioguideId": "H001104",
      "firstName": "Jon",
      "fullName": "Sen. Husted, Jon [R-OH]",
      "isOriginalCosponsor": "False",
      "lastName": "Husted",
      "party": "R",
      "sponsorshipDate": "2025-05-15",
      "state": "OH"
    },
    {
      "bioguideId": "L000577",
      "firstName": "Mike",
      "fullName": "Sen. Lee, Mike [R-UT]",
      "isOriginalCosponsor": "False",
      "lastName": "Lee",
      "party": "R",
      "sponsorshipDate": "2025-05-19",
      "state": "UT"
    },
    {
      "bioguideId": "G000359",
      "firstName": "Lindsey",
      "fullName": "Sen. Graham, Lindsey [R-SC]",
      "isOriginalCosponsor": "False",
      "lastName": "Graham",
      "party": "R",
      "sponsorshipDate": "2025-06-24",
      "state": "SC"
    },
    {
      "bioguideId": "M001198",
      "firstName": "Roger",
      "fullName": "Sen. Marshall, Roger [R-KS]",
      "isOriginalCosponsor": "False",
      "lastName": "Marshall",
      "party": "R",
      "sponsorshipDate": "2025-09-02",
      "state": "KS"
    },
    {
      "bioguideId": "M001243",
      "firstName": "David",
      "fullName": "Sen. McCormick, David [R-PA]",
      "isOriginalCosponsor": "False",
      "lastName": "McCormick",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2025-11-07",
      "state": "PA"
    },
    {
      "bioguideId": "M001190",
      "firstName": "Markwayne",
      "fullName": "Sen. Mullin, Markwayne [R-OK]",
      "isOriginalCosponsor": "False",
      "lastName": "Mullin",
      "party": "R",
      "sponsorshipDate": "2025-11-19",
      "state": "OK"
    },
    {
      "bioguideId": "C001095",
      "firstName": "Tom",
      "fullName": "Sen. Cotton, Tom [R-AR]",
      "isOriginalCosponsor": "False",
      "lastName": "Cotton",
      "party": "R",
      "sponsorshipDate": "2026-02-24",
      "state": "AR"
    },
    {
      "bioguideId": "S001198",
      "firstName": "Dan",
      "fullName": "Sen. Sullivan, Dan [R-AK]",
      "isOriginalCosponsor": "False",
      "lastName": "Sullivan",
      "party": "R",
      "sponsorshipDate": "2026-03-17",
      "state": "AK"
    },
    {
      "bioguideId": "B001319",
      "firstName": "Katie",
      "fullName": "Sen. Britt, Katie Boyd [R-AL]",
      "isOriginalCosponsor": "False",
      "lastName": "Britt",
      "party": "R",
      "sponsorshipDate": "2026-04-15",
      "state": "AL"
    },
    {
      "bioguideId": "M001242",
      "firstName": "Bernie",
      "fullName": "Sen. Moreno, Bernie [R-OH]",
      "isOriginalCosponsor": "False",
      "lastName": "Moreno",
      "party": "R",
      "sponsorshipDate": "2026-04-20",
      "state": "OH"
    },
    {
      "bioguideId": "W000437",
      "firstName": "Roger",
      "fullName": "Sen. Wicker, Roger F. [R-MS]",
      "isOriginalCosponsor": "False",
      "lastName": "Wicker",
      "middleName": "F.",
      "party": "R",
      "sponsorshipDate": "2026-05-18",
      "state": "MS"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s478is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 478\nIN THE SENATE OF THE UNITED STATES\nFebruary 6 (legislative day, February 5), 2025 Mr. Kennedy (for himself, Mr. Moran , Mr. Grassley , Mr. Daines , Mrs. Blackburn , Mr. Ricketts , Mr. Rounds , Mr. Cramer , Mr. Banks , Mr. Tillis , Mr. Cassidy , Mr. Boozman , Mr. Scott of Florida , Mr. Tuberville , Ms. Murkowski , and Mr. Sheehy ) introduced the following bill; which was read twice and referred to the Committee on Veterans' Affairs\nA BILL\nTo amend title 38, United States Code, to prohibit the Secretary of Veterans Affairs from transmitting certain information to the Department of Justice for use by the national instant criminal background check system.\n#### 1. Short title\nThis Act may be cited as the Veterans 2nd Amendment Protection Act of 2025 .\n#### 2. Prohibition on Secretary of Veterans Affairs transmittal of certain information to the Department of Justice for use by the national instant criminal background check system\n##### (a) In general\nChapter 55 of title 38, United States Code, is amended by inserting after section 5501A the following new section:\n5501B. Prohibition on transmittal of certain information to the Department of Justice for use by the national instant criminal background check system The Secretary may not transmit to any entity in the Department of Justice, for use by the national instant criminal background check system established under section 103 of the Brady Handgun Violence Prevention Act ( 34 U.S.C. 40901 ), personally identifiable information of a beneficiary, solely on the basis of a determination by the Secretary to pay benefits to a fiduciary for the use and benefit of the beneficiary under section 5502 of this title, without the order or finding of a judge, magistrate, or other judicial authority of competent jurisdiction that such beneficiary is a danger to themselves or others. .\n##### (b) Clerical amendment\nThe table of sections at the beginning of chapter 55 of such title is amended by inserting after the item relating to section 5501A the following new item:\n5501B. Prohibition on transmittal of certain information to the Department of Justice for use by the national instant criminal background check system. .",
      "versionDate": "2025-02-06",
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
        "actionDate": "2025-06-05",
        "text": "Placed on the Union Calendar, Calendar No. 112."
      },
      "number": "1041",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Veterans 2nd Amendment Protection Act",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Criminal justice information and records",
            "updateDate": "2025-03-21T18:44:14Z"
          },
          {
            "name": "Firearms and explosives",
            "updateDate": "2025-03-21T18:44:14Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2025-03-21T18:44:14Z"
          },
          {
            "name": "Veterans' pensions and compensation",
            "updateDate": "2025-03-21T18:44:14Z"
          }
        ]
      },
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2025-03-19T20:46:58Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-06",
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
          "measure-id": "id119s478",
          "measure-number": "478",
          "measure-type": "s",
          "orig-publish-date": "2025-02-06",
          "originChamber": "SENATE",
          "update-date": "2025-03-24"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s478v00",
            "update-date": "2025-03-24"
          },
          "action-date": "2025-02-06",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Veterans 2nd Amendment Protection Act of 2025</strong></p><p>This bill prohibits the Department of Veterans Affairs (VA) from transmitting certain information to the National Instant Criminal Background Check System (NICS) utilized by licensed importers or dealers of firearms.</p><p>Specifically, the bill prohibits the VA from transmitting personally identifying information of a veteran or a beneficiary to the NICS solely on the basis that such veteran or beneficiary has an appointed fiduciary to manage their benefits, unless there is an order or finding of a judicial authority that such veteran or beneficiary is a danger to themselves or others.</p>"
        },
        "title": "Veterans 2nd Amendment Protection Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s478.xml",
    "summary": {
      "actionDate": "2025-02-06",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Veterans 2nd Amendment Protection Act of 2025</strong></p><p>This bill prohibits the Department of Veterans Affairs (VA) from transmitting certain information to the National Instant Criminal Background Check System (NICS) utilized by licensed importers or dealers of firearms.</p><p>Specifically, the bill prohibits the VA from transmitting personally identifying information of a veteran or a beneficiary to the NICS solely on the basis that such veteran or beneficiary has an appointed fiduciary to manage their benefits, unless there is an order or finding of a judicial authority that such veteran or beneficiary is a danger to themselves or others.</p>",
      "updateDate": "2025-03-24",
      "versionCode": "id119s478"
    },
    "title": "Veterans 2nd Amendment Protection Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-02-06",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Veterans 2nd Amendment Protection Act of 2025</strong></p><p>This bill prohibits the Department of Veterans Affairs (VA) from transmitting certain information to the National Instant Criminal Background Check System (NICS) utilized by licensed importers or dealers of firearms.</p><p>Specifically, the bill prohibits the VA from transmitting personally identifying information of a veteran or a beneficiary to the NICS solely on the basis that such veteran or beneficiary has an appointed fiduciary to manage their benefits, unless there is an order or finding of a judicial authority that such veteran or beneficiary is a danger to themselves or others.</p>",
      "updateDate": "2025-03-24",
      "versionCode": "id119s478"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-06",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s478is.xml"
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
      "title": "Veterans 2nd Amendment Protection Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-19T11:03:43Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Veterans 2nd Amendment Protection Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-13T01:23:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title 38, United States Code, to prohibit the Secretary of Veterans Affairs from transmitting certain information to the Department of Justice for use by the national instant criminal background check system.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-13T01:18:33Z"
    }
  ]
}
```
