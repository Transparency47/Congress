# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3034?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3034
- Title: NFA SBS Act
- Congress: 119
- Bill type: HR
- Bill number: 3034
- Origin chamber: House
- Introduced date: 2025-04-28
- Update date: 2026-05-02T19:06:21Z
- Update date including text: 2026-05-02T19:06:21Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-04-28: Introduced in House
- 2025-04-28 - IntroReferral: Introduced in House
- 2025-04-28 - IntroReferral: Introduced in House
- 2025-04-28 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-04-28 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-04-28: Introduced in House

## Actions

- 2025-04-28 - IntroReferral: Introduced in House
- 2025-04-28 - IntroReferral: Introduced in House
- 2025-04-28 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-04-28 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-28",
    "latestAction": {
      "actionDate": "2025-04-28",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3034",
    "number": "3034",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "B001325",
        "district": "3",
        "firstName": "Sheri",
        "fullName": "Rep. Biggs, Sheri [R-SC-3]",
        "lastName": "Biggs",
        "party": "R",
        "state": "SC"
      }
    ],
    "title": "NFA SBS Act",
    "type": "HR",
    "updateDate": "2026-05-02T19:06:21Z",
    "updateDateIncludingText": "2026-05-02T19:06:21Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-28",
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
      "text": "Referred to the Committee on Ways and Means, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-28",
      "committees": {
        "item": {
          "name": "Ways and Means Committee",
          "systemCode": "hswm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Ways and Means, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-04-28",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-28",
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
          "date": "2025-04-28T16:03:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-04-28T16:03:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
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
      "bioguideId": "C001118",
      "district": "6",
      "firstName": "Ben",
      "fullName": "Rep. Cline, Ben [R-VA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Cline",
      "party": "R",
      "sponsorshipDate": "2025-04-28",
      "state": "VA"
    },
    {
      "bioguideId": "C001120",
      "district": "2",
      "firstName": "Dan",
      "fullName": "Rep. Crenshaw, Dan [R-TX-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Crenshaw",
      "party": "R",
      "sponsorshipDate": "2025-04-28",
      "state": "TX"
    },
    {
      "bioguideId": "M001211",
      "district": "15",
      "firstName": "Mary",
      "fullName": "Rep. Miller, Mary E. [R-IL-15]",
      "isOriginalCosponsor": "True",
      "lastName": "Miller",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-04-28",
      "state": "IL"
    },
    {
      "bioguideId": "M001194",
      "district": "2",
      "firstName": "John",
      "fullName": "Rep. Moolenaar, John R. [R-MI-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Moolenaar",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-04-28",
      "state": "MI"
    },
    {
      "bioguideId": "T000480",
      "district": "4",
      "firstName": "William",
      "fullName": "Rep. Timmons, William R. [R-SC-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Timmons",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-04-28",
      "state": "SC"
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
      "sponsorshipDate": "2025-04-28",
      "state": "TX"
    },
    {
      "bioguideId": "G000603",
      "district": "26",
      "firstName": "Brandon",
      "fullName": "Rep. Gill, Brandon [R-TX-26]",
      "isOriginalCosponsor": "True",
      "lastName": "Gill",
      "party": "R",
      "sponsorshipDate": "2025-04-28",
      "state": "TX"
    },
    {
      "bioguideId": "S001212",
      "district": "8",
      "firstName": "Pete",
      "fullName": "Rep. Stauber, Pete [R-MN-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Stauber",
      "party": "R",
      "sponsorshipDate": "2025-04-29",
      "state": "MN"
    },
    {
      "bioguideId": "P000605",
      "district": "10",
      "firstName": "Scott",
      "fullName": "Rep. Perry, Scott [R-PA-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Perry",
      "party": "R",
      "sponsorshipDate": "2025-05-05",
      "state": "PA"
    },
    {
      "bioguideId": "D000634",
      "district": "2",
      "firstName": "Troy",
      "fullName": "Rep. Downing, Troy [R-MT-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Downing",
      "party": "R",
      "sponsorshipDate": "2025-05-07",
      "state": "MT"
    },
    {
      "bioguideId": "B001317",
      "district": "2",
      "firstName": "Josh",
      "fullName": "Rep. Brecheen, Josh [R-OK-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Brecheen",
      "party": "R",
      "sponsorshipDate": "2025-05-07",
      "state": "OK"
    },
    {
      "bioguideId": "H001101",
      "district": "10",
      "firstName": "Pat",
      "fullName": "Rep. Harrigan, Pat [R-NC-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Harrigan",
      "party": "R",
      "sponsorshipDate": "2025-05-13",
      "state": "NC"
    },
    {
      "bioguideId": "B001295",
      "district": "12",
      "firstName": "Mike",
      "fullName": "Rep. Bost, Mike [R-IL-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Bost",
      "party": "R",
      "sponsorshipDate": "2025-05-13",
      "state": "IL"
    },
    {
      "bioguideId": "H001098",
      "district": "8",
      "firstName": "Abraham",
      "fullName": "Rep. Hamadeh, Abraham J. [R-AZ-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Hamadeh",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-05-15",
      "state": "AZ"
    },
    {
      "bioguideId": "H001052",
      "district": "1",
      "firstName": "Andy",
      "fullName": "Rep. Harris, Andy [R-MD-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Harris",
      "party": "R",
      "sponsorshipDate": "2025-07-25",
      "state": "MD"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3034ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3034\nIN THE HOUSE OF REPRESENTATIVES\nApril 28, 2025 Mrs. Biggs of South Carolina (for herself, Mr. Cline , Mr. Crenshaw , Mrs. Miller of Illinois , Mr. Moolenaar , Mr. Timmons , Mr. Weber of Texas , and Mr. Gill of Texas ) introduced the following bill; which was referred to the Committee on Ways and Means , and in addition to the Committee on the Judiciary , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend the Internal Revenue Code of 1986 to remove short-barreled shotguns from the definition of firearms for purposes of the National Firearms Act, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the No Frivolous Application for Short-Barreled Shotguns Act or as the NFA SBS Act .\n#### 2. Short-barreled shotguns\n##### (a) In general\nSection 5845(a) of the Internal Revenue Code of 1986 is amended\u2014\n**(1)**\nby striking (1) a shotgun having a barrel or barrels of less than 18 inches in length; (2) a weapon made from a shotgun if such weapon as modified has an overall length of less than 26 inches or a barrel or barrels of less than 18 inches in length; (3) and inserting (1) , and\n**(2)**\nby redesignating paragraphs (4) through (8) as paragraphs (2) through (6), respectively.\n##### (b) Shotguns not treated as destructive devices\nSection 5845(f) of such Code is amended by striking except a shotgun or shotgun shell which the Secretary finds is generally recognized as particularly suitable for sporting purposes and inserting except shotgun shells and any weapon that is designed to shoot shotgun shells .\n##### (c) Effective date\nThe amendment made by this section shall apply to calendar quarters beginning more than 90 days after the date of the enactment of this Act.\n#### 3. Elimination of disparate treatment of short-barreled shotguns used for lawful purposes\nSection 922 of title 18, United States Code, is amended in each of subsections (a)(4) and (b)(4) by striking short-barreled shotgun, .\n#### 4. Treatment of short-barreled shotguns determined by reference to National Firearms Act\nSection 5841 of the Internal Revenue Code of 1986 is amended by adding at the end the following:\n(f) Short-Barreled shotgun requirements determined by reference In the case of any short-barreled shotgun registration or licensing requirement under State or local law which is determined by reference to the National Firearms Act, any person who acquires or possesses such a shotgun in accordance with chapter 44 of title 18, United States Code, shall be treated as meeting any such registration or licensing requirement with respect to such shotgun. .\n#### 5. Preemption of certain State laws in relation to short-barreled shotguns\nSection 927 of title 18, United States Code, is amended by adding at the end the following: Notwithstanding the preceding sentence, a law of a State or a political subdivision of a State that imposes a tax, other than a generally applicable sales or use tax, on making, transferring, using, possessing, or transporting a short-barreled shotgun in or affecting interstate or foreign commerce, or imposes a marking, recordkeeping or registration requirement with respect to such a shotgun, shall have no force or effect. .\n#### 6. Destruction of records\n##### (a) In general\nNot later than 365 days after the date of the enactment of this Act, the Attorney General shall destroy any registration of an applicable shotgun maintained in the National Firearms Registration and Transfer Record pursuant to section 5841 of the Internal Revenue Code of 1986, any application to transfer filed under section 5812 of the Internal Revenue Code of 1986 that identifies the transferee of an applicable shotgun, and any application filed under section 5822 of the Internal Revenue Code of 1986 that identifies the maker of an applicable shotgun.\n##### (b) Applicable shotgun\nFor purposes of this section, the term applicable shotgun means any shotgun\u2014\n**(1)**\ndescribed in paragraph (1) or (2) of section 5845(a) of the Internal Revenue Code of 1986 (as in effect on the day before the enactment of this Act), or\n**(2)**\ntreated as destructive device under 5845(f) of such Code (as in effect on the day before the enactment of this Act) and not so treated under such section as in effect immediately after such date.",
      "versionDate": "2025-04-28",
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
        "name": "Taxation",
        "updateDate": "2025-05-28T16:07:35Z"
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
      "date": "2025-04-28",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3034ih.xml"
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
      "title": "NFA SBS Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-09T04:08:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "NFA SBS Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-09T04:08:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "No Frivolous Application for Short-Barreled Shotguns Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-09T04:08:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to remove short-barreled shotguns from the definition of firearms for purposes of the National Firearms Act, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-09T03:48:15Z"
    }
  ]
}
```
