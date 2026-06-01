# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/334?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/334
- Title: American Values Act
- Congress: 119
- Bill type: S
- Bill number: 334
- Origin chamber: Senate
- Introduced date: 2025-01-30
- Update date: 2025-12-19T21:50:29Z
- Update date including text: 2025-12-19T21:50:29Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-30: Introduced in Senate
- 2025-01-30 - IntroReferral: Introduced in Senate
- 2025-01-30 - IntroReferral: Read twice and referred to the Committee on Foreign Relations.
- Latest action: 2025-01-30: Introduced in Senate

## Actions

- 2025-01-30 - IntroReferral: Introduced in Senate
- 2025-01-30 - IntroReferral: Read twice and referred to the Committee on Foreign Relations.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-30",
    "latestAction": {
      "actionDate": "2025-01-30",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/334",
    "number": "334",
    "originChamber": "Senate",
    "policyArea": {
      "name": "International Affairs"
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
    "title": "American Values Act",
    "type": "S",
    "updateDate": "2025-12-19T21:50:29Z",
    "updateDateIncludingText": "2025-12-19T21:50:29Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-01-30",
      "committees": {
        "item": {
          "name": "Foreign Relations Committee",
          "systemCode": "ssfr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Foreign Relations.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-01-30",
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
          "date": "2025-01-30T19:42:16Z",
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
      "bioguideId": "M001198",
      "firstName": "Roger",
      "fullName": "Sen. Marshall, Roger [R-KS]",
      "isOriginalCosponsor": "True",
      "lastName": "Marshall",
      "party": "R",
      "sponsorshipDate": "2025-01-30",
      "state": "KS"
    },
    {
      "bioguideId": "P000603",
      "firstName": "Rand",
      "fullName": "Sen. Paul, Rand [R-KY]",
      "isOriginalCosponsor": "True",
      "lastName": "Paul",
      "party": "R",
      "sponsorshipDate": "2025-01-30",
      "state": "KY"
    },
    {
      "bioguideId": "S001217",
      "firstName": "Rick",
      "fullName": "Sen. Scott, Rick [R-FL]",
      "isOriginalCosponsor": "True",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-01-30",
      "state": "FL"
    },
    {
      "bioguideId": "M001190",
      "firstName": "Markwayne",
      "fullName": "Sen. Mullin, Markwayne [R-OK]",
      "isOriginalCosponsor": "True",
      "lastName": "Mullin",
      "party": "R",
      "sponsorshipDate": "2025-01-30",
      "state": "OK"
    },
    {
      "bioguideId": "B001243",
      "firstName": "Marsha",
      "fullName": "Sen. Blackburn, Marsha [R-TN]",
      "isOriginalCosponsor": "True",
      "lastName": "Blackburn",
      "party": "R",
      "sponsorshipDate": "2025-01-30",
      "state": "TN"
    },
    {
      "bioguideId": "D000618",
      "firstName": "Steve",
      "fullName": "Sen. Daines, Steve [R-MT]",
      "isOriginalCosponsor": "True",
      "lastName": "Daines",
      "party": "R",
      "sponsorshipDate": "2025-01-30",
      "state": "MT"
    },
    {
      "bioguideId": "S001232",
      "firstName": "Tim",
      "fullName": "Sen. Sheehy, Tim [R-MT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sheehy",
      "party": "R",
      "sponsorshipDate": "2025-01-30",
      "state": "MT"
    },
    {
      "bioguideId": "R000618",
      "firstName": "Pete",
      "fullName": "Sen. Ricketts, Pete [R-NE]",
      "isOriginalCosponsor": "True",
      "lastName": "Ricketts",
      "party": "R",
      "sponsorshipDate": "2025-01-30",
      "state": "NE"
    },
    {
      "bioguideId": "H000601",
      "firstName": "Bill",
      "fullName": "Sen. Hagerty, Bill [R-TN]",
      "isOriginalCosponsor": "True",
      "lastName": "Hagerty",
      "party": "R",
      "sponsorshipDate": "2025-01-30",
      "state": "TN"
    },
    {
      "bioguideId": "C001098",
      "firstName": "Ted",
      "fullName": "Sen. Cruz, Ted [R-TX]",
      "isOriginalCosponsor": "True",
      "lastName": "Cruz",
      "party": "R",
      "sponsorshipDate": "2025-01-30",
      "state": "TX"
    },
    {
      "bioguideId": "B001261",
      "firstName": "John",
      "fullName": "Sen. Barrasso, John [R-WY]",
      "isOriginalCosponsor": "False",
      "lastName": "Barrasso",
      "party": "R",
      "sponsorshipDate": "2025-02-03",
      "state": "WY"
    },
    {
      "bioguideId": "Y000064",
      "firstName": "Todd",
      "fullName": "Sen. Young, Todd [R-IN]",
      "isOriginalCosponsor": "False",
      "lastName": "Young",
      "party": "R",
      "sponsorshipDate": "2025-02-13",
      "state": "IN"
    },
    {
      "bioguideId": "H001104",
      "firstName": "Jon",
      "fullName": "Sen. Husted, Jon [R-OH]",
      "isOriginalCosponsor": "False",
      "lastName": "Husted",
      "party": "R",
      "sponsorshipDate": "2025-07-28",
      "state": "OH"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s334is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 334\nIN THE SENATE OF THE UNITED STATES\nJanuary 30, 2025 Mr. Risch (for himself, Mr. Marshall , Mr. Paul , Mr. Scott of Florida , Mr. Mullin , Mrs. Blackburn , Mr. Daines , Mr. Sheehy , Mr. Ricketts , Mr. Hagerty , and Mr. Cruz ) introduced the following bill; which was read twice and referred to the Committee on Foreign Relations\nA BILL\nTo permanently enact certain appropriations Act restrictions on the use of funds for abortions and involuntary sterilizations, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the American Values Act .\n#### 2. Permanent enactment of certain general provisions\n##### (a) Foreign Assistance Act of 1961\nSection 104(f) of the Foreign Assistance Act of 1961 ( 22 U.S.C. 2151b(f) ) is amended to read as follows:\n(f) Prohibition on use of funds for abortions and involuntary sterilizations None of the funds authorized to be appropriated or otherwise made available to carry out this Act may be made available\u2014 (1) to pay for the performance of abortions as a method of family planning or to motivate or coerce any person to practice abortions; (2) to pay for the performance of involuntary sterilization as a method of family planning or to coerce or provide any financial incentive to any person to undergo sterilizations; (3) to pay for biomedical research which relates in whole or in part, to methods of, or the performance of, abortions or involuntary sterilization as a means of family planning; (4) to lobby for or against abortion; or (5) to any organization or program which, as determined by the President, supports or participates in the management of a program of coercive abortion or involuntary sterilization. .\n##### (b) Peace Corps Act\nSection 301(b) of the Peace Corps Act ( 22 U.S.C. 2501a(b) ) is amended by adding at the end the following:\n(3) Subject to section 614 of the Financial Services and General Government Appropriations Act, 2014 (division E of Public Law 113\u201376 ; 128 Stat. 227), none of the funds authorized to be appropriated or otherwise made available to carry out this Act may be used to pay for abortions. .",
      "versionDate": "2025-01-30",
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
        "name": "International Affairs",
        "updateDate": "2025-04-22T20:53:13Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-30",
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
          "measure-id": "id119s334",
          "measure-number": "334",
          "measure-type": "s",
          "orig-publish-date": "2025-01-30",
          "originChamber": "SENATE",
          "update-date": "2025-12-19"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s334v00",
            "update-date": "2025-12-19"
          },
          "action-date": "2025-01-30",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>American Values Act</strong></p><p>This bill expands restrictions on using U.S. foreign assistance to pay for or promote abortions, involuntary sterilizations, or other related activities.</p><p>Specifically, the bill expands existing prohibitions, including prohibitions against using foreign assistance to pay for abortions or involuntary sterilization for family planning, to apply to all assistance provided under the Foreign Assistance Act of 1961 (FAA). (Currently, these prohibitions apply to only certain parts of the FAA.)</p><p>Furthermore, assistance provided under the FAA may not be made available to (1) pay for lobbying for or against abortion, or (2) any organization that supports a program of coercive abortion or involuntary sterilization. (These prohibitions have typically been in appropriations acts, but the bill would make the prohibitions a permanent part of the FAA.)</p><p>The bill also makes permanent a prohibition against using funds made available to the Peace Corps to pay for abortions except\u00a0when the pregnancy is the result of rape or\u00a0incest or when the life of the mother would be endangered if the fetus were carried to term.</p>"
        },
        "title": "American Values Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s334.xml",
    "summary": {
      "actionDate": "2025-01-30",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>American Values Act</strong></p><p>This bill expands restrictions on using U.S. foreign assistance to pay for or promote abortions, involuntary sterilizations, or other related activities.</p><p>Specifically, the bill expands existing prohibitions, including prohibitions against using foreign assistance to pay for abortions or involuntary sterilization for family planning, to apply to all assistance provided under the Foreign Assistance Act of 1961 (FAA). (Currently, these prohibitions apply to only certain parts of the FAA.)</p><p>Furthermore, assistance provided under the FAA may not be made available to (1) pay for lobbying for or against abortion, or (2) any organization that supports a program of coercive abortion or involuntary sterilization. (These prohibitions have typically been in appropriations acts, but the bill would make the prohibitions a permanent part of the FAA.)</p><p>The bill also makes permanent a prohibition against using funds made available to the Peace Corps to pay for abortions except\u00a0when the pregnancy is the result of rape or\u00a0incest or when the life of the mother would be endangered if the fetus were carried to term.</p>",
      "updateDate": "2025-12-19",
      "versionCode": "id119s334"
    },
    "title": "American Values Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-30",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>American Values Act</strong></p><p>This bill expands restrictions on using U.S. foreign assistance to pay for or promote abortions, involuntary sterilizations, or other related activities.</p><p>Specifically, the bill expands existing prohibitions, including prohibitions against using foreign assistance to pay for abortions or involuntary sterilization for family planning, to apply to all assistance provided under the Foreign Assistance Act of 1961 (FAA). (Currently, these prohibitions apply to only certain parts of the FAA.)</p><p>Furthermore, assistance provided under the FAA may not be made available to (1) pay for lobbying for or against abortion, or (2) any organization that supports a program of coercive abortion or involuntary sterilization. (These prohibitions have typically been in appropriations acts, but the bill would make the prohibitions a permanent part of the FAA.)</p><p>The bill also makes permanent a prohibition against using funds made available to the Peace Corps to pay for abortions except\u00a0when the pregnancy is the result of rape or\u00a0incest or when the life of the mother would be endangered if the fetus were carried to term.</p>",
      "updateDate": "2025-12-19",
      "versionCode": "id119s334"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s334is.xml"
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
      "title": "American Values Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-30T12:48:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "American Values Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-04T12:53:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to permanently enact certain appropriations Act restrictions on the use of funds for abortions and involuntary sterilizations, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-04T12:48:21Z"
    }
  ]
}
```
