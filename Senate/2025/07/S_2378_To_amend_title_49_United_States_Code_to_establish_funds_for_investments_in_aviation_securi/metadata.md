# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2378?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2378
- Title: SAFEGUARDS Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 2378
- Origin chamber: Senate
- Introduced date: 2025-07-22
- Update date: 2026-05-12T16:53:59Z
- Update date including text: 2026-05-12T16:53:59Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-07-22: Introduced in Senate
- 2025-07-22 - IntroReferral: Introduced in Senate
- 2025-07-22 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- 2026-04-14 - Committee: Committee on Commerce, Science, and Transportation. Ordered to be reported with an amendment in the nature of a substitute favorably.
- Latest action: 2025-07-22: Introduced in Senate

## Actions

- 2025-07-22 - IntroReferral: Introduced in Senate
- 2025-07-22 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- 2026-04-14 - Committee: Committee on Commerce, Science, and Transportation. Ordered to be reported with an amendment in the nature of a substitute favorably.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-22",
    "latestAction": {
      "actionDate": "2025-07-22",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2378",
    "number": "2378",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "M000934",
        "district": "",
        "firstName": "Jerry",
        "fullName": "Sen. Moran, Jerry [R-KS]",
        "lastName": "Moran",
        "party": "R",
        "state": "KS"
      }
    ],
    "title": "SAFEGUARDS Act of 2025",
    "type": "S",
    "updateDate": "2026-05-12T16:53:59Z",
    "updateDateIncludingText": "2026-05-12T16:53:59Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-04-14",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Commerce, Science, and Transportation. Ordered to be reported with an amendment in the nature of a substitute favorably.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-07-22",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Commerce, Science, and Transportation.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-07-22",
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
            "date": "2026-04-14T14:00:06Z",
            "name": "Markup By"
          },
          {
            "date": "2025-07-22T19:05:15Z",
            "name": "Referred To"
          },
          {
            "date": "2025-07-22T19:05:15Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Commerce, Science, and Transportation Committee",
      "systemCode": "sscm00",
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
      "bioguideId": "V000128",
      "firstName": "Chris",
      "fullName": "Sen. Van Hollen, Chris [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Hollen",
      "party": "D",
      "sponsorshipDate": "2025-07-22",
      "state": "MD"
    },
    {
      "bioguideId": "B001267",
      "firstName": "Michael",
      "fullName": "Sen. Bennet, Michael F. [D-CO]",
      "isOriginalCosponsor": "True",
      "lastName": "Bennet",
      "party": "D",
      "sponsorshipDate": "2025-07-22",
      "state": "CO"
    },
    {
      "bioguideId": "B001236",
      "firstName": "John",
      "fullName": "Sen. Boozman, John [R-AR]",
      "isOriginalCosponsor": "True",
      "lastName": "Boozman",
      "party": "R",
      "sponsorshipDate": "2025-07-22",
      "state": "AR"
    },
    {
      "bioguideId": "D000618",
      "firstName": "Steve",
      "fullName": "Sen. Daines, Steve [R-MT]",
      "isOriginalCosponsor": "False",
      "lastName": "Daines",
      "party": "R",
      "sponsorshipDate": "2025-09-30",
      "state": "MT"
    },
    {
      "bioguideId": "S001232",
      "firstName": "Tim",
      "fullName": "Sen. Sheehy, Tim [R-MT]",
      "isOriginalCosponsor": "False",
      "lastName": "Sheehy",
      "party": "R",
      "sponsorshipDate": "2025-10-07",
      "state": "MT"
    },
    {
      "bioguideId": "C001047",
      "firstName": "Shelley",
      "fullName": "Sen. Capito, Shelley Moore [R-WV]",
      "isOriginalCosponsor": "False",
      "lastName": "Capito",
      "middleName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-10-14",
      "state": "WV"
    },
    {
      "bioguideId": "H000273",
      "firstName": "John",
      "fullName": "Sen. Hickenlooper, John W. [D-CO]",
      "isOriginalCosponsor": "False",
      "lastName": "Hickenlooper",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2025-10-14",
      "state": "CO"
    },
    {
      "bioguideId": "H001079",
      "firstName": "Cindy",
      "fullName": "Sen. Hyde-Smith, Cindy [R-MS]",
      "isOriginalCosponsor": "False",
      "lastName": "Hyde-Smith",
      "party": "R",
      "sponsorshipDate": "2025-10-28",
      "state": "MS"
    },
    {
      "bioguideId": "R000608",
      "firstName": "Jacky",
      "fullName": "Sen. Rosen, Jacky [D-NV]",
      "isOriginalCosponsor": "False",
      "lastName": "Rosen",
      "party": "D",
      "sponsorshipDate": "2025-11-03",
      "state": "NV"
    },
    {
      "bioguideId": "C000880",
      "firstName": "Mike",
      "fullName": "Sen. Crapo, Mike [R-ID]",
      "isOriginalCosponsor": "False",
      "lastName": "Crapo",
      "party": "R",
      "sponsorshipDate": "2025-12-17",
      "state": "ID"
    },
    {
      "bioguideId": "R000584",
      "firstName": "James",
      "fullName": "Sen. Risch, James E. [R-ID]",
      "isOriginalCosponsor": "False",
      "lastName": "Risch",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2026-01-08",
      "state": "ID"
    },
    {
      "bioguideId": "Y000064",
      "firstName": "Todd",
      "fullName": "Sen. Young, Todd [R-IN]",
      "isOriginalCosponsor": "False",
      "lastName": "Young",
      "party": "R",
      "sponsorshipDate": "2026-03-12",
      "state": "IN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2378is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2378\nIN THE SENATE OF THE UNITED STATES\nJuly 22, 2025 Mr. Moran (for himself, Mr. Van Hollen , Mr. Bennet , and Mr. Boozman ) introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nA BILL\nTo amend title 49, United States Code, to establish funds for investments in aviation security checkpoint technology, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Spending Aviation Fees for Equipment, Guaranteeing Upgraded and Advanced Risk Detection and Safety Act of 2025 or the SAFEGUARDS Act of 2025 .\n#### 2. Sense of Congress\nIt is the sense of Congress that\u2014\n**(1)**\nthe fee collected in accordance with section 44940 of title 49, United States Code (commonly known as the 9/11 Security Fee ), is an airline passenger-paid fee established with the express purpose of enhancing the safety and security of the aviation system of the United States;\n**(2)**\nrevenue generated from the 9/11 Security Fee should be used exclusively to fund activities, programs, equipment, and initiatives that directly improve the security of commercial aviation, including passenger and baggage screening, security technology upgrades, and the support of personnel responsible for aviation security;\n**(3)**\nthe use of the 9/11 Security Fee for purposes unrelated to aviation security undermines public trust and the original intent of the fee, and all proceeds from the fee should be reserved and expended solely for measures that strengthen the safety and security of the traveling public within the aviation sector; and\n**(4)**\nthe diversion of 9/11 Security Fee revenue to other purposes should be ended no later than 2027, in accordance with section 44940(i)(4) of title 49, United States Code, as it read on the date of the enactment of this Act.\n#### 3. Improving the aviation security capital fund\nSection 44923(h) of title 49, United States Code, is amended to read as follows:\n(h) Aviation Security Capital Fund (1) In general There is established within the Department of Homeland Security a fund to be known as the Aviation Security Capital Fund (in this subsection referred to as the Fund ). (2) Source of funding (A) In each of fiscal years 2004 through 2025 the first $250,000,000 derived from fees received under section 44940(a)(1) shall be available to be deposited in the Fund in paragraph (1). The Administrator of the Transportation Security Administration shall impose the fee authorized by section 44940(a)(1) so as to collect at least $250,000,000 in each of such fiscal years for deposit into the Fund; and (B) Beginning in fiscal year 2026, and for each fiscal year thereafter, the first $500,000,000 derived from fees received under section 44940(a)(1) shall be available to be deposited in the Fund under paragraph (1). The Administrator of the Transportation Security Administration shall impose the fee authorized by section 44940(a)(1) so as to collect at least $500,000,000 in each of such fiscal years for deposit into the Fund. (3) Grant authority Amounts in the Fund shall be available to the Administrator of the Transportation Security Administration to make grants under this section. .\n#### 4. Establishment of the aviation security checkpoint technology fund\nSection 44923 of title 49, United States Code, is amended by\u2014\n**(1)**\nby redesignating subsection (i) as subsection (j); and\n**(2)**\nby inserting after subsection (h) the following new subsection (i):\n(i) Aviation Security Checkpoint Technology fund (1) In general There is established within the Department of Homeland Security a fund to be known as the Aviation Security Checkpoint Technology Fund (in this subsection referred to as the ASCT Fund ). (2) Funding Beginning in fiscal year 2026, and for each fiscal year thereafter, after the first $500,000,000 is deposited into the Aviation Security Capital Fund pursuant to subsection (h)(2), the next $250,000,000 from fees received under section 44940(a)(1) shall be available to be deposited in the ASCT Fund. The Administrator of the Transportation Security Administration shall impose the fee authorized by section 44940(a)(1) so as to collect not less than $250,000,000 in each of such fiscal years for deposit into the ASCT Fund. Amounts in the ASCT Fund shall be available until expended to the Administrator of the Transportation Security Administration to fund the procurement, deployment, and sustainment of aviation security checkpoint and exit lane technology. (3) Grant authority (A) In general Amounts in the ASCT Fund shall be available to the Administrator of the Transportation Security Administration to make grants under this section. (B) Retroactive application of grant funds The Administrator may retroactively approve the use of grant funds under this subsection for projects to support the procurement, deployment, and sustainment of aviation security checkpoint and exit lane technology that were implemented on or after January 1, 2023. .",
      "versionDate": "2025-07-22",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Aviation and airports",
            "updateDate": "2026-05-12T16:53:09Z"
          },
          {
            "name": "Government trust funds",
            "updateDate": "2026-05-12T16:53:34Z"
          },
          {
            "name": "Public contracts and procurement",
            "updateDate": "2026-05-12T16:53:59Z"
          },
          {
            "name": "Transportation programs funding",
            "updateDate": "2026-05-12T16:53:49Z"
          },
          {
            "name": "Transportation safety and security",
            "updateDate": "2026-05-12T16:53:04Z"
          },
          {
            "name": "Travel and tourism",
            "updateDate": "2026-05-12T16:53:25Z"
          },
          {
            "name": "User charges and fees",
            "updateDate": "2026-05-12T16:53:16Z"
          }
        ]
      },
      "policyArea": {
        "name": "Transportation and Public Works",
        "updateDate": "2025-09-12T14:55:40Z"
      }
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-07-22",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2378is.xml"
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
      "title": "SAFEGUARDS Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-15T11:03:26Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "SAFEGUARDS Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-01T05:23:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Spending Aviation Fees for Equipment, Guaranteeing Upgraded and Advanced Risk Detection and Safety Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-01T05:23:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title 49, United States Code, to establish funds for investments in aviation security checkpoint technology, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-01T05:18:31Z"
    }
  ]
}
```
