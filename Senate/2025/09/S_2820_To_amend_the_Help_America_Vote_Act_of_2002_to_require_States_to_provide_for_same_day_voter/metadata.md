# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2820?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2820
- Title: Same Day Registration Act
- Congress: 119
- Bill type: S
- Bill number: 2820
- Origin chamber: Senate
- Introduced date: 2025-09-16
- Update date: 2025-09-30T23:16:37Z
- Update date including text: 2025-09-30T23:16:37Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-09-16: Introduced in Senate
- 2025-09-16 - IntroReferral: Introduced in Senate
- 2025-09-16 - IntroReferral: Read twice and referred to the Committee on Rules and Administration.
- Latest action: 2025-09-16: Introduced in Senate

## Actions

- 2025-09-16 - IntroReferral: Introduced in Senate
- 2025-09-16 - IntroReferral: Read twice and referred to the Committee on Rules and Administration.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2820",
    "number": "2820",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "K000367",
        "district": "",
        "firstName": "Amy",
        "fullName": "Sen. Klobuchar, Amy [D-MN]",
        "lastName": "Klobuchar",
        "party": "D",
        "state": "MN"
      }
    ],
    "title": "Same Day Registration Act",
    "type": "S",
    "updateDate": "2025-09-30T23:16:37Z",
    "updateDateIncludingText": "2025-09-30T23:16:37Z"
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
          "name": "Rules and Administration Committee",
          "systemCode": "ssra00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Rules and Administration.",
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
        "item": {
          "date": "2025-09-16T20:57:06Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Rules and Administration Committee",
      "systemCode": "ssra00",
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
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "CA"
    },
    {
      "bioguideId": "A000382",
      "firstName": "Angela",
      "fullName": "Sen. Alsobrooks, Angela D. [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Alsobrooks",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "MD"
    },
    {
      "bioguideId": "B001267",
      "firstName": "Michael",
      "fullName": "Sen. Bennet, Michael F. [D-CO]",
      "isOriginalCosponsor": "True",
      "lastName": "Bennet",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "CO"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "CT"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "NJ"
    },
    {
      "bioguideId": "C001113",
      "firstName": "Catherine",
      "fullName": "Sen. Cortez Masto, Catherine [D-NV]",
      "isOriginalCosponsor": "True",
      "lastName": "Cortez Masto",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "NV"
    },
    {
      "bioguideId": "D000563",
      "firstName": "Richard",
      "fullName": "Sen. Durbin, Richard J. [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Durbin",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "IL"
    },
    {
      "bioguideId": "G000555",
      "firstName": "Kirsten",
      "fullName": "Sen. Gillibrand, Kirsten E. [D-NY]",
      "isOriginalCosponsor": "True",
      "lastName": "Gillibrand",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "NY"
    },
    {
      "bioguideId": "H001042",
      "firstName": "Mazie",
      "fullName": "Sen. Hirono, Mazie K. [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Hirono",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "HI"
    },
    {
      "bioguideId": "K000384",
      "firstName": "Timothy",
      "fullName": "Sen. Kaine, Tim [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Kaine",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "VA"
    },
    {
      "bioguideId": "K000394",
      "firstName": "Andy",
      "fullName": "Sen. Kim, Andy [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Kim",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "NJ"
    },
    {
      "bioguideId": "M000133",
      "firstName": "Edward",
      "fullName": "Sen. Markey, Edward J. [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Markey",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "MA"
    },
    {
      "bioguideId": "S000033",
      "firstName": "Bernie",
      "fullName": "Sen. Sanders, Bernard [I-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sanders",
      "party": "I",
      "sponsorshipDate": "2025-09-16",
      "state": "VT"
    },
    {
      "bioguideId": "S001150",
      "firstName": "Adam",
      "fullName": "Sen. Schiff, Adam B. [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Schiff",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "CA"
    },
    {
      "bioguideId": "W000817",
      "firstName": "Elizabeth",
      "fullName": "Sen. Warren, Elizabeth [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warren",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "MA"
    },
    {
      "bioguideId": "W000779",
      "firstName": "Ron",
      "fullName": "Sen. Wyden, Ron [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Wyden",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "OR"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2820is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2820\nIN THE SENATE OF THE UNITED STATES\nSeptember 16, 2025 Ms. Klobuchar (for herself, Mr. Padilla , Ms. Alsobrooks , Mr. Bennet , Mr. Blumenthal , Mr. Booker , Ms. Cortez Masto , Mr. Durbin , Mrs. Gillibrand , Ms. Hirono , Mr. Kaine , Mr. Kim , Mr. Markey , Mr. Sanders , Mr. Schiff , Ms. Warren , and Mr. Wyden ) introduced the following bill; which was read twice and referred to the Committee on Rules and Administration\nA BILL\nTo amend the Help America Vote Act of 2002 to require States to provide for same day voter registration.\n#### 1. Short title\nThis Act may be cited as the Same Day Registration Act .\n#### 2. Same day registration\n##### (a) In general\nTitle III of the Help America Vote Act of 2002 ( 52 U.S.C. 21081 et seq. ) is amended\u2014\n**(1)**\nby redesignating sections 304, 305, and 306 as sections 305, 306, and 307, respectively; and\n**(2)**\nby inserting after section 303 the following new section:\n304. Same day registration (a) In general (1) Registration Each State shall permit any eligible individual on the day of a Federal election and on any day when voting, including early voting, is permitted for a Federal election\u2014 (A) to register to vote in such election at the polling place using a form that meets the requirements under section 9(b) of the National Voter Registration Act of 1993 ( 52 U.S.C. 20508(b) ) (or, if the individual is already registered to vote, to revise any of the individual\u2019s voter registration information); and (B) to cast a vote in such election. (2) Exception The requirements under paragraph (1) shall not apply to a State in which, under a State law in effect continuously on and after the date of the enactment of this section, there is no voter registration requirement for individuals in the State with respect to elections for Federal office. (b) Eligible individual For purposes of this section, the term eligible individual means, with respect to any election for Federal office, an individual who is otherwise qualified to vote in that election. (c) Ensuring availability of forms The State shall ensure that each polling place has copies of any forms an individual may be required to complete in order to register to vote or revise the individual\u2019s voter registration information under this section. (d) Effective date (1) In general Subject to paragraph (2), each State shall be required to comply with the requirements of this section for the regularly scheduled general election for Federal office occurring in November 2026 and for any subsequent election for Federal office. (2) Special rules for elections before November 2030 (A) Elections prior to November 2028 general election A State shall be deemed to be in compliance with the requirements of this section for the regularly scheduled general election for Federal office occurring in November 2026 and subsequent elections for Federal office occurring before the regularly scheduled general election for Federal office in November 2028 if not fewer than 1 location for each 15,000 registered voters in each jurisdiction in the State meets such requirements, and such location is reasonably located to serve voting populations equitably across the jurisdiction. (B) Additional elections prior to November 2030 general election If a State certifies to the Commission not later than November 7, 2028, that the State will not be in compliance with the requirements of this section for the regularly scheduled general election for Federal office occurring in November 2028 because it would be impracticable to do so and includes in the certification the reasons for the failure to meet such requirements, the State shall be deemed to be in compliance with the requirements of this section for the regularly scheduled general election for Federal office in November 2028 and subsequent elections for Federal office occurring before the regularly scheduled general election for Federal office in November 2030, if not fewer than 1 location for each 15,000 registered voters in each jurisdiction in the State meets such requirements, and such location is reasonably located to serve voting populations equitably across the jurisdiction. .\n##### (b) Conforming amendment relating to enforcement\nSection 401 of such Act ( 52 U.S.C. 21111 ) is amended by striking sections 301, 302, 303, and 304 and inserting subtitle A of title III .\n##### (c) Clerical amendments\nThe table of contents of such Act is amended\u2014\n**(1)**\nby redesignating the items relating to sections 304, 305, and 306 as relating to sections 305, 306, and 307, respectively;\n**(2)**\nin the item relating to section 305, as so redesignated, by striking Confirming access and inserting Access ; and\n**(3)**\nby inserting after the item relating to section 303 the following new item:\nSec. 304. Same day registration. .",
      "versionDate": "2025-09-16",
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
        "name": "Government Operations and Politics",
        "updateDate": "2025-09-30T23:16:37Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2820is.xml"
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
      "title": "Same Day Registration Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-30T04:38:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Same Day Registration Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-30T04:38:14Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Help America Vote Act of 2002 to require States to provide for same day voter registration.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-30T04:33:17Z"
    }
  ]
}
```
