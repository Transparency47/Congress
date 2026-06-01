# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/364?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/364
- Title: Hearing Protection Act
- Congress: 119
- Bill type: S
- Bill number: 364
- Origin chamber: Senate
- Introduced date: 2025-02-03
- Update date: 2025-12-05T21:32:59Z
- Update date including text: 2025-12-05T21:32:59Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-02-03: Introduced in Senate
- 2025-02-03 - IntroReferral: Introduced in Senate
- 2025-02-03 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-02-03: Introduced in Senate

## Actions

- 2025-02-03 - IntroReferral: Introduced in Senate
- 2025-02-03 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-03",
    "latestAction": {
      "actionDate": "2025-02-03",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/364",
    "number": "364",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "C000880",
        "district": "",
        "firstName": "Mike",
        "fullName": "Sen. Crapo, Mike [R-ID]",
        "lastName": "Crapo",
        "party": "R",
        "state": "ID"
      }
    ],
    "title": "Hearing Protection Act",
    "type": "S",
    "updateDate": "2025-12-05T21:32:59Z",
    "updateDateIncludingText": "2025-12-05T21:32:59Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-03",
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
      "actionDate": "2025-02-03",
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
          "date": "2025-02-03T22:23:25Z",
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
      "bioguideId": "R000584",
      "firstName": "James",
      "fullName": "Sen. Risch, James E. [R-ID]",
      "isOriginalCosponsor": "True",
      "lastName": "Risch",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-02-03",
      "state": "ID"
    },
    {
      "bioguideId": "C001075",
      "firstName": "Bill",
      "fullName": "Sen. Cassidy, Bill [R-LA]",
      "isOriginalCosponsor": "True",
      "lastName": "Cassidy",
      "party": "R",
      "sponsorshipDate": "2025-02-03",
      "state": "LA"
    },
    {
      "bioguideId": "M001190",
      "firstName": "Markwayne",
      "fullName": "Sen. Mullin, Markwayne [R-OK]",
      "isOriginalCosponsor": "True",
      "lastName": "Mullin",
      "party": "R",
      "sponsorshipDate": "2025-02-03",
      "state": "OK"
    },
    {
      "bioguideId": "L000575",
      "firstName": "James",
      "fullName": "Sen. Lankford, James [R-OK]",
      "isOriginalCosponsor": "True",
      "lastName": "Lankford",
      "party": "R",
      "sponsorshipDate": "2025-02-03",
      "state": "OK"
    },
    {
      "bioguideId": "S001217",
      "firstName": "Rick",
      "fullName": "Sen. Scott, Rick [R-FL]",
      "isOriginalCosponsor": "True",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-02-03",
      "state": "FL"
    },
    {
      "bioguideId": "M001198",
      "firstName": "Roger",
      "fullName": "Sen. Marshall, Roger [R-KS]",
      "isOriginalCosponsor": "True",
      "lastName": "Marshall",
      "party": "R",
      "sponsorshipDate": "2025-02-03",
      "state": "KS"
    },
    {
      "bioguideId": "C001096",
      "firstName": "Kevin",
      "fullName": "Sen. Cramer, Kevin [R-ND]",
      "isOriginalCosponsor": "True",
      "lastName": "Cramer",
      "party": "R",
      "sponsorshipDate": "2025-02-03",
      "state": "ND"
    },
    {
      "bioguideId": "B001243",
      "firstName": "Marsha",
      "fullName": "Sen. Blackburn, Marsha [R-TN]",
      "isOriginalCosponsor": "True",
      "lastName": "Blackburn",
      "party": "R",
      "sponsorshipDate": "2025-02-03",
      "state": "TN"
    },
    {
      "bioguideId": "B001236",
      "firstName": "John",
      "fullName": "Sen. Boozman, John [R-AR]",
      "isOriginalCosponsor": "True",
      "lastName": "Boozman",
      "party": "R",
      "sponsorshipDate": "2025-02-03",
      "state": "AR"
    },
    {
      "bioguideId": "J000312",
      "firstName": "James",
      "fullName": "Sen. Justice, James C. [R-WV]",
      "isOriginalCosponsor": "True",
      "lastName": "Justice",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2025-02-03",
      "state": "WV"
    },
    {
      "bioguideId": "G000359",
      "firstName": "Lindsey",
      "fullName": "Sen. Graham, Lindsey [R-SC]",
      "isOriginalCosponsor": "True",
      "lastName": "Graham",
      "party": "R",
      "sponsorshipDate": "2025-02-03",
      "state": "SC"
    },
    {
      "bioguideId": "R000605",
      "firstName": "Mike",
      "fullName": "Sen. Rounds, Mike [R-SD]",
      "isOriginalCosponsor": "True",
      "lastName": "Rounds",
      "party": "R",
      "sponsorshipDate": "2025-02-03",
      "state": "SD"
    },
    {
      "bioguideId": "R000618",
      "firstName": "Pete",
      "fullName": "Sen. Ricketts, Pete [R-NE]",
      "isOriginalCosponsor": "True",
      "lastName": "Ricketts",
      "party": "R",
      "sponsorshipDate": "2025-02-03",
      "state": "NE"
    },
    {
      "bioguideId": "S001232",
      "firstName": "Tim",
      "fullName": "Sen. Sheehy, Tim [R-MT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sheehy",
      "party": "R",
      "sponsorshipDate": "2025-02-03",
      "state": "MT"
    },
    {
      "bioguideId": "T000476",
      "firstName": "Thomas",
      "fullName": "Sen. Tillis, Thomas [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Tillis",
      "middleName": "Roland",
      "party": "R",
      "sponsorshipDate": "2025-02-03",
      "state": "NC"
    },
    {
      "bioguideId": "L000577",
      "firstName": "Mike",
      "fullName": "Sen. Lee, Mike [R-UT]",
      "isOriginalCosponsor": "True",
      "lastName": "Lee",
      "party": "R",
      "sponsorshipDate": "2025-02-03",
      "state": "UT"
    },
    {
      "bioguideId": "H001079",
      "firstName": "Cindy",
      "fullName": "Sen. Hyde-Smith, Cindy [R-MS]",
      "isOriginalCosponsor": "True",
      "lastName": "Hyde-Smith",
      "party": "R",
      "sponsorshipDate": "2025-02-03",
      "state": "MS"
    },
    {
      "bioguideId": "F000463",
      "firstName": "Deb",
      "fullName": "Sen. Fischer, Deb [R-NE]",
      "isOriginalCosponsor": "True",
      "lastName": "Fischer",
      "party": "R",
      "sponsorshipDate": "2025-02-03",
      "state": "NE"
    },
    {
      "bioguideId": "L000571",
      "firstName": "Cynthia",
      "fullName": "Sen. Lummis, Cynthia M. [R-WY]",
      "isOriginalCosponsor": "True",
      "lastName": "Lummis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-02-03",
      "state": "WY"
    },
    {
      "bioguideId": "K000393",
      "firstName": "John",
      "fullName": "Sen. Kennedy, John [R-LA]",
      "isOriginalCosponsor": "True",
      "lastName": "Kennedy",
      "party": "R",
      "sponsorshipDate": "2025-02-03",
      "state": "LA"
    },
    {
      "bioguideId": "M000934",
      "firstName": "Jerry",
      "fullName": "Sen. Moran, Jerry [R-KS]",
      "isOriginalCosponsor": "True",
      "lastName": "Moran",
      "party": "R",
      "sponsorshipDate": "2025-02-03",
      "state": "KS"
    },
    {
      "bioguideId": "D000618",
      "firstName": "Steve",
      "fullName": "Sen. Daines, Steve [R-MT]",
      "isOriginalCosponsor": "True",
      "lastName": "Daines",
      "party": "R",
      "sponsorshipDate": "2025-02-03",
      "state": "MT"
    },
    {
      "bioguideId": "W000437",
      "firstName": "Roger",
      "fullName": "Sen. Wicker, Roger F. [R-MS]",
      "isOriginalCosponsor": "True",
      "lastName": "Wicker",
      "middleName": "F.",
      "party": "R",
      "sponsorshipDate": "2025-02-03",
      "state": "MS"
    },
    {
      "bioguideId": "B001305",
      "firstName": "Ted",
      "fullName": "Sen. Budd, Ted [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Budd",
      "party": "R",
      "sponsorshipDate": "2025-02-03",
      "state": "NC"
    },
    {
      "bioguideId": "H001061",
      "firstName": "John",
      "fullName": "Sen. Hoeven, John [R-ND]",
      "isOriginalCosponsor": "True",
      "lastName": "Hoeven",
      "party": "R",
      "sponsorshipDate": "2025-02-03",
      "state": "ND"
    },
    {
      "bioguideId": "C001095",
      "firstName": "Tom",
      "fullName": "Sen. Cotton, Tom [R-AR]",
      "isOriginalCosponsor": "True",
      "lastName": "Cotton",
      "party": "R",
      "sponsorshipDate": "2025-02-03",
      "state": "AR"
    },
    {
      "bioguideId": "H001089",
      "firstName": "Josh",
      "fullName": "Sen. Hawley, Josh [R-MO]",
      "isOriginalCosponsor": "True",
      "lastName": "Hawley",
      "party": "R",
      "sponsorshipDate": "2025-02-03",
      "state": "MO"
    },
    {
      "bioguideId": "J000293",
      "firstName": "Ron",
      "fullName": "Sen. Johnson, Ron [R-WI]",
      "isOriginalCosponsor": "True",
      "lastName": "Johnson",
      "party": "R",
      "sponsorshipDate": "2025-02-03",
      "state": "WI"
    },
    {
      "bioguideId": "C001056",
      "firstName": "John",
      "fullName": "Sen. Cornyn, John [R-TX]",
      "isOriginalCosponsor": "False",
      "lastName": "Cornyn",
      "party": "R",
      "sponsorshipDate": "2025-02-27",
      "state": "TX"
    },
    {
      "bioguideId": "S001198",
      "firstName": "Dan",
      "fullName": "Sen. Sullivan, Dan [R-AK]",
      "isOriginalCosponsor": "False",
      "lastName": "Sullivan",
      "party": "R",
      "sponsorshipDate": "2025-03-25",
      "state": "AK"
    },
    {
      "bioguideId": "B001319",
      "firstName": "Katie",
      "fullName": "Sen. Britt, Katie Boyd [R-AL]",
      "isOriginalCosponsor": "False",
      "lastName": "Britt",
      "party": "R",
      "sponsorshipDate": "2025-03-25",
      "state": "AL"
    },
    {
      "bioguideId": "E000295",
      "firstName": "Joni",
      "fullName": "Sen. Ernst, Joni [R-IA]",
      "isOriginalCosponsor": "False",
      "lastName": "Ernst",
      "party": "R",
      "sponsorshipDate": "2025-06-02",
      "state": "IA"
    },
    {
      "bioguideId": "H001104",
      "firstName": "Jon",
      "fullName": "Sen. Husted, Jon [R-OH]",
      "isOriginalCosponsor": "False",
      "lastName": "Husted",
      "party": "R",
      "sponsorshipDate": "2025-06-12",
      "state": "OH"
    },
    {
      "bioguideId": "C001114",
      "firstName": "John",
      "fullName": "Sen. Curtis, John R. [R-UT]",
      "isOriginalCosponsor": "False",
      "lastName": "Curtis",
      "party": "R",
      "sponsorshipDate": "2025-10-23",
      "state": "UT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s364is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 364\nIN THE SENATE OF THE UNITED STATES\nFebruary 3, 2025 Mr. Crapo (for himself, Mr. Risch , Mr. Cassidy , Mr. Mullin , Mr. Lankford , Mr. Scott of Florida , Mr. Marshall , Mr. Cramer , Mrs. Blackburn , Mr. Boozman , Mr. Justice , Mr. Graham , Mr. Rounds , Mr. Ricketts , Mr. Sheehy , Mr. Tillis , Mr. Lee , Mrs. Hyde-Smith , Mrs. Fischer , Ms. Lummis , Mr. Kennedy , Mr. Moran , Mr. Daines , Mr. Wicker , Mr. Budd , Mr. Hoeven , Mr. Cotton , Mr. Hawley , and Mr. Johnson ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend the Internal Revenue Code of 1986 to remove silencers from the definition of firearms, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Hearing Protection Act .\n#### 2. Equal treatment of silencers and firearms\n##### (a) In general\nSection 5845(a) of the Internal Revenue Code of 1986 is amended by striking (7) any silencer and all that follows through ; and (8) and inserting and (7) .\n##### (b) Effective date\nThe amendment made by this section shall apply to calendar quarters beginning more than 90 days after the date of the enactment of this Act.\n#### 3. Treatment of certain silencers\nSection 5841 of the Internal Revenue Code of 1986 is amended by adding at the end the following:\n(f) Firearm silencers A person acquiring or possessing a firearm silencer in accordance with chapter 44 of title 18, United States Code, shall be treated as meeting any registration and licensing requirements of the National Firearms Act with respect to such silencer. .\n#### 4. Preemption of certain State laws in relation to firearm silencers\nSection 927 of title 18, United States Code, is amended by adding at the end the following: Notwithstanding the preceding sentence, a law of a State or a political subdivision of a State that imposes a tax, other than a generally applicable sales or use tax, on making, transferring, using, possessing, or transporting a firearm silencer in or affecting interstate or foreign commerce, or imposes a marking, recordkeeping, or registration requirement with respect to such a firearm silencer, shall have no force or effect. .\n#### 5. Destruction of records\nNot later than 365 days after the date of the enactment of this Act, the Attorney General shall destroy any registration of a silencer maintained in the National Firearms Registration and Transfer Record pursuant to section 5841 of the Internal Revenue Code of 1986, any application to transfer filed under section 5812 of the Internal Revenue Code of 1986 that identifies the transferee of a silencer, and any application to make filed under section 5822 of the Internal Revenue Code of 1986 that identifies the maker of a silencer.\n#### 6. Amendments to title 18, United States Code\nChapter 44 of title 18, United States Code, is amended\u2014\n**(1)**\nin section 921(a), by striking paragraph (25) and inserting the following:\n(25) The terms firearm silencer and firearm muffler mean\u2014 (A) any device designed or redesigned, made or remade, and intended\u2014 (i) to silence, muffle, or diminish the auditory report of a portable firearm; and (ii) to be attached to a portable firearm, directly or through a mount, adaptor, or other device that is not a firearm silencer or firearm muffler; or (B) the outer tube or other single part of any device that\u2014 (i) provides the primary housing or is the primary structure for internal sound-reduction components designed or redesigned, made or remade, and intended to silence, muffle, or diminish the auditory report of a portable firearm; and (ii) attaches to a portable firearm, directly or through a mount, adaptor, or other device that is not a firearm silencer or firearm muffler. ;\n**(2)**\nin section 922(b)\u2014\n**(A)**\nin paragraph (1), by striking shotgun or rifle the first place it appears and inserting shotgun, rifle, firearm silencer, or firearm muffler ; and\n**(B)**\nin paragraph (3), by striking rifle or shotgun and inserting shotgun, rifle, firearm silencer, or firearm muffler ; and\n**(3)**\nin section 923(i)\u2014\n**(A)**\nby striking Licensed and inserting the following: (1) In the case of a firearm other than a firearm silencer or firearm muffler, licensed ; and\n**(B)**\nby adding at the end the following:\n(2) In the case of a firearm silencer or firearm muffler, licensed importers and licensed manufacturers shall identify by means of a serial number engraved or cast on the outer tube or other single part that provides the primary housing or primary structure of the firearm silencer or firearm muffler, in such manner as the Attorney General shall by regulations prescribe, each firearm silencer or firearm muffler imported or manufactured by such importer or manufacturer, except that, if marking the outer tube or other single part that provides the primary housing or primary structure is impractical, licensed importers or licensed manufacturers shall submit a request for a marking variance to the Attorney General. The Attorney General shall grant such a request except on showing good cause that marking the firearm silencer or firearm muffler as requested would not further the purposes of this chapter. .\n#### 7. Imposition of tax on firearm silencers or firearm mufflers\n##### (a) In general\nSection 4181 of the Internal Revenue Code of 1986 is amended by adding at the end of the list relating to Articles taxable at 10 percent the following:\nFirearm silencers or firearm mufflers.\n##### (b) Firearm silencers; firearm mufflers\nSection 4181 of such Code is amended by adding at the end the following:\nFor purposes of this part, the terms firearm silencer and firearm muffler mean any device for silencing, muffling, or diminishing the report of a portable firearm. .\n##### (c) Conforming amendments\n**(1)**\nSection 4181 of such Code is amended by striking other than pistols and revolvers and inserting other than articles taxable at 10 percent under this section .\n**(2)**\nSection 4182(b) of such Code is amended by striking firearms, pistols, revolvers, shells, and cartridges and inserting articles described in section 4181 and .\n**(3)**\nSection 4182(c)(1) of such Code is amended by striking or firearm and inserting firearm, firearm silencer, or firearm muffler, .\n##### (d) Effective date\nThe amendments made by this section shall apply to articles sold by the manufacturer, producer, or importer in any calendar quarter beginning more than 90 days after the date of the enactment of this Act.",
      "versionDate": "2025-02-03",
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
        "actionDate": "2025-01-15",
        "text": "Referred to the Committee on Ways and Means, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "404",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Hearing Protection Act",
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
        "updateDate": "2025-05-06T12:31:02Z"
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
      "date": "2025-02-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s364is.xml"
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
      "title": "Hearing Protection Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-24T11:03:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Hearing Protection Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-06T03:08:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Internal Revenue Code of 1986 to remove silencers from the definition of firearms, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-06T03:03:30Z"
    }
  ]
}
```
