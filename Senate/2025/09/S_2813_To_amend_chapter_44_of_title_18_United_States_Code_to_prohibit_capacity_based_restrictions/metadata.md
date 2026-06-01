# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2813?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2813
- Title: FIRE Act
- Congress: 119
- Bill type: S
- Bill number: 2813
- Origin chamber: Senate
- Introduced date: 2025-09-16
- Update date: 2026-03-17T13:50:10Z
- Update date including text: 2026-03-17T13:50:10Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-09-16: Introduced in Senate
- 2025-09-16 - IntroReferral: Introduced in Senate
- 2025-09-16 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2025-09-16: Introduced in Senate

## Actions

- 2025-09-16 - IntroReferral: Introduced in Senate
- 2025-09-16 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-16",
    "latestAction": {
      "actionDate": "2025-09-16",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2813",
    "number": "2813",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "R000584",
        "district": "",
        "firstName": "James",
        "fullName": "Sen. Risch, James E. [R-ID]",
        "lastName": "Risch",
        "party": "R",
        "state": "ID"
      }
    ],
    "title": "FIRE Act",
    "type": "S",
    "updateDate": "2026-03-17T13:50:10Z",
    "updateDateIncludingText": "2026-03-17T13:50:10Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-09-16",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-09-16",
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
            "date": "2025-09-16T18:34:46Z",
            "name": "Referred To"
          },
          {
            "date": "2025-09-16T18:34:46Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Judiciary Committee",
      "systemCode": "ssju00",
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
      "bioguideId": "C001095",
      "firstName": "Tom",
      "fullName": "Sen. Cotton, Tom [R-AR]",
      "isOriginalCosponsor": "True",
      "lastName": "Cotton",
      "party": "R",
      "sponsorshipDate": "2025-09-16",
      "state": "AR"
    },
    {
      "bioguideId": "C000880",
      "firstName": "Mike",
      "fullName": "Sen. Crapo, Mike [R-ID]",
      "isOriginalCosponsor": "True",
      "lastName": "Crapo",
      "party": "R",
      "sponsorshipDate": "2025-09-16",
      "state": "ID"
    },
    {
      "bioguideId": "H001079",
      "firstName": "Cindy",
      "fullName": "Sen. Hyde-Smith, Cindy [R-MS]",
      "isOriginalCosponsor": "True",
      "lastName": "Hyde-Smith",
      "party": "R",
      "sponsorshipDate": "2025-09-16",
      "state": "MS"
    },
    {
      "bioguideId": "J000312",
      "firstName": "James",
      "fullName": "Sen. Justice, James C. [R-WV]",
      "isOriginalCosponsor": "True",
      "lastName": "Justice",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2025-09-16",
      "state": "WV"
    },
    {
      "bioguideId": "L000571",
      "firstName": "Cynthia",
      "fullName": "Sen. Lummis, Cynthia M. [R-WY]",
      "isOriginalCosponsor": "True",
      "lastName": "Lummis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-09-16",
      "state": "WY"
    },
    {
      "bioguideId": "M001190",
      "firstName": "Markwayne",
      "fullName": "Sen. Mullin, Markwayne [R-OK]",
      "isOriginalCosponsor": "True",
      "lastName": "Mullin",
      "party": "R",
      "sponsorshipDate": "2025-09-16",
      "state": "OK"
    },
    {
      "bioguideId": "T000476",
      "firstName": "Thomas",
      "fullName": "Sen. Tillis, Thomas [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Tillis",
      "middleName": "Roland",
      "party": "R",
      "sponsorshipDate": "2025-09-16",
      "state": "NC"
    },
    {
      "bioguideId": "B001305",
      "firstName": "Ted",
      "fullName": "Sen. Budd, Ted [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Budd",
      "party": "R",
      "sponsorshipDate": "2025-09-16",
      "state": "NC"
    },
    {
      "bioguideId": "L000577",
      "firstName": "Mike",
      "fullName": "Sen. Lee, Mike [R-UT]",
      "isOriginalCosponsor": "False",
      "lastName": "Lee",
      "party": "R",
      "sponsorshipDate": "2025-09-18",
      "state": "UT"
    },
    {
      "bioguideId": "G000359",
      "firstName": "Lindsey",
      "fullName": "Sen. Graham, Lindsey [R-SC]",
      "isOriginalCosponsor": "False",
      "lastName": "Graham",
      "party": "R",
      "sponsorshipDate": "2025-09-18",
      "state": "SC"
    },
    {
      "bioguideId": "K000393",
      "firstName": "John",
      "fullName": "Sen. Kennedy, John [R-LA]",
      "isOriginalCosponsor": "False",
      "lastName": "Kennedy",
      "party": "R",
      "sponsorshipDate": "2025-10-03",
      "state": "LA"
    },
    {
      "bioguideId": "C001056",
      "firstName": "John",
      "fullName": "Sen. Cornyn, John [R-TX]",
      "isOriginalCosponsor": "False",
      "lastName": "Cornyn",
      "party": "R",
      "sponsorshipDate": "2026-02-25",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2813is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2813\nIN THE SENATE OF THE UNITED STATES\nSeptember 16, 2025 Mr. Risch (for himself, Mr. Cotton , Mr. Crapo , Mrs. Hyde-Smith , Mr. Justice , Ms. Lummis , Mr. Mullin , Mr. Tillis , and Mr. Budd ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo amend chapter 44 of title 18, United States Code, to prohibit capacity-based restrictions on firearm magazines, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Freedom from Improper Regulation and Enforcement Act or the FIRE Act .\n#### 2. Prohibitions relating to capacity-based restrictions on firearm magazines\n##### (a) Federal restrictions\nSection 926 of title 18, United States Code, is amended by adding at the end the following:\n(d) Capacity-Based restrictions on firearm magazines An officer or employee of the Federal Government may not prescribe or enforce any regulation that imposes any limitation or prohibition in relation to a firearm magazine based on the capacity of the magazine. .\n##### (b) State and local restrictions\nSection 927 of title 18, United States Code, is amended\u2014\n**(1)**\nby inserting (a) In general .\u2014 before No ; and\n**(2)**\nby adding at the end the following:\n(b) Capacity-Based restrictions on firearm magazines A State or local law that imposes any limitation, prohibition, or penalty in relation to a firearm magazine based on the capacity of the magazine shall have no force or effect. .\n##### (c) Firearm magazine defined\nSection 921(a) of title 18, United States Code, is amended by adding at the end the following:\n(39) (A) The term firearm magazine means a fixed or detachable device used to store ammunition and feed ammunition into a firearm. (B) The term capacity means, with respect to a firearm magazine, the number of rounds of ammunition that can be stored in the magazine. .\n##### (d) Effective date\nThe amendments made by this section shall apply with respect to conduct engaged in on or after the date that is 30 days after the date of enactment of this Act.",
      "versionDate": "2025-09-16",
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
        "actionDate": "2025-07-17",
        "text": "Referred to the House Committee on the Judiciary."
      },
      "number": "4546",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "FIRE Act",
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
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-09-29T13:29:56Z"
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
      "date": "2025-09-16",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2813is.xml"
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
      "title": "FIRE Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-26T12:03:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "FIRE Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-27T03:38:14Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Freedom from Improper Regulation and Enforcement Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-27T03:38:14Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend chapter 44 of title 18, United States Code, to prohibit capacity-based restrictions on firearm magazines, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-27T03:33:20Z"
    }
  ]
}
```
