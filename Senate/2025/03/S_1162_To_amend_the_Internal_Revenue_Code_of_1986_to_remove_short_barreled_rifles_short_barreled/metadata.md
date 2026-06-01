# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1162?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/1162
- Title: SHORT Act
- Congress: 119
- Bill type: S
- Bill number: 1162
- Origin chamber: Senate
- Introduced date: 2025-03-27
- Update date: 2025-07-01T11:06:18Z
- Update date including text: 2025-07-01T11:06:18Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-03-27: Introduced in Senate
- 2025-03-27 - IntroReferral: Introduced in Senate
- 2025-03-27 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-03-27: Introduced in Senate

## Actions

- 2025-03-27 - IntroReferral: Introduced in Senate
- 2025-03-27 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-27",
    "latestAction": {
      "actionDate": "2025-03-27",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/1162",
    "number": "1162",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "M001198",
        "district": "",
        "firstName": "Roger",
        "fullName": "Sen. Marshall, Roger [R-KS]",
        "lastName": "Marshall",
        "party": "R",
        "state": "KS"
      }
    ],
    "title": "SHORT Act",
    "type": "S",
    "updateDate": "2025-07-01T11:06:18Z",
    "updateDateIncludingText": "2025-07-01T11:06:18Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-27",
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
      "actionDate": "2025-03-27",
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
          "date": "2025-03-27T14:16:18Z",
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
      "bioguideId": "L000571",
      "firstName": "Cynthia",
      "fullName": "Sen. Lummis, Cynthia M. [R-WY]",
      "isOriginalCosponsor": "True",
      "lastName": "Lummis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-03-27",
      "state": "WY"
    },
    {
      "bioguideId": "S001217",
      "firstName": "Rick",
      "fullName": "Sen. Scott, Rick [R-FL]",
      "isOriginalCosponsor": "True",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-03-27",
      "state": "FL"
    },
    {
      "bioguideId": "T000278",
      "firstName": "Tommy",
      "fullName": "Sen. Tuberville, Tommy [R-AL]",
      "isOriginalCosponsor": "True",
      "lastName": "Tuberville",
      "party": "R",
      "sponsorshipDate": "2025-03-27",
      "state": "AL"
    },
    {
      "bioguideId": "C001096",
      "firstName": "Kevin",
      "fullName": "Sen. Cramer, Kevin [R-ND]",
      "isOriginalCosponsor": "True",
      "lastName": "Cramer",
      "party": "R",
      "sponsorshipDate": "2025-03-27",
      "state": "ND"
    },
    {
      "bioguideId": "R000584",
      "firstName": "James",
      "fullName": "Sen. Risch, James E. [R-ID]",
      "isOriginalCosponsor": "True",
      "lastName": "Risch",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-03-27",
      "state": "ID"
    },
    {
      "bioguideId": "C000880",
      "firstName": "Mike",
      "fullName": "Sen. Crapo, Mike [R-ID]",
      "isOriginalCosponsor": "True",
      "lastName": "Crapo",
      "party": "R",
      "sponsorshipDate": "2025-03-27",
      "state": "ID"
    },
    {
      "bioguideId": "J000312",
      "firstName": "James",
      "fullName": "Sen. Justice, James C. [R-WV]",
      "isOriginalCosponsor": "True",
      "lastName": "Justice",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2025-03-27",
      "state": "WV"
    },
    {
      "bioguideId": "H001079",
      "firstName": "Cindy",
      "fullName": "Sen. Hyde-Smith, Cindy [R-MS]",
      "isOriginalCosponsor": "True",
      "lastName": "Hyde-Smith",
      "party": "R",
      "sponsorshipDate": "2025-03-27",
      "state": "MS"
    },
    {
      "bioguideId": "B001319",
      "firstName": "Katie",
      "fullName": "Sen. Britt, Katie Boyd [R-AL]",
      "isOriginalCosponsor": "True",
      "lastName": "Britt",
      "party": "R",
      "sponsorshipDate": "2025-03-27",
      "state": "AL"
    },
    {
      "bioguideId": "S001232",
      "firstName": "Tim",
      "fullName": "Sen. Sheehy, Tim [R-MT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sheehy",
      "party": "R",
      "sponsorshipDate": "2025-03-27",
      "state": "MT"
    },
    {
      "bioguideId": "R000618",
      "firstName": "Pete",
      "fullName": "Sen. Ricketts, Pete [R-NE]",
      "isOriginalCosponsor": "True",
      "lastName": "Ricketts",
      "party": "R",
      "sponsorshipDate": "2025-03-27",
      "state": "NE"
    },
    {
      "bioguideId": "R000605",
      "firstName": "Mike",
      "fullName": "Sen. Rounds, Mike [R-SD]",
      "isOriginalCosponsor": "True",
      "lastName": "Rounds",
      "party": "R",
      "sponsorshipDate": "2025-03-27",
      "state": "SD"
    },
    {
      "bioguideId": "B001261",
      "firstName": "John",
      "fullName": "Sen. Barrasso, John [R-WY]",
      "isOriginalCosponsor": "False",
      "lastName": "Barrasso",
      "party": "R",
      "sponsorshipDate": "2025-05-19",
      "state": "WY"
    },
    {
      "bioguideId": "B001243",
      "firstName": "Marsha",
      "fullName": "Sen. Blackburn, Marsha [R-TN]",
      "isOriginalCosponsor": "False",
      "lastName": "Blackburn",
      "party": "R",
      "sponsorshipDate": "2025-06-02",
      "state": "TN"
    },
    {
      "bioguideId": "B001305",
      "firstName": "Ted",
      "fullName": "Sen. Budd, Ted [R-NC]",
      "isOriginalCosponsor": "False",
      "lastName": "Budd",
      "party": "R",
      "sponsorshipDate": "2025-06-02",
      "state": "NC"
    },
    {
      "bioguideId": "D000618",
      "firstName": "Steve",
      "fullName": "Sen. Daines, Steve [R-MT]",
      "isOriginalCosponsor": "False",
      "lastName": "Daines",
      "party": "R",
      "sponsorshipDate": "2025-06-02",
      "state": "MT"
    },
    {
      "bioguideId": "E000295",
      "firstName": "Joni",
      "fullName": "Sen. Ernst, Joni [R-IA]",
      "isOriginalCosponsor": "False",
      "lastName": "Ernst",
      "party": "R",
      "sponsorshipDate": "2025-06-09",
      "state": "IA"
    },
    {
      "bioguideId": "B001236",
      "firstName": "John",
      "fullName": "Sen. Boozman, John [R-AR]",
      "isOriginalCosponsor": "False",
      "lastName": "Boozman",
      "party": "R",
      "sponsorshipDate": "2025-06-09",
      "state": "AR"
    },
    {
      "bioguideId": "L000577",
      "firstName": "Mike",
      "fullName": "Sen. Lee, Mike [R-UT]",
      "isOriginalCosponsor": "False",
      "lastName": "Lee",
      "party": "R",
      "sponsorshipDate": "2025-06-10",
      "state": "UT"
    },
    {
      "bioguideId": "C001075",
      "firstName": "Bill",
      "fullName": "Sen. Cassidy, Bill [R-LA]",
      "isOriginalCosponsor": "False",
      "lastName": "Cassidy",
      "party": "R",
      "sponsorshipDate": "2025-06-16",
      "state": "LA"
    },
    {
      "bioguideId": "S001227",
      "firstName": "Eric",
      "fullName": "Sen. Schmitt, Eric [R-MO]",
      "isOriginalCosponsor": "False",
      "lastName": "Schmitt",
      "middleName": "S.",
      "party": "R",
      "sponsorshipDate": "2025-06-16",
      "state": "MO"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1162is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1162\nIN THE SENATE OF THE UNITED STATES\nMarch 27, 2025 Mr. Marshall (for himself, Ms. Lummis , Mr. Scott of Florida , Mr. Tuberville , Mr. Cramer , Mr. Risch , Mr. Crapo , Mr. Justice , Mrs. Hyde-Smith , Mrs. Britt , Mr. Sheehy , Mr. Ricketts , and Mr. Rounds ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend the Internal Revenue Code of 1986 to remove short-barreled rifles, short-barreled shotguns, and certain other weapons from the definition of firearms for purposes of the National Firearms Act, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Stop Harassing Owners of Rifles Today Act or the SHORT Act .\n#### 2. Definition of firearm\n##### (a) In general\nSubsection (a) of section 5845 of the Internal Revenue Code of 1986 is amended\u2014\n**(1)**\nby striking (1) a shotgun and all that follows through as defined in subsection (e); , and\n**(2)**\nby redesignating paragraphs (6) through (8) as paragraphs (1) through (3), respectively.\n##### (b) Shotguns not treated as destructive devices\nSection 5845(f) of the Internal Revenue Code of 1986 is amended by striking except a shotgun or shotgun shell which the Secretary finds is generally recognized as particularly suitable for sporting purposes and inserting except shotgun shells and any weapon that is designed to shoot shotgun shells .\n##### (c) Conforming amendment\nSection 5811(a) of the Internal Revenue Code of 1986 is amended by striking , except, the transfer tax on any firearm classified as any other weapon under section 5845(e) shall be at the rate of $5 for each such firearm transferred .\n##### (d) Effective date\nThe amendment made by this section shall apply to calendar quarters beginning more than 90 days after the date of the enactment of this Act.\n#### 3. Elimination of disparate treatment of short-barreled rifles and short-barreled shotguns used for lawful purposes\nSection 922 of title 18, United States Code, is amended\u2014\n**(1)**\nin subsection (a)(4)\u2014\n**(A)**\nby striking device, and inserting device or ; and\n**(B)**\nby striking short-barreled shotgun, or short-barreled rifle, ; and\n**(2)**\nin subsection (b)(4)\u2014\n**(A)**\nby striking device, and inserting device or ; and\n**(B)**\nby striking short-barreled shotgun, or short-barreled rifle, .\n#### 4. Treatment of short-barreled rifles, short-barreled shotguns, and other weapons determined by reference to National Firearms Act\nSection 5841 of the Internal Revenue Code of 1986 is amended by adding at the end the following:\n(f) Requirements for short-Barreled rifles, short-Barreled shotguns, and other weapons determined by reference In the case of any registration or licensing requirement under State or local law with respect to a short-barreled rifle, short-barreled shotgun, or any other weapon (as defined in section 5845(e)) which is determined by reference to the National Firearms Act, any person who acquires or possesses such rifle, shotgun, or other weapon in accordance with chapter 44 of title 18, United States Code, shall be treated as meeting any such registration or licensing requirement with respect to such rifle, shotgun, or other weapon. .\n#### 5. Preemption of certain State laws in relation to short-barreled rifles, short-barreled shotguns, and other weapons\nSection 927 of title 18, United States Code, is amended\u2014\n**(1)**\nby striking No provision and inserting the following:\n(a) In general No provision ; and\n**(2)**\nby adding at the end the following:\n(b) Taxes on short-Barreled rifles, short-Barreled shotguns, and other weapons Notwithstanding subsection (a), a law of a State or a political subdivision of a State that imposes a tax, other than a generally applicable sales or use tax, on making, transferring, using, possessing, or transporting a short-barreled rifle, short-barreled shotgun, or any other weapon (as that term is defined in section 5845 of the Internal Revenue Code of 1986) in or affecting interstate or foreign commerce, or imposes a marking, recordkeeping, or registration requirement with respect to such a rifle, shotgun, or other weapon, shall have no force or effect. .\n#### 6. Destruction of records\n##### (a) In general\nNot later than 365 days after the date of the enactment of this Act, the Attorney General shall destroy\u2014\n**(1)**\nany registration of an applicable weapon maintained in the National Firearms Registration and Transfer Record pursuant to section 5841 of the Internal Revenue Code of 1986,\n**(2)**\nany application to transfer filed under section 5812 of such Code that identifies the transferee of an applicable weapon, and\n**(3)**\nany application to make filed under section 5822 of such Code that identifies the maker of an applicable weapon.\n##### (b) Applicable weapon\nFor purposes of this section, the term applicable weapon means\u2014\n**(1)**\na rifle, or weapon made from a rifle, described in paragraph (3) or (4) of section 5845(a) of the Internal Revenue Code of 1986 (as in effect on the day before the enactment of this Act),\n**(2)**\nany shotgun\u2014\n**(A)**\ndescribed in paragraph (1) or (2) of section 5845(a) of the Internal Revenue Code of 1986 (as in effect on the day before the enactment of this Act), or\n**(B)**\ntreated as destructive device under 5845(f) of such Code (as in effect on the day before the enactment of this Act) and not so treated under such section as in effect immediately after such date, and\n**(3)**\nany other weapon, as defined in section 5845(e) of such Code.",
      "versionDate": "2025-03-27",
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
        "actionDate": "2025-03-27",
        "text": "Referred to the Committee on Ways and Means, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "2395",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "SHORT Act",
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
        "name": "Taxation",
        "updateDate": "2025-05-08T19:59:19Z"
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
      "date": "2025-03-27",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1162is.xml"
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
      "title": "SHORT Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-25T11:03:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "SHORT Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-11T02:38:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Stop Harassing Owners of Rifles Today Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-11T02:38:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Internal Revenue Code of 1986 to remove short-barreled rifles, short-barreled shotguns, and certain other weapons from the definition of firearms for purposes of the National Firearms Act, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-11T02:33:29Z"
    }
  ]
}
```
