# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/65?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/65
- Title: Constitutional Concealed Carry Reciprocity Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 65
- Origin chamber: Senate
- Introduced date: 2025-01-09
- Update date: 2025-10-15T11:03:13Z
- Update date including text: 2025-10-15T11:03:13Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-09: Introduced in Senate
- 2025-01-09 - IntroReferral: Introduced in Senate
- 2025-01-09 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2025-01-09: Introduced in Senate

## Actions

- 2025-01-09 - IntroReferral: Introduced in Senate
- 2025-01-09 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

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
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/65",
    "number": "65",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "C001056",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Cornyn, John [R-TX]",
        "lastName": "Cornyn",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "Constitutional Concealed Carry Reciprocity Act of 2025",
    "type": "S",
    "updateDate": "2025-10-15T11:03:13Z",
    "updateDateIncludingText": "2025-10-15T11:03:13Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-01-09",
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
      "actionDate": "2025-01-09",
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
          "date": "2025-01-09T21:02:48Z",
          "name": "Referred To"
        }
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
      "bioguideId": "T000250",
      "firstName": "John",
      "fullName": "Sen. Thune, John [R-SD]",
      "isOriginalCosponsor": "True",
      "lastName": "Thune",
      "party": "R",
      "sponsorshipDate": "2025-01-09",
      "state": "SD"
    },
    {
      "bioguideId": "T000476",
      "firstName": "Thomas",
      "fullName": "Sen. Tillis, Thomas [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Tillis",
      "middleName": "Roland",
      "party": "R",
      "sponsorshipDate": "2025-01-09",
      "state": "NC"
    },
    {
      "bioguideId": "C001098",
      "firstName": "Ted",
      "fullName": "Sen. Cruz, Ted [R-TX]",
      "isOriginalCosponsor": "True",
      "lastName": "Cruz",
      "party": "R",
      "sponsorshipDate": "2025-01-09",
      "state": "TX"
    },
    {
      "bioguideId": "G000386",
      "firstName": "Chuck",
      "fullName": "Sen. Grassley, Chuck [R-IA]",
      "isOriginalCosponsor": "True",
      "lastName": "Grassley",
      "party": "R",
      "sponsorshipDate": "2025-01-09",
      "state": "IA"
    },
    {
      "bioguideId": "C001096",
      "firstName": "Kevin",
      "fullName": "Sen. Cramer, Kevin [R-ND]",
      "isOriginalCosponsor": "True",
      "lastName": "Cramer",
      "party": "R",
      "sponsorshipDate": "2025-01-09",
      "state": "ND"
    },
    {
      "bioguideId": "T000278",
      "firstName": "Tommy",
      "fullName": "Sen. Tuberville, Tommy [R-AL]",
      "isOriginalCosponsor": "True",
      "lastName": "Tuberville",
      "party": "R",
      "sponsorshipDate": "2025-01-09",
      "state": "AL"
    },
    {
      "bioguideId": "H001079",
      "firstName": "Cindy",
      "fullName": "Sen. Hyde-Smith, Cindy [R-MS]",
      "isOriginalCosponsor": "True",
      "lastName": "Hyde-Smith",
      "party": "R",
      "sponsorshipDate": "2025-01-09",
      "state": "MS"
    },
    {
      "bioguideId": "H000601",
      "firstName": "Bill",
      "fullName": "Sen. Hagerty, Bill [R-TN]",
      "isOriginalCosponsor": "True",
      "lastName": "Hagerty",
      "party": "R",
      "sponsorshipDate": "2025-01-09",
      "state": "TN"
    },
    {
      "bioguideId": "L000577",
      "firstName": "Mike",
      "fullName": "Sen. Lee, Mike [R-UT]",
      "isOriginalCosponsor": "True",
      "lastName": "Lee",
      "party": "R",
      "sponsorshipDate": "2025-01-09",
      "state": "UT"
    },
    {
      "bioguideId": "C001095",
      "firstName": "Tom",
      "fullName": "Sen. Cotton, Tom [R-AR]",
      "isOriginalCosponsor": "True",
      "lastName": "Cotton",
      "party": "R",
      "sponsorshipDate": "2025-01-09",
      "state": "AR"
    },
    {
      "bioguideId": "R000584",
      "firstName": "James",
      "fullName": "Sen. Risch, James E. [R-ID]",
      "isOriginalCosponsor": "True",
      "lastName": "Risch",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-01-09",
      "state": "ID"
    },
    {
      "bioguideId": "B001243",
      "firstName": "Marsha",
      "fullName": "Sen. Blackburn, Marsha [R-TN]",
      "isOriginalCosponsor": "True",
      "lastName": "Blackburn",
      "party": "R",
      "sponsorshipDate": "2025-01-09",
      "state": "TN"
    },
    {
      "bioguideId": "R000618",
      "firstName": "Pete",
      "fullName": "Sen. Ricketts, Pete [R-NE]",
      "isOriginalCosponsor": "True",
      "lastName": "Ricketts",
      "party": "R",
      "sponsorshipDate": "2025-01-09",
      "state": "NE"
    },
    {
      "bioguideId": "M001198",
      "firstName": "Roger",
      "fullName": "Sen. Marshall, Roger [R-KS]",
      "isOriginalCosponsor": "True",
      "lastName": "Marshall",
      "party": "R",
      "sponsorshipDate": "2025-01-09",
      "state": "KS"
    },
    {
      "bioguideId": "S001217",
      "firstName": "Rick",
      "fullName": "Sen. Scott, Rick [R-FL]",
      "isOriginalCosponsor": "True",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-01-09",
      "state": "FL"
    },
    {
      "bioguideId": "L000575",
      "firstName": "James",
      "fullName": "Sen. Lankford, James [R-OK]",
      "isOriginalCosponsor": "True",
      "lastName": "Lankford",
      "party": "R",
      "sponsorshipDate": "2025-01-09",
      "state": "OK"
    },
    {
      "bioguideId": "B001319",
      "firstName": "Katie",
      "fullName": "Sen. Britt, Katie Boyd [R-AL]",
      "isOriginalCosponsor": "True",
      "lastName": "Britt",
      "party": "R",
      "sponsorshipDate": "2025-01-09",
      "state": "AL"
    },
    {
      "bioguideId": "G000359",
      "firstName": "Lindsey",
      "fullName": "Sen. Graham, Lindsey [R-SC]",
      "isOriginalCosponsor": "True",
      "lastName": "Graham",
      "party": "R",
      "sponsorshipDate": "2025-01-09",
      "state": "SC"
    },
    {
      "bioguideId": "C001075",
      "firstName": "Bill",
      "fullName": "Sen. Cassidy, Bill [R-LA]",
      "isOriginalCosponsor": "True",
      "lastName": "Cassidy",
      "party": "R",
      "sponsorshipDate": "2025-01-09",
      "state": "LA"
    },
    {
      "bioguideId": "L000571",
      "firstName": "Cynthia",
      "fullName": "Sen. Lummis, Cynthia M. [R-WY]",
      "isOriginalCosponsor": "True",
      "lastName": "Lummis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-01-09",
      "state": "WY"
    },
    {
      "bioguideId": "B001305",
      "firstName": "Ted",
      "fullName": "Sen. Budd, Ted [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Budd",
      "party": "R",
      "sponsorshipDate": "2025-01-09",
      "state": "NC"
    },
    {
      "bioguideId": "J000293",
      "firstName": "Ron",
      "fullName": "Sen. Johnson, Ron [R-WI]",
      "isOriginalCosponsor": "True",
      "lastName": "Johnson",
      "party": "R",
      "sponsorshipDate": "2025-01-09",
      "state": "WI"
    },
    {
      "bioguideId": "S001232",
      "firstName": "Tim",
      "fullName": "Sen. Sheehy, Tim [R-MT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sheehy",
      "party": "R",
      "sponsorshipDate": "2025-01-09",
      "state": "MT"
    },
    {
      "bioguideId": "K000393",
      "firstName": "John",
      "fullName": "Sen. Kennedy, John [R-LA]",
      "isOriginalCosponsor": "True",
      "lastName": "Kennedy",
      "party": "R",
      "sponsorshipDate": "2025-01-09",
      "state": "LA"
    },
    {
      "bioguideId": "C000880",
      "firstName": "Mike",
      "fullName": "Sen. Crapo, Mike [R-ID]",
      "isOriginalCosponsor": "True",
      "lastName": "Crapo",
      "party": "R",
      "sponsorshipDate": "2025-01-09",
      "state": "ID"
    },
    {
      "bioguideId": "D000618",
      "firstName": "Steve",
      "fullName": "Sen. Daines, Steve [R-MT]",
      "isOriginalCosponsor": "True",
      "lastName": "Daines",
      "party": "R",
      "sponsorshipDate": "2025-01-09",
      "state": "MT"
    },
    {
      "bioguideId": "S001227",
      "firstName": "Eric",
      "fullName": "Sen. Schmitt, Eric [R-MO]",
      "isOriginalCosponsor": "True",
      "lastName": "Schmitt",
      "middleName": "S.",
      "party": "R",
      "sponsorshipDate": "2025-01-09",
      "state": "MO"
    },
    {
      "bioguideId": "Y000064",
      "firstName": "Todd",
      "fullName": "Sen. Young, Todd [R-IN]",
      "isOriginalCosponsor": "True",
      "lastName": "Young",
      "party": "R",
      "sponsorshipDate": "2025-01-09",
      "state": "IN"
    },
    {
      "bioguideId": "S001198",
      "firstName": "Dan",
      "fullName": "Sen. Sullivan, Dan [R-AK]",
      "isOriginalCosponsor": "True",
      "lastName": "Sullivan",
      "party": "R",
      "sponsorshipDate": "2025-01-09",
      "state": "AK"
    },
    {
      "bioguideId": "B001261",
      "firstName": "John",
      "fullName": "Sen. Barrasso, John [R-WY]",
      "isOriginalCosponsor": "True",
      "lastName": "Barrasso",
      "party": "R",
      "sponsorshipDate": "2025-01-09",
      "state": "WY"
    },
    {
      "bioguideId": "B001299",
      "firstName": "Jim",
      "fullName": "Sen. Banks, Jim [R-IN]",
      "isOriginalCosponsor": "True",
      "lastName": "Banks",
      "party": "R",
      "sponsorshipDate": "2025-01-09",
      "state": "IN"
    },
    {
      "bioguideId": "S001184",
      "firstName": "Tim",
      "fullName": "Sen. Scott, Tim [R-SC]",
      "isOriginalCosponsor": "True",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-01-09",
      "state": "SC"
    },
    {
      "bioguideId": "M001242",
      "firstName": "Bernie",
      "fullName": "Sen. Moreno, Bernie [R-OH]",
      "isOriginalCosponsor": "True",
      "lastName": "Moreno",
      "party": "R",
      "sponsorshipDate": "2025-01-09",
      "state": "OH"
    },
    {
      "bioguideId": "F000463",
      "firstName": "Deb",
      "fullName": "Sen. Fischer, Deb [R-NE]",
      "isOriginalCosponsor": "True",
      "lastName": "Fischer",
      "party": "R",
      "sponsorshipDate": "2025-01-09",
      "state": "NE"
    },
    {
      "bioguideId": "M000934",
      "firstName": "Jerry",
      "fullName": "Sen. Moran, Jerry [R-KS]",
      "isOriginalCosponsor": "True",
      "lastName": "Moran",
      "party": "R",
      "sponsorshipDate": "2025-01-09",
      "state": "KS"
    },
    {
      "bioguideId": "R000605",
      "firstName": "Mike",
      "fullName": "Sen. Rounds, Mike [R-SD]",
      "isOriginalCosponsor": "True",
      "lastName": "Rounds",
      "party": "R",
      "sponsorshipDate": "2025-01-09",
      "state": "SD"
    },
    {
      "bioguideId": "C001114",
      "firstName": "John",
      "fullName": "Sen. Curtis, John R. [R-UT]",
      "isOriginalCosponsor": "True",
      "lastName": "Curtis",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-01-09",
      "state": "UT"
    },
    {
      "bioguideId": "B001236",
      "firstName": "John",
      "fullName": "Sen. Boozman, John [R-AR]",
      "isOriginalCosponsor": "True",
      "lastName": "Boozman",
      "party": "R",
      "sponsorshipDate": "2025-01-09",
      "state": "AR"
    },
    {
      "bioguideId": "E000295",
      "firstName": "Joni",
      "fullName": "Sen. Ernst, Joni [R-IA]",
      "isOriginalCosponsor": "True",
      "lastName": "Ernst",
      "party": "R",
      "sponsorshipDate": "2025-01-09",
      "state": "IA"
    },
    {
      "bioguideId": "W000437",
      "firstName": "Roger",
      "fullName": "Sen. Wicker, Roger F. [R-MS]",
      "isOriginalCosponsor": "True",
      "lastName": "Wicker",
      "middleName": "F.",
      "party": "R",
      "sponsorshipDate": "2025-01-09",
      "state": "MS"
    },
    {
      "bioguideId": "H001061",
      "firstName": "John",
      "fullName": "Sen. Hoeven, John [R-ND]",
      "isOriginalCosponsor": "True",
      "lastName": "Hoeven",
      "party": "R",
      "sponsorshipDate": "2025-01-09",
      "state": "ND"
    },
    {
      "bioguideId": "C001047",
      "firstName": "Shelley",
      "fullName": "Sen. Capito, Shelley Moore [R-WV]",
      "isOriginalCosponsor": "True",
      "lastName": "Capito",
      "middleName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-01-09",
      "state": "WV"
    },
    {
      "bioguideId": "M001190",
      "firstName": "Markwayne",
      "fullName": "Sen. Mullin, Markwayne [R-OK]",
      "isOriginalCosponsor": "True",
      "lastName": "Mullin",
      "party": "R",
      "sponsorshipDate": "2025-01-09",
      "state": "OK"
    },
    {
      "bioguideId": "M001243",
      "firstName": "David",
      "fullName": "Sen. McCormick, David [R-PA]",
      "isOriginalCosponsor": "True",
      "lastName": "McCormick",
      "party": "R",
      "sponsorshipDate": "2025-01-09",
      "state": "PA"
    },
    {
      "bioguideId": "H001104",
      "firstName": "Jon",
      "fullName": "Sen. Husted, Jon [R-OH]",
      "isOriginalCosponsor": "False",
      "lastName": "Husted",
      "party": "R",
      "sponsorshipDate": "2025-02-03",
      "state": "OH"
    },
    {
      "bioguideId": "J000312",
      "firstName": "James",
      "fullName": "Sen. Justice, James C. [R-WV]",
      "isOriginalCosponsor": "False",
      "lastName": "Justice",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2025-02-10",
      "state": "WV"
    },
    {
      "bioguideId": "M001244",
      "firstName": "Ashley",
      "fullName": "Sen. Moody, Ashley [R-FL]",
      "isOriginalCosponsor": "False",
      "lastName": "Moody",
      "party": "R",
      "sponsorshipDate": "2025-10-14",
      "state": "FL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s65is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 65\nIN THE SENATE OF THE UNITED STATES\nJanuary 9, 2025 Mr. Cornyn (for himself, Mr. Thune , Mr. Tillis , Mr. Cruz , Mr. Grassley , Mr. Cramer , Mr. Tuberville , Mrs. Hyde-Smith , Mr. Hagerty , Mr. Lee , Mr. Cotton , Mr. Risch , Mrs. Blackburn , Mr. Ricketts , Mr. Marshall , Mr. Scott of Florida , Mr. Lankford , Mrs. Britt , Mr. Graham , Mr. Cassidy , Ms. Lummis , Mr. Budd , Mr. Johnson , Mr. Sheehy , Mr. Kennedy , Mr. Crapo , Mr. Daines , Mr. Schmitt , Mr. Young , Mr. Sullivan , Mr. Barrasso , Mr. Banks , Mr. Scott of South Carolina , Mr. Moreno , Mrs. Fischer , Mr. Moran , Mr. Rounds , Mr. Curtis , Mr. Boozman , Ms. Ernst , Mr. Wicker , Mr. Hoeven , Mrs. Capito , Mr. Mullin , and Mr. McCormick ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo allow reciprocity for the carrying of certain concealed firearms.\n#### 1. Short title\nThis Act may be cited as the Constitutional Concealed Carry Reciprocity Act of 2025 .\n#### 2. Reciprocity for the carrying of certain concealed firearms\n##### (a) In general\nChapter 44 of title 18, United States Code, is amended by inserting after section 926C the following:\n926D. Reciprocity for the carrying of certain concealed firearms (a) In general Notwithstanding any provision of the law of any State or political subdivision thereof to the contrary\u2014 (1) an individual who is not prohibited by Federal law from possessing, transporting, shipping, or receiving a firearm, and who is carrying a government-issued photographic identification document and a valid license or permit which is issued pursuant to the law of a State and which permits the individual to carry a concealed firearm, may possess or carry a concealed handgun (other than a machinegun or destructive device) that has been shipped or transported in interstate or foreign commerce in any State other than the State of residence of the individual that\u2014 (A) has a statute that allows residents of the State to obtain licenses or permits to carry concealed firearms; or (B) does not prohibit the carrying of concealed firearms by residents of the State for lawful purposes; and (2) an individual who is not prohibited by Federal law from possessing, transporting, shipping, or receiving a firearm, and who is carrying a government-issued photographic identification document and is entitled and not prohibited from carrying a concealed firearm in the State in which the individual resides otherwise than as described in paragraph (1), may possess or carry a concealed handgun (other than a machinegun or destructive device) that has been shipped or transported in interstate or foreign commerce in any State other than the State of residence of the individual that\u2014 (A) has a statute that allows residents of the State to obtain licenses or permits to carry concealed firearms; or (B) does not prohibit the carrying of concealed firearms by residents of the State for lawful purposes. (b) Conditions and limitations The possession or carrying of a concealed handgun in a State under this section shall be subject to the same conditions and limitations, except as to eligibility to possess or carry, imposed by or under Federal or State law or the law of a political subdivision of a State, that apply to the possession or carrying of a concealed handgun by residents of the State or political subdivision who are licensed by the State or political subdivision to do so, or not prohibited by the State from doing so. (c) Unrestricted license or permit In a State that allows the issuing authority for licenses or permits to carry concealed firearms to impose restrictions on the carrying of firearms by individual holders of such licenses or permits, an individual carrying a concealed handgun under this section shall be permitted to carry a concealed handgun according to the same terms authorized by an unrestricted license of or permit issued to a resident of the State. (d) Rule of construction Nothing in this section shall be construed to preempt any provision of State law with respect to the issuance of licenses or permits to carry concealed firearms. .\n##### (b) Clerical amendment\nThe table of sections for chapter 44 of title 18, United States Code, is amended by inserting after the item relating to section 926C the following:\n926D. Reciprocity for the carrying of certain concealed firearms. .\n##### (c) Severability\nNotwithstanding any other provision of this Act, if any provision of this Act, or any amendment made by this Act, or the application of such provision or amendment to any person or circumstance is held to be unconstitutional, this Act and amendments made by this Act and the application of such provision or amendment to other persons or circumstances shall not be affected thereby.\n##### (d) Effective date\nThe amendments made by this Act shall take effect 90 days after the date of enactment of this Act.",
      "versionDate": "2025-01-09",
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
            "name": "Civil actions and liability",
            "updateDate": "2025-02-12T19:30:20Z"
          },
          {
            "name": "Firearms and explosives",
            "updateDate": "2025-02-12T19:30:20Z"
          },
          {
            "name": "Forests, forestry, trees",
            "updateDate": "2025-02-12T19:30:20Z"
          },
          {
            "name": "Intergovernmental relations",
            "updateDate": "2025-02-12T19:30:20Z"
          },
          {
            "name": "Judicial procedure and administration",
            "updateDate": "2025-02-12T19:30:20Z"
          },
          {
            "name": "Land use and conservation",
            "updateDate": "2025-02-12T19:30:20Z"
          },
          {
            "name": "Legal fees and court costs",
            "updateDate": "2025-02-12T19:30:20Z"
          },
          {
            "name": "Parks, recreation areas, trails",
            "updateDate": "2025-02-12T19:30:20Z"
          },
          {
            "name": "State and local government operations",
            "updateDate": "2025-02-12T19:30:20Z"
          },
          {
            "name": "Wilderness and natural areas, wildlife refuges, wild rivers, habitats",
            "updateDate": "2025-02-12T19:30:20Z"
          }
        ]
      },
      "policyArea": {
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-02-10T17:40:50Z"
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
          "measure-id": "id119s65",
          "measure-number": "65",
          "measure-type": "s",
          "orig-publish-date": "2025-01-09",
          "originChamber": "SENATE",
          "update-date": "2025-03-07"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s65v00",
            "update-date": "2025-03-07"
          },
          "action-date": "2025-01-09",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Constitutional Concealed Carry Reciprocity Act of 2025\u00a0</strong></p><p>This bill allows a qualified individual to carry a concealed handgun into or possess a concealed handgun in another state that allows its residents to carry concealed firearms.</p><p>A qualified individual must (1) be eligible to possess, transport, or receive a firearm under federal law; (2) carry a valid photo identification document; and (3) carry a valid state-issued concealed carry permit, or be eligible to carry a concealed firearm in his or her state of residence.</p><p>\u00a0</p>"
        },
        "title": "Constitutional Concealed Carry Reciprocity Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s65.xml",
    "summary": {
      "actionDate": "2025-01-09",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Constitutional Concealed Carry Reciprocity Act of 2025\u00a0</strong></p><p>This bill allows a qualified individual to carry a concealed handgun into or possess a concealed handgun in another state that allows its residents to carry concealed firearms.</p><p>A qualified individual must (1) be eligible to possess, transport, or receive a firearm under federal law; (2) carry a valid photo identification document; and (3) carry a valid state-issued concealed carry permit, or be eligible to carry a concealed firearm in his or her state of residence.</p><p>\u00a0</p>",
      "updateDate": "2025-03-07",
      "versionCode": "id119s65"
    },
    "title": "Constitutional Concealed Carry Reciprocity Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-01-09",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Constitutional Concealed Carry Reciprocity Act of 2025\u00a0</strong></p><p>This bill allows a qualified individual to carry a concealed handgun into or possess a concealed handgun in another state that allows its residents to carry concealed firearms.</p><p>A qualified individual must (1) be eligible to possess, transport, or receive a firearm under federal law; (2) carry a valid photo identification document; and (3) carry a valid state-issued concealed carry permit, or be eligible to carry a concealed firearm in his or her state of residence.</p><p>\u00a0</p>",
      "updateDate": "2025-03-07",
      "versionCode": "id119s65"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s65is.xml"
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
      "title": "Constitutional Concealed Carry Reciprocity Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-15T11:03:13Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Constitutional Concealed Carry Reciprocity Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-08T05:08:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to allow reciprocity for the carrying of certain concealed firearms.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-08T05:03:25Z"
    }
  ]
}
```
